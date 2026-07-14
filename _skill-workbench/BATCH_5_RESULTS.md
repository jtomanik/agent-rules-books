# Rule-Book Skill Conversion Batch 5 Results

Date: 2026-07-14

## Verdict

The final source book, Refactoring.Guru, is accepted as a source-faithful skill
conversion. No meaningful source guidance was removed because another skill
covers similar material. All 38 canonical mini bullets remain exact in the
runtime body, all 17 nano rules are mapped, and the complete canonical full rule
is byte-identical in `references/full.md`.

The accepted post-router behavioral matrix passes source/package fidelity,
required-skill discovery, progressive disclosure, application, and attribution.
All 11 current records include every required skill. Ordinary controls stay in
the compact body `5/5`, focused controls reach full detail `4/5`, and the
comprehensive control reads the full source `1/1`. One nondeterministic E2 run
stays ordinary, and E2 answers add solver-authored numeric heuristics; both are
preserved diagnostics rather than package guidance or release blockers.

Earlier valid failures remain immutable. The initial catalog missed the unnamed
library-gap activation in three runs and used a noncanonical E7 fallback. The
first corrected catalog fixed discovery and E7 but exposed systematic ordinary
over-read plus an invented answer-level technique name. None of those records
was overwritten or retried into a majority result.

## Scope

This batch converted the repository's remaining book under the authoritative
contracts in `_rule-workbench/PROCESS.md`, `_rule-workbench/RELEASE.md`,
`_skill-workbench/PROCESS.md`, and `_skill-workbench/EVALUATION.md`.

| Skill | Shape tested | Catalog role |
| --- | --- | --- |
| `refactoring-guru` | Large smell and named-technique catalog with ordinary, focused, and exhaustive uses | Classify concrete smells and choose the smallest catalog treatment whose preconditions and tradeoffs fit, including incomplete-library-class decisions. |

Its neighbor boundary remains explicit:

- `refactoring` owns ordinary behavior-preserving structural change.
- `clean-code` owns local readability and low-surprise implementation.
- `working-effectively-with-legacy-code` owns gaining first feedback when current behavior is materially unknown.
- Refactoring.Guru owns explicit smell-family classification, named catalog treatment selection, and source-specific treatment detail.

The runtime package uses the established progressive-disclosure shape:

```text
.agents/skills/refactoring-guru/
  SKILL.md
  agents/openai.yaml
  references/index.md
  references/full.md
```

Mappings, fixtures, immutable manifests, result records, and conversion history
remain under `_skill-workbench/` and do not enter the runtime package.

## Conversion Result

| Lines | Mini/skill words | Packaging overhead | Mini wording | Nano mapping | Full sections | Description |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 79 | 1,142/1,289 | 147 | 38/38 exact | 17/17 | 20/20 | 488 chars |

The 38 physical mini bullets use stable traceability IDs `M1-M36`: `M30` and
`M35` each intentionally represent two separate physical bullets. The runtime
package preserves every physical bullet exactly; it does not invent `M37-M38`
to make the IDs match a physical-bullet count.

The primary bias and all eight final-checklist items are exact. Rules are grouped
by concern without paraphrase. Nano supplies activation vocabulary and salience
without becoming a duplicated rules body.

The final hashes are:

- Full source and packaged full: `c92bdfcb8fc5d64a21f10fe268a02bf6a9a9ce6228f83ac85743905cba4b2497`
- Mini: `bb086ec559cbe0814518cf2fc479174244d94028529f870e05820fa7ab7a1a4c`
- Nano: `d909b7fdf6527d6b784fb54c98ae6f03d41e8fb2c53c3992e7b31dcfb7d67c52`
- `SKILL.md`: `f6130665b1f3603a61a6ce13ab15cabeec3e53731334169f34427bebca6b4235`

## Source-Fidelity Repair

Exact mini-to-skill wording is not enough when the mini itself compressed or
altered source semantics. Reverse tracing repaired the canonical mini and nano
before packaging. The repairs restored:

- feature, bug, and review timing;
- smell-versus-style diagnosis;
- rejection of a treatment whose tradeoff is worse than the smell;
- test protection, risky-step checks, brittle-test handling, and the prohibition on deleting tests to manufacture success;
- cleaner-result, re-diagnosis, scope-boundary, and stopping requirements;
- the Rule of Three as a consideration rather than a mandatory abstraction;
- exact `SHOULD` modalities where compression had weakened them;
- correct `M33` null-check traceability and the broader semantic checks' actual ownership.

The canonical full source was never edited. Public mini/nano copies and
workbench copies are byte-identical. The package retains every mini bullet and
routes all 20 full sections through an exact index.

## Catalog And Activation

The initial 14-description catalog was 6,789 bytes at SHA-256
`93d0f9b418a7071997419765278f894a5415bc397085f473b265aca678c6fd4a`.
The unnamed vendor-library fixture validly applied the source judgment but
selected only neighboring skills in all three runs. This isolated a description
discovery defect.

The corrected 488-character description replaces solution-only
`foreign-method-versus-local-extension` vocabulary with the source-backed
symptom: missing operations on an external class that cannot be modified. The
final 14-description catalog is 6,841 bytes at SHA-256
`f23977d3f201fc519c399fef75d7ed8d0f3b80e08f56da7a8659ad9c68d71a82`.
Independent audit reproduced the exact payload and approved every active
ownership contract before new manifests were created.

The description correction does not repeat the full treatment. It only makes
the activation condition discoverable. The compact body still gives the
narrow-versus-substantial rule, while migration and vendor-update compatibility
remain focused `Technique Playbook` detail.

## Progressive Disclosure

The final router distinguishes three levels:

1. Use `SKILL.md` alone when its rules resolve smell classification, treatment comparison, risk ordering, verification, and stopping.
2. Read the index and the smallest full sections only for source detail absent from the body, including exact treatment triads, named-technique conditions and steps, or incomplete-library migration/update compatibility.
3. Read the full reference end to end only for an explicit complete catalog audit.

The accepted current matrix records modes `6 ordinary / 4 focused / 1
comprehensive`. The semantic controls are:

- Ordinary: E1 x3, E3, and E6 pass `5/5` body-only.
- Focused: E2 x3, E4, and E7 reach full detail `4/5`; E2 run 3 is the one preserved body-only miss.
- Comprehensive: E5b records a complete `*` read.

E7 reads eight of 20 Refactoring.Guru sections and 14 of 20 Refactoring
sections. This is material context-cost evidence but not systematic tier
collapse: it occurs in one complex two-skill case, reaches the intended
sections, and returns the canonical hierarchy-collapse fallback.

## Behavioral History

### Initial Catalog

- E1 direct discovery selected Refactoring.Guru `3/3`.
- E2 unnamed discovery missed Refactoring.Guru `0/3` despite applying the relevant judgment.
- E3-E6 passed their application controls.
- E7 selected both required skills but stayed body-only and substituted a factory/registry fallback for the canonical hierarchy-collapse fallback.

These were valid behavioral failures, not harness errors. They remain attached
to the 6,789-byte catalog.

### Corrected Catalog

The source-backed description and first router correction produced 11 valid
records with required inclusion `11/11` and repaired E7. Independent attribution
review still failed this snapshot because:

- two of three E1 runs and E3 over-read focused references;
- one E1 body-only answer presented `Remove Comments` as a named technique;
- one E2 run stayed ordinary and introduced contradictory numeric escalation thresholds.

This snapshot remains immutable. The package was not changed to legitimize the
solver's invented technique name or thresholds.

### Accepted Post-Router Matrix

The second router correction changes only loading policy. It tells agents not to
open references merely to confirm a body-supported answer and explicitly routes
the E2 migration/update request to existing source detail.

All 11 accepted records use unique task IDs, inner exit zero, the same catalog,
the same frozen mapping, unique manifest hashes, and empty selection, integrity,
manifest, and Codex error arrays. Every required set is a subset of the selected
skills.

E1, E3, E4, E5b, E6, and E7b pass without an attribution finding. E2 passes
with diagnostics: all three runs select Refactoring.Guru, two load focused
source, and one stays ordinary. All three add some solver-authored numeric
specificity. The package itself preserves the canonical boundary and none of
the answers claims those numbers are source-defined rules, so the additions are
recorded as answer-level diagnostics rather than imported package guidance.

## Process Learnings

Batch 5 adds three durable corrections:

1. **Stable traceability IDs are authoritative.** Physical bullet count and ID count may differ when one accepted ID spans multiple separate bullets. Validators must check both without inventing IDs.
2. **Classify every requested output.** A case is focused when its main decision is compact but a requested migration, compatibility, precondition, exact triad, or other detail exists only in full.
3. **Make the ordinary stop explicit.** References are not opened merely to confirm or elaborate a body-supported answer. Focused catch-alls still keep every full section reachable.

The batch also confirms the established acceptance hierarchy:

- unsupported package guidance or removed source content is a release blocker;
- false attribution to the book is an answer failure;
- compatible or unsupported solver additions remain answer-level diagnostics unless package wording caused them;
- additional relevant skills are permitted;
- selection checks require every intended skill, not exactly one skill;
- one nondeterministic disclosure miss is preserved and reviewed for materiality rather than retried into disappearance.

## Final Verification

- `validate_conversion.py` across all 14 live skills: all pass; only previously documented soft packaging-overhead warnings remain.
- `check_rule_wording.py`: `38/38` Refactoring.Guru mini bullets match exactly, with exact primary bias and checklist.
- Official `quick_validate.py`: `Skill is valid!`.
- `python3 -m unittest discover ...`: `53/53` tests pass.
- `validate_evaluation_contracts.py`: durable required-skill and versioned contracts pass.
- `cmp` and SHA-256 checks: canonical/workbench mini and nano copies match, and packaged full is byte-identical to canonical full.
- README metrics match the final 64-line mini and 41-line nano files.
- Accepted matrix: 11 records, 11 unique task IDs, required inclusion `11/11`, no hard-gate errors.
- Independent final attribution review: PASS with the E2 and E7 diagnostics retained above.
- `git diff --check`, scoped trailing-whitespace scan, and scoped final-newline scan: all pass; unrelated `.superpowers/` scratch remains untouched.
