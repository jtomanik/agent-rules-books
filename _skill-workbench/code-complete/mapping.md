# Code Complete Skill Mapping

## Scope

- Distinctive lens: disciplined software construction that coordinates defect-risk decisions across requirements and architecture fit, routines and data, control flow, defensive boundaries, errors, verification, integration, tooling, and measured tuning.
- Intended invocation: invoke `code-complete` across the canonical implementation, change, review, debugging, refactoring, and tuning contexts when a nontrivial task coordinates several construction concerns or a nano-derived pressure signal threatens defect control. Solution-first coding, happy-path-only tests, mixed behavior/refactoring, guess-driven debugging that is already driving a code change, and evidence-free tuning are independent activation branches.
- Positive boundary: generic task labels remain insufficient. Code Complete owns one coordinated construction decision; `clean-code`, `refactoring`, `working-effectively-with-legacy-code`, `release-it`, `clean-architecture`, or DDIA joins only when its own explicit objective is present rather than merely sharing construction vocabulary.
- Closest neighboring skills: `clean-code`, `refactoring`, `working-effectively-with-legacy-code`, `release-it`, `a-philosophy-of-software-design`, `clean-architecture`, `designing-data-intensive-applications`, and `the-pragmatic-programmer`.
- Leading vocabulary: Code Complete, construction discipline, construction prerequisites, defect risk, inspectability, explicit data meaning, defensive programming, verifiable increments, and evidence before fixes or tuning.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true` because repo-local manual-only metadata and description gating were not enforced. The description preserves nano pressure branches while giving Code Complete ownership of coordinated construction and requiring a separate explicit concern before co-invocation.
- Canonical inputs: `code-complete/code-complete.md`, `code-complete/code-complete.mini.md`, `code-complete/code-complete.nano.md`, and `_rule-workbench/code-complete/traceability.md`.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Lens | `construction during implementation, change, review, debugging, refactoring, and tuning` | Preserves the canonical use contexts without selecting from a task label alone. |
| Coordinated construction | `a nontrivial task coordinates several construction concerns` | Code Complete owns the integrated construction decision instead of adding local-readability or architecture lenses for routine construction vocabulary. |
| Pressure branches | `solution-first coding`, `happy-path-only tests`, `mixed behavior/refactoring`, `guess-driven debugging driving a code change`, or `evidence-free tuning` | Promotes the corrected nano triggers into discovery without making diagnosis-only or behavior-preserving-only work sufficient. |
| Neighbor and overlap boundary | `generic labels are insufficient`, and another lens needs `its own explicit objective rather than shared construction vocabulary` | Preserves generic negatives, suppresses vocabulary-only over-selection, and permits compatible co-invocation for independently central readability, structural, legacy, operational, architecture, or data concerns. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Apply the complete Code Complete lens to this importer." | `code-complete` | Direct book invocation; comprehensive routing reads `full.md` end to end. |
| "Before implementing this untrusted-input quote module, settle its data, validation, error, control, and test decisions." | `code-complete` | Several construction concerns must be coordinated for one production slice. |
| "The manager chose copy-loop-catch-all before batch failure and capacity semantics are known; define the smallest validated slice." | `code-complete`, `release-it` | Code Complete owns the coordinated construction decision; Release It owns the explicit production failure and capacity contract. |
| "Should this stable category matrix become a validated table? Resolve it under Code Complete." | `code-complete` | A bounded Code Complete dispute requires focused reference retrieval. |
| "Rename this local flag and remove a comment that narrates one fully specified helper." | `clean-code`, not `code-complete` | Local readability is the whole decision; broad construction discipline would duplicate the tighter lens. |
| "Extract this duplicated conditional in green-tested code without changing behavior." | `refactoring`, not `code-complete` | Behavior-preserving transformation sequence and stop conditions dominate. |
| "This untested class opens the real database; gain first feedback before adding a rule." | `working-effectively-with-legacy-code`, not `code-complete` | Characterization and a seam must establish control before construction guidance applies inside the change area. |
| "This isolated test deterministically proves integer division; diagnose the exact cause." | no project book skill; not `code-complete` | The debugging workflow already has reproducible evidence and no broad construction decision. |
| "Implement and review this fully specified pure clamp function." | no project book skill from wording alone | Generic implementation/review and a trivial local contract do not cross the activation threshold. |
| "First expose validation through behavior-preserving moves, then add typed rejection reasons and boundary tests." | `refactoring`, then `code-complete` | Refactoring owns preparatory structural safety; Code Complete owns the coordinated new construction. |
| "Add bounded retries, overload behavior, recovery, and production diagnostics." | `release-it`, not `code-complete` | Production failure behavior is the explicit objective; local construction concerns are not independently central. |
| "Add bounded retry behavior and also redesign opaque retry state, validation, error semantics, and tests." | `release-it`, `code-complete` | Production survivability and a broad construction decision are both explicit and complementary. |
| "Move policy out of the ORM so dependencies point inward." | `clean-architecture`, not `code-complete` | Policy independence and dependency direction arbitrate the change. |
| "Define source-of-truth, replay order, schema evolution, and repair for this derived projection." | `designing-data-intensive-applications`, not `code-complete` | Distributed data semantics, not local construction discipline, arbitrate correctness. |
| "Implement the ticket and review the PR." | no book skill from wording alone | Generic task labels are not construction-discipline evidence. |
| "Keep this tested one-line helper clever so review can finish today." | `clean-code`, not `code-complete` | Local readability and pressure are central, but no coordinated construction decision exists. |
| "Apply a guessed retry before diagnosing this deterministic stale-read failure." | no project book skill; not `code-complete` | The debugging workflow must establish evidence; guess-driven diagnosis alone does not cross the construction threshold. |

## Shared-Term Review

| Shared term | Code Complete meaning | Neighbor boundary |
| --- | --- | --- |
| Readability | One construction outcome coordinated with defect risk, data, flow, boundaries, and verification. | Clean Code owns a local readability problem when broader coordination or pressure is absent. |
| Refactoring | One evidence-based construction practice, separated from behavior change when useful. | Refactoring owns behavior-preserving transformations, named moves, safety nets, and stop conditions. |
| Debugging | Reproduce, isolate, explain, fix, and verify as part of defect-risk construction. | The debugging workflow owns diagnosis; Code Complete joins only when a substantial change also has independently central coordinated construction decisions. |
| Testing | Risk-matched defect finding across boundaries, contracts, tables, integration, and regression. | TDD or generic implementation workflows own ordinary test sequencing; Legacy Code owns first-feedback tests. |
| Boundaries | Validate trust boundaries and keep contracts, errors, and module responsibilities explicit. | Release It owns production failure boundaries; Clean Architecture owns policy direction; DDIA owns distributed data semantics. |
| Complexity | Rising working-memory and control-flow cost is defect risk during construction. | APoSD owns module depth and total system complexity; Refactoring owns structural treatment of an existing smell. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description; early-guidance; final-check | Coordinated-construction description branch; `Construction Context`; first checklist item | Promotes complete `M1`, `M2`, and `M20` without creating a second authoritative rule. |
| `N2` | early-guidance; final-check | `Readable Routines and Data`; `Inspectable Control and Tables`; second and fourth checklist items | Clever compactness raises salience after invocation but does not independently activate the broad skill; complete `M3` and `M8` remain authoritative. |
| `N3` | early-guidance; reference-router; final-check | `Readable Routines and Data`; `Boundaries, Errors, and Modules`; routine and module index routes; second checklist item | Cohesion and interface size are preserved through `M5`, `M12`, `M21`, and `M26`; they do not independently activate broad guidance. |
| `N4` | early-guidance; reference-router; final-check | `Readable Routines and Data`; variable/data index routes; second and third checklist items | Complete `M6`, `M7`, and `M22` supply the authoritative data rules. |
| `N5` | early-guidance; reference-router; final-check | `Boundaries, Errors, and Modules`; defensive/error/contract routes; third checklist item | Complete `M10`, `M11`, and `M23` stay colocated. |
| `N6` | early-guidance; reference-router; final-check | `Inspectable Control and Tables`; control/table routes; fourth checklist item | Complete `M8`, `M9`, `M24`, and `M25` remain authoritative. |
| `N7` | description; early-guidance; final-check | Coordinated-construction and evidence-free-tuning description branches; `Incremental Defect Finding`; `Refactoring, Tuning, and Tools`; fifth and sixth checklist items | Promotes the complete evidence rules `M14`-`M18` and triggers `M27`-`M30`. |
| `N8` | early-guidance; reference-router; final-check | `Comments and Standards`; comment and standards routes; second and fifth checklist items | Complete `M18`, `M19`, `M31`, and `M32` reduce manual and reader effort without hiding structure. |
| `N9` | description; early-guidance | Solution-first description branch; `Construction Context` | Complete trigger `M20` and context rules `M1`-`M2` preserve the operational response. |
| `N10` | early-guidance; reference-router | `Readable Routines and Data`; variable/data routes | Complete trigger `M22` is authoritative; local naming alone stays below the broad activation threshold. |
| `N11` | early-guidance; reference-router | `Readable Routines and Data`; routine route | Complete `M5` and `M21` stay adjacent; a routine-only readability issue still routes to Clean Code unless broader construction pressure exists. |
| `N12` | early-guidance; reference-router; final-check | `Boundaries, Errors, and Modules`; defensive/error routes; third checklist item | Complete trigger `M23` is colocated with `M10` and `M11`. |
| `N13` | early-guidance; reference-router; final-check | `Inspectable Control and Tables`; flow/table routes; fourth checklist item | Complete `M24` and `M25` preserve the simplification and table criteria. |
| `N14` | description; early-guidance; reference-router; final-check | Happy-path-only-tests description branch; `Incremental Defect Finding`; testing route; fifth checklist item | Complete trigger `M27` supplies the required test categories. |
| `N15` | description; early-guidance; reference-router; final-check | Guess-driven-debugging and evidence-free-tuning description branches; `Incremental Defect Finding`; `Refactoring, Tuning, and Tools`; quality/performance routes; fifth checklist item | Complete `M28` and `M30` distinguish diagnosis from measured tuning; diagnosis-only work remains outside when no code change is requested. |
| `N16` | early-guidance; reference-router; final-check | `Comments and Standards`; comment route; second checklist item | Complete `M19` and `M31` preserve the comment decision without adding comment-only activation. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Construction Context` | Moved unchanged. | Colocated with solution-first trigger `M20`; restated by the first checklist item. |
| `M2` | `Construction Context` | Moved unchanged. | Small validated slices remain the response to upstream uncertainty. |
| `M3` | `Readable Routines and Data` | Moved unchanged. | Promoted by `N2`; restated by the second and fourth checklist items. |
| `M4` | `Readable Routines and Data` | Moved unchanged. | Pseudocode and retained-comment conditions remain one complete rule. |
| `M5` | `Readable Routines and Data` | Moved unchanged. | Colocated with routine trigger `M21`. |
| `M6` | `Readable Routines and Data` | Moved unchanged. | Colocated with explicit-data trigger `M22`. |
| `M7` | `Readable Routines and Data` | Moved unchanged. | Kept beside variable/data meaning rather than split into a priority fragment. |
| `M8` | `Inspectable Control and Tables` | Moved unchanged. | Colocated with hard-to-verify-flow trigger `M24`. |
| `M9` | `Inspectable Control and Tables` | Moved unchanged. | Colocated with repeated-branching trigger `M25`. |
| `M10` | `Boundaries, Errors, and Modules` | Moved unchanged. | Colocated with trust-boundary trigger `M23`. |
| `M11` | `Boundaries, Errors, and Modules` | Moved unchanged. | Error abstraction, context, standardization, normal path, and impossible state remain intact. |
| `M12` | `Boundaries, Errors, and Modules` | Moved unchanged. | Colocated with abstraction-boundary trigger `M26`. |
| `M13` | `Boundaries, Errors, and Modules` | Moved unchanged. | Complexity remains framed as defect risk. |
| `M14` | `Incremental Defect Finding` | Moved unchanged. | Promoted by `N7`; restated by the sixth checklist item. |
| `M15` | `Incremental Defect Finding` | Moved unchanged. | Colocated with test and diagnosis triggers `M27` and `M28`. |
| `M16` | `Refactoring, Tuning, and Tools` | Moved unchanged. | Colocated with risky-refactoring trigger `M29`. |
| `M17` | `Refactoring, Tuning, and Tools` | Moved unchanged. | Colocated with performance trigger `M30`. |
| `M18` | `Refactoring, Tuning, and Tools` | Moved unchanged. | Tooling stays evidence-supporting rather than understanding-replacing. |
| `M19` | `Comments and Standards` | Moved unchanged. | Colocated with comment and style triggers `M31` and `M32`. |
| `M20` | `Construction Context` | Moved unchanged. | Immediately follows construction prerequisite `M1`. |
| `M21` | `Readable Routines and Data` | Moved unchanged. | Immediately follows complete routine rule `M5`. |
| `M22` | `Readable Routines and Data` | Moved unchanged. | Immediately follows complete variable/data rules `M6` and `M7`. |
| `M23` | `Boundaries, Errors, and Modules` | Moved unchanged. | Immediately follows trust-boundary rule `M10`. |
| `M24` | `Inspectable Control and Tables` | Moved unchanged. | Immediately follows control-flow rule `M8`. |
| `M25` | `Inspectable Control and Tables` | Moved unchanged. | Immediately follows table-driven rule `M9`. |
| `M26` | `Boundaries, Errors, and Modules` | Moved unchanged. | Immediately follows class/module rule `M12`. |
| `M27` | `Incremental Defect Finding` | Moved unchanged. | Immediately follows risk-matched quality rule `M15`. |
| `M28` | `Incremental Defect Finding` | Moved unchanged. | Colocated with the complete debugging clause in `M15`. |
| `M29` | `Refactoring, Tuning, and Tools` | Moved unchanged. | Immediately follows refactoring rule `M16` and supplies the mixed behavior/refactoring pressure branch. |
| `M30` | `Refactoring, Tuning, and Tools` | Moved unchanged. | Immediately follows tuning rule `M17`. |
| `M31` | `Comments and Standards` | Moved unchanged. | Immediately follows comment/layout rule `M19`. |
| `M32` | `Comments and Standards` | Moved unchanged. | Kept beside shared-style guidance in `M19`. |

## Wording Fidelity

- Verbatim primary bias: exact.
- Verbatim mini rules: every authoritative `M1`-`M32` sentence appears exactly once in `SKILL.md` with canonical wording.
- Verbatim final checklist and order: all six items are exact and remain in source order.
- Reworded mini rules: none.
- Faithful mini-rule merges: none.
- Nano handling: no `N*` item is installed as a second authoritative rule; nano affects description routing, concern order, focused routes, and the existing final checklist as recorded above.
- Authored packaging text: frontmatter, concern headings, the three-branch reference router, and index `Read when` conditions provide activation and navigation without replacing mini guidance.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 921 words.
- `SKILL.md`: 1,083 words across 82 lines.
- Packaging overhead: 162 words.
- Frontmatter description: 500 characters, excluding the terminating newline.
- Decision: retain the source-driven exception because the canonical mini already exceeds 500 words. Every mini rule remains required for complete ordinary use; the twelve-word soft-target overage preserves the ordinary stop, narrow interpretation-dispute route, nano-derived pressure branches, construction ownership, and compatible co-invocation boundary.

## Evaluation Environment

- Durable case files were created before the skill package and before any behavioral GREEN execution.
- Behavioral runs are deliberately withheld until the parent reviews these contracts, per assignment.
- The shared `_skill-workbench/evaluations/cases/catalog-null.md` remains the sole catalog-null fixture; this conversion does not duplicate it.
- Planned runner: `_skill-workbench/scripts/run_skill_eval.py` with the same pinned model and configuration for RED and GREEN, fresh agents, packaged-only GREEN reads, and independent source tracing.

## Evaluation Cases

### E1: Complete Construction Audit

- Class: direct invocation; comprehensive retrieval; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/comprehensive-construction-audit.md`.
- Required skills: `{code-complete, release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications}`.
- Required order: none; Code Complete owns coordinated construction while Release It owns production failure and capacity behavior.
- Reference mode: `comprehensive`.
- Expected sections: every section in `code-complete/references/full.md`, read end to end.
- Forbidden sections: none inside Code Complete; references from other book skills are forbidden.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: GREEN must produce a prioritized, bounded construction audit that covers prerequisites, routines/data, flow, boundaries/errors, modules/complexity, verification, tools, standards, and final review without importing a neighbor lens.
- Source trace: `M1`-`M32`, `N1`-`N16`, and every full-reference heading.
- Result: not run.

### E2: Ordinary Verifiable Construction Slice

- Class: distinctive multi-concern recognition; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/ordinary-construction-slice.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `ordinary`.
- Expected sections: none; `SKILL.md` is complete for the specified construction slice.
- Forbidden sections: every full-reference section for every book skill.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: GREEN must coordinate explicit data meaning, trust-boundary validation, arithmetic/control clarity, domain error semantics, boundary and invalid-input tests, and one small verifiable increment without broad cleanup or architecture.
- Source trace: `M1`-`M3`, `M6`-`M11`, `M14`, `M15`, `M20`, `M22`-`M24`, `M27`; `N1`, `N2`, `N4`-`N7`, `N9`, `N10`, `N12`-`N14`.
- Result: not run.

### E3: Focused Table-Driven Decision

- Class: focused retrieval; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/focused-table-driven-decision.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `focused`.
- Expected sections: `Statement, Conditional, and Loop Rules`; `Table-Driven and Data-Driven Rules`; `Testing Rules`.
- Forbidden sections: every other Code Complete full-reference section and every other book reference.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: GREEN must choose a table only if it is clearer, explicit, synchronized, and validated, then require representative combination and invalid-state tests without opening unrelated guidance.
- Source trace: `M8`, `M9`, `M25`, `M27`; `N6`, `N13`, `N14`; the three expected full headings.
- Result: not run.

### E4: Solution-First Construction Pressure

- Class: distinctive symptom recognition; pressure; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/solution-first-pressure.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `ordinary`.
- Expected sections: none; both skill bodies must survive schedule and authority pressure without unnecessary reference loading.
- Forbidden sections: every full-reference section for every book skill.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: GREEN must reject copy-loop-catch-all construction before requirements and failure semantics are settled, identify the missing decisions, define a result and validation contract, bound batch demand and dependency effects, and propose the smallest testable slice rather than a rewrite.
- Source trace: Code Complete `M1`-`M3`, `M8`, `M10`, `M11`, `M14`, `M15`, `M20`, `M23`, `M24`, `M27`, `M28`; `N1`, `N2`, `N5`-`N7`, `N9`, `N12`-`N15`; Release It `M1`, `M3-M8`, `M12`, `M16-M20`, `N3-N6`, `N9`.
- Result: not run.

### E5: Clean Code Local-Readability Neighbor

- Class: near-neighbor; pair-specific negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/clean-code-neighbor.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}` only if behavior-preserving transformation mechanics become central.
- Forbidden skills: `{code-complete, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none; Clean Code owns the target local shape.
- Reference mode: `ordinary` for Clean Code; `none` for Code Complete.
- Expected sections: none from Code Complete.
- Forbidden sections: every Code Complete reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: adding Code Complete must not turn a fully specified local formatter cleanup into a broad construction audit or duplicate the tighter Clean Code lens.
- Source trace: neighbor contract from `docs/compatibility/clean-code/code-complete.md`; no Code Complete application trace is expected.
- Result: not run.

### E6: Refactoring-Only Neighbor

- Class: near-neighbor; pair-specific negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/refactoring-neighbor.md`.
- Required skills: `{refactoring}`.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `ordinary` for Refactoring; `none` for Code Complete.
- Expected sections: none from Code Complete.
- Forbidden sections: every Code Complete reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: adding Code Complete must not displace behavior preservation, named small moves, verification after each move, and the current-smell stop condition with a general construction review.
- Source trace: neighbor contract from `docs/compatibility/code-complete/refactoring.md`; no Code Complete application trace is expected.
- Result: not run.

### E7: Legacy First-Feedback Neighbor

- Class: near-neighbor; pair-specific negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/legacy-control-neighbor.md`.
- Required skills: `{working-effectively-with-legacy-code}`.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, release-it, clean-architecture, designing-data-intensive-applications}` until control exists.
- Required order: none; only Legacy Code is required in the initial task.
- Reference mode: `focused` for Legacy Code; `none` for Code Complete.
- Expected sections: exactly Legacy Code `Testing Strategy Rules`, `Seam Rules`, and `Dependency Breaking Rules`.
- Forbidden sections: every Code Complete section and every Legacy Code section outside the expected set.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: adding Code Complete must not encourage construction improvement before characterization and the smallest dependency seam establish trustworthy feedback.
- Source trace: neighbor contract from `docs/compatibility/code-complete/working-effectively-with-legacy-code.md`; no Code Complete application trace is expected.
- Result: not run.

### E8: Debugging-Only Negative

- Class: debugging-workflow counterexample; pair-specific negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/debugging-only-negative.md`.
- Required skills: `{}` from the project book catalog.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none` for Code Complete.
- Expected sections: none.
- Forbidden sections: every Code Complete packaged file.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: the existing debugging workflow must diagnose integer division directly; Code Complete must not activate merely because source code and a defect are present.
- Source trace: description boundary `bug diagnosis alone do not qualify`; no Code Complete application trace is expected.
- Result: not run.

### E9: Preparatory Refactoring and New Construction

- Class: compatible overlap; application; ordering.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/refactoring-compatible-overlap.md`.
- Required skills: `{refactoring, code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `refactoring` then `code-complete`; first expose validation without behavior change, then construct the typed semantic change.
- Reference mode: `ordinary` for both required skills.
- Expected sections: none; both skill bodies are sufficient.
- Forbidden sections: every full-reference section for every book skill.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: GREEN must separate the behavior-preserving structural phase from the typed-result behavior change, preserve old behavior during phase one, then make data meaning, validation, result semantics, and rejection tests explicit in phase two.
- Source trace: Code Complete `M5`-`M8`, `M10`, `M11`, `M15`, `M16`, `M21`-`M24`, `M27`, `M29`; Refactoring mapping is reviewed independently; compatibility order from `docs/compatibility/code-complete/refactoring.md`.
- Result: not run.

### E10: Generic Implementation and Review Negative

- Class: generic-request counterexample; pair-specific negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/generic-implementation-negative.md`.
- Required skills: `{}` from the project book catalog.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none` for Code Complete.
- Expected sections: none.
- Forbidden sections: every Code Complete packaged file.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: the normal implementation workflow must implement the fully specified pure function without loading broad construction discipline merely from `implement` or `review` wording.
- Source trace: positive activation threshold and generic-work exclusion in the description; no Code Complete application trace is expected.
- Result: not run.

### E11: Guess-Driven Debugging Negative

- Class: ambiguous-neighbor counterexample; debugging-workflow negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/guess-driven-debugging-negative.md`.
- Required skills: `{}` from the project book catalog.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none`.
- Expected sections: none.
- Forbidden sections: every packaged book skill and reference.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: the debugging workflow must reproduce, isolate, and explain the stale-read failure before a fix; guess pressure alone must not activate broad Code Complete or another book lens.
- Source trace: Code Complete description requires coordinated construction concerns; `M15` and `M28` remain source support only after invocation and do not create an independent discovery branch.
- Result: not run.

### E12: Clever Local Readability Pressure

- Class: ambiguous near-neighbor; pressure; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/clever-local-readability-pressure.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}` only if behavior-preserving transformation mechanics become central.
- Forbidden skills: `{code-complete, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none; Clean Code owns the local readability decision.
- Reference mode: `ordinary`.
- Expected sections: none; the Clean Code body is sufficient.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by assignment.
- Behavioral delta: schedule and cleverness pressure must not widen one tested helper into Code Complete; Clean Code must improve names, the boolean mode, and expression shape locally.
- Source trace: Clean Code description and local readability guidance; Code Complete `N2`, `M3`, and `M8` remain salience inside a matched construction decision rather than independent activation.
- Result: not run.

### E12b: Current-Catalog Clean Code Pressure Overlap

- Class: compatible co-invocation; pressure; current-catalog replacement for the earlier source-suppressing Clean Code-only classification.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/local-readability-pressure.md`.
- Required skills: `{code-complete, clean-code}`.
- Allowed skills: `{refactoring}` only if behavior-preserving transformation mechanics become central.
- Forbidden skills: `{working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` establishes the construction decision, then `clean-code` resolves the explicit local-readability obstacles.
- Reference mode: `ordinary` for both required skills.
- Expected sections: none.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: existing package-free runs are retained; the replacement selection contract was predeclared before its GREEN execution.
- Post-skill runs: not run under this replacement contract.
- Behavioral delta: resist the proposed extra branch, preserve the existing additive discount, and improve the explicit boolean-mode, mutation, naming, and responsibility problems without widening into architecture, legacy-control, operational, or distributed-data work.
- Source trace: Code Complete `M1-M3`, `M5-M8`, `M10-M15`, `M20-M24`, `M27`, `N1-N7`, `N9-N14`; Clean Code exact source trace remains in its mapping.
- Result: predeclared replacement; pending repeated GREEN.

### E13: Shared Catalog Null

- Class: catalog-null control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/catalog-null.md`.
- Required skills: `{}`.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none`.
- Expected sections: none.
- Forbidden sections: every packaged book skill and reference.
- Baseline runs: existing shared control evidence remains outside this conversion; rerun after catalog addition only after parent contract review.
- Post-skill runs: not run by assignment.
- Behavioral delta: adding Code Complete must not cause a pure output-explanation request to select any book lens.
- Source trace: catalog routing only; no book guidance should apply.
- Result: not run for the expanded catalog.

### E4b: Ordinary Solution-Pressure Replacement

- Class: distinctive symptom recognition; pressure; ordinary application; replacement for E4's Release It!/focused-disclosure ambiguity.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/solution-first-local-pressure.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `ordinary`.
- Expected sections: none; the Code Complete body is sufficient for the fully specified local construction decision.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: reject the happy-path loop despite schedule pressure, preserve the supplied product contract, and propose one typed, validated, testable slice without inventing production-resilience work.
- Source trace: `M1-M3`, `M6-M11`, `M14-M15`, `M20`, `M22-M24`, `M27`; `N1-N2`, `N4-N7`, `N9-N14`.
- Result: replacement predeclared; not executed.

### E9b: Refactoring and Construction Replacement

- Class: compatible co-invocation; application; ordering; replacement for E9's too-small construction fixture.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/refactoring-construction-overlap.md`.
- Required skills: `{refactoring, code-complete}`.
- Allowed skills: `{clean-code}` when local readability is treated as an independent concern.
- Forbidden skills: `{working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `refactoring` then `code-complete`.
- Reference mode: `ordinary`.
- Expected sections: none; the selected bodies are sufficient for the bounded module change.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: preserve behavior while exposing parsing/validation, then separately construct typed per-line results, explicit boundary/error semantics, routines, and complete rejection tests.
- Source trace: Refactoring safety, sequencing, and behavior-preservation guidance; Code Complete `M5-M11`, `M14-M16`, `M21-M24`, `M27`, `M29`.
- Result: replacement predeclared; not executed.

### E11b: Observable Debugging Replacement

- Class: ambiguous-neighbor counterexample; debugging-workflow negative; replacement for E11's unknown cache behavior.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/observable-debugging-negative.md`.
- Required skills: `{}` from the project book catalog.
- Allowed skills: `{}`.
- Forbidden skills: `{code-complete, clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none`.
- Expected sections: none.
- Forbidden sections: every packaged book skill and reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: diagnose the deterministic string-normalization defect directly; guess pressure alone must not activate Code Complete, and fully observable pure code must not activate Legacy Code.
- Source trace: Code Complete's positive coordinated-construction threshold and bug-diagnosis exclusion; Legacy Code's blocked-first-feedback threshold.
- Result: replacement predeclared; not executed.

### X1: Explicit Ordinary Acceptance

- Class: explicit invocation; ordinary disclosure.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/manual-ordinary.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` only.
- Reference mode: `ordinary`.
- Expected sections: none.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: apply the complete normal-use construction body without turning one bounded slice into focused or comprehensive retrieval.
- Source trace: `M1-M3`, `M6-M11`, `M14-M15`, `M20`, `M22-M24`, `M27`.
- Result: pending.

### X2: Explicit Focused Acceptance

- Class: explicit invocation; focused disputed interpretation.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/manual-focused.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` only.
- Reference mode: `focused`.
- Expected sections: `Statement, Conditional, and Loop Rules`, `Table-Driven and Data-Driven Rules`, and `Testing Rules` are required; `Primary Directive` is allowed.
- Forbidden sections: every other Code Complete section and every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle the table decision from a bounded source set without a complete audit.
- Source trace: `M8-M9`, `M25`, `M27`, `N6`, `N13-N14` and the named headings.
- Result: pending.

### X2b: Explicit Focused Bounded Replacement

- Class: explicit invocation; focused replacement for X2's narrow subsection contract.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/manual-focused-bounded.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` only.
- Reference mode: `focused`.
- Expected sections: exactly `Primary Directive`, `Statement, Conditional, and Loop Rules`, `Table-Driven and Data-Driven Rules`, `Testing Rules`, and `Final Instruction`.
- Forbidden sections: every other Code Complete section and every other book reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle and arbitrate the table decision from five coherent headings without a complete audit.
- Source trace: `M8-M9`, `M25`, `M27`, `N6`, `N13-N14` and the named headings.
- Result: pending.

### X3: Explicit Comprehensive Acceptance

- Class: explicit invocation; comprehensive retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/manual-comprehensive.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` only.
- Reference mode: `comprehensive`.
- Expected sections: all 27 Code Complete headings, recorded as `*`.
- Forbidden sections: every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: provide source-grounded end-to-end construction coverage unavailable to the package-free baseline.
- Source trace: every `M*`, `N*`, checklist item, and full heading.
- Result: pending.

### P1: Manual-Policy Implicit Exclusion

- Class: invocation-policy counterexample; repeated catalog control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/solution-first-local-pressure.md`.
- Required skills: `{}` under the explicit-only policy.
- Allowed skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}` are neutral for this Code Complete policy check.
- Forbidden skills: `{code-complete}`.
- Required order: none.
- Reference mode: `none` for Code Complete; other allowed skills follow their own contracts.
- Expected sections: none from Code Complete.
- Forbidden sections: every Code Complete packaged file.
- Baseline runs: retained unnamed baselines already resisted the shortcut reliably.
- Post-skill runs: not run under the explicit-only policy.
- Behavioral delta: the package must not add automatic context when the user did not invoke it.
- Source trace: invocation policy only.
- Result: pending `3/3` policy probe.

### E14: Implicit Greenfield Construction Qualification

- Class: unnamed distinctive recognition; ordinary application; repeated implicit-policy qualification.
- Prompt or artifact: `_skill-workbench/evaluations/cases/code-complete/implicit-greenfield-construction.md`.
- Required skills: `{code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`.
- Required order: `code-complete` only.
- Reference mode: `ordinary`.
- Expected sections: none.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before final frozen-metadata GREEN.
- Post-skill runs: not run.
- Behavioral delta: coordinate the jointly unresolved pre-implementation decisions without importing local-cleanup, architecture, data-system, or production-resilience lenses.
- Source trace: `M1-M3`, `M5-M15`, `M20-M28`, `N1-N7`, `N9-N14`.
- Result: pending `3/3` qualification.

## Independent Review

- Reviewers: independent reverse-trace and catalog reviews `019f58a9-d0d9-7153-b03e-e89cd1eedc09`, `019f58ba-0c72-7460-af90-48434c787ef8`, `019f58ca-56d5-7a83-ade1-2a7d4aac7dfc`, and the final acceptance review recorded in `_skill-workbench/BATCH_2_RESULTS.md`.
- Catalog snapshot: all seven live project book skills plus Code Complete compatibility records.
- Semantic verdict: PASS after rule-layer and description repair. The package preserves the canonical construction contexts, nano pressure branches, exact mini guidance, and valid compatible overlap without unsupported active mechanisms.
- Unsupported or altered active guidance: none.

## Source And Description Repair

- Reverse-trace review removed unsupported tuning steps, table synchronization/categories, tooling caveats, recursion, pre-refactoring tests/analysis, and data-model redesign from mini/nano and traceability. Workbench and released copies match; the canonical full rule was not edited.
- The first broad description collided with Clean Code; the next pre-implementation-only description suppressed canonical implementation, review, debugging, refactoring, tuning, and co-invocation contexts. The final description uses the nano-derived solution-first, happy-path, mixed behavior/refactoring, guess-driven-change, and evidence-free-tuning branches while assigning shared construction vocabulary to Code Complete unless another lens has its own explicit objective.
- Manual-only metadata and description gating were not enforced by the repo-local runtime. The final package therefore uses implicit invocation with a tested but imperfect catalog boundary.

## Final Batch Reconciliation

- Explicit progressive disclosure: the accepted manual ordinary result used only `SKILL.md`; the bounded focused result read `Primary Directive`, `Statement, Conditional, and Loop Rules`, `Table-Driven and Data-Driven Rules`, `Testing Rules`, and `Final Instruction`; the comprehensive result recorded `*` after an end-to-end read.
- Refactoring overlap: `refactoring-compatible-overlap/green-final-scope-{1,2,3}.json` selected Refactoring then Code Complete, stayed ordinary, and passed fidelity in `3/3`.
- Clean Code overlap replacement: `local-readability-pressure/green-final-cc-overlap-{1,2,3}.json` selected Code Complete then Clean Code with ordinary disclosure in `3/3`; two runs preserved the additive discount, while one flattened it and failed fidelity.
- Generic negative: `generic-implementation-negative/green-final-scope-{1,2,3}.json` selected no project skill in `3/3`.
- Clean Architecture boundary: `ordinary-policy-detail-design/green-final-cc-scope-{1,2,3}.json` excluded Code Complete in `3/3`.
- Broad implicit construction: `implicit-greenfield-construction/green-final-scope2-{1,2,3}.json` included required Code Complete plus Clean Architecture and Clean Code in `3/3`. Disclosure was ordinary in `3/3`; unsupported fixture assumptions remain answer-level diagnostics.
- Local solution-first pressure: `solution-first-local-pressure/green-final-scope2-{1,2,3}.json` included required Code Complete in `3/3`, added Clean Code in two runs, and stayed ordinary in `3/3`. The extra applicable skill and general solver additions are permitted diagnostics.
- DDIA overlap: required DDIA and Code Complete appeared in `3/3` final-scope runs, and one run added Clean Code. The frozen comprehensive expectation was malformed for this fixture; two unsupported stream/ack additions remain solver diagnostics.
- Diagnosis-only diagnostic: required Legacy Code appeared in `3/3`; Code Complete also appeared in `1/3`. The extra selection remains a context-cost observation, not a conversion failure.
- Baseline timing: package-free baselines ran after draft authoring. They remain optional diagnostic evidence under the current protocol.
- Current-policy status: **accepted conversion**. Source and package semantics pass, every positive current run includes its required target skills, and explicit ordinary/focused/comprehensive probes pass. Additional skills, selection order, malformed exact-tier contracts, and general solver additions remain non-blocking diagnostics.

## Validation Evidence

- Structural validation: 82 lines, 1,083 words, 162 packaging words, 32 mini IDs, 16 nano IDs, and 27 full-reference sections; the 500-character description passes the hard limit.
- Wording validation: 32/32 exact rules, exact primary bias, and exact final checklist wording and order.
- Full-reference equality: `cmp -s` exits 0; canonical and packaged files share SHA-256 `57ca8fab93baea0761eeeca6c491fe79b093df47feb4172c0917a96f8ddc95a4`.
- Index validation: repository validation confirms all 27 headings, GitHub anchors, order, and heading-to-last-nonempty line ranges.
- Official validator: `/Users/jakubtomanik/.codex/skills/.system/skill-creator/scripts/quick_validate.py` reports `Skill is valid!` through `uv run --with pyyaml`.
- Evaluation contracts: the required-skill contract validator passes, including the E12b target set; historical allowed/forbidden partitions remain preserved diagnostics.
- Remaining risk: the broad construction lens still attracts neighboring book skills and model answers still invent fixture requirements even when no source wording supports them.
