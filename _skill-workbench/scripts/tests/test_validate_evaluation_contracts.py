from __future__ import annotations

import hashlib
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

    def write_case(self, root: Path, content: str = "# Positive case\n") -> tuple[str, str]:
        relative = "_skill-workbench/evaluations/cases/alpha/positive.md"
        case = root / relative
        case.parent.mkdir(parents=True)
        case.write_text(content, encoding="utf-8")
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        return relative, digest

    def versioned_mapping(
        self,
        case_path: str,
        digest: str,
        *,
        reference_expectation: str = "ordinary",
        extra_case_fields: str = "",
        verdicts: str | None = None,
    ) -> str:
        if verdicts is None:
            verdicts = """## Verdicts

- Source/package verdict: `pending`.
- Original behavioral observation: `pending`.
- Current-state gate: `pending`.
- Residual diagnostics: none.
"""
        return f"""# Mapping

Evaluation contract version: 2

### E1: Positive

- Class: application.
- Prompt or artifact: `{case_path}`.
- Fixture SHA-256: `{digest}`.
- Required skills: `{{alpha}}`.
- Distinctive judgment: Alpha owns the central decision.
- Neighbor ownership: Beta may contribute but does not own the decision.
- Ownership review: pending independent review.
- Reference expectation: {reference_expectation}.
{extra_case_fields}- Runs: pending.
- Package fidelity trace: pending.
- Attribution review: pending.
- Behavioral result: pending.
- Diagnostics: none.

## Independent Review

- Reviewer: pending independent reviewer.
- Catalog snapshot: pending complete catalog.
- Semantic verdict: pending.
- Unsupported or altered guidance: pending review.

## Validation Evidence

- Structural validation: pending.

{verdicts}"""

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

    def test_versioned_contract_with_required_fields_and_matching_hash_passes(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(self.versioned_mapping(case_path, digest), encoding="utf-8")

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertEqual(errors, [])

    def test_versioned_contract_requires_distinctive_judgment(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(case_path, digest).replace(
                "- Distinctive judgment: Alpha owns the central decision.\n", ""
            ),
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing distinctive judgment" in error for error in errors), errors)

    def test_versioned_focused_contract_requires_body_gap_and_index_destinations(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(case_path, digest, reference_expectation="focused"),
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing compact-body gap" in error for error in errors), errors)
        self.assertTrue(any("missing intended index destinations" in error for error in errors), errors)

    def test_versioned_contract_rejects_fixture_hash_mismatch(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, _ = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(self.versioned_mapping(case_path, "0" * 64), encoding="utf-8")

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("fixture SHA-256 mismatch" in error for error in errors), errors)

    def test_versioned_contract_requires_standard_verdict_fields(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(
                case_path,
                digest,
                verdicts="""## Verdicts

- Source/package verdict: `pending`.
- Original behavioral observation: `pending`.
- Residual diagnostics: none.
""",
            ),
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing current-state gate" in error for error in errors), errors)

    def test_versioned_contract_requires_independent_review_fields(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(case_path, digest).replace(
                "- Semantic verdict: pending.\n", ""
            ),
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing independent review semantic verdict" in error for error in errors), errors)

    def test_versioned_contract_requires_verdicts_as_final_section(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(case_path, digest)
            + "\n## Postscript\n\n- Note: this must not follow verdicts.\n",
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("Verdicts must be the final level-two section" in error for error in errors), errors)

    def test_case_level_version_opt_in_enforces_new_fields_in_legacy_mapping(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping_text = self.versioned_mapping(case_path, digest)
        mapping_text = mapping_text.replace("Evaluation contract version: 2\n\n", "")
        mapping_text = mapping_text.replace(
            "- Class: application.\n", "- Contract version: 2.\n- Class: application.\n"
        )
        mapping_text = mapping_text.replace(
            "- Distinctive judgment: Alpha owns the central decision.\n", ""
        )
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(mapping_text, encoding="utf-8")

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("missing distinctive judgment" in error for error in errors), errors)

    def test_unsupported_mapping_contract_version_fails(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            self.versioned_mapping(case_path, digest).replace(
                "Evaluation contract version: 2", "Evaluation contract version: 3"
            ),
            encoding="utf-8",
        )

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("unsupported evaluation contract version 3" in error for error in errors), errors)

    def test_unsupported_case_contract_version_fails(self) -> None:
        temporary, root = self.make_fixture("# placeholder\n")
        self.addCleanup(temporary.cleanup)
        case_path, digest = self.write_case(root)
        mapping_text = self.versioned_mapping(case_path, digest)
        mapping_text = mapping_text.replace("Evaluation contract version: 2\n\n", "")
        mapping_text = mapping_text.replace(
            "- Class: application.\n", "- Contract version: 3.\n- Class: application.\n"
        )
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(mapping_text, encoding="utf-8")

        errors = validate_evaluation_contracts.validate_repository(root)

        self.assertTrue(any("unsupported contract version 3" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
