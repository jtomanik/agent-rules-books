#!/usr/bin/env python3
"""Validate deterministic invariants for manually converted rule-book skills."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


RULE_SECTIONS = {"Decision rules", "Trigger rules"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
INDEX_ROW_PATTERN = re.compile(
    r"^\|\s*\[([^]]+)]\(full\.md#([^)]+)\)\s*"
    r"\|\s*`(\d+)-(\d+)`\s*\|\s*(.*?)\s*\|\s*$"
)
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
SOFT_SKILL_WORD_LIMIT = 500
TARGET_PACKAGING_OVERHEAD_WORDS = 150
MAX_PACKAGING_OVERHEAD_WORDS = 200
MAX_DESCRIPTION_CHARACTERS = 500


@dataclass
class Validation:
    name: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    facts: list[str] = field(default_factory=list)

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def read_text(path: Path, validation: Validation) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        validation.errors.append(f"cannot read {path}: {error}")
        return ""


def extract_frontmatter(text: str, validation: Validation) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        validation.errors.append("SKILL.md must start with YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        validation.errors.append("SKILL.md frontmatter is not closed")
        return {}

    result: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            validation.errors.append(f"invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in result:
            validation.errors.append(f"duplicate frontmatter key: {key}")
        result[key] = value.strip()
    return result


def parse_simple_yaml(text: str, validation: Validation) -> dict[str, dict[str, str]]:
    """Parse the deliberately small two-level agents/openai.yaml contract."""
    result: dict[str, dict[str, str]] = {}
    current: str | None = None
    for number, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if not raw.startswith((" ", "\t")) and raw.endswith(":"):
            current = raw[:-1]
            if current in result:
                validation.errors.append(f"duplicate openai.yaml section: {current}")
            result[current] = {}
            continue
        if current is None or not raw.startswith("  ") or ":" not in raw:
            validation.errors.append(f"unsupported openai.yaml syntax on line {number}: {raw!r}")
            continue
        key, value = raw.strip().split(":", 1)
        if key in result[current]:
            validation.errors.append(f"duplicate openai.yaml key: {current}.{key}")
        result[current][key] = value.strip()
    return result


def parse_quoted(value: str, field_name: str, validation: Validation) -> str:
    if not (value.startswith('"') and value.endswith('"')):
        validation.errors.append(f"{field_name} must be double quoted")
        return value
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as error:
        validation.errors.append(f"invalid quoted value for {field_name}: {error}")
        return value
    if not isinstance(parsed, str):
        validation.errors.append(f"{field_name} must be a string")
        return value
    return parsed


def extract_rules(text: str) -> list[str]:
    rules: list[str] = []
    active = False
    for line in text.splitlines():
        if line.startswith("## "):
            active = line[3:].strip() in RULE_SECTIONS
            continue
        if active and line.startswith("- "):
            rules.append(line[2:].strip())
    return rules


def extract_mapping_ids(text: str, heading: str, prefix: str) -> list[str]:
    active = False
    ids: list[str] = []
    row_pattern = re.compile(rf"^\|\s*`({prefix}\d+)`\s*\|")
    for line in text.splitlines():
        if line.startswith("## "):
            active = line[3:].strip() == heading
            continue
        if active:
            match = row_pattern.match(line)
            if match:
                ids.append(match.group(1))
    return ids


def markdown_section(text: str, heading: str) -> str:
    active = False
    values: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if active:
                break
            active = line[3:].strip() == heading
            continue
        if active:
            values.append(line)
    return "\n".join(values).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def github_anchor(heading: str) -> str:
    heading = re.sub(r"<[^>]*>", "", heading).lower().strip()
    heading = "".join(char for char in heading if char.isalnum() or char in " _-")
    return heading.replace(" ", "-")


def full_sections(text: str) -> list[tuple[str, str, int, int]]:
    lines = text.splitlines()
    headings = [(index + 1, line[3:].strip()) for index, line in enumerate(lines) if line.startswith("## ")]
    sections: list[tuple[str, str, int, int]] = []
    anchor_counts: dict[str, int] = {}
    for position, (start, title) in enumerate(headings):
        next_start = headings[position + 1][0] if position + 1 < len(headings) else len(lines) + 1
        end = next_start - 1
        while end > start and not lines[end - 1].strip():
            end -= 1
        base_anchor = github_anchor(title)
        count = anchor_counts.get(base_anchor, 0)
        anchor_counts[base_anchor] = count + 1
        anchor = base_anchor if count == 0 else f"{base_anchor}-{count}"
        sections.append((title, anchor, start, end))
    return sections


def index_sections(text: str, validation: Validation) -> list[tuple[str, str, int, int]]:
    rows: list[tuple[str, str, int, int]] = []
    for line in text.splitlines():
        if not line.startswith("|") or "[" not in line:
            continue
        match = INDEX_ROW_PATTERN.match(line)
        if not match:
            validation.errors.append(f"invalid reference-index row: {line}")
            continue
        title, anchor, start, end, read_when = match.groups()
        validation.require(bool(read_when.strip()), f"empty Read when condition for {title}")
        rows.append((title, anchor, int(start), int(end)))
    return rows


def validate_links(skill_dir: Path, text: str, validation: Validation) -> None:
    links = re.findall(r"\[[^]]*]\((references/[^)#]+)(?:#[^)]+)?\)", text)
    validation.require("references/index.md" in links, "SKILL.md must link references/index.md")
    validation.require("references/full.md" in links, "SKILL.md must link references/full.md")
    for link in links:
        relative = Path(link)
        validation.require(len(relative.parts) == 2, f"reference link must be one level deep: {link}")
        validation.require((skill_dir / relative).is_file(), f"reference link does not resolve: {link}")


def validate_one(root: Path, name: str) -> Validation:
    validation = Validation(name)
    source_dir = root / name
    skill_dir = root / ".agents" / "skills" / name
    workbench_dir = root / "_skill-workbench" / name
    paths = {
        "full source": source_dir / f"{name}.md",
        "mini source": source_dir / f"{name}.mini.md",
        "nano source": source_dir / f"{name}.nano.md",
        "SKILL.md": skill_dir / "SKILL.md",
        "openai.yaml": skill_dir / "agents" / "openai.yaml",
        "full reference": skill_dir / "references" / "full.md",
        "reference index": skill_dir / "references" / "index.md",
        "mapping": workbench_dir / "mapping.md",
    }
    for label, path in paths.items():
        validation.require(path.is_file(), f"missing {label}: {path}")
    if validation.errors:
        return validation

    skill_text = read_text(paths["SKILL.md"], validation)
    metadata_text = read_text(paths["openai.yaml"], validation)
    full_text = read_text(paths["full reference"], validation)
    index_text = read_text(paths["reference index"], validation)
    mini_text = read_text(paths["mini source"], validation)
    nano_text = read_text(paths["nano source"], validation)
    mapping_text = read_text(paths["mapping"], validation)

    frontmatter = extract_frontmatter(skill_text, validation)
    validation.require(set(frontmatter) == {"name", "description"}, "frontmatter must contain only name and description")
    validation.require(frontmatter.get("name") == name, "frontmatter name must equal the skill folder name")
    validation.require(bool(NAME_PATTERN.fullmatch(name)), "skill name must be lowercase kebab-case")
    validation.require(len(name) <= 64, "skill name must be at most 64 characters")
    validation.require(bool(frontmatter.get("description")), "frontmatter description must not be empty")
    description_length = len(frontmatter.get("description", ""))
    validation.require(description_length <= 1024, "frontmatter description must be at most 1024 characters")
    validation.require(
        description_length <= MAX_DESCRIPTION_CHARACTERS,
        f"frontmatter description has {description_length} characters; expected at most {MAX_DESCRIPTION_CHARACTERS}",
    )
    skill_lines = len(skill_text.splitlines())
    skill_words = word_count(skill_text)
    mini_words = word_count(mini_text)
    packaging_overhead = max(0, skill_words - mini_words)
    size_exception = markdown_section(mapping_text, "Size Exception")
    packaging_fidelity = markdown_section(mapping_text, "Packaging Prose Fidelity")
    validation.require(skill_lines <= 100, f"SKILL.md has {skill_lines} lines; expected at most 100")
    if skill_words > SOFT_SKILL_WORD_LIMIT or packaging_overhead > TARGET_PACKAGING_OVERHEAD_WORDS:
        validation.require(
            bool(size_exception),
            f"SKILL.md has {skill_words} words with {packaging_overhead} words of packaging overhead; add a documented ## Size Exception to mapping.md",
        )
    if packaging_overhead > TARGET_PACKAGING_OVERHEAD_WORDS:
        validation.warnings.append(
            f"packaging overhead is {packaging_overhead} words, above the {TARGET_PACKAGING_OVERHEAD_WORDS}-word soft target"
        )
    validation.require(
        packaging_overhead <= MAX_PACKAGING_OVERHEAD_WORDS,
        f"SKILL.md adds {packaging_overhead} words beyond mini; hard maximum is {MAX_PACKAGING_OVERHEAD_WORDS}",
    )
    validation.require(not PLACEHOLDER_PATTERN.search(skill_text), "SKILL.md contains placeholder text")
    validate_links(skill_dir, skill_text, validation)
    validation.require(
        bool(packaging_fidelity),
        "mapping.md must contain a non-empty ## Packaging Prose Fidelity inventory",
    )
    if packaging_fidelity:
        directive_declaration = re.search(
            r"^- Newly authored technical directives:\s*(\S.+)$",
            packaging_fidelity,
            re.MULTILINE,
        )
        validation.require(
            bool(directive_declaration),
            "Packaging Prose Fidelity must declare newly authored technical directives",
        )

    metadata = parse_simple_yaml(metadata_text, validation)
    validation.require(set(metadata) == {"interface", "policy"}, "openai.yaml must contain exactly interface and policy sections")
    interface = metadata.get("interface", {})
    policy = metadata.get("policy", {})
    validation.require(
        set(interface) == {"display_name", "short_description", "default_prompt"},
        "openai.yaml interface must contain display_name, short_description, and default_prompt",
    )
    validation.require(set(policy) == {"allow_implicit_invocation"}, "openai.yaml policy must contain allow_implicit_invocation")
    display_name = parse_quoted(interface.get("display_name", ""), "interface.display_name", validation)
    short_description = parse_quoted(interface.get("short_description", ""), "interface.short_description", validation)
    default_prompt = parse_quoted(interface.get("default_prompt", ""), "interface.default_prompt", validation)
    validation.require(bool(display_name), "interface.display_name must not be empty")
    validation.require(25 <= len(short_description) <= 64, "interface.short_description must be 25-64 characters")
    token_pattern = re.compile(rf"\${re.escape(name)}(?![a-z0-9-])")
    validation.require(len(token_pattern.findall(default_prompt)) == 1, f"default_prompt must contain exactly one ${name} token")
    validation.require(policy.get("allow_implicit_invocation") in {"true", "false"}, "allow_implicit_invocation must be true or false")

    try:
        canonical_bytes = paths["full source"].read_bytes()
        reference_bytes = paths["full reference"].read_bytes()
        validation.require(canonical_bytes == reference_bytes, "references/full.md is not byte-identical to the canonical full rule")
    except OSError as error:
        validation.errors.append(f"cannot compare full reference: {error}")

    expected_sections = full_sections(full_text)
    actual_sections = index_sections(index_text, validation)
    validation.require(actual_sections == expected_sections, "reference index headings, anchors, order, or last-nonempty line ranges do not match full.md")
    validation.require("[full.md](full.md)" in index_text, "reference index must link full.md")

    mini_count = len(extract_rules(mini_text))
    nano_count = len(extract_rules(nano_text))
    expected_mini_ids = [f"M{number}" for number in range(1, mini_count + 1)]
    expected_nano_ids = [f"N{number}" for number in range(1, nano_count + 1)]
    actual_mini_ids = extract_mapping_ids(mapping_text, "Mini Mapping", "M")
    actual_nano_ids = extract_mapping_ids(mapping_text, "Nano Mapping", "N")
    validation.require(actual_mini_ids == expected_mini_ids, "Mini Mapping must contain every M ID exactly once and in source order")
    validation.require(actual_nano_ids == expected_nano_ids, "Nano Mapping must contain every N ID exactly once and in source order")
    validation.require(
        not re.search(r"^## Full Reference Routing\s*$", mapping_text, re.MULTILINE),
        "references/index.md must remain the single source of truth; remove duplicated ## Full Reference Routing from mapping.md",
    )
    validation.require(not PLACEHOLDER_PATTERN.search(mapping_text), "mapping.md contains placeholder text")

    validation.facts.extend(
        [
            f"SKILL.md {skill_lines} lines",
            f"{skill_words} words ({packaging_overhead} beyond mini)",
            f"{mini_count} mini rules and {nano_count} nano rules mapped",
            f"{len(expected_sections)} full-reference sections indexed",
        ]
    )
    return validation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills", nargs="+", help="Skill names to validate")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root (default: current directory)")
    args = parser.parse_args()

    failed = False
    for name in args.skills:
        validation = validate_one(args.repo.resolve(), name)
        if validation.errors:
            failed = True
            print(f"FAIL {name}")
            for error in validation.errors:
                print(f"  - {error}")
        else:
            print(f"PASS {name}: " + "; ".join(validation.facts))
            for warning in validation.warnings:
                print(f"  WARNING: {warning}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
