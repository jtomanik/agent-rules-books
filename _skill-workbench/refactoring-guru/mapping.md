# Refactoring.Guru Skill Mapping

Evaluation contract version: 2

## Scope

- Distinctive lens: classify a concrete code smell and choose the smallest catalog treatment whose preconditions and tradeoffs fit, including the foreign-method-versus-local-extension decision for incomplete library classes.
- Intended invocation: select when explicit smell classification, comparison among named catalog techniques, or the incomplete-library treatment boundary is central after behavior is known or protected.
- Closest neighboring skills: `refactoring` owns the default process for ordinary behavior-preserving structural change; `clean-code` owns local readability and low-surprise implementation; `working-effectively-with-legacy-code` owns gaining first feedback when behavior is not yet known or protected. Refactoring.Guru adds explicit smell-family classification and catalog treatment selection. Compatible skills may co-invoke when those concerns are independently central.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`; all additional relevant selected skills are permitted, and acceptance checks only required inclusion.
- Canonical inputs: `refactoring-guru/refactoring-guru.md`, repaired `refactoring-guru/refactoring-guru.mini.md`, repaired `refactoring-guru/refactoring-guru.nano.md`, and `_rule-workbench/refactoring-guru/traceability.md` as read on 2026-07-14.
- Initial behavioral catalog freeze: independent ownership audit reproduced the sorted 14-description payload at 6,789 bytes and SHA-256 `93d0f9b418a7071997419765278f894a5415bc397085f473b265aca678c6fd4a`.
- Corrected catalog freeze: independent ownership audit reproduced the sorted 14-description payload at 6,841 bytes with SHA-256 `f23977d3f201fc519c399fef75d7ed8d0f3b80e08f56da7a8659ad9c68d71a82` and approved replacement manifest creation.

## Source Repair

- The authoritative traceability records manual source-fidelity repairs on 2026-07-14 that restored ordinary-work timing, review, treatment tradeoffs, test safety, cleaner-result requirements, bounded stopping, and exact `SHOULD` versus controlling modalities without changing stable rule IDs.
- Canonical repaired mini SHA-256: `bb086ec559cbe0814518cf2fc479174244d94028529f870e05820fa7ab7a1a4c`.
- Canonical repaired nano SHA-256: `d909b7fdf6527d6b784fb54c98ae6f03d41e8fb2c53c3992e7b31dcfb7d67c52`.
- No meaningful source content is removed because another book or skill overlaps. The complete repaired mini remains active guidance, and the complete canonical full source remains byte-identical in `references/full.md`.
- The canonical full remained untouched. Source defects were repaired through `_rule-workbench/PROCESS.md` in both mini/nano copies and traceability before the runtime package was regenerated; rejected fixtures remain immutable diagnostics with separately named replacements.

## Description Branches

Initial description (436 characters):

> Refactoring.Guru guidance for code-smell classification and catalog treatment selection. Use when explicit smell classification, choosing between named refactoring techniques and their preconditions or tradeoffs, or a foreign-method-versus-local-extension decision is central after behavior is known or protected. Refactoring owns ordinary behavior-preserving structural change; Clean Code local readability; Legacy Code first feedback.

Corrected description (488 characters):

> Refactoring.Guru guidance for code-smell classification, catalog treatment selection, and incomplete-library-class decisions. Use when explicit smell classification, choosing among named techniques and their preconditions or tradeoffs, or deciding how to add missing operations to an external class you cannot modify is central after behavior is known or protected. Refactoring owns ordinary behavior-preserving structural change; Clean Code local readability; Legacy Code first feedback.

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Explicit smell classification | `explicit smell classification` | Ordinary structural change with an already-known target belongs to `refactoring`; local readability without catalog classification belongs to `clean-code`. |
| Named catalog treatment choice | `choosing among named techniques and their preconditions or tradeoffs` | The generic small-step refactoring process remains owned by `refactoring`; this branch requires catalog applicability or treatment comparison to be central. |
| Incomplete library class | `incomplete-library-class decisions` plus `missing operations to an external class you cannot modify` | A narrow missing-operation versus substantial repeated-gap choice is a distinct full-only discovery branch, not generic wrapper or API design. The natural-language symptom replaces solution-only catalog terms after E2 missed discovery in three valid initial runs. |
| Feedback threshold | `after behavior is known or protected` | When a semantic change is blocked because first feedback is absent, `working-effectively-with-legacy-code` owns the task until control exists. |
| Catalog boundaries | `Refactoring owns ordinary behavior-preserving structural change; Clean Code local readability; Legacy Code first feedback` | Prevents catalog vocabulary from absorbing the neighboring default process, local hygiene, or first-feedback problem. |

## Activation Coverage

| Full-only candidate | Source trace | Nano coverage | Neighbor boundary | Decision and evidence |
| --- | --- | --- | --- | --- |
| Incomplete Library Class: foreign method versus local extension | Full lines `401-407`; `Technique Selection Rules`; `Technique Playbook` | Not covered by nano | Distinct from ordinary Refactoring because the central question is which named library-gap treatment fits; general wrapper design is insufficient | **PROMOTE.** Source-backed, realistic as a central unnamed decision, distinct within the description budget, and covered by E2 `unnamed-vendor-library-gap.md` with required `{refactoring-guru}` and three required runs. |
| Temporary Field and method object | `Object-Orientation Abusers`; `Smell-to-Treatment Priority Map`; `Technique Playbook` | Nano mentions method objects only as a heavier treatment | Ordinary Refactoring owns safe structural execution after the smell/treatment is selected | **REJECT as metadata branch.** This is catalog detail reached after explicit smell or technique selection, not a distinct invocation branch. |
| Alternative Classes with Different Interfaces | `Object-Orientation Abusers`; `Smell-to-Treatment Priority Map` | Not named | Interface alignment is catalog detail after classification and overlaps ordinary Refactoring | **REJECT as metadata branch.** Route through the index when the named smell is disputed. |
| Parallel Inheritance Hierarchies | `Change Preventers`; `Smell-to-Treatment Priority Map` | Not named | Refactoring supplies the safe sequence; Refactoring.Guru contributes the named smell and treatment triad only when explicitly central | **REJECT as metadata branch.** E7b tests focused retrieval of the missing trigger and preferred/fallback/risky triad without broadening description discovery. |
| Data Class, collection encapsulation, GUI/domain synchronization, and association direction | `Dispensables`; `Technique Selection Rules`; `Technique Playbook`; `Technique Execution Safety` | Nano includes data/association semantics only as a safety trigger | These are post-selection data-reorganization details rather than separate catalog discovery branches | **REJECT as metadata branches.** Keep in full-reference routes after the smell or named technique is central. |
| Query/modifier split, assertions, error codes, exceptions, and factories | `Technique Selection Rules`; `Technique Playbook`; `Technique Execution Safety` | Nano covers semantic verification, not these names | Local API semantics are ordinary Refactoring or Clean Code concerns unless a named technique dispute already activates this skill | **REJECT as metadata branches.** Route by named technique; do not add independent description vocabulary. |
| Technical debt and feature/bug/review timing | `When to Refactor`; `Technical Debt Rules`; `Refactoring Workflow for Agents` | Covered by `N1-N5` control salience | Refactoring owns the default process and timing boundary | **REJECT as distinct invocation branches.** Preserve as active body guidance because the repaired mini requires it, but do not use generic timing/debt vocabulary to activate this catalog skill. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Use the Refactoring.Guru lens to classify invoice smells and compare named treatments." | Required `{refactoring-guru}` | Direct catalog retrieval and treatment comparison are central; additional relevant skills are permitted. |
| "A vendor date type lacks one operation today, while only speculative future gaps suggest a wrapper or extension." | Required `{refactoring-guru}` | The promoted foreign-method-versus-local-extension branch is central without naming the book or technique. |
| "Tests pass; classify a long invoice renderer and choose the smallest named treatment without changing behavior." | Required `{refactoring-guru}` | Explicit smell classification and treatment selection are central; ordinary Refactoring may also be useful. |
| "Preserve behavior while renaming, extracting, and moving code after the target structure is already decided." | Required `{refactoring}` | Ordinary behavior-preserving structural change is central; no catalog classification or treatment dispute remains. |
| "Rename vague locals, remove flow-narrating comments, and split a mixed-responsibility helper." | Required `{clean-code}`, optionally `refactoring` | Local readability is central without an explicit catalog classification objective. |
| "We cannot observe current behavior and need a seam before changing a dependency." | Required `{working-effectively-with-legacy-code}` | First feedback is blocked; Refactoring.Guru's post-protection catalog lens is premature. |
| "Duplicate Observed Data is proposed, but its exact applicability, safe steps, and verification are disputed." | Required `{refactoring-guru}` | A bounded named-technique question requires focused `Technique Playbook` retrieval. |
| "Classify mirrored exporter/formatter hierarchies, retrieve the treatment triad, then give a safe behavior-preserving sequence." | Required `{refactoring-guru, refactoring}` | Refactoring.Guru owns the named smell and preferred/fallback/risky treatment; Refactoring owns safe execution. |
| "Apply the complete Refactoring.Guru lens across the entire catalog." | Required `{refactoring-guru}` | Explicit exhaustive objective requires the complete full reference. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | early-guidance, final-check | `Refactoring Scope, Control, and Stopping`; final checklist | Promotes complete `M1` and its boundary check without duplicating nano wording. |
| `N2` | description, early-guidance, final-check | Description smell/treatment branches; `Refactoring Scope, Control, and Stopping`; final checklist | Promotes complete `M2`, `M3`, `M6`, and `M36` so diagnosis, verification, and stopping remain whole. |
| `N3` | early-guidance | `Refactoring Scope, Control, and Stopping` | Promotes complete `M4` before catalog detail. |
| `N4` | early-guidance, final-check | `Refactoring Scope, Control, and Stopping`; final checklist | Promotes complete `M5`, including protection, risky-step checks, failure diagnosis, and the test-deletion prohibition. |
| `N5` | early-guidance, final-check | `Refactoring Scope, Control, and Stopping`; final checklist | Promotes complete `M6` and `M36` for cleaner-result and bounded-stop control. |
| `N6` | description, early-guidance, reference-router | Description treatment-choice branch; first two concern groups; focused router | Promotes complete smallest-treatment and category treatment rules; named applicability disputes route to source detail. |
| `N7` | early-guidance, final-check | `Smell Families and Treatment Choice`; `Transformation Safety and Exceptions`; final checklist | Promotes complete `M18` and `M24` rather than installing a second speculative-abstraction rule. |
| `N8` | early-guidance | `Smell Families and Treatment Choice` | Promotes complete `M16`. |
| `N9` | early-guidance, final-check | `Transformation Safety and Exceptions`; final checklist | Promotes complete `M19` and public-compatibility checking. |
| `N10` | early-guidance, reference-router | `Smell Families and Treatment Choice`; `Catalog Triggers`; focused router | Promotes complete `M13` and the dead/speculative deletion bullet represented by `M35`; exact reachability detail remains routed. The library-gap bullet is promoted independently by the description and E2, not by `N10`. |
| `N11` | early-guidance, reference-router | `Catalog Triggers`; `Transformation Safety and Exceptions`; focused router | Promotes complete `M25` and `M20`; exact extraction steps route to the playbook/safety sections. |
| `N12` | early-guidance, reference-router | `Catalog Triggers`; focused router | Promotes complete `M26` and supports `M29`; exact class/change-preventer treatment remains available by focused route. |
| `N13` | early-guidance, reference-router | `Smell Families and Treatment Choice`; `Catalog Triggers`; focused router | Promotes complete `M11` and `M32`; exact polymorphism conditions remain available by named-technique route. |
| `N14` | early-guidance | `Refactoring Scope, Control, and Stopping` | Promotes complete `M7` without splitting Rule of Three from coincidental-similarity protection; the canonical nano checklist does not restate this trigger. |
| `N15` | early-guidance, reference-router | `Catalog Triggers`; focused router | Promotes complete `M27` and `M28`; exact data-organization details remain in full. |
| `N16` | early-guidance, reference-router | `Smell Families and Treatment Choice`; `Catalog Triggers`; focused router | Promotes complete `M14` and both canonical bullets represented by `M30`. |
| `N17` | early-guidance, reference-router | `Transformation Safety and Exceptions`; `Catalog Triggers`; focused router | Promotes complete `M21`, `M22`, and `M31-M33`; bounded semantics questions route to the named full sections. The canonical nano checklist does not restate this trigger. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Opens with refactoring/behavior separation and source-repaired feature, bug, and review timing. |
| `M2` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Keeps diagnosis, cost, expected end state, verification, and stop condition together. |
| `M3` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Keeps smallest treatment, escalation, and tradeoff rejection together. |
| `M4` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Preserves small named transformations and broad-redesign avoidance. |
| `M5` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Preserves the complete repaired protection, checks, failure diagnosis, brittle-test, and no-deletion rule. |
| `M6` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Preserves cleaner-result, re-diagnosis, ownership/API/scope boundaries, and separate-smell stopping. |
| `M7` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Kept whole after nano-salient verification and stop rules. |
| `M8` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Keeps debt guidance active without making debt a description branch. |
| `M9` | `Smell Families and Treatment Choice` | Moved verbatim | Opens category classification and retains incomplete library gaps. |
| `M10` | `Smell Families and Treatment Choice` | Moved verbatim | Keeps bloater treatment priority intact. |
| `M11` | `Smell Families and Treatment Choice` | Moved verbatim | Keeps isolation-before-polymorphism and stable/repeated variation together. |
| `M12` | `Smell Families and Treatment Choice` | Moved verbatim | Keeps change ownership and one-main-edit-site pressure together. |
| `M13` | `Smell Families and Treatment Choice` | Moved verbatim | Preserves all external-reachability qualifiers. |
| `M14` | `Smell Families and Treatment Choice` | Moved verbatim | Preserves boundary-layer exceptions to middle-man reduction. |
| `M15` | `Smell Families and Treatment Choice` | Moved verbatim | Keeps rationale comments and code-clarity replacements together. |
| `M16` | `Smell Families and Treatment Choice` | Moved verbatim | Preserves the interchangeable-behavior exception. |
| `M17` | `Smell Families and Treatment Choice` | Moved verbatim | Keeps encapsulation tied to behavior and exposed-data manipulation. |
| `M18` | `Smell Families and Treatment Choice` | Moved verbatim | Preserves every speculative-abstraction example and evidence threshold. |
| `M19` | `Transformation Safety and Exceptions` | Moved verbatim | Keeps public compatibility and transition paths ahead of technique mechanics. |
| `M20` | `Transformation Safety and Exceptions` | Moved verbatim | Preserves complete extraction/movement preconditions. |
| `M21` | `Transformation Safety and Exceptions` | Moved verbatim | Preserves conditional/algorithm semantic and performance checks. |
| `M22` | `Transformation Safety and Exceptions` | Moved verbatim | Preserves all data-reorganization semantic dimensions. |
| `M23` | `Transformation Safety and Exceptions` | Moved verbatim | Preserves real shared behavior and substitutability. |
| `M24` | `Transformation Safety and Exceptions` | Moved verbatim | Preserves deliberate exceptions and every canonical example. |
| `M25` | `Catalog Triggers` | Moved verbatim | Long-method trigger and smaller treatments remain whole. |
| `M26` | `Catalog Triggers` | Moved verbatim | Large-class trigger retains stable-variant and client-subset conditions. |
| `M27` | `Catalog Triggers` | Moved verbatim | Primitive/type-code modeling remains evidence-gated. |
| `M28` | `Catalog Triggers` | Moved verbatim | Parameter-list treatment keeps the real-recurring-concept condition. |
| `M29` | `Catalog Triggers` | Moved verbatim | Shotgun-change trigger retains centralization pressure. |
| `M30` | `Catalog Triggers` | Two canonical bullets moved verbatim | Stable traceability ID spans the separate Message Chains and Middle Man mini bullets; each bullet appears exactly once and is not merged or split. |
| `M31` | `Catalog Triggers` | Moved verbatim | Query/modifier split retains the atomic read-modify exception. |
| `M32` | `Catalog Triggers` | Moved verbatim | Conditional treatment retains side-effect and ordering checks. |
| `M33` | `Catalog Triggers` | Moved verbatim | Null-object trigger retains the explicit-error exception; broader semantics remain in `M21-M22` and the full reference. |
| `M34` | `Catalog Triggers` | Moved verbatim | Inheritance trigger keeps both push-down and delegation treatments. |
| `M35` | `Catalog Triggers` | Two canonical bullets moved verbatim | Stable traceability ID spans the separate dead/speculative deletion and incomplete-library mini bullets; each appears exactly once. |
| `M36` | `Refactoring Scope, Control, and Stopping` | Moved verbatim | Promoted beside `M6` so cleanup-spread stopping remains early and complete. |

## Wording Fidelity

- Verbatim primary bias: exact.
- Verbatim mini rules: all 38 canonical decision and trigger bullets represented by stable IDs `M1-M36` are moved whole and exact. `M30` and `M35` each represent two separate canonical bullets; no bullet is merged, split, duplicated, omitted, or reworded.
- Verbatim final checklist and order: all eight repaired items are exact and remain in canonical order.
- Documented wording exceptions: none.
- Reordering inventory: `M36` moves beside `M6` so the cleanup-spread stop rule remains nano-salient; `M7-M8` follow it. All other rules retain source-relative order within the requested concern groups.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Description inventory: code-smell classification and named treatment selection trace to `M2-M3`, `M9-M14`, `M25-M35`, `N2`, `N6`, and the full catalog; the corrected incomplete-library-class and external-class-missing-operations branch traces to full lines `401-407`, `Technique Selection Rules`, and `Technique Playbook`; neighbor boundaries come from the reviewed compatibility contract and add no Refactoring.Guru technical guidance.
- Concern-heading inventory: the four headings only group complete verbatim mini rules by the assignment's approved concern design.
- Ordinary loading directive: body-only loading when the active rules resolve smell classification, treatment comparison, risk ordering, verification, and stopping is the progressive-disclosure packaging stop condition; references are not opened merely to confirm or elaborate that answer.
- Focused loading directive: eight common source-detail questions link directly to canonical full headings, including treatment triads, named-technique conditions, execution safety, and incomplete-library-class detail; every other bounded canonical question uses the exhaustive index. These are packaging-only routes and add no treatment.
- Comprehensive loading directive: an explicit complete Refactoring.Guru lens or exhaustive catalog audit routes to the full reference end to end.
- Index inventory: all 20 `Read when` cells route to their same-named canonical H2 sections and introduce no technical mechanism, default, guarantee, or preference beyond those sections.

## Size Exception

- Canonical mini: 1,142 words.
- `SKILL.md`: 1,325 words across 88 lines.
- Packaging overhead: 183 words, within the documented 151-200 allowance.
- Description: 488 characters.
- Decision: retain the source-driven exception to the 500-word skill target because the repaired canonical mini already exceeds it and the assignment requires all 38 canonical mini bullets plus the eight-item checklist verbatim. The 33-word soft-target overage provides eight direct focused routes without duplicating the exhaustive index; no line-count exception is needed.

## Behavioral Correction

- Initial E2 discovery observation: three valid runs applied the source-backed one-gap-versus-substantial-gap judgment but selected only neighboring skills, so required `{refactoring-guru}` inclusion failed `0/3`. Empty record-integrity, manifest, and Codex error lists isolate a description-discovery defect rather than source application or harness failure.
- Initial E7b disclosure/application observation: the valid run selected required `{refactoring-guru, refactoring}` but stayed ordinary, read no full-reference section, and substituted a factory/registry fallback. The canonical fallback is hierarchy collapse, so this is a material focused-routing and attribution failure.
- Description correction: replace the solution-only `foreign-method-versus-local-extension` phrase with source-backed symptom language about incomplete library classes and missing operations on an external class that cannot be modified. This exposes the promoted full-only trigger without changing its treatment rule.
- Router correction: add explicit preferred/fallback/risky treatment-triad requests to focused routing only when unresolved after the compact body. This loads existing canonical detail for E7b while retaining body-only resolution for E1 and E3.
- Change-impact decision: preserve all initial manifests and results, then create 11 uniquely named records under the corrected catalog: E1 x3, E2 x3, and E3, E4, E5b, E6, E7b x1 each. E5a and E7a remain NOT-RUN diagnostics.
- Independent correction review: PASS - the reviewer classified E2 as description discovery, E7b as material focused routing/application, found both corrections source-backed and bounded across all 14 skills, and prescribed the exact 11-record rerun set.
- Corrected-catalog matrix: all 11 records included every required skill with clean manifests, integrity, and execution. E7b retrieved the canonical hierarchy-collapse fallback. Independent attribution review nevertheless failed the behavioral gate: E2 run 3 stayed ordinary and introduced contradictory numeric escalation thresholds; two of three E1 runs and E3 over-read focused references; one body-only E1 answer invented `Remove Comments` as a named catalog technique.
- Second router correction: keep body-resolved classification, treatment comparison, risk, verification, and stopping ordinary; explicitly route incomplete-library migration and vendor-update compatibility to existing full detail. This changes only packaging/loading policy, not canonical guidance, treatment terminology, or the description catalog.
- Second change-impact decision: preserve the complete corrected-catalog matrix, then create 11 uniquely named post-router records for the affected E1 x3, E2 x3, E3, E4, E5b, E6, and E7b contracts. No invented anti-threshold or technique-naming rule is added to the package.

## Evaluation Cases

All additional relevant selected skills are permitted. Required inclusion is the acceptance contract.

### E1: Direct catalog treatment

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/direct-catalog-treatment.md`
- Fixture SHA-256: `a3062883ef19a20652b61f7f18a85f05af216434307c49aa96f84537687b5f8f`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Classify the concrete smells, compare plausible named catalog treatments, and choose the smallest justified treatment through the explicit Refactoring.Guru lens.
- Neighbor ownership: Refactoring may contribute execution safety, but the fixture centrally asks for catalog classification and treatment comparison.
- Ownership review: PASS - independently approved pre-run contract supplied with the assignment against the live catalog.
- Reference expectation: ordinary
- Runs: initial catalog `green-final-preflight-1`, `green-final-2`, and `green-final-3`; corrected catalog `green-corrected-preflight-1`, `green-corrected-2`, and `green-corrected-3`; accepted post-router `green-disclosure-preflight-1`, `green-disclosure-2`, and `green-disclosure-3` complete.
- Package fidelity trace: `M2-M5`, `M9-M10`, `M15`, `M20`, `M25`, `M28`; `N2-N6`, `N11`, `N15`.
- Attribution review: PASS - post-router runs selected Refactoring.Guru `3/3`, stayed ordinary `3/3`, and did not present `Remove Comments` as a named catalog technique.
- Behavioral result: PASS.
- Diagnostics: preserve the initial and corrected over-reads plus invented answer-level technique as historical observations; the accepted router keeps body-resolved treatment comparison ordinary without adding a terminology rule.

### E2: Unnamed vendor library gap

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/unnamed-vendor-library-gap.md`
- Fixture SHA-256: `fdb10c9c150501ca8963e74cb00c6d568f71d2302c4ee30ba0ab8debf7ef7aea`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Choose a foreign method for the current narrow gap and reserve a local extension for substantial repeated gaps without speculative wrapping or forking.
- Neighbor ownership: Ordinary Refactoring can sequence a chosen structure, but only Refactoring.Guru contributes the promoted foreign-method-versus-local-extension catalog boundary.
- Ownership review: PASS - independently approved promoted unnamed discovery contract supplied with the assignment.
- Reference expectation: focused
- Compact-body gap: `SKILL.md` selects a foreign method for one narrow gap and a local extension for substantial repeated gaps, but intentionally omits the full playbook's migration path and vendor-package update compatibility details requested by this fixture.
- Intended index destinations: `Technique Playbook` only.
- Runs: initial catalog `green-final-1`, `green-final-2`, and `green-final-3`; corrected catalog `green-corrected-1`, `green-corrected-2`, and `green-corrected-3`; accepted post-router `green-disclosure-1`, `green-disclosure-2`, and `green-disclosure-3` complete.
- Package fidelity trace: `M3`, `M18`, both `M35` bullets; full `Incomplete Library Class`, `Moving Features Between Objects`, and `Technique Playbook` entries.
- Attribution review: PASS with diagnostics - accepted runs selected Refactoring.Guru `3/3`; two used focused source detail and one remained ordinary. Solver-authored `two or more`, `2-3`, and `three or more` heuristics are noncanonical answer-level diagnostics, not package rules or false source attribution.
- Behavioral result: PASS with diagnostics; required discovery `3/3`, focused disclosure `2/3`, one preserved nondeterministic body-only miss.
- Diagnostics: preserve the initial discovery failures, corrected body-only contradiction, accepted focused miss, and numeric specificity. The package retains the canonical narrow-versus-substantial boundary and adds no numeric threshold.

### E3: Ordinary smell treatment

- Class: application
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/ordinary-smell-treatment.md`
- Fixture SHA-256: `a7fef3a4e4216e9bd28ed9351def55d6730add83176afec1bca87b478e3e833d`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Diagnose the invoice smell, choose and bound the smallest catalog treatment, preserve behavior, verify, and stop from compact guidance alone.
- Neighbor ownership: Refactoring may be additionally relevant, but explicit smell diagnosis and treatment choice make Refactoring.Guru central.
- Ownership review: PASS - independently approved pre-run contract supplied with the assignment.
- Reference expectation: ordinary
- Runs: initial `green-final-1`, corrected `green-corrected-1`, accepted post-router `green-disclosure-1`, and post-map `green-inline-map-1` complete; the latest run selected the target with compatible Clean Code and Refactoring in `ordinary` mode and read no references.
- Package fidelity trace: `M1-M6`, `M9-M10`, `M15`, `M20-M21`, `M25`, `M28`, `M36`; `N1-N6`, `N11`, `N15`.
- Attribution review: original accepted answer `PASS`; post-map `green-inline-map-1` `FAIL` because it presents `Parallel Arrays` as part of the Refactoring.Guru catalog although the packaged canonical catalog contains no such smell. The observation is valid general advice, but the book attribution is unsupported.
- Behavioral result: original accepted behavior remains `PASS`; the post-map ordinary run has an answer-level attribution failure. Source/package fidelity remains `PASS` because the unsupported catalog name is absent from the package.
- Diagnostics: preserve the corrected seven-section over-read and the post-map false attribution; do not add an invented `Parallel Arrays` catalog entry to make the solver answer appear supported.

### E4: Focused Duplicate Observed Data

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/focused-duplicate-observed-data.md`
- Fixture SHA-256: `c61373f3c6762594a5fb6cec59b1cbaad9e92897d45c9d90d4cfd3af21d22ea3`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Retrieve the exact Duplicate Observed Data symptom, use condition, avoid condition, safe steps, and two-way-update verification.
- Neighbor ownership: Refactoring can supply general safe-change discipline, but it does not supply this named catalog technique's complete bounded playbook.
- Ownership review: PASS - independently approved focused contract; the compact gap and smallest destination were audited before execution.
- Reference expectation: focused
- Compact-body gap: `SKILL.md` preserves data-reorganization semantics but intentionally omits Duplicate Observed Data's specific GUI-held-domain-data symptom, use condition, avoid condition, safe steps, and two-way-update verification.
- Intended index destinations: `Technique Playbook` only.
- Runs: initial `green-final-1`, corrected `green-corrected-1`, accepted post-router `green-disclosure-1`, and post-map `green-inline-map-1` complete; the latest run selected only the target and read exactly `Technique Playbook` in focused mode.
- Package fidelity trace: `M22`, `N17`; full heading `Technique Playbook`.
- Attribution review: PASS - accepted answer used exactly focused `Technique Playbook` retrieval and applied the named technique's symptom, conditions, steps, and two-way verification.
- Behavioral result: PASS.
- Diagnostics: the focused contract permits additional relevant sections but judges material tier collapse separately.

### E5a: Preserved invalid named comprehensive diagnostic

- Class: diagnostic
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/comprehensive-catalog-audit.md`
- Fixture SHA-256: `3298aeb412ab99ebe0febfa444bc92b8cc55acb4c1d4faf3af309b1685f71b79`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Original contract expected complete Refactoring.Guru source application across every smell family, treatment family, playbook, safety rule, workflow, and review check.
- Neighbor ownership: Target ownership was central, but the fixture disclosed the required book and lens rather than testing blind comprehensive routing.
- Ownership review: FAIL - preserved pre-run diagnostic. The title and instruction name Refactoring.Guru, which is permitted for direct discovery but invalid for a disclosure fixture.
- Reference expectation: comprehensive
- Runs: NOT-RUN; preserved exactly as a pre-run diagnostic and not accepted as behavioral evidence.
- Package fidelity trace: `M1-M36`, `N1-N17`, and all 20 full-reference H2 sections.
- Attribution review: not run because the disclosure ownership contract failed before execution.
- Behavioral result: not-run
- Diagnostics: do not alter or relax this fixture; E5b is the independently audited unnamed replacement.

### E5b: Comprehensive structural catalog audit

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/comprehensive-structural-catalog-audit.md`
- Fixture SHA-256: `96d5d4b2338f5d616ada48bacbdcea6af96433ece336583bf77651521df0150a`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Exhaustively apply the complete target smell/treatment catalog across every relevant smell family, treatment family, playbook, safety rule, workflow, and review check.
- Neighbor ownership: Refactoring and other neighboring skills may add compatible structural, readability, construction, or design judgment, but none owns exhaustive application of this smell/treatment catalog and none is required.
- Ownership review: PASS - independently audited before execution against the frozen 14-skill catalog; the fixture reveals no required skill, book, lens, or private evaluation rationale, comprehensive loading is semantically compelled, and Refactoring.Guru's distinctive catalog judgment is central.
- Reference expectation: comprehensive
- Runs: initial `green-final-1`, corrected `green-corrected-1`, accepted post-router `green-disclosure-1`, and post-map `green-inline-map-1` complete; the latest run selected Refactoring.Guru plus compatible Refactoring and read both references comprehensively, including target `sections=["*"]`.
- Package fidelity trace: `M1-M36`, `N1-N17`, and all 20 full-reference H2 sections.
- Attribution review: PASS - accepted answer recorded comprehensive `*` reads and applied the catalog across the requested audit; extra Refactoring selection is permitted.
- Behavioral result: PASS.
- Diagnostics: replacement for the preserved invalid disclosure fixture; acceptance requires an end-to-end full read recorded as comprehensive, and additional relevant skill selections remain permitted.

### E6: Pressure against mechanical polymorphism

- Class: pressure
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/pressure-polymorphism-cleanup.md`
- Fixture SHA-256: `84a0c005494d54809887146920bc058d8cb2563be84273bb4f4703d08e26f08d`
- Required skills: `{refactoring-guru}`
- Distinctive judgment: Distinguish a real switch/type-code smell from style pressure and reject Strategy/polymorphism unless variation is stable and repeated.
- Neighbor ownership: Clean Code or Refactoring may be additionally useful, but the central judgment is catalog classification and the named treatment's preconditions/tradeoffs.
- Ownership review: PASS - independently approved pressure contract supplied with the assignment.
- Reference expectation: ordinary
- Runs: initial `green-final-1`, corrected `green-corrected-1`, and accepted post-router `green-disclosure-1` complete.
- Package fidelity trace: `M2-M6`, `M11`, `M18`, `M24`, `M32`, `M36`; `N2-N7`, `N13`.
- Attribution review: PASS - accepted answer stayed ordinary and rejected mechanical Strategy/polymorphism using source-backed preconditions.
- Behavioral result: PASS.
- Diagnostics: schedule and authority pressure must not turn a simple honest conditional into a mechanical pattern application.

### E7a: Preserved invalid parallel-hierarchies diagnostic

- Class: diagnostic
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/refactoring-compatible-parallel-hierarchies.md`
- Fixture SHA-256: `eee813dec522ecefacb226309453b003d552773b11cbe39b79ef3ec707c2e81a`
- Required skills: `{refactoring-guru, refactoring}`
- Distinctive judgment: Original contract expected Refactoring.Guru to classify Parallel Inheritance Hierarchies and provide its preferred/fallback/risky triad while Refactoring supplied safe behavior-preserving sequencing.
- Neighbor ownership: Both skills were originally marked central, but the fixture wording explicitly revealed `refactoring` and therefore invalidated blind ownership discovery.
- Ownership review: FAIL - preserved pre-run diagnostic. The wording revealed `refactoring`, and the exact Parallel Inheritance Hierarchies trigger plus preferred/fallback/risky triad is absent from the compact body.
- Reference expectation: ordinary
- Runs: NOT-RUN; preserved exactly as a pre-run diagnostic and not accepted as behavioral evidence.
- Package fidelity trace: full `Change Preventers` and `Smell-to-Treatment Priority Map`; Refactoring behavior-preserving sequencing.
- Attribution review: not run because the ownership contract failed before execution.
- Behavioral result: not-run
- Diagnostics: do not alter or relax this fixture; E7b is the independently prescribed replacement.

### E7b: Catalog-compatible parallel hierarchies

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-guru/catalog-compatible-parallel-hierarchies.md`
- Fixture SHA-256: `03e05956061970302b29dcdf7d0652aed393767e13e47a6bcb39f2c9ddcb1233`
- Required skills: `{refactoring-guru, refactoring}`
- Distinctive judgment: Refactoring.Guru must retrieve the exact Parallel Inheritance Hierarchies trigger and preferred/fallback/risky treatment triad; Refactoring must provide the safe behavior-preserving sequence.
- Neighbor ownership: Both required skills contribute distinct central judgments; Clean Architecture or design skills may be relevant but do not replace either catalog classification or safe structural execution.
- Ownership review: PASS - exact replacement independently prescribed and audited; compact gap and smallest coherent destinations approved.
- Reference expectation: focused
- Compact-body gap: `SKILL.md` names change preventers generally but omits the named Parallel Inheritance Hierarchies trigger and its preferred moving-members, fallback hierarchy-collapse, and risky next-paired-subclass triad.
- Intended index destinations: `Change Preventers` and `Smell-to-Treatment Priority Map`.
- Runs: initial `green-final-1`, corrected `green-corrected-1`, and accepted post-router `green-disclosure-1` complete.
- Package fidelity trace: `M9`, `M12`, `M23`, `M29`; full headings `Change Preventers` and `Smell-to-Treatment Priority Map`; Refactoring small-step, safety-net, and stop guidance.
- Attribution review: PASS - accepted answer selected both required skills and supplied the exact preferred move-members treatment, hierarchy-collapse fallback, risky paired-subclass treatment, and safe sequence.
- Behavioral result: PASS with context-cost diagnostic.
- Diagnostics: preserve the valid initial factory/registry failure. The accepted focused read reached the intended sections but was broad: eight of 20 Refactoring.Guru sections and 14 of 20 Refactoring sections. This isolated complex overlap is not systematic tier collapse.

## Independent Review

- Reviewer: PASS - independent full package reverse trace initially found one modality blocker, one false `M33` trace, and three mapping-role/evidence corrections; focused rereview verified every repair with no remaining P1/P2/P3 finding.
- Catalog snapshot: PASS - initial audit reproduced 14 rows, 6,789 bytes, SHA-256 `93d0f9b418a7071997419765278f894a5415bc397085f473b265aca678c6fd4a`; corrected audit reproduced 14 rows, 6,841 bytes, SHA-256 `f23977d3f201fc519c399fef75d7ed8d0f3b80e08f56da7a8659ad9c68d71a82` and approved all active ownership contracts after E2 was correctly classified as focused.
- Semantic verdict: initial PASS - exact mini/package wording, source modalities, traceability, initial description/router, all 20 index rows, metadata, and byte-identical full reference were independently accepted before execution. The compact technical guidance and full reference remain unchanged.
- Behavioral correction review: PASS - an independent reviewer traced the E2 discovery and E7b focused-routing/application failures, approved the 488-character source-backed description and packaging-only router correction, and prescribed all 11 replacement runs.
- Corrected catalog snapshot: PASS - no remaining ownership, description-boundary, router, source-preservation, required-set, fixture-hash, or disclosure-contract blocker to manifest creation.
- Corrected-catalog attribution review: source/package fidelity PASS and required discovery PASS `11/11`, but behavioral gate FAIL. E2 run 3 supplied a contradictory numeric threshold without reading required source detail; E1/E3 showed systematic ordinary over-read; one E1 answer invented a named `Remove Comments` technique. E4-E7b passed, including the repaired hierarchy-collapse fallback.
- Second router review: PASS - independent freeze audit verified the packaging-only body stop, explicit incomplete-library focused branch, bounded canonical catch-all, all seven disclosure expectations, exact 11-record change-impact set, unchanged 38/38 wording, byte-identical full reference, and unchanged 14-row catalog.
- Final attribution review: the previously accepted E1-E7b matrix remains `PASS`, but post-map E3 is `FAIL` because it falsely attributes `Parallel Arrays` to Refactoring.Guru. Independent review confirmed this is an answer-level failure, not unsupported package guidance.
- Unsupported or altered guidance: none identified in the package. The compact rules and full reference remain unchanged; neither router correction adds a technical treatment or retrofits the solver's invented thresholds or technique name.

## Validation Evidence

- Wording validation: PASS; `check_rule_wording.py` reports `38/38` exact mini rules, exact primary bias, and exact eight-item final checklist wording/order.
- Structural validation: PASS. The initial validator incorrectly derived `M1-M38` from 38 physical bullets; a test-first repair now accepts authoritative traceability IDs while checking physical wording separately. `validate_conversion.py` passes all 14 skills and reports 38 Refactoring.Guru mini bullets represented by stable `M1-M36`.
- Evaluation-contract validation: PASS; `validate_evaluation_contracts.py` accepts all durable required-skill sets, version-2 fields, fixture paths and hashes, independent-review fields, and final verdict block.
- Official skill validation: PASS; `uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/refactoring-guru` reports `Skill is valid!`.
- Full-reference equality: PASS; `cmp` exits `0`, and canonical full plus `references/full.md` share SHA-256 `c92bdfcb8fc5d64a21f10fe268a02bf6a9a9ce6228f83ac85743905cba4b2497`.
- Index validation: PASS independently of the mapping-ID failure; `20` canonical H2 sections equal `20` index rows with exact source order, anchors, and last-nonempty ranges, and the index parser reports no errors.
- Whitespace validation: PASS; `git diff --check` reports no tracked whitespace errors, the scoped artifact scan finds no trailing whitespace, and every scoped new file ends with a newline.
- Source release hashes: repaired mini `bb086ec559cbe0814518cf2fc479174244d94028529f870e05820fa7ab7a1a4c`; repaired nano `d909b7fdf6527d6b784fb54c98ae6f03d41e8fb2c53c3992e7b31dcfb7d67c52`; accepted `SKILL.md` `f6130665b1f3603a61a6ce13ab15cabeec3e53731334169f34427bebca6b4235`.
- Script tests: PASS; all 53 `_skill-workbench/scripts/tests` tests pass, including the stable-ID/multiple-physical-bullets regression.
- Invocation evaluation: PASS; accepted E1 and E2 each include Refactoring.Guru `3/3`, and all 11 current records include every required skill under subset semantics.
- Application evaluation: PASS with diagnostics; current E1-E7b pass, E2 preserves one focused-disclosure miss plus solver-authored numeric heuristics, and E7 preserves one broad focused read.
- Current matrix integrity: PASS; 11 records use 11 unique task IDs, catalog SHA-256 `f23977d3f201fc519c399fef75d7ed8d0f3b80e08f56da7a8659ad9c68d71a82`, frozen mapping SHA-256 `32a4e10c49537f0357c30b8b1ad202e2b322342af5497571511940c952b36a7b`, 11 unique manifest hashes, inner exit zero, and empty selection, integrity, manifest, and Codex error arrays.
- Remaining risks: only the preserved answer-level and context-cost diagnostics below; no source/package or current release blocker remains.

## Verdicts

- Source/package verdict: PASS - deterministic and independent semantic gates accept the repaired canonical compression and package without removed, weakened, strengthened, or imported guidance.
- Original behavioral observation: FAIL - initial E2 missed required Refactoring.Guru discovery in three valid runs, and initial E7b materially collapsed focused routing and supplied a noncanonical fallback. E1 and E3-E6 passed; E5a/E7a remain immutable NOT-RUN diagnostics.
- Current-state gate: FAIL for post-map answer attribution; source/package fidelity, required-skill inclusion, and progressive disclosure remain `PASS`.
- Residual diagnostics: preserved E5a/E7a ownership failures; valid initial E2/E7b failures; corrected-catalog E2 tier/threshold failure, E1/E3 over-reads, E1 invented technique name, and post-map E3 false `Parallel Arrays` catalog attribution; accepted E2 numeric heuristics plus one focused miss; accepted E7 broad focused read; repaired initial modality, traceability, and validator findings.
