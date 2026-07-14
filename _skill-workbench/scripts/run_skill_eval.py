#!/usr/bin/env python3
"""Run one blind guidance-skill evaluation case through Codex."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import evaluation_manifest


BLIND_WRAPPER = """\
Solve the task below as a read-only engineering analysis. Use project skills naturally when they are available, but do not force a skill merely because it exists.

For repository book guidance, use only `.agents/skills` packages discovered through normal skill selection. Do not inspect top-level canonical book directories, canonical full/mini/nano rule files, compatibility documents, `_skill-workbench`, mapping files, evaluation files, or expected results. Do not modify any file.

Reporting fields only describe reads the task already required. Never open a skill or reference to populate reporting fields, confirm an answer, or make the record look complete.

In the structured result:
- `answer` is the complete user-facing answer.
- `selected_project_skills` lists only repository book skills whose `.agents/skills/<name>/SKILL.md` was actually consulted; omit global process skills.
- `consulted_files` lists every `.agents/skills` skill or reference file read and no canonical source files.
- `consulted_reference_sections` lists each selected project skill whose `full.md` was read with the exact level-two headings consulted. Use `sections: ["*"]` only for an end-to-end full-reference read. When no `full.md` was read, the entire field must be the empty array `[]`; do not add an entry for a `SKILL.md`-only read. Do not encode the empty list as a section string such as `sections: ["[]"]`.
- `reference_mode` is `none` when no repository book skill was read, `ordinary` for skill body only, `focused` whenever an index or bounded `full.md` section was read, or `comprehensive` for an end-to-end full-reference read.

Task:

{case}
"""


def build_prompt(case: str) -> str:
    return BLIND_WRAPPER.format(case=case.strip())


def build_command(
    *, cwd: Path, model: str, schema: Path, output_message: Path, prompt: str
) -> list[str]:
    return [
        "rtk",
        "codex",
        "exec",
        "--ignore-user-config",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--json",
        "--model",
        model,
        "--output-schema",
        str(schema),
        "--output-last-message",
        str(output_message),
        "--cd",
        str(cwd),
        prompt,
    ]


def extract_thread_id(events: str) -> str | None:
    for line in events.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started":
            value = event.get("thread_id")
            return value if isinstance(value, str) else None
    return None


def extract_error_messages(events: str) -> list[str]:
    messages: list[str] = []
    for line in events.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        message: object = None
        if event.get("type") == "error":
            message = event.get("message")
        elif event.get("type") == "turn.failed":
            error = event.get("error")
            if isinstance(error, dict):
                message = error.get("message")
        if isinstance(message, str) and message and message not in messages:
            messages.append(message)
    return messages


def clean_stderr(stderr: str) -> str:
    ignored = (
        "Reading additional input from stdin...",
        "state db discrepancy during find_thread_path_by_id_str_in_subdir: falling_back",
    )
    return "\n".join(
        line for line in stderr.splitlines() if not any(value in line for value in ignored)
    ).strip()


def validate_result_integrity(result: dict[str, object]) -> list[str]:
    errors: list[str] = []
    selected = result.get("selected_project_skills")
    consulted = result.get("consulted_files")
    sections = result.get("consulted_reference_sections")
    mode = result.get("reference_mode")
    if not isinstance(selected, list) or not all(isinstance(value, str) for value in selected):
        return ["selected_project_skills must be a list of strings"]
    if not isinstance(consulted, list) or not all(isinstance(value, str) for value in consulted):
        return ["consulted_files must be a list of strings"]
    if not isinstance(sections, list):
        return ["consulted_reference_sections must be a list"]
    section_map: dict[str, list[str]] = {}
    for entry in sections:
        if not isinstance(entry, dict) or set(entry) != {"skill", "sections"}:
            return ["consulted_reference_sections entries require skill and sections"]
        name = entry.get("skill")
        headings = entry.get("sections")
        if not isinstance(name, str) or not name or not isinstance(headings, list) or not headings:
            return ["consulted_reference_sections entries require a skill and non-empty sections"]
        if not all(isinstance(heading, str) and heading for heading in headings):
            return ["consulted_reference_sections headings must be non-empty strings"]
        if name in section_map:
            errors.append(f"consulted_reference_sections contains duplicate skill {name}")
        section_map[name] = headings
        if "*" in headings and headings != ["*"]:
            errors.append(f"consulted_reference_sections {name} mixes * with headings")

    marker = ".agents/skills/"
    consulted_skills: set[str] = set()
    read_skill_files: set[str] = set()
    index_skills: set[str] = set()
    full_skills: set[str] = set()
    for path in consulted:
        if marker not in path:
            errors.append(f"consulted file is outside .agents/skills: {path}")
            continue
        relative = path.split(marker, 1)[1]
        parts = relative.split("/")
        if len(parts) < 2 or not parts[0]:
            errors.append(f"consulted file has no skill name: {path}")
            continue
        name = parts[0]
        consulted_skills.add(name)
        suffix = "/".join(parts[1:])
        if suffix == "SKILL.md":
            read_skill_files.add(name)
        elif suffix == "references/index.md":
            index_skills.add(name)
        elif suffix == "references/full.md":
            full_skills.add(name)

    selected_set = set(selected)
    if len(selected_set) != len(selected):
        errors.append("selected_project_skills contains duplicates")
    if selected_set != read_skill_files:
        errors.append(
            "selected_project_skills must exactly match consulted SKILL.md files: "
            f"selected={sorted(selected_set)}, consulted={sorted(read_skill_files)}"
        )
    if consulted_skills != read_skill_files:
        errors.append("every consulted reference must have its skill SKILL.md in consulted_files")

    section_skills = set(section_map)
    if section_skills != full_skills:
        errors.append(
            "consulted_reference_sections must exactly match skills whose full.md was read: "
            f"sections={sorted(section_skills)}, full={sorted(full_skills)}"
        )
    if not section_skills <= selected_set:
        errors.append("consulted_reference_sections names must be selected project skills")
    comprehensive_skills = {
        name for name, headings in section_map.items() if headings == ["*"]
    }

    if mode == "none":
        if consulted or selected or section_map:
            errors.append("reference_mode none requires no selected or consulted project skills")
    elif mode == "ordinary":
        if not selected or index_skills or full_skills or section_map:
            errors.append("reference_mode ordinary requires SKILL.md files and no references")
    elif mode == "focused":
        if (
            not selected
            or not (index_skills or full_skills)
            or comprehensive_skills
        ):
            errors.append(
                "reference_mode focused requires SKILL.md plus index.md or bounded full.md sections"
            )
    elif mode == "comprehensive":
        if not selected or not full_skills or not comprehensive_skills:
            errors.append(
                "reference_mode comprehensive requires SKILL.md, full.md, and a * section record"
            )
    else:
        errors.append(f"unsupported reference_mode: {mode!r}")
    return errors


def validate_required_skill_inclusion(
    result: dict[str, object], required_skills: list[str]
) -> list[str]:
    selected = result.get("selected_project_skills")
    selected_set = set(selected) if isinstance(selected, list) else set()
    return [
        f"required project skill not selected: {name}"
        for name in sorted(set(required_skills) - selected_set)
    ]


def validate_record_against_manifest(
    record: dict[str, object], manifest: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    case = manifest.get("case", {})
    execution = manifest.get("execution", {})
    comparisons = (
        ("case", case.get("path"), "record case differs from manifest"),
        ("case_sha256", case.get("sha256"), "record case SHA-256 differs from manifest"),
        ("mode", execution.get("mode"), "record mode differs from manifest"),
        ("run", execution.get("run"), "record run differs from manifest"),
        ("model", execution.get("model"), "record model differs from manifest"),
        (
            "configuration",
            execution.get("configuration"),
            "record configuration differs from manifest",
        ),
        (
            "required_project_skills",
            manifest.get("required_project_skills"),
            "record required project skills differ from manifest",
        ),
    )
    for field, expected, message in comparisons:
        if record.get(field) != expected:
            errors.append(message)
    return errors


def load_manifest_arguments(repo: Path, manifest_path: Path) -> argparse.Namespace:
    repo = repo.resolve()
    manifest_path = manifest_path.resolve()
    try:
        manifest_value = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise evaluation_manifest.ManifestError(
            f"cannot read evaluation manifest {manifest_path}: {error}"
        ) from error
    if not isinstance(manifest_value, dict):
        raise evaluation_manifest.ManifestError("evaluation manifest must be a JSON object")
    errors = evaluation_manifest.validate_manifest(
        repo,
        manifest_value,
        runner=Path(__file__).resolve(),
    )
    if errors:
        raise evaluation_manifest.ManifestError("; ".join(errors))
    try:
        case = repo / manifest_value["case"]["path"]
        execution = manifest_value["execution"]
        output = repo / execution["output"]
        schema = repo / execution["schema"]["path"]
        required_skills = manifest_value["required_project_skills"]
        if not isinstance(required_skills, list) or not all(
            isinstance(value, str) for value in required_skills
        ):
            raise TypeError("required_project_skills must be a list of strings")
    except (KeyError, TypeError) as error:
        raise evaluation_manifest.ManifestError(
            f"evaluation manifest has an invalid execution envelope: {error}"
        ) from error
    if output.exists():
        raise evaluation_manifest.ManifestError(
            f"output already exists; use a new run name: {output}"
        )
    return argparse.Namespace(
        case=case,
        mode=execution["mode"],
        run=execution["run"],
        required_skill=list(required_skills),
        output=output,
        model=execution["model"],
        repo=repo,
        schema=schema,
        timeout=execution["timeout"],
        evaluation_manifest=manifest_value,
        evaluation_manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    )


def codex_version() -> str:
    result = subprocess.run(
        ["rtk", "codex", "--version"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() or result.stderr.strip() or "unknown"


def run(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    case_path = args.case.resolve()
    schema = args.schema.resolve()
    output_path = args.output.resolve()
    case_text = case_path.read_text(encoding="utf-8")
    prompt = build_prompt(case_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="skill-eval-") as temporary:
        cwd = repo if args.mode == "green" else Path(temporary)
        final_message = Path(temporary) / "final.json"
        command = build_command(
            cwd=cwd,
            model=args.model,
            schema=schema,
            output_message=final_message,
            prompt=prompt,
        )
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=args.timeout,
        )
        final_text = final_message.read_text(encoding="utf-8") if final_message.exists() else ""
        try:
            final_result = json.loads(final_text) if final_text else None
        except json.JSONDecodeError:
            final_result = None
        integrity_errors = (
            validate_result_integrity(final_result) if isinstance(final_result, dict) else []
        )
        required_skills = sorted(set(getattr(args, "required_skill", [])))
        selection_errors = (
            validate_required_skill_inclusion(final_result, required_skills)
            if args.mode == "green" and isinstance(final_result, dict)
            else []
        )

        record = {
            "case": str(case_path.relative_to(repo)),
            "case_sha256": hashlib.sha256(case_text.encode("utf-8")).hexdigest(),
            "mode": args.mode,
            "run": args.run,
            "model": args.model,
            "codex_version": codex_version(),
            "configuration": dict(evaluation_manifest.RUN_CONFIGURATION),
            "thread_id": extract_thread_id(completed.stdout),
            "exit_code": completed.returncode,
            "codex_errors": extract_error_messages(completed.stdout),
            "result": final_result,
            "integrity_errors": integrity_errors,
            "required_project_skills": required_skills,
            "selection_errors": selection_errors,
            "stderr": clean_stderr(completed.stderr),
        }
        manifest_errors: list[str] = []
        manifest = getattr(args, "evaluation_manifest", None)
        if isinstance(manifest, dict):
            manifest_errors = validate_record_against_manifest(record, manifest)
            record["evaluation_manifest"] = manifest
            record["evaluation_manifest_sha256"] = args.evaluation_manifest_sha256
            record["manifest_errors"] = manifest_errors
        output_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    if completed.returncode != 0:
        print(completed.stderr, file=sys.stderr)
        return completed.returncode or 1
    if final_result is None:
        print("Codex did not produce valid structured output", file=sys.stderr)
        return 1
    if integrity_errors:
        for error in integrity_errors:
            print(f"result integrity error: {error}", file=sys.stderr)
        return 1
    if selection_errors:
        for error in selection_errors:
            print(f"selection acceptance error: {error}", file=sys.stderr)
        return 1
    if manifest_errors:
        for error in manifest_errors:
            print(f"manifest integrity error: {error}", file=sys.stderr)
        return 1
    print(f"wrote {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--case", type=Path)
    parser.add_argument("--mode", choices=("baseline", "green"))
    parser.add_argument("--run")
    parser.add_argument(
        "--required-skill",
        action="append",
        default=[],
        help="Project skill that every GREEN result must include; repeat for multiple targets.",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--model")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--timeout", type=int)
    args = parser.parse_args()
    repo = args.repo.resolve()
    if args.manifest:
        conflicts = {
            "--case": args.case,
            "--mode": args.mode,
            "--run": args.run,
            "--required-skill": args.required_skill,
            "--output": args.output,
            "--model": args.model,
            "--schema": args.schema,
            "--timeout": args.timeout,
        }
        supplied = [name for name, value in conflicts.items() if value]
        if supplied:
            parser.error(f"--manifest cannot be combined with {', '.join(supplied)}")
        manifest_path = args.manifest if args.manifest.is_absolute() else repo / args.manifest
        try:
            manifest_args = load_manifest_arguments(repo, manifest_path)
        except evaluation_manifest.ManifestError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            return 1
        return run(manifest_args)

    missing = [
        name
        for name, value in (
            ("--case", args.case),
            ("--mode", args.mode),
            ("--run", args.run),
            ("--output", args.output),
        )
        if not value
    ]
    if missing:
        parser.error(f"direct mode requires {', '.join(missing)}")
    args.model = args.model or "gpt-5.4"
    args.schema = args.schema or Path(
        "_skill-workbench/evaluations/result-v2.schema.json"
    )
    args.timeout = args.timeout or 900
    args.evaluation_manifest = None
    args.evaluation_manifest_sha256 = None
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
