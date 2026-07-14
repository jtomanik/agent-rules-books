from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "validate_conversion.py"
SPEC = importlib.util.spec_from_file_location("validate_conversion", SCRIPT)
assert SPEC and SPEC.loader
validate_conversion = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_conversion
SPEC.loader.exec_module(validate_conversion)


class ConversionSizeBudgetTests(unittest.TestCase):
    def make_fixture(
        self,
        *,
        size_exception: bool,
        duplicate_routing: bool = False,
        extra_packaging_words: int = 0,
        packaging_fidelity: bool = True,
    ) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        name = "example"
        source = root / name
        skill = root / ".agents" / "skills" / name
        rule_workbench = root / "_rule-workbench" / name
        workbench = root / "_skill-workbench" / name
        source.mkdir(parents=True)
        (skill / "agents").mkdir(parents=True)
        (skill / "references").mkdir(parents=True)
        rule_workbench.mkdir(parents=True)
        workbench.mkdir(parents=True)

        long_rule = " ".join(["preserved"] * 510) + "."
        full = "# Full\n\n## One section\n\nFull guidance.\n"
        mini = f"""# Mini

## Primary bias to correct

Keep the bias.

## Decision rules

- {long_rule}

## Trigger rules

## Final checklist

- Check it?
"""
        nano = """# Nano

## Decision rules

- Preserve it.

## Trigger rules
"""
        extra_packaging = " ".join(["context"] * extra_packaging_words)
        skill_text = f"""---
name: example
description: Use when preserved example guidance is central to the task.
---

# Example

## Primary Bias

Keep the bias.

## Guidance

- {long_rule}

{extra_packaging}

## Reference Router

Use this file alone for ordinary work. Read [references/index.md](references/index.md) for focused work and [references/full.md](references/full.md) end to end for comprehensive work.

## Final Checklist

- Check it?
"""
        mapping = """# Mapping

## Nano Mapping

| ID | Role |
| --- | --- |
| `N1` | description |

## Mini Mapping

| ID | Destination |
| --- | --- |
| `M1` | Guidance |
"""
        traceability = """# Traceability

## Mini mapping

- `M1` Preserve the complete mini guidance.

## Nano mapping

- `N1` Preserve the nano guidance.
"""
        if packaging_fidelity:
            mapping += """

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: description, headings, transitions, and routing prose add no technical rule.
"""
        if size_exception:
            mapping += """

## Size Exception

The canonical mini source already exceeds the 500-word target. The skill preserves it verbatim and adds less than 150 words of packaging.
"""
        if duplicate_routing:
            mapping += """

## Full Reference Routing

| Full section | Read when |
| --- | --- |
| One section | The one section is needed. |
"""

        (source / f"{name}.md").write_text(full, encoding="utf-8")
        (source / f"{name}.mini.md").write_text(mini, encoding="utf-8")
        (source / f"{name}.nano.md").write_text(nano, encoding="utf-8")
        (rule_workbench / "traceability.md").write_text(traceability, encoding="utf-8")
        (skill / "SKILL.md").write_text(skill_text, encoding="utf-8")
        (skill / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "Example"\n  short_description: "Apply preserved example guidance"\n  default_prompt: "Use $example for this task."\n\npolicy:\n  allow_implicit_invocation: true\n',
            encoding="utf-8",
        )
        (skill / "references" / "full.md").write_text(full, encoding="utf-8")
        (skill / "references" / "index.md").write_text(
            "# Index\n\n[full.md](full.md)\n\n| Section | Lines | Read when |\n| --- | ---: | --- |\n| [One section](full.md#one-section) | `3-5` | The one section is needed. |\n",
            encoding="utf-8",
        )
        (workbench / "mapping.md").write_text(mapping, encoding="utf-8")
        return temporary, root

    def test_traceability_id_may_cover_multiple_verbatim_mini_rules(self) -> None:
        temporary, root = self.make_fixture(size_exception=True)
        self.addCleanup(temporary.cleanup)

        mini = root / "example" / "example.mini.md"
        mini.write_text(
            mini.read_text(encoding="utf-8").replace(
                "## Trigger rules\n",
                "- Keep the second rule.\n\n## Trigger rules\n",
            ),
            encoding="utf-8",
        )
        skill = root / ".agents" / "skills" / "example" / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace(
                "\n\n## Reference Router",
                "\n- Keep the second rule.\n\n## Reference Router",
            ),
            encoding="utf-8",
        )

        result = validate_conversion.validate_one(root, "example")

        self.assertEqual(result.errors, [])

    def test_oversized_skill_without_documented_exception_fails(self) -> None:
        temporary, root = self.make_fixture(size_exception=False)
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertTrue(any("Size Exception" in error for error in result.errors), result.errors)

    def test_source_driven_size_exception_passes(self) -> None:
        temporary, root = self.make_fixture(size_exception=True)
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertEqual(result.errors, [])

    def test_small_documented_packaging_overage_passes_with_warning(self) -> None:
        temporary, root = self.make_fixture(
            size_exception=True,
            extra_packaging_words=130,
        )
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertEqual(result.errors, [])
        self.assertTrue(any("soft target" in warning for warning in result.warnings), result.warnings)

    def test_small_packaging_overage_requires_documented_exception(self) -> None:
        temporary, root = self.make_fixture(
            size_exception=False,
            extra_packaging_words=130,
        )
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertTrue(any("Size Exception" in error for error in result.errors), result.errors)

    def test_materially_excessive_packaging_fails_even_with_exception(self) -> None:
        temporary, root = self.make_fixture(
            size_exception=True,
            extra_packaging_words=190,
        )
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertTrue(any("hard maximum" in error for error in result.errors), result.errors)

    def test_mapping_must_not_duplicate_reference_index_routing(self) -> None:
        temporary, root = self.make_fixture(size_exception=True, duplicate_routing=True)
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertTrue(any("single source of truth" in error for error in result.errors), result.errors)

    def test_mapping_requires_packaging_prose_fidelity_inventory(self) -> None:
        temporary, root = self.make_fixture(
            size_exception=True,
            packaging_fidelity=False,
        )
        self.addCleanup(temporary.cleanup)

        result = validate_conversion.validate_one(root, "example")

        self.assertTrue(
            any("Packaging Prose Fidelity" in error for error in result.errors),
            result.errors,
        )


if __name__ == "__main__":
    unittest.main()
