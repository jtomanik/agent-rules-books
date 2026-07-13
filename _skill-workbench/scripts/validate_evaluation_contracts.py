#!/usr/bin/env python3
"""Validate required-skill contracts against the live project-skill catalog."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CASE_HEADING = re.compile(r"^### ([A-Z]+\d+[a-z]*):\s+(.+)$")
REQUIRED_LINE = re.compile(r"^- Required skills:\s+(.+)$")
BRACED_SET = re.compile(r"\{([^}]*)\}")


def live_catalog(root: Path) -> set[str]:
    skills = root / ".agents" / "skills"
    if not skills.is_dir():
        return set()
    return {
        path.parent.name
        for path in skills.glob("*/SKILL.md")
        if path.parent.is_dir()
    }


def parse_skill_set(value: str) -> set[str] | None:
    match = BRACED_SET.search(value)
    if not match:
        return None
    content = match.group(1).strip()
    if not content:
        return set()
    return {item.strip().strip("`") for item in content.split(",") if item.strip()}


def mapping_cases(path: Path) -> list[tuple[str, dict[str, set[str] | None]]]:
    cases: list[tuple[str, dict[str, set[str] | None]]] = []
    current: tuple[str, dict[str, set[str] | None]] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = CASE_HEADING.match(line)
        if heading:
            if current:
                cases.append(current)
            current = (heading.group(1), {})
            continue
        if current and line.startswith("## "):
            cases.append(current)
            current = None
            continue
        if not current:
            continue
        required_line = REQUIRED_LINE.match(line)
        if required_line:
            current[1]["required"] = parse_skill_set(required_line.group(1))
    if current:
        cases.append(current)
    return cases


def validate_repository(root: Path) -> list[str]:
    catalog = live_catalog(root)
    errors: list[str] = []
    if not catalog:
        return ["live catalog is empty: .agents/skills/*/SKILL.md not found"]

    mappings = sorted((root / "_skill-workbench").glob("*/mapping.md"))
    for mapping in mappings:
        for case_id, sets in mapping_cases(mapping):
            label = f"{mapping.relative_to(root)} {case_id}"
            if "required" not in sets:
                errors.append(f"{label}: missing required skills line")
                continue
            if sets["required"] is None:
                errors.append(f"{label}: required skills must contain an explicit {{...}} set")
                continue

            unknown = sorted((sets["required"] or set()) - catalog)
            if unknown:
                errors.append(f"{label}: unknown required skill {', '.join(unknown)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    errors = validate_repository(args.repo.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: every durable evaluation case names only live required skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
