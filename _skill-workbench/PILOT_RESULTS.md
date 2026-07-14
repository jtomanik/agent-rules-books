# Rule-Book Skill Conversion Pilot Results

Date: 2026-07-12

## Verdict

The manual conversion architecture and all four runtime pilots are accepted for the next conversion batch. The preserved evaluation retrofit includes skill-disabled controls, durable raw cases, repeated high-risk runs, catalog-null diagnostics, reviewer traces, and result-integrity checks. Under the 2026-07-13 policy, source/package fidelity and required-skill inclusion are acceptance gates; extra skill selections and general solver knowledge are diagnostic. No pilot needs to be redone.

The three pilot shapes preserved progressive disclosure:

1. Skill metadata decides whether the lens is relevant.
2. `SKILL.md` provides complete normal-use guidance derived from mini.
3. `references/index.md` routes focused questions into the canonical full rule.
4. `references/full.md` preserves the exhaustive rule and remains available for complete reads.

Nano remains useful as activation, salience, routing, and final-check evidence. It is not shipped as a second reference because its authoritative guidance is already represented by the complete mini rules.

## Pilot Shapes

| Shape | Conversion | Why it was selected |
| --- | --- | --- |
| Broad, high-frequency guidance | `clean-code` | Tests whether a common code-quality lens can activate on distinctive symptoms without becoming an always-on generic coding skill. |
| Specialized operational guidance | `release-it` | Tests a narrower lens with concrete production-failure, overload, recovery, and operability triggers. |
| High-overlap neighboring guidance | `refactoring` plus `working-effectively-with-legacy-code` | Tests whether descriptions and bodies can preserve a meaningful boundary while permitting ordered co-invocation. |

The third shape intentionally produced two skills. It cannot validate overlap if only one side of the boundary exists in the live catalog.

## Deterministic Results

| Skill | Lines | Mini/skill words | Packaging overhead | Mini wording | Nano mapping | Full sections | Full copy | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| `clean-code` | 68 | 582/731 | 149 | 22/22 exact | 10/10 | 22/22 | Byte-identical | Static and behavioral pass |
| `release-it` | 69 | 848/1020 | 172 | 22/22 exact | 12/12 | 22/22 | Byte-identical | Pass; documented soft-target warning |
| `refactoring` | 67 | 739/842 | 103 | 24/24 exact | 14/14 | 20/20 | Byte-identical | Static and behavioral pass |
| `working-effectively-with-legacy-code` | 71 | 796/922 | 126 | 23/23 exact | 12/12 | 18/18 | Byte-identical | Static and behavioral pass |

Across the pilots, all four primary biases, all 91 mini decision and trigger rules, and all final-checklist items in source order match exactly. No rule was added, omitted, merged, or reworded.

`validate_conversion.py` also passed folder/name agreement, frontmatter and 500-character description constraints, source-driven size exceptions, the 150-word packaging-overhead soft target and 200-word hard maximum, UI metadata constraints, direct reference links, full-reference equality, exact heading anchors and line ranges, complete `M*` and `N*` mapping, and placeholder checks.

## Original Behavioral Results

These are useful historical runtime observations. The conversions predate the current result-integrity protocol, and the exact prompts and artifacts were not retained consistently. Later retrofit evidence supplies the current required-skill and disclosure checks; source/package acceptance does not depend on proving a RED-to-GREEN improvement.

### Broad skill

Fresh-agent probes selected `clean-code` for explicit local-readability symptoms and did not select it for generic code explanation, legacy characterization, or pure refactoring mechanics. A focused ambiguity loaded the index and two bounded full sections. A comprehensive audit read the 297-line full reference end to end. A mixed reliability-and-readability task selected compatible skills for separate concerns.

### Specialized skill

Fresh-agent probes selected `release-it` for remote-provider failure handling, a disputed supervised-consumer stability decision, and an explicit comprehensive audit. A pure-function rename and split did not select it. Ordinary work used the skill body, focused work routed into relevant full sections, and comprehensive work read the 382-line full reference.

### Overlap pair

Fresh-agent probes produced the intended boundary:

- A well-tested behavior-preserving long-method and conditional cleanup selected `refactoring` alone.
- An untested class with constructor database I/O, ambient time, and uncertain behavior selected `working-effectively-with-legacy-code` alone.
- A mixed task selected Legacy Code first to establish characterization and seams, then Refactoring for the protected structural change.
- A greenfield in-memory API-design task selected neither overlap skill. It legitimately selected Clean Code and general interface-design guidance instead.

The focused probes consulted each index and only the relevant full sections. The mixed probe kept structural preparation separate from the requested semantic change.

## Evaluation Retrofit

- Clean Code's focused command-query case now consistently distinguishes a strict non-returning population command plus nonmutating query from a load-and-return exception. Its ordinary, focused, comprehensive, pressure, and Legacy-neighbor roles are accepted.
- Release It!'s hotspot and supervised-consumer cases select only Release It! with focused disclosure in `3/3`; malformed downstream data remains a dependency-contract failure in `3/3`. The new one-decision ordinary control uses `SKILL.md` alone in `3/3`, and the comprehensive audit remains exhaustive.
- The Refactoring/Legacy boundary is stable: well-tested cleanup excludes Legacy `3/3`; blocked-first-feedback work selects only Legacy `3/3`; mixed work selects Legacy then Refactoring with focused disclosure `6/6`; greenfield work selects neither; both solo comprehensive controls pass.
- Catalog-null selects no book skill in `3/3` final runs.
- One multi-concern carrier case still alternates between ordinary and focused disclosure, and one frozen mixed case prescribed a less-safe patch order. Both are retained as case-design evidence and have predeclared replacement controls; neither is treated as a runtime guidance defect.
- The runner now rejects selected/consulted mismatches, references without a consulted skill, non-packaged book paths, and disclosure modes inconsistent with opened files. Contradictory records are preserved under explicit invalid names and excluded from final evidence.

## Process Corrections

The pilots and their process review exposed these details, now incorporated into the canonical process and `_skill-workbench/EVALUATION.md`:

1. **Wording preservation must be mechanically checked.** Manual review alone is too weak for detecting small modal, qualifier, exception, primary-bias, or final-checklist changes. `check_rule_wording.py` checks rule multisets plus exact bias and checklist order.
2. **Index ranges need one canonical convention.** A section range now ends at the last non-empty line before the next level-two heading or end of file. This removes harmless but noisy differences between converters.
3. **Structural validation must be reproducible locally.** `validate_conversion.py` replaces the pilot's one-off aggregate command and checks the conversion-specific contract. The installed `skill-creator` validator also passes for all four skills when run through `uv run --with pyyaml`; it complements rather than replaces the repository validator.
4. **Source fidelity is the primary acceptance gate.** A good answer cannot compensate for unsupported, strengthened, weakened, or invented package guidance.
5. **Discovery, application, disclosure, and package fidelity are separate evidence.** Required-skill omission and material disclosure collapse can fail their own gates; general answer variance remains diagnostic unless the package caused it.
6. **Positive discovery uses inclusion.** Every required target must be selected; additional relevant skills and their order do not fail the case.
7. **Context budgets must account for the source and clarity.** Every pilot mini already exceeds 500 words. Packaging overhead now has a 150-word review target and 200-word hard maximum; a small documented overage is preferable to compressing activation or routing guidance.
8. **Mapping must not duplicate the semantic index.** `references/index.md` is now the single source of truth for `Read when` guidance.
9. **Catalog growth needs positive regression and independent review.** Repeated direct and unnamed cases must retain required targets; broad, null, and ambiguous cases diagnose context cost, and the converter cannot provide final semantic acceptance.
10. **Positive activation thresholds outperform long negative lists.** Repeating neighbor-case terms inside exclusions can itself increase accidental selection. State what must be central or blocked, then use only the minimum necessary exclusions.
11. **Focused routing needs evidence thresholds.** Bare `ambiguity`, `detail`, and `hotspot` invite reference over-reading. Use explicit disputes, demonstrated hotspots, or book-specific unresolved decisions, and state when ordinary work stops at `SKILL.md`.
12. **Preserve historical contracts when policy changes.** Keep the original observation, then add a current-policy reclassification rather than rewriting evidence.
13. **Skill-disabled baselines are optional diagnostics.** They can measure incremental value or calibrate disclosure, but a pretrained model's prior knowledge does not determine conversion faithfulness.
14. **Structured output still needs relational validation.** JSON-schema-valid fields can contradict one another; the harness must check selected skills, consulted files, and disclosure mode as one evidence record.

## Limits And Follow-Up Risk

- Three runs are a stability probe, not a statistical guarantee; future catalog growth can expose new collisions.
- `consulted_files` proves package isolation but not exact line ranges read inside `full.md`; v2 heading records capture observed access while independent review checks whether package guidance remains source-faithful.
- Some controls have a strong skill-disabled baseline and therefore validate selection or disclosure rather than behavioral improvement.
- The live catalog contains only the converted pilots. Collisions with future Clean Architecture, DDIA, Code Complete, Refactoring Guru, and other book skills still require catalog-level tests when those skills are added.
- Exact wording does not by itself prove correct grouping or application. Manual semantic review and forward testing remain required.
- Canonical full-rule edits can stale copied references and line ranges. Both validators must be rerun after source changes.
- The repository validator checks the documented local contract; it does not replace future constraints added by an official validator.

## Scaling Decision

Proceed to the next three books. Keep the current pilots as the regression catalog; no bounded rework remains queued for them.

Use one manual conversion thread per rule book, with disjoint file ownership and a separate reviewer. Do not build an automatic prose translator. Automate source-copy equality, wording fidelity, metadata shape, context budgets, mapping completeness, links, anchors, ranges, result integrity, and catalog test execution; keep lens definition, concern grouping, description design, `Read when` guidance, application fidelity, and collision judgments manual.
