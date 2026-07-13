from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "run_skill_eval.py"


class EvaluationRunnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = importlib.util.spec_from_file_location("run_skill_eval", SCRIPT)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        cls.runner = module

    def test_blind_prompt_contains_case_without_expectation_vocabulary(self) -> None:
        prompt = self.runner.build_prompt("Review this raw function.")

        self.assertIn("Review this raw function.", prompt)
        self.assertNotIn("required skills", prompt.lower())
        self.assertNotIn("forbidden skills", prompt.lower())
        self.assertNotIn("expected sections", prompt.lower())
        self.assertNotIn("source_support", prompt)
        self.assertNotIn("`recommendations`", prompt)
        self.assertIn("only `.agents/skills`", prompt)
        self.assertIn("canonical book directories", prompt)
        self.assertIn("Never open a skill or reference to populate reporting fields", prompt)
        self.assertIn("Do not encode the empty list as a section string", prompt)

    def test_command_pins_model_and_read_only_configuration(self) -> None:
        command = self.runner.build_command(
            cwd=Path("/tmp/eval"),
            model="gpt-5.4",
            schema=Path("/repo/schema.json"),
            output_message=Path("/tmp/final.json"),
            prompt="case",
        )

        self.assertIn("gpt-5.4", command)
        self.assertIn("read-only", command)
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ephemeral", command)
        self.assertIn("--json", command)
        self.assertIn("/tmp/eval", command)

    def test_thread_id_is_extracted_from_json_events(self) -> None:
        events = '{"type":"thread.started","thread_id":"abc-123"}\n{"type":"turn.completed"}\n'

        self.assertEqual(self.runner.extract_thread_id(events), "abc-123")

    def test_known_ephemeral_warnings_are_removed_from_stderr(self) -> None:
        stderr = "\n".join(
            [
                "Reading additional input from stdin...",
                "2026-07-11 WARN state db discrepancy during find_thread_path_by_id_str_in_subdir: falling_back",
                "real warning",
            ]
        )

        self.assertEqual(self.runner.clean_stderr(stderr), "real warning")

    def test_required_skill_inclusion_allows_additional_selections(self) -> None:
        result = {
            "selected_project_skills": ["code-complete", "clean-code"],
        }

        errors = self.runner.validate_required_skill_inclusion(
            result,
            ["code-complete"],
        )

        self.assertEqual(errors, [])

    def test_required_skill_inclusion_reports_only_missing_targets(self) -> None:
        result = {
            "selected_project_skills": ["clean-code"],
        }

        errors = self.runner.validate_required_skill_inclusion(
            result,
            ["code-complete", "clean-code"],
        )

        self.assertEqual(errors, ["required project skill not selected: code-complete"])

    def test_result_rejects_consulted_skill_missing_from_selection(self) -> None:
        result = {
            "answer": "Use the legacy boundary.",
            "selected_project_skills": ["working-effectively-with-legacy-code"],
            "consulted_files": [
                ".agents/skills/working-effectively-with-legacy-code/SKILL.md",
                ".agents/skills/clean-code/SKILL.md",
            ],
            "consulted_reference_sections": [],
            "reference_mode": "ordinary",
        }

        errors = self.runner.validate_result_integrity(result)

        self.assertTrue(any("selected_project_skills" in error for error in errors), errors)

    def test_result_rejects_reference_mode_that_does_not_match_files(self) -> None:
        result = {
            "answer": "Use focused guidance.",
            "selected_project_skills": ["release-it"],
            "consulted_files": [
                ".agents/skills/release-it/SKILL.md",
                ".agents/skills/release-it/references/index.md",
                ".agents/skills/release-it/references/full.md",
            ],
            "consulted_reference_sections": [
                {"skill": "release-it", "sections": ["Dependency Protection Rules"]},
            ],
            "reference_mode": "ordinary",
        }

        errors = self.runner.validate_result_integrity(result)

        self.assertTrue(any("reference_mode" in error for error in errors), errors)

    def test_result_accepts_consistent_focused_evidence(self) -> None:
        result = {
            "answer": "Use focused guidance.",
            "selected_project_skills": ["release-it"],
            "consulted_files": [
                "/repo/.agents/skills/release-it/SKILL.md",
                "/repo/.agents/skills/release-it/references/index.md",
                "/repo/.agents/skills/release-it/references/full.md",
            ],
            "consulted_reference_sections": [
                {"skill": "release-it", "sections": ["Dependency Protection Rules"]},
            ],
            "reference_mode": "focused",
        }

        self.assertEqual(self.runner.validate_result_integrity(result), [])

    def test_focused_result_requires_named_reference_sections(self) -> None:
        result = {
            "answer": "Use focused guidance.",
            "selected_project_skills": ["release-it"],
            "consulted_files": [
                ".agents/skills/release-it/SKILL.md",
                ".agents/skills/release-it/references/index.md",
                ".agents/skills/release-it/references/full.md",
            ],
            "consulted_reference_sections": [],
            "reference_mode": "focused",
        }

        errors = self.runner.validate_result_integrity(result)

        self.assertTrue(any("consulted_reference_sections" in error for error in errors), errors)

    def test_ordinary_result_rejects_reference_sections(self) -> None:
        result = {
            "answer": "Use ordinary guidance.",
            "selected_project_skills": ["release-it"],
            "consulted_files": [".agents/skills/release-it/SKILL.md"],
            "consulted_reference_sections": [
                {"skill": "release-it", "sections": ["Dependency Protection Rules"]},
            ],
            "reference_mode": "ordinary",
        }

        errors = self.runner.validate_result_integrity(result)

        self.assertTrue(any("consulted_reference_sections" in error for error in errors), errors)

    def test_comprehensive_result_uses_star_for_full_read(self) -> None:
        result = {
            "answer": "Use comprehensive guidance.",
            "selected_project_skills": ["release-it"],
            "consulted_files": [
                ".agents/skills/release-it/SKILL.md",
                ".agents/skills/release-it/references/full.md",
            ],
            "consulted_reference_sections": [
                {"skill": "release-it", "sections": ["*"]},
            ],
            "reference_mode": "comprehensive",
        }

        self.assertEqual(self.runner.validate_result_integrity(result), [])


if __name__ == "__main__":
    unittest.main()
