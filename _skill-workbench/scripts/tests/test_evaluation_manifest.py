from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "evaluation_manifest.py"
SPEC = importlib.util.spec_from_file_location("evaluation_manifest", SCRIPT)
assert SPEC and SPEC.loader
evaluation_manifest = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = evaluation_manifest
SPEC.loader.exec_module(evaluation_manifest)


class EvaluationManifestTests(unittest.TestCase):
    def make_repository(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        descriptions = {
            "zeta": "Use when zeta is central.",
            "alpha": "Use when alpha is central.",
        }
        for name, description in descriptions.items():
            skill = root / ".agents" / "skills" / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: {description}\n---\n",
                encoding="utf-8",
            )

        case = root / "_skill-workbench" / "evaluations" / "cases" / "alpha" / "positive.md"
        case.parent.mkdir(parents=True)
        case.write_text("# Positive case\n", encoding="utf-8")
        case_hash = hashlib.sha256(case.read_bytes()).hexdigest()

        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.parent.mkdir(parents=True)
        mapping.write_text(
            f"""# Mapping

Evaluation contract version: 2

### E1: Positive

- Prompt or artifact: `_skill-workbench/evaluations/cases/alpha/positive.md`.
- Fixture SHA-256: `{case_hash}`.
- Required skills: `{{zeta, alpha}}`.
- Ownership review: PASS - independently reviewed.
""",
            encoding="utf-8",
        )

        scripts = root / "_skill-workbench" / "scripts"
        scripts.mkdir(exist_ok=True)
        (scripts / "run_skill_eval.py").write_text("# runner\n", encoding="utf-8")
        schema = root / "_skill-workbench" / "evaluations" / "result-v2.schema.json"
        schema.write_text("{}\n", encoding="utf-8")
        return temporary, root, case

    def test_catalog_snapshot_hashes_the_sorted_exact_payload(self) -> None:
        temporary, root, _ = self.make_repository()
        self.addCleanup(temporary.cleanup)
        payload = (
            "alpha\tUse when alpha is central.\n"
            "zeta\tUse when zeta is central.\n"
        ).encode("utf-8")

        snapshot = evaluation_manifest.catalog_snapshot(root)

        self.assertEqual(
            snapshot["entries"],
            [
                {"name": "alpha", "description": "Use when alpha is central."},
                {"name": "zeta", "description": "Use when zeta is central."},
            ],
        )
        self.assertEqual(snapshot["byte_count"], len(payload))
        self.assertEqual(snapshot["sha256"], hashlib.sha256(payload).hexdigest())

    def test_manifest_derives_required_skills_from_the_mapping(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)

        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=root / "_skill-workbench" / "evaluations" / "result-v2.schema.json",
            runner=root / "_skill-workbench" / "scripts" / "run_skill_eval.py",
            timeout=123,
        )

        self.assertEqual(manifest["contract"]["case_id"], "E1")
        self.assertEqual(manifest["required_project_skills"], ["alpha", "zeta"])
        self.assertEqual(manifest["execution"]["run"], "green-1")
        self.assertEqual(manifest["execution"]["timeout"], 123)
        self.assertEqual(manifest["catalog"]["skill_count"], 2)

    def test_manifest_uses_versioned_replacement_after_historical_same_fixture(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        case_hash = hashlib.sha256(case.read_bytes()).hexdigest()
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            f"""# Mapping

### E1: Historical

- Prompt or artifact: `_skill-workbench/evaluations/cases/alpha/positive.md`.
- Fixture SHA-256: `{case_hash}`.
- Required skills: `{{alpha}}`.

### R1: Versioned replacement

- Contract version: 2
- Prompt or artifact: `_skill-workbench/evaluations/cases/alpha/positive.md`.
- Fixture SHA-256: `{case_hash}`.
- Required skills: `{{zeta, alpha}}`.
- Ownership review: PASS - independently reviewed.
""",
            encoding="utf-8",
        )

        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=root / "_skill-workbench" / "evaluations" / "result-v2.schema.json",
            runner=root / "_skill-workbench" / "scripts" / "run_skill_eval.py",
            timeout=123,
        )

        self.assertEqual(manifest["contract"]["case_id"], "R1")
        self.assertEqual(manifest["required_project_skills"], ["alpha", "zeta"])

    def test_manifest_rejects_pending_ownership_review(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        mapping = root / "_skill-workbench" / "alpha" / "mapping.md"
        mapping.write_text(
            mapping.read_text(encoding="utf-8").replace(
                "Ownership review: PASS - independently reviewed.",
                "Ownership review: pending independent review.",
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(
            evaluation_manifest.ManifestError,
            "no version 2 mapping contract",
        ):
            evaluation_manifest.build_manifest(
                repo=root,
                case=case,
                mode="green",
                run="green-1",
                output=root / "results" / "green-1.json",
                model="gpt-test",
                schema=root / "_skill-workbench" / "evaluations" / "result-v2.schema.json",
                runner=root / "_skill-workbench" / "scripts" / "run_skill_eval.py",
                timeout=123,
            )

    def test_manifest_validation_detects_catalog_drift(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        runner = root / "_skill-workbench" / "scripts" / "run_skill_eval.py"
        schema = root / "_skill-workbench" / "evaluations" / "result-v2.schema.json"
        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=schema,
            runner=runner,
            timeout=123,
        )
        alpha = root / ".agents" / "skills" / "alpha" / "SKILL.md"
        alpha.write_text(
            "---\nname: alpha\ndescription: Use when changed alpha is central.\n---\n",
            encoding="utf-8",
        )

        errors = evaluation_manifest.validate_manifest(root, manifest, runner=runner)

        self.assertTrue(any("catalog snapshot" in error for error in errors), errors)

    def test_manifest_validation_detects_skill_body_drift(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        runner = root / "_skill-workbench" / "scripts" / "run_skill_eval.py"
        schema = root / "_skill-workbench" / "evaluations" / "result-v2.schema.json"
        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=schema,
            runner=runner,
            timeout=123,
        )
        alpha = root / ".agents" / "skills" / "alpha" / "SKILL.md"
        alpha.write_text(alpha.read_text(encoding="utf-8") + "\nChanged body.\n", encoding="utf-8")

        errors = evaluation_manifest.validate_manifest(root, manifest, runner=runner)

        self.assertTrue(any("package snapshot" in error for error in errors), errors)

    def test_manifest_validation_detects_required_set_tampering(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        runner = root / "_skill-workbench" / "scripts" / "run_skill_eval.py"
        schema = root / "_skill-workbench" / "evaluations" / "result-v2.schema.json"
        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=schema,
            runner=runner,
            timeout=123,
        )
        manifest["required_project_skills"] = ["alpha"]

        errors = evaluation_manifest.validate_manifest(root, manifest, runner=runner)

        self.assertTrue(any("required project skills" in error for error in errors), errors)

    def test_manifest_round_trip_preserves_deterministic_json(self) -> None:
        temporary, root, case = self.make_repository()
        self.addCleanup(temporary.cleanup)
        manifest = evaluation_manifest.build_manifest(
            repo=root,
            case=case,
            mode="green",
            run="green-1",
            output=root / "results" / "green-1.json",
            model="gpt-test",
            schema=root / "_skill-workbench" / "evaluations" / "result-v2.schema.json",
            runner=root / "_skill-workbench" / "scripts" / "run_skill_eval.py",
            timeout=123,
        )
        manifest_path = root / "manifest.json"

        evaluation_manifest.write_manifest(manifest_path, manifest)

        self.assertEqual(json.loads(manifest_path.read_text(encoding="utf-8")), manifest)
        self.assertTrue(manifest_path.read_text(encoding="utf-8").endswith("\n"))


if __name__ == "__main__":
    unittest.main()
