#!/usr/bin/env python3
"""Build and validate reproducible guidance-skill evaluation manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_evaluation_contracts import (  # noqa: E402
    BACKTICK_VALUE,
    SHA256_VALUE,
    contract_version,
    mapping_cases,
    normalized_scalar,
    parse_skill_set,
)


MANIFEST_VERSION = 2
DEFAULT_SCHEMA = Path("_skill-workbench/evaluations/result-v2.schema.json")
DEFAULT_RUNNER = Path("_skill-workbench/scripts/run_skill_eval.py")
RUN_CONFIGURATION = {
    "ignore_user_config": True,
    "ephemeral": True,
    "sandbox": "read-only",
    "green_workspace": "repository",
    "baseline_workspace": "temporary directory without project skills",
}


class ManifestError(ValueError):
    """Raised when frozen evaluation inputs cannot form a valid manifest."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def repository_path(repo: Path, path: Path, label: str) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(repo.resolve()).as_posix()
    except ValueError as error:
        raise ManifestError(f"{label} must be inside the repository: {path}") from error


def frontmatter_description(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ManifestError(f"SKILL.md has no YAML frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ManifestError(f"SKILL.md frontmatter is not closed: {path}") from error
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ManifestError(f"unsupported SKILL.md frontmatter line in {path}: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    description = fields.get("description", "")
    if not description:
        raise ManifestError(f"SKILL.md description is empty: {path}")
    return description


def catalog_snapshot(repo: Path) -> dict[str, Any]:
    skill_files = sorted((repo / ".agents" / "skills").glob("*/SKILL.md"))
    if not skill_files:
        raise ManifestError("live catalog is empty: .agents/skills/*/SKILL.md not found")
    entries = [
        {"name": path.parent.name, "description": frontmatter_description(path)}
        for path in skill_files
    ]
    payload = "".join(
        f"{entry['name']}\t{entry['description']}\n" for entry in entries
    ).encode("utf-8")
    return {
        "skill_count": len(entries),
        "byte_count": len(payload),
        "sha256": sha256_bytes(payload),
        "entries": entries,
    }


def package_snapshot(repo: Path) -> dict[str, Any]:
    skill_root = repo / ".agents" / "skills"
    files = sorted(
        path
        for pattern in ("*/SKILL.md", "*/references/index.md", "*/references/full.md")
        for path in skill_root.glob(pattern)
    )
    if not files:
        raise ManifestError("live package is empty: .agents/skills skill and reference files not found")
    entries = [
        {
            "path": repository_path(repo, path, "package file"),
            "byte_count": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in files
    ]
    payload = "".join(
        f"{entry['path']}\t{entry['byte_count']}\t{entry['sha256']}\n"
        for entry in entries
    ).encode("utf-8")
    return {
        "file_count": len(entries),
        "byte_count": sum(entry["byte_count"] for entry in entries),
        "sha256": sha256_bytes(payload),
        "entries": entries,
    }


def case_contract(repo: Path, case: Path) -> dict[str, Any]:
    case_relative = repository_path(repo, case, "case")
    matches: list[dict[str, Any]] = []
    for mapping in sorted((repo / "_skill-workbench").glob("*/mapping.md")):
        lines = mapping.read_text(encoding="utf-8").splitlines()
        mapping_version = contract_version(lines)
        for case_id, fields in mapping_cases(lines):
            path_match = BACKTICK_VALUE.search(fields.get("prompt or artifact", ""))
            if not path_match or Path(path_match.group(1)).as_posix() != case_relative:
                continue
            case_version = normalized_scalar(fields.get("contract version", ""))
            if mapping_version != 2 and case_version != "2":
                continue
            ownership = normalized_scalar(fields.get("ownership review", ""))
            if not re.match(r"^pass\b", ownership):
                continue
            required = parse_skill_set(fields.get("required skills", ""))
            if required is None:
                raise ManifestError(
                    f"{mapping.relative_to(repo)} {case_id} has no explicit required-skill set"
                )
            digest_match = SHA256_VALUE.search(fields.get("fixture sha-256", ""))
            if not digest_match:
                raise ManifestError(
                    f"{mapping.relative_to(repo)} {case_id} has no fixture SHA-256"
                )
            matches.append(
                {
                    "mapping": repository_path(repo, mapping, "mapping"),
                    "mapping_sha256": sha256_file(mapping),
                    "case_id": case_id,
                    "evaluation_contract_version": 2,
                    "fixture_sha256": digest_match.group(1).lower(),
                    "required_project_skills": sorted(required),
                }
            )
    if not matches:
        raise ManifestError(f"no version 2 mapping contract found for {case_relative}")
    if len(matches) > 1:
        labels = ", ".join(f"{match['mapping']} {match['case_id']}" for match in matches)
        raise ManifestError(f"multiple mapping contracts found for {case_relative}: {labels}")
    return matches[0]


def build_manifest(
    *,
    repo: Path,
    case: Path,
    mode: str,
    run: str,
    output: Path,
    model: str,
    schema: Path,
    runner: Path,
    timeout: int,
) -> dict[str, Any]:
    repo = repo.resolve()
    case = case.resolve()
    schema = schema.resolve()
    runner = runner.resolve()
    output = output.resolve()
    if mode not in {"baseline", "green"}:
        raise ManifestError(f"unsupported evaluation mode: {mode}")
    if not run.strip():
        raise ManifestError("run name must not be empty")
    if not model.strip():
        raise ManifestError("model must not be empty")
    if timeout <= 0:
        raise ManifestError("timeout must be positive")
    for label, path in (("case", case), ("schema", schema), ("runner", runner)):
        if not path.is_file():
            raise ManifestError(f"{label} file not found: {path}")
    repository_path(repo, output, "output")

    contract = case_contract(repo, case)
    case_sha256 = sha256_file(case)
    if contract["fixture_sha256"] != case_sha256:
        raise ManifestError(
            "mapping fixture SHA-256 differs from the current case: "
            f"expected {contract['fixture_sha256']}, actual {case_sha256}"
        )
    required_skills = contract["required_project_skills"] if mode == "green" else []
    return {
        "manifest_version": MANIFEST_VERSION,
        "contract": contract,
        "catalog": catalog_snapshot(repo),
        "packages": package_snapshot(repo),
        "case": {
            "path": repository_path(repo, case, "case"),
            "sha256": case_sha256,
        },
        "required_project_skills": required_skills,
        "execution": {
            "mode": mode,
            "run": run,
            "model": model,
            "timeout": timeout,
            "output": repository_path(repo, output, "output"),
            "schema": {
                "path": repository_path(repo, schema, "schema"),
                "sha256": sha256_file(schema),
            },
            "runner": {
                "path": repository_path(repo, runner, "runner"),
                "sha256": sha256_file(runner),
            },
            "configuration": dict(RUN_CONFIGURATION),
        },
    }


def validate_manifest(repo: Path, manifest: dict[str, Any], *, runner: Path) -> list[str]:
    errors: list[str] = []
    if manifest.get("manifest_version") != MANIFEST_VERSION:
        errors.append(
            f"unsupported manifest version: {manifest.get('manifest_version')!r}"
        )
        return errors
    try:
        case_data = manifest["case"]
        execution = manifest["execution"]
        schema_data = execution["schema"]
        expected = build_manifest(
            repo=repo,
            case=repo / case_data["path"],
            mode=execution["mode"],
            run=execution["run"],
            output=repo / execution["output"],
            model=execution["model"],
            schema=repo / schema_data["path"],
            runner=runner,
            timeout=execution["timeout"],
        )
    except (KeyError, TypeError, ManifestError, OSError, UnicodeError) as error:
        errors.append(f"cannot reproduce manifest: {error}")
        return errors

    comparisons = (
        ("contract", "mapping contract"),
        ("catalog", "catalog snapshot"),
        ("packages", "package snapshot"),
        ("case", "case evidence"),
        ("required_project_skills", "required project skills"),
        ("execution", "execution contract"),
    )
    for field, label in comparisons:
        if manifest.get(field) != expected.get(field):
            errors.append(f"{label} differs from current repository state")
    return errors


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    if path.exists():
        raise ManifestError(f"manifest already exists; use a new run name: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--mode", choices=("baseline", "green"), required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--runner", type=Path, default=DEFAULT_RUNNER)
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    repo = args.repo.resolve()
    try:
        manifest = build_manifest(
            repo=repo,
            case=(repo / args.case).resolve() if not args.case.is_absolute() else args.case,
            mode=args.mode,
            run=args.run,
            output=(repo / args.output).resolve() if not args.output.is_absolute() else args.output,
            model=args.model,
            schema=(repo / args.schema).resolve() if not args.schema.is_absolute() else args.schema,
            runner=(repo / args.runner).resolve() if not args.runner.is_absolute() else args.runner,
            timeout=args.timeout,
        )
        manifest_path = (
            (repo / args.manifest).resolve()
            if not args.manifest.is_absolute()
            else args.manifest
        )
        repository_path(repo, manifest_path, "manifest")
        write_manifest(manifest_path, manifest)
    except (ManifestError, OSError, UnicodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"wrote {manifest_path} "
        f"(catalog {manifest['catalog']['sha256']}, "
        f"required {manifest['required_project_skills']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
