from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "validate_evaluation_contracts.py"
SPEC = importlib.util.spec_from_file_location("validate_evaluation_contracts", SCRIPT)
assert SPEC and SPEC.loader
validate_evaluation_contracts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_evaluation_contracts
SPEC.loader.exec_module(validate_evaluation_contracts)


class EvaluationContractTests(unittest.TestCase):
    def make_fixture(self, mapping: str) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        for name in ("alpha", "beta"):
            skill = root / ".agents" / "skills" / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Example.\n---\n",
                encoding="utf-8",
            )
        workbench = root / "_skill-workbench" / "alpha"
        workbench.mkdir(parents=True)
        (workbench / "mapping.md").write_text(mapping, encoding="utf-8")
        return temporary, root

    def test_required_skill_contract_passes_without_catalog_partition(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### E1: Positive

- Required skills: `{alpha}`.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertEqual(errors, [])

    def test_missing_required_skills_line_fails(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### E1: Missing target

- Allowed skills: `{}`.
- Forbidden skills: `{beta}`.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing required skills line" in error for error in errors), errors)

    def test_additional_catalog_skills_need_no_classification(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### O1: Positive with overlap

- Required skills: `{alpha}`.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertEqual(errors, [])

    def test_selection_notes_do_not_create_catalog_requirements(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### E1: Unknown

- Required skills: `{alpha}`.
- Selection notes: `gamma` may also be relevant.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertEqual(errors, [])

    def test_unknown_required_skill_fails(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### E1: Unknown target

- Required skills: `{gamma}`.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("unknown required skill gamma" in error for error in errors), errors)

    def test_letter_suffixed_case_is_validated(self) -> None:
        temporary, root = self.make_fixture(
            """# Mapping

### E1b: Replacement control

- Required skills: `{alpha}`.
"""
        )
        self.addCleanup(temporary.cleanup)

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
