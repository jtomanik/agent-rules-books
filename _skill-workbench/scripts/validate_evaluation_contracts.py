#!/usr/bin/env python3
"""Validate required-skill and versioned evaluation contracts."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


CASE_HEADING = re.compile(r"^### ([A-Z]+\d+[a-z]*):\s+(.+)$")
CONTRACT_VERSION = re.compile(r"^Evaluation contract version:\s*(\d+)\s*$")
FIELD_LINE = re.compile(r"^- ([^:]+):\s*(.*)$")
BRACED_SET = re.compile(r"\{([^}]*)\}")
BACKTICK_VALUE = re.compile(r"`([^`]+)`")
SHA256_VALUE = re.compile(r"\b([0-9a-fA-F]{64})\b")

VERSION_2_CASE_FIELDS = (
    "class",
    "prompt or artifact",
    "fixture sha-256",
    "required skills",
    "distinctive judgment",
    "neighbor ownership",
    "ownership review",
    "reference expectation",
    "runs",
    "package fidelity trace",
    "attribution review",
    "behavioral result",
    "diagnostics",
)
VERSION_2_FOCUSED_FIELDS = ("compact-body gap", "intended index destinations")
VERSION_2_VERDICT_FIELDS = (
    "source/package verdict",
    "original behavioral observation",
    "current-state gate",
    "residual diagnostics",
)
VERSION_2_INDEPENDENT_REVIEW_FIELDS = (
    "reviewer",
    "catalog snapshot",
    "semantic verdict",
    "unsupported or altered guidance",
)


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


def normalized_field_name(value: str) -> str:
    return " ".join(value.lower().split())


def contract_version(lines: list[str]) -> int | None:
    for line in lines:
        match = CONTRACT_VERSION.match(line)
        if match:
            return int(match.group(1))
    return None


def mapping_cases(lines: list[str]) -> list[tuple[str, dict[str, str]]]:
    cases: list[tuple[str, dict[str, str]]] = []
    current: tuple[str, dict[str, str]] | None = None
    for line in lines:
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
        field = FIELD_LINE.match(line)
        if field:
            current[1][normalized_field_name(field.group(1))] = field.group(2).strip()
    if current:
        cases.append(current)
    return cases


def section_fields(lines: list[str], heading: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    in_section = False
    for line in lines:
        if line == f"## {heading}":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        field = FIELD_LINE.match(line)
        if field:
            fields[normalized_field_name(field.group(1))] = field.group(2).strip()
    return fields


def normalized_scalar(value: str) -> str:
    return value.strip().rstrip(".").strip("`").strip().lower()


def validate_fixture(root: Path, label: str, fields: dict[str, str]) -> list[str]:
    errors: list[str] = []
    path_match = BACKTICK_VALUE.search(fields["prompt or artifact"])
    if not path_match:
        return [f"{label}: prompt or artifact must contain one repository-relative path in backticks"]

    relative = Path(path_match.group(1))
    if relative.is_absolute():
        return [f"{label}: prompt or artifact path must be repository-relative"]
    fixture = (root / relative).resolve()
    try:
        fixture.relative_to(root)
    except ValueError:
        return [f"{label}: prompt or artifact path escapes repository root"]
    if not fixture.is_file():
        return [f"{label}: fixture file not found: {relative}"]

    digest_match = SHA256_VALUE.search(fields["fixture sha-256"])
    if not digest_match:
        return [f"{label}: fixture SHA-256 must contain a 64-character hexadecimal digest"]
    expected = digest_match.group(1).lower()
    actual = hashlib.sha256(fixture.read_bytes()).hexdigest()
    if expected != actual:
        errors.append(f"{label}: fixture SHA-256 mismatch: expected {expected}, actual {actual}")
    return errors


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    catalog = live_catalog(root)
    errors: list[str] = []
    if not catalog:
        return ["live catalog is empty: .agents/skills/*/SKILL.md not found"]

    mappings = sorted((root / "_skill-workbench").glob("*/mapping.md"))
    for mapping in mappings:
        lines = mapping.read_text(encoding="utf-8").splitlines()
        version = contract_version(lines)
        if version not in (None, 2):
            errors.append(
                f"{mapping.relative_to(root)}: unsupported evaluation contract version {version}"
            )
        cases = mapping_cases(lines)
        for case_id, fields in cases:
            label = f"{mapping.relative_to(root)} {case_id}"
            if "required skills" not in fields:
                errors.append(f"{label}: missing required skills line")
                continue
            required = parse_skill_set(fields["required skills"])
            if required is None:
                errors.append(f"{label}: required skills must contain an explicit {{...}} set")
                continue

            unknown = sorted(required - catalog)
            if unknown:
                errors.append(f"{label}: unknown required skill {', '.join(unknown)}")

            case_version = normalized_scalar(fields.get("contract version", ""))
            if case_version and case_version != "2":
                errors.append(f"{label}: unsupported contract version {case_version}")
                continue
            if version != 2 and case_version != "2":
                continue
            for field in VERSION_2_CASE_FIELDS:
                if not fields.get(field):
                    errors.append(f"{label}: missing {field}")
            if any(not fields.get(field) for field in VERSION_2_CASE_FIELDS):
                continue

            expectation = normalized_scalar(fields["reference expectation"])
            if expectation == "focused":
                for field in VERSION_2_FOCUSED_FIELDS:
                    if not fields.get(field):
                        errors.append(f"{label}: missing {field}")
            errors.extend(validate_fixture(root, label, fields))

        if version == 2:
            mapping_label = str(mapping.relative_to(root))
            headings = [line for line in lines if line.startswith("## ")]
            if not headings or headings[-1] != "## Verdicts":
                errors.append(
                    f"{mapping_label}: Verdicts must be the final level-two section"
                )

            review_fields = section_fields(lines, "Independent Review")
            for field in VERSION_2_INDEPENDENT_REVIEW_FIELDS:
                if not review_fields.get(field):
                    errors.append(
                        f"{mapping_label}: missing independent review {field}"
                    )

            verdict_fields = section_fields(lines, "Verdicts")
            for field in VERSION_2_VERDICT_FIELDS:
                if not verdict_fields.get(field):
                    errors.append(f"{mapping_label}: missing {field}")
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
    print("PASS: durable required-skill and versioned evaluation contracts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
