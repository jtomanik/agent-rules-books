#!/usr/bin/env python3
"""Report wording changes between canonical mini rules and a guidance skill."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import Counter
from pathlib import Path


MINI_RULE_HEADINGS = {"decision rules", "trigger rules"}
SKILL_NON_RULE_HEADINGS = {
    "when to use",
    "primary bias",
    "primary bias to correct",
    "reference map",
    "reference router",
    "final checklist",
}
MINI_PRIMARY_BIAS_HEADINGS = {"primary bias to correct"}
SKILL_PRIMARY_BIAS_HEADINGS = {"primary bias"}
FINAL_CHECKLIST_HEADINGS = {"final checklist"}


def normalize_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).lower()


def normalize_rule(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def extract_rules(path: Path, *, source: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    current_heading = ""
    rules: list[str] = []

    for index, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter:
            if index > 0 and stripped == "---":
                in_frontmatter = False
            continue

        heading_match = re.match(r"^##+\s+(.+?)\s*$", line)
        if heading_match:
            current_heading = normalize_heading(heading_match.group(1))
            continue

        if not line.startswith("- "):
            continue

        if source == "mini" and current_heading not in MINI_RULE_HEADINGS:
            continue
        if source == "skill" and current_heading in SKILL_NON_RULE_HEADINGS:
            continue

        rules.append(normalize_rule(line[2:]))

    return rules


def extract_section_lines(path: Path, headings: set[str]) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    active = False
    values: list[str] = []

    for index, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter:
            if index > 0 and stripped == "---":
                in_frontmatter = False
            continue

        heading_match = re.match(r"^##+\s+(.+?)\s*$", line)
        if heading_match:
            normalized = normalize_heading(heading_match.group(1))
            if active and normalized not in headings:
                break
            active = normalized in headings
            continue

        if active and stripped:
            values.append(stripped)

    return values


def extract_section_text(path: Path, headings: set[str]) -> str:
    return normalize_rule(" ".join(extract_section_lines(path, headings)))


def extract_section_bullets(path: Path, headings: set[str]) -> list[str]:
    return [normalize_rule(line[2:]) for line in extract_section_lines(path, headings) if line.startswith("- ")]


def expand_counter(counter: Counter[str]) -> list[str]:
    values: list[str] = []
    for rule, count in counter.items():
        values.extend([rule] * count)
    return values


def word_diff(before: str, after: str) -> str:
    return " ".join(difflib.ndiff(before.split(), after.split()))


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare canonical mini decision/trigger bullets with guidance bullets "
            "in SKILL.md without treating reordering as a wording change."
        )
    )
    parser.add_argument("--mini", required=True, type=Path)
    parser.add_argument("--skill", required=True, type=Path)
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.35,
        help="Minimum similarity for displaying a closest skill rule (default: 0.35).",
    )
    args = parser.parse_args()

    mini_rules = extract_rules(args.mini, source="mini")
    skill_rules = extract_rules(args.skill, source="skill")
    mini_bias = extract_section_text(args.mini, MINI_PRIMARY_BIAS_HEADINGS)
    skill_bias = extract_section_text(args.skill, SKILL_PRIMARY_BIAS_HEADINGS)
    mini_checklist = extract_section_bullets(args.mini, FINAL_CHECKLIST_HEADINGS)
    skill_checklist = extract_section_bullets(args.skill, FINAL_CHECKLIST_HEADINGS)

    mini_counter = Counter(mini_rules)
    skill_counter = Counter(skill_rules)
    missing = expand_counter(mini_counter - skill_counter)
    added = expand_counter(skill_counter - mini_counter)
    exact_count = sum((mini_counter & skill_counter).values())

    print(f"mini rules: {len(mini_rules)}")
    print(f"skill guidance rules: {len(skill_rules)}")
    print(f"exact wording matches: {exact_count}")
    print(f"missing or reworded mini rules: {len(missing)}")
    print(f"added or reworded skill rules: {len(added)}")
    bias_exact = bool(mini_bias) and mini_bias == skill_bias
    checklist_exact = bool(mini_checklist) and mini_checklist == skill_checklist
    print(f"primary bias wording: {'exact' if bias_exact else 'different'}")
    print(
        "final checklist wording and order: "
        f"{'exact' if checklist_exact else 'different'}"
    )

    if not missing and not added and bias_exact and checklist_exact:
        print("wording fidelity: exact")
        return 0

    if not bias_exact:
        print(f"\nPRIMARY BIAS SOURCE: {mini_bias or '<missing>'}")
        print(f"PRIMARY BIAS SKILL: {skill_bias or '<missing>'}")
        if mini_bias and skill_bias:
            print(f"PRIMARY BIAS WORD DIFF: {word_diff(mini_bias, skill_bias)}")

    if not checklist_exact:
        print("\nFINAL CHECKLIST SOURCE:")
        for position, item in enumerate(mini_checklist, start=1):
            print(f"  {position}. {item}")
        print("FINAL CHECKLIST SKILL:")
        for position, item in enumerate(skill_checklist, start=1):
            print(f"  {position}. {item}")
        if Counter(mini_checklist) == Counter(skill_checklist):
            print("  wording matches, but item order differs")

    candidate_pool = added or skill_rules
    for position, original in enumerate(missing, start=1):
        print(f"\nMISSING {position}: {original}")
        if not candidate_pool:
            continue

        candidate = max(
            candidate_pool,
            key=lambda value: difflib.SequenceMatcher(None, original, value).ratio(),
        )
        ratio = difflib.SequenceMatcher(None, original, candidate).ratio()
        if ratio < args.similarity_threshold:
            print("  closest skill rule: none above similarity threshold")
            continue

        print(f"  closest skill rule ({ratio:.0%}): {candidate}")
        print(f"  word diff: {word_diff(original, candidate)}")

    if added:
        print("\nADDED OR REWORDED SKILL RULES:")
        for position, rule in enumerate(added, start=1):
            print(f"  {position}. {rule}")

    print(
        "\nwording fidelity: differences require removal or explicit mapping rationale",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
