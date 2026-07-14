# The Pragmatic Programmer Skill Mapping

Evaluation contract version: 2

## Scope

- Distinctive lens: own engineering outcomes across the local edit by keeping knowledge authoritative, concerns orthogonal, volatile choices reversible, learning incremental, repeated work automated, and feedback fast.
- Intended invocation: select only when accountability, adaptability, knowledge ownership, change fan-out, premature commitment, prototype fossilization, manual delivery and feedback, or blackboard-style coordination are central across a change; ordinary coding quality or a single shared word is insufficient.
- Closest neighboring skills: `clean-code` owns local readability and code shape; `code-complete` owns construction coordination and defect control; `refactoring` owns behavior-preserving structural change; `working-effectively-with-legacy-code` owns gaining first feedback when safe change is blocked; `release-it` owns production failure and capacity behavior; `a-philosophy-of-software-design` owns module depth, information hiding, and complexity reduction.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`; the description uses a positive centrality threshold and names neighbor ownership to avoid acting as an always-selected umbrella.
- Canonical source repair: the 2026-07-14 reverse trace removed unsupported schedule-pressure blame, vendor debugging-blame examples, validated/controlled metadata routing, an automatic regression-test mandate, and unsupported `example` and `recovery` qualifiers; it restored the full source's repeated-tool-friction trigger. Independent-review repairs then restored `M28`'s canonical generated-code, tools, specifications, and formal-methods categories, removed diagram broadening, and made `M29` require a working slice without a prototype alternative. The canonical full source was not edited.

## Description Branches

Candidate description (497 characters):

> The Pragmatic Programmer guidance for accountable, adaptable delivery. Use when outcome ownership, duplicated knowledge, change fan-out, irreversible commitment, prototype fossilization, manual delivery/feedback loops, or blackboard-style coordination are central across a change. Clean Code owns local readability; Code Complete construction; Refactoring behavior-preserving change; Legacy Code blocked first feedback; Release It! production failure; A Philosophy of Software Design module depth.

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Outcome ownership | `accountable, adaptable delivery` and `outcome ownership` | Generic implementation work where no cross-edit outcome or ownership decision is central. |
| Knowledge and coupling | `duplicated knowledge` and `change fan-out` | Clean Code's local textual duplication and A Philosophy of Software Design's module-depth and information-hiding decisions. |
| Adaptability under uncertainty | `irreversible commitment` and `prototype fossilization` | Refactoring's behavior-preserving sequencing and Legacy Code's blocked-first-feedback control. |
| Delivery feedback | `manual delivery/feedback loops` | Code Complete's general construction coordination and Release It!'s production failure behavior. |
| Coordination fit | `blackboard-style coordination` | DDIA may add ordering, replay, or distributed-data semantics, but this source owns when the named shared-space mechanism fits uncertain order, multiple sources, or opportunistic collaboration. |
| Positive threshold | `central across a change` | Broad quality, maintainability, coding, review, testing, or tooling vocabulary without the distinctive cross-change ownership lens. |
| Neighbor ownership | `Refactoring behavior-preserving change; Legacy Code blocked first feedback` plus the remaining explicit final sentence | Preserves the live distinction between protected structural change and gaining first feedback while allowing co-invocation for independently central concerns. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Use The Pragmatic Programmer lens to keep a tax export accountable, reversible, orthogonal, and fast to verify." | `the-pragmatic-programmer` | Direct invocation plus the target's distinctive outcome, knowledge, reversibility, and feedback concerns. |
| "Three entry points copy one rule, the vendor schema owns the domain, and six release commands live in one engineer's memory." | `the-pragmatic-programmer` | Unnamed ownership, DRY knowledge, reversibility, automation, and feedback pressure. |
| "Rename this boolean, split this mixed function, and remove its flow-narrating comments." | `clean-code` | Local readability and code shape are central without cross-change outcome ownership. |
| "Coordinate requirements, data representation, error policy, tests, review, debugging, and tuning for this implementation." | `code-complete` | Construction coordination and defect control are central; broad construction vocabulary alone does not activate this skill. |
| "Make this module deeper, hide volatile representation, and reduce interface complexity." | `a-philosophy-of-software-design` | Module depth, information hiding, and complexity reduction are the objective. |
| "Extract and move these methods without changing supplied observable behavior." | `refactoring` | Behavior-preserving structural change is central; no independent pragmatic outcome decision is stated. |
| "Behavior is unknown and the database dependency blocks the first focused test." | `working-effectively-with-legacy-code` | Gaining first feedback is blocked, so Legacy Code owns control before broader improvement. |
| "Keep provider knowledge reversible and automate failover while defining bounded retries, timeouts, isolation, and recovery." | `the-pragmatic-programmer`, `release-it` | Pragmatic ownership, reversibility, and automation are central alongside independent production-failure semantics. |
| "Several handlers receive evidence in uncertain order and may collaborate opportunistically through one shared case board." | `the-pragmatic-programmer`; DDIA may co-invoke | The target owns whether blackboard-style coordination fits; DDIA may independently contribute ordering or replay semantics without replacing the target. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance | Description lens; `Accountability and Adaptability` | Promotes complete pragmatic stopping rule `M1`. |
| `N2` | description, early-guidance, final-check | Description knowledge branch; `Knowledge Ownership and Orthogonality`; final checklist | Promotes `M4` and `M24` without creating a shortened active rule. |
| `N3` | description, early-guidance, final-check | Description fan-out branch; `Knowledge Ownership and Orthogonality`; final checklist | Promotes complete orthogonality rules `M5` and `M25`. |
| `N4` | description, early-guidance, final-check | Description commitment branch; `Accountability and Adaptability`; final checklist | Promotes `M6`, `M26`, and `M27`. |
| `N5` | description, early-guidance, final-check | Description prototype branch; `Feedback and Tool Leverage`; final checklist | Promotes tracer, prototype, and feedback rules `M8`, `M9`, `M12`, `M28`, and `M29`. |
| `N6` | description, early-guidance, final-check | Description manual-delivery branch; `Knowledge Ownership and Orthogonality`; `Feedback and Tool Leverage`; final checklist | Promotes `M11`, `M16`, and `M33`. |
| `N7` | early-guidance, final-check | `Contracts, Failure, and State`; final checklist | Promotes complete contract, failure, resource, and cross-boundary rules `M13`-`M15`, `M30`, and `M31`. |
| `N8` | early-guidance, final-check | `Contracts, Failure, and State`; final checklist | Promotes shared-state and concurrency rules `M17` and `M32`. |
| `N9` | early-guidance | `Feedback and Tool Leverage` | Promotes complete reproduced-facts debugging rules `M19` and `M36`. |
| `N10` | description, early-guidance, final-check | Description feedback branch; `Feedback and Tool Leverage`; final checklist | Promotes complete feedback and test-path rules `M12` and `M34`. |
| `N11` | early-guidance | `Accountability and Adaptability` | Promotes complete requirements rule `M10`. |
| `N12` | description, early-guidance, final-check | Description accountability branch; `Accountability and Adaptability`; final checklist | Promotes result ownership, touched-area responsibility, team quality, and broken-window rules `M2`, `M3`, `M22`, `M23`, and `M37`. |
| `N13` | description, early-guidance, final-check | Description knowledge branch; `Knowledge Ownership and Orthogonality`; final checklist | Promotes `M4` and copied-fact trigger `M24`. |
| `N14` | description, early-guidance, final-check | Description fan-out branch; `Knowledge Ownership and Orthogonality`; final checklist | Promotes `M5` and `M25`. |
| `N15` | description, early-guidance, final-check | Description commitment branch; `Accountability and Adaptability`; final checklist | Promotes `M6`, `M26`, and `M27`. |
| `N16` | description, early-guidance, final-check | Description manual-delivery branch; `Feedback and Tool Leverage`; final checklist | Promotes `M11` and `M33`. |
| `N17` | description, early-guidance, reference-router, final-check | Description prototype branch; `Feedback and Tool Leverage`; router to `Tooling Rules`; final checklist | Promotes `M18`, `M19`, `M28`, and `M36`; full-only tool detail remains focused reference material. |
| `N18` | early-guidance, final-check | `Contracts, Failure, and State`; final checklist | Promotes `M14`, `M15`, `M17`, `M31`, and `M32`. |
| `N19` | early-guidance | `Accountability and Adaptability` | Promotes `M10` without adding a separate requirements rule. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Accountability and Adaptability` | Moved verbatim | Leads with pragmatic outcomes and stopping. |
| `M2` | `Accountability and Adaptability` | Moved verbatim | Keeps explicit ownership and blame boundary early. |
| `M3` | `Accountability and Adaptability` | Moved verbatim | Keeps future maintenance and low-cost touched-area improvement together. |
| `M4` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Establishes one owner and automated duplicated process steps. |
| `M5` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Co-locates orthogonality with fan-out trigger `M25`. |
| `M6` | `Accountability and Adaptability` | Moved verbatim | Promoted by reversibility salience and placed beside `M26` and `M27`. |
| `M7` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Keeps domain language beside knowledge boundaries. |
| `M8` | `Feedback and Tool Leverage` | Moved verbatim | Opens the feedback group with a thin real slice. |
| `M9` | `Feedback and Tool Leverage` | Moved verbatim | Co-locates prototype learning with fossilization trigger `M28`. |
| `M10` | `Accountability and Adaptability` | Moved verbatim | Keeps requirements discovery beside reversible learning. |
| `M11` | `Feedback and Tool Leverage` | Moved verbatim | Co-locates automation with repeated-step trigger `M33`. |
| `M12` | `Feedback and Tool Leverage` | Moved verbatim | Preserves fast-feedback salience. |
| `M13` | `Contracts, Failure, and State` | Moved verbatim | Opens explicit contract ownership. |
| `M14` | `Contracts, Failure, and State` | Moved verbatim | Keeps complete failure distinctions and containment. |
| `M15` | `Contracts, Failure, and State` | Moved verbatim | Keeps resource ownership and cleanup together. |
| `M16` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Keeps inspectable formats beside authoritative knowledge. |
| `M17` | `Contracts, Failure, and State` | Moved verbatim | Co-locates state costs with cross-boundary state trigger `M32`. |
| `M18` | `Feedback and Tool Leverage` | Moved verbatim | Keeps tool leverage beside source understanding and debugging. |
| `M19` | `Feedback and Tool Leverage` | Moved verbatim | Co-locates reproduced-facts debugging with `M36`. |
| `M20` | `Accountability and Adaptability` | Moved verbatim | Keeps increments beside uncertainty and feedback. |
| `M21` | `Accountability and Adaptability` | Moved verbatim | Treats communication artifacts as outcome ownership. |
| `M22` | `Accountability and Adaptability` | Moved verbatim | Keeps shared team responsibility beside individual ownership. |
| `M23` | `Accountability and Adaptability` | Moved verbatim | Keeps broken-window containment beside `M37`. |
| `M24` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Co-locates copied facts with `M4`. |
| `M25` | `Knowledge Ownership and Orthogonality` | Moved verbatim | Co-locates fan-out with `M5`. |
| `M26` | `Accountability and Adaptability` | Moved verbatim | Complete repaired reversibility trigger beside `M6`. |
| `M27` | `Accountability and Adaptability` | Moved verbatim | Keeps uncertainty remedies beside tracer and prototype guidance. |
| `M28` | `Feedback and Tool Leverage` | Moved verbatim | Preserves prototype hardening plus the canonical generated-code, tools, specifications, and formal-methods categories; diagram skepticism is not folded into this rule. |
| `M29` | `Accountability and Adaptability` | Moved verbatim | Keeps the canonical working-slice-only specification-trap remedy beside requirements `M10`; prototype use remains in `M9`, `M27`, `M28`, and `N5`. |
| `M30` | `Contracts, Failure, and State` | Moved verbatim | Keeps hidden assumptions beside explicit contracts `M13`. |
| `M31` | `Contracts, Failure, and State` | Moved verbatim | Keeps recovery, context, and cleanup ownership together. |
| `M32` | `Contracts, Failure, and State` | Moved verbatim | Keeps state, synchronization, cleanup, and ordering together. |
| `M33` | `Feedback and Tool Leverage` | Moved verbatim | Keeps repeated rituals beside automation `M11`. |
| `M34` | `Feedback and Tool Leverage` | Moved verbatim | Keeps degraded test feedback beside `M12`. |
| `M35` | `Feedback and Tool Leverage` | Moved verbatim | Restored canonical repeated-tool-friction trigger. |
| `M36` | `Feedback and Tool Leverage` | Moved verbatim | Keeps unexplained behavior beside debugging `M19`. |
| `M37` | `Accountability and Adaptability` | Moved verbatim | Keeps local decay beside broken windows `M23`. |

## Wording Fidelity

- Verbatim primary bias: yes; exact canonical mini text.
- Verbatim mini rules: yes; all 37 decision and trigger bullets match exactly as an unordered multiset.
- Verbatim final checklist and order: yes; all 10 items match exactly and retain order.
- Documented exceptions: none in package authoring; source-compression repairs were completed before package generation and are recorded in traceability and Scope.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: the description only routes invocation and assigns catalog ownership; its blackboard branch traces exactly to `Resource and Coupling Rules` line 243. Concern headings only organize canonical rules; router prose only chooses ordinary, focused, or comprehensive access. The focused router names full-source topic families but adds no mechanism, default, guarantee, failure mode, exception, or preference.
- Prescriptive router conditions: `Use this file alone for ordinary matched work, and stop when it resolves the task` implements the process's ordinary tier; the bounded unresolved-question route implements focused disclosure; the comprehensive-audit or explicit-complete-lens route implements exhaustive disclosure.

## Size Exception

- Canonical mini: 992 words.
- `SKILL.md`: 1,106 words and 80 lines.
- Packaging overhead: 114 words, within the 150-word target.
- Rationale: the canonical mini already exceeds 500 words. Source and wording fidelity require retaining all 37 complete rules and the 10-item checklist; no additional compression was performed during conversion.

## Evaluation Cases

### E1: Direct Accountable Delivery

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/direct-accountable-delivery.md`
- Fixture SHA-256: `f417b32d5bf76be34dc02066185cc491faa87283bdc43f5ae7afb83bb9808fa6`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: The target owns accountable delivery, authoritative knowledge, orthogonality, reversibility, automation, and fast feedback as one operating-style decision.
- Neighbor ownership: Clean Code and Code Complete may help with local implementation, but the fixture makes cross-entry-point knowledge ownership and reversible delivery central; no production-failure or blocked-first-feedback objective is stated.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: current valid `green-batch4-description-final-1`, `green-batch4-description-final-integrity-replacement-2`, and `green-batch4-description-final-3`; required target included `3/3`; all ordinary
- Package fidelity trace: `M1-M12`, `M20-M27`, `M29`, `M33`, `N1-N6`, `N10-N16`, and the final checklist
- Attribution review: `PASS`; all three answers apply source-backed knowledge ownership, reversibility, orthogonality, automated feedback, and explicit outcome ownership while keeping concrete golden-file, adapter, and rollout details as general additions
- Behavioral result: `pass`; direct discovery and distinctive application are `3/3`
- Diagnostics: preserve current invalid `green-batch4-description-final-2` and historical invalid `green-batch4-2` as index-only/ordinary reporting evidence; neither is a behavioral sample

### E2: Distinctive Unnamed Outcome Ownership

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/unnamed-outcome-ownership.md`
- Fixture SHA-256: `d869553f51c12d27bb19473b82db8448dc7c3c58408000fcda992863b5071a60`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: The unnamed fixture requires ownership beyond team and tool blame, one authority for copied rules, reversible vendor commitment, a thin real slice, automation, and early feedback.
- Neighbor ownership: Schedule and code vocabulary are incidental; Clean Code does not own process or knowledge authority, Code Complete does not own the distinctive outcome-accountability combination, and Legacy Code is not blocked from first feedback.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-description-final-1`, `green-batch4-description-final-2`, and `green-batch4-description-final-3`; required target included `3/3`; all ordinary
- Package fidelity trace: `M2`, `M4`, `M6`, `M8`, `M11`, `M12`, `M20`, `M22`, `M24`, `M26`, `M27`, `M33`, `N2`, `N4-N6`, `N10`, `N12`, `N13`, `N15`, and `N16`
- Attribution review: `PASS`; Pragmatic remains primary in all three answers, while APoSD, Clean Architecture, and Code Complete extras are independently source-backed and secondary; concrete component names and schedules remain general additions
- Behavioral result: `pass`; unnamed discovery and distinctive application are `3/3`
- Diagnostics: fixture does not name the book, skill, or lens; APoSD appears in all three runs, Clean Architecture in run 2, and Code Complete in run 3; all are allowed extras and all records remain body-only

### E3: Ordinary Version and Release Duplication

- Class: application
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/ordinary-version-release-duplication.md`
- Fixture SHA-256: `bfa0fbe8216743c3d9602a0985b95213d6893eac3c269ed76a465c2e3976d4f0`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: Choose one owner for the version fact, decouple build from promotion, automate repeated release work, and shorten verification without broad redesign.
- Neighbor ownership: Code Complete construction discipline is secondary; no local readability, behavior-preserving refactor, blocked legacy feedback, or production resilience decision is central.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: current valid `green-batch4-description-final-required-set-replacement-1`; selected the required target in ordinary mode
- Package fidelity trace: `M1`, `M4`, `M5`, `M11`, `M12`, `M16`, `M20`, `M24`, `M25`, `M33`, `N1-N3`, `N6`, `N10`, `N13`, `N14`, and `N16`
- Attribution review: `PASS`; the answer applies source-backed one-owner knowledge, orthogonal build/promotion, automation, and earlier verification while keeping `package.json`, exact-artifact promotion, and filename checks as general choices
- Behavioral result: `pass`; the correctly configured ordinary replacement includes the target and applies the intended bounded judgment
- Diagnostics: preserve `green-batch4-description-final-1` as invalid invocation evidence because dispatch added `release-it` to the frozen target-only required set; it is not a valid selection miss

### E4: Focused Opportunistic Coordination

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/focused-opportunistic-coordination.md`
- Fixture SHA-256: `eb9cebc246459bba2209bf55add49670c5134790849bed085a97c7960108b6fa`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: Decide whether uncertain order, multiple sources, or opportunistic collaboration justify blackboard-style coordination without turning the case into a general architecture audit.
- Neighbor ownership: A Philosophy of Software Design may assess module interfaces, but the requested source-specific mechanism and its applicability conditions belong to this full rule; Code Complete does not own that mechanism.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: focused
- Compact-body gap: `SKILL.md` says shared state and coupling must earn their cost but does not state when blackboard-style coordination is justified.
- Intended index destinations: `Resource and Coupling Rules`
- Runs: `green-batch4-description-final-1`; selected the required target and read exactly `Resource and Coupling Rules` in focused mode
- Package fidelity trace: full heading `Resource and Coupling Rules`, especially canonical rule 7 at lines 243-244
- Attribution review: `PASS`; the answer retrieves and applies the exact source-backed uncertain-order, multiple-sources, and opportunistic-collaboration conditions while keeping case-state and confidence mechanics as general additions
- Behavioral result: `pass`; required discovery, one-section retrieval, and distinctive blackboard applicability judgment all pass
- Diagnostics: fixture does not name the book, skill, or lens; preserve historical valid DDIA-only miss `green-batch4-1`; DDIA remains a permitted extra but cannot replace the target's source-specific judgment

### E5: Comprehensive Delivery Audit

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/comprehensive-delivery-audit.md`
- Fixture SHA-256: `3f375252a29f73cf615cd6cc3131d1306f6d6ae02a8018a7371be26355621934`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: Apply the complete accountable-delivery, knowledge, orthogonality, reversibility, feedback, automation, contract, resource, team, and broken-window lens end to end.
- Neighbor ownership: Other skills may contribute to particular findings, but the explicit complete-reference objective and the listed cross-cutting concerns make this target central; added skills remain compatible diagnostics.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: comprehensive
- Runs: `green-batch4-description-final-1`; selected the required target and read `full.md` end to end with `sections=["*"]`
- Package fidelity trace: `M1-M37`, `N1-N19`, all 26 full headings, and the final checklist
- Attribution review: `PASS`; the answer applies the complete source lens and explicitly separates source-backed findings from general implementation suggestions
- Behavioral result: `pass`; exhaustive application and comprehensive retrieval both pass
- Diagnostics: fixture does not name the book, skill, or lens and explicitly requests end-to-end packaged reference use; no attribution or disclosure issue remains

### E6: Vendor Deadline Pressure

- Class: pressure
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/pressure-vendor-deadline.md`
- Fixture SHA-256: `7318fcfaaf8d2ebe0cbdcaa22b683d539d8ddc521126ab483269f1b19dd5d13a`
- Required skills: `{the-pragmatic-programmer}`
- Distinctive judgment: Under deadline, authority, and sunk-cost pressure, retain outcome ownership, one knowledge authority, reversibility, a thin real slice, automatic tests, diagnostic context, and explicit prototype hardening.
- Neighbor ownership: Clean Code schedule pressure is not the requested local-readability decision; Code Complete may support construction, but the central pressure is accountability and adaptability across delivery.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-description-final-1`; selected the required target in focused mode
- Package fidelity trace: `M2`, `M4`, `M6`, `M8`, `M9`, `M11`, `M12`, `M14`, `M20`, `M22`, `M24`, `M26-M28`, `M33`, `N2`, `N4-N7`, `N10`, `N12`, `N13`, `N15-N17`, and the final checklist
- Attribution review: `PASS`; the answer applies source-backed reversibility, vendor-boundary isolation, one knowledge owner, automation, fast feedback, and prototype-hardening guidance while keeping pilot-domain and test mechanics as general additions
- Behavioral result: `pass`; the target remains selected and distinctive guidance is applied under deadline and sunk-cost pressure
- Diagnostics: expected ordinary but read 11/26 coherent target sections across several concern families; preserve as a nonblocking high-context over-read, not material tier collapse

### E7: Release It!-Compatible Provider Boundary

- Class: application
- Prompt or artifact: `_skill-workbench/evaluations/cases/the-pragmatic-programmer/release-it-compatible-provider.md`
- Fixture SHA-256: `d1da8b3808de35b35cf4af89b80270bf980451e51f199260a2215eed664ac0ea`
- Required skills: `{the-pragmatic-programmer, release-it}`
- Distinctive judgment: The target owns provider-knowledge authority, reversible commitment, automated failover, diagnostic responsibility, and explicit boundary ownership; Release It! independently owns timeout, retry safety, demand limits, isolation, recovery, and production readiness.
- Neighbor ownership: Neither skill subsumes the other. Clean Architecture may be compatible if policy direction becomes central, but the fixture supplies a provider-boundary objective rather than a policy-import dispute.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-description-final-1`; selected required Pragmatic and Release It! plus APoSD in ordinary mode
- Package fidelity trace: target `M2`, `M4-M6`, `M11-M17`, `M24-M27`, `M30-M33`, `N2-N8`, `N10`, `N12-N16`, `N18`; Release It! fidelity remains governed by its own mapping
- Attribution review: `PASS`; Pragmatic independently owns provider knowledge, reversibility, automation, diagnostics responsibility, and boundary ownership; Release It! independently owns timeouts, retry safety, limits, isolation, recovery, and production readiness; APoSD's caller-centered boundary advice is source-backed and secondary
- Behavioral result: `pass`; both required skills contribute materially distinct guidance in a body-only answer
- Diagnostics: APoSD is an allowed extra; exact timeout numbers, object names, re-drive view, and metric fields remain general solver additions

## Independent Review

- Reviewer: `.superpowers/sdd/task-3-rereview.md` passed the source body; `.superpowers/sdd/task-3-description-review.md` passed the source-backed blackboard description branch; `.superpowers/sdd/attribution-pragmatic-final-report.md` passed current application, attribution, and disclosure with no findings.
- Catalog snapshot: `PASS - FREEZE`; `.superpowers/sdd/catalog-review-final.md` independently approved all 21 active contracts against the corrected 13-description payload, 6,335 bytes, SHA-256 `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`.
- Semantic verdict: `PASS`; canonical mini/nano, body, index, full reference, corrected description, and all seven active ownership contracts are independently approved.
- Unsupported or altered guidance: none. The new activation branch traces exactly to canonical `Resource and Coupling Rules` line 243; independent description review found no broadening or neighbor-boundary defect.

## Validation Evidence

- Structural validation: `rtk python3 _skill-workbench/scripts/validate_conversion.py the-pragmatic-programmer` passed after the description correction: `SKILL.md 80 lines; 1106 words (114 beyond mini); 37 mini rules and 19 nano rules mapped; 26 full-reference sections indexed`.
- Official skill validation: `rtk uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/the-pragmatic-programmer` passed with `Skill is valid!`.
- Full-reference equality: `rtk cmp the-pragmatic-programmer/the-pragmatic-programmer.md .agents/skills/the-pragmatic-programmer/references/full.md` passed; both files have SHA-256 `ea10063caff1989c1442c2aff501a942281fb5b06456e822ab856c701fc5e28d`.
- Released compression equality: scoped `rtk cmp` checks passed for workbench versus public mini and nano copies.
- Index validation: repository validation passed all 26 H2 headings, anchors, source order, line ranges, and nonempty `Read when` routes.
- Wording validation: passed after repair with 37/37 exact mini-rule matches, exact primary bias, exact final checklist wording and order, and zero missing, added, or reworded rules.
- Evaluation-contract validation: `rtk python3 _skill-workbench/scripts/validate_evaluation_contracts.py` passed with `durable required-skill and versioned evaluation contracts are valid`; all seven fixture hashes match.
- Whitespace validation: scoped `rtk git diff --check` passed; a scoped final-newline and trailing-whitespace audit passed for tracked and untracked assigned files.
- Invocation evaluation: current direct recognition `3/3`; current unnamed recognition `3/3`; every valid record includes the target
- Application evaluation: current `11/11` valid post-description records include every required skill and apply distinctive source guidance; disclosure modes are ordinary `8`, focused `2`, and comprehensive `1`
- Remaining risks: preserve the two current invalid process-boundary records, historical direct invalid record, historical focused required-skill miss, pressure over-read, allowed extras, and nonfatal environment warnings.

## Verdicts

- Source/package verdict: PASS; canonical source, mini/nano, body, index, full reference, and the source-backed description correction pass independent review
- Original behavioral observation: valid focused E4 run missed the required target and selected DDIA alone; one direct run was separately rejected for self-report integrity, its named replacement passed, and the original matrix stopped before E5-E7
- Current-state gate: PASS for the current `11/11` valid post-description records; corrected catalog ownership, required-skill inclusion, distinctive application, attribution, and progressive disclosure pass without absorbing excluded evidence
- Residual diagnostics: preserve current invalid direct reporting and wrong-required-set records, the historical direct invalid record, the historical focused DDIA-only miss, E6's high-context over-read, allowed extras in E2/E7, general solver additions, and nonfatal environment warnings
