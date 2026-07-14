from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "check_rule_wording.py"


MINI = """\
# Example

## When to use

Use for examples.

## Primary bias to correct

Preserve the important bias exactly.

## Decision rules

- Keep the first rule unchanged.

## Trigger rules

- When the trigger appears, apply the second rule.

## Final checklist

- First check preserved?
- Second check preserved?
"""


def skill(*, bias: str, checklist: tuple[str, str]) -> str:
    return f"""\
---
name: example
description: Use when an example is needed.
---

# Example

## Primary Bias

{bias}

## Guidance

- When the trigger appears, apply the second rule.
- Keep the first rule unchanged.

## Reference Map

Use this file alone.

- Focused detail: [Full section](references/full.md#full-section)

## Final Checklist

- {checklist[0]}
- {checklist[1]}
"""


class WordingCheckerTests(unittest.TestCase):
    def run_checker(self, skill_text: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            mini_path = root / "example.mini.md"
            skill_path = root / "SKILL.md"
            mini_path.write_text(MINI, encoding="utf-8")
            skill_path.write_text(skill_text, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--mini",
                    str(mini_path),
                    "--skill",
                    str(skill_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_exact_bias_rules_and_checklist_pass_despite_rule_reordering(self) -> None:
        result = self.run_checker(
            skill(
                bias="Preserve the important bias exactly.",
                checklist=("First check preserved?", "Second check preserved?"),
            )
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("primary bias wording: exact", result.stdout)
        self.assertIn("final checklist wording and order: exact", result.stdout)

    def test_changed_primary_bias_fails(self) -> None:
        result = self.run_checker(
            skill(
                bias="Preserve a similar but different bias.",
                checklist=("First check preserved?", "Second check preserved?"),
            )
        )

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("primary bias wording: different", result.stdout)

    def test_changed_checklist_wording_fails(self) -> None:
        result = self.run_checker(
            skill(
                bias="Preserve the important bias exactly.",
                checklist=("First check preserved?", "Second check changed?"),
            )
        )

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("final checklist wording and order: different", result.stdout)

    def test_reordered_checklist_fails(self) -> None:
        result = self.run_checker(
            skill(
                bias="Preserve the important bias exactly.",
                checklist=("Second check preserved?", "First check preserved?"),
            )
        )

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("final checklist wording and order: different", result.stdout)


if __name__ == "__main__":
    unittest.main()
