# Patterns of Enterprise Application Architecture Skill Mapping

Evaluation contract version: 2

## Scope

- Distinctive lens: choose the smallest force-fit set of enterprise application patterns while making responsibility, persistence, transaction, concurrency, session-state, integration, and remote-boundary ownership explicit.
- Intended invocation: load when choosing or correcting business-logic, persistence, Unit of Work/identity/loading, lock/transaction, session-state, presentation/integration, or distribution patterns is central rather than merely present.
- Closest neighboring skills: Domain-Driven Design owns model discovery and deeper domain modeling; Implementing Domain-Driven Design owns tactical implementation after DDD commitment; Clean Architecture owns policy independence and dependency direction; Designing Data-Intensive Applications owns distributed-data authority, consistency, ordering, replay, and schema evolution; Code Complete owns general construction coordination.

## Reverse Trace and Source Repairs

- Reverse-traced every mini and nano prescription against the 404-line canonical full source before package authoring. The finding was book-specific; no shared process edit was required or permitted.
- Removed unsupported `framework` activation from the mini primary bias and checklist and from traceability framing; retained source-supported ORM, schema, and transport pressure.
- Split Remote Facade from DTO scope so Remote Facade remains remote-only while DTOs retain process/layer-boundary use (`M6`).
- Replaced broad object-relational `evolution cost` with the source's explicit serialization versioning condition (`M9`).
- Removed unsupported stale-lock cleanup and stale-lock diagnosis, then split Coarse-Grained Lock's related-object/user-edit predicate from Implicit Lock's hidden-acquisition and visibility predicate (`M11`, `M25`).
- Replaced Special Case `null/default` wording with the source's `null or exceptional` handling (`M15`).
- Restored the source's `when possible` qualifier for isolated domain tests (`M18`).
- Removed unsupported SQL-script, trigger, and framework-glue locations and the unsupported explicit-exception path from the misplaced-domain-behavior trigger (`M19`).
- Removed unsupported scattered lock acquisition and generic policy prescription from the centralization trigger (`M23`).
- Split long-running workflow handling from lock choice and restored explicit transaction ownership rather than one immediate transaction (`M25`).
- Replaced unsupported session owner, lifetime, and failover criteria with source-stated storage, integrity, security, scaling, cleanup, durability, server-farm sharing, and database-load criteria (`M27` and both checklists).
- Restored Identity Map's `where needed` applicability qualifier (`M8`).
- Restored `when possible` for avoiding remote-call transaction spans in the final checklist (`M10`).
- Split final checklist obligations so integration boundaries require clear translation without shaping internal design, while remote boundaries separately require coarse contracts, separation from local object design, versioning, and partial-failure awareness (`M13`, `M16`).
- Restored Plugin selection/extension without changing core code and Service Stub test-or-run scope (`M15`).
- Rechecked nano and nano trace after these repairs; no nano text changes are required because `N5` keeps general lock visibility and `N6-N7` already distinguish integration behavior from remote-boundary forces.
- `_rule-workbench/.../mini.md` and `nano.md` are byte-identical to their public book copies after repair. The canonical full source was not edited.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Force-based business logic | `choosing business-logic ... patterns is central`, reinforced by Transaction Script vs Table Module vs Domain Model | DDD model discovery and Implementing DDD's committed tactical model |
| Persistence and state | `persistence ... session-state ... patterns is central`, reinforced by Repository/Data Mapper/Gateway/Active Record | Clean Architecture policy/detail direction and DDIA data-authority semantics |
| Transactions and concurrency | `transaction, concurrency ... patterns is central` | DDIA distributed consistency, ordering, replay, and coordination semantics |
| Remote boundaries | `remote-boundary patterns is central` | DDIA cross-system data correctness and Release It production-failure survival |

Description length: 484 characters. The opening names the established lens; all branches require pattern choice to be central.

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| Choose Transaction Script, Table Module, or Domain Model for a use case | `{patterns-of-enterprise-application-architecture}` | Force-fit enterprise business-logic pattern choice is the central decision; DDD is not yet committed. |
| Discover missing domain concepts and resolve Ubiquitous Language conflicts | `{domain-driven-design}` | Model discovery is central; no enterprise pattern-family choice is requested. |
| Stop policy code from importing ORM and HTTP details | `{clean-architecture}` | Dependency direction and policy independence are central; persistence pattern choice is secondary unless separately requested. |
| Define authority, idempotency, ordering, schema evolution, and projection repair for a distributed write | `{designing-data-intensive-applications}` | Distributed-data semantics are central; this skill co-applies only when application/persistence/boundary pattern placement is also central. |
| Coordinate a broad implementation with defect-control and validation concerns | `{code-complete}` | General construction coordination is central; shared words such as implementation, review, and tests do not establish enterprise pattern ownership. |
| Place Service Layer, Repository/Data Mapper, Unit of Work, and DTO boundaries while defining durable event delivery | `{patterns-of-enterprise-application-architecture, designing-data-intensive-applications}` | Pattern placement and distributed-data correctness contribute independent central judgments. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description; early-guidance; final-check | Description; Responsibility and Business Logic Patterns; Final Checklist | Responsibility ownership is the opening active concern. |
| `N2` | description; early-guidance; final-check | Description; Responsibility and Business Logic Patterns; Final Checklist | Promotes the complete `M3-M4` business-logic choice. |
| `N3` | early-guidance | Responsibility and Business Logic Patterns | Promotes complete Service Layer rule `M5`. |
| `N4` | description; early-guidance; final-check | Description; Persistence, Identity, and State; Final Checklist | Promotes persistence choice `M7` without duplicating it. |
| `N5` | early-guidance; reference-router; final-check | Persistence, Identity, and State; Transactions and Concurrency; index rows for identity and concurrency; Final Checklist | Keeps Unit of Work, identity, loading, transaction, and lock visibility salient. |
| `N6` | early-guidance; final-check | Presentation, Integration, and Distribution; Final Checklist | Promotes complete boundary-behavior rules `M6`, `M12`, and `M13`. |
| `N7` | description; early-guidance; reference-router; final-check | Description; Presentation, Integration, and Distribution; distribution and workflow index rows; Final Checklist | Preserves coarse remote boundary and failure-cost pressure. |
| `N8` | description; early-guidance; final-check | Description; Responsibility and Business Logic Patterns; Persistence, Identity, and State; Final Checklist | Promotes session/base-pattern pressure and forbidden-pattern blocker `M28`. |
| `N9` | early-guidance | Responsibility and Business Logic Patterns | Promotes complete collapsed-responsibility trigger `M20`. |
| `N10` | early-guidance | Responsibility and Business Logic Patterns | Promotes complete Transaction Script escalation trigger `M21`. |
| `N11` | description; early-guidance | Description; Responsibility and Business Logic Patterns; Persistence, Identity, and State | Promotes ORM/database capture trigger `M22`. |
| `N12` | early-guidance; reference-router | Persistence, Identity, and State; Transactions and Concurrency; identity and concurrency index rows | Promotes `M24-M25` and bounded source routing. |
| `N13` | description; early-guidance; reference-router | Description; Presentation, Integration, and Distribution; workflow and distribution index rows | Promotes complete remote API trigger `M26`. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | Responsibility and Business Logic Patterns | Verbatim | First active rule under `N1` salience. |
| `M2` | Responsibility and Business Logic Patterns | Verbatim | Co-located with responsibility ownership. |
| `M3` | Responsibility and Business Logic Patterns | Verbatim | Promoted by `N2`. |
| `M4` | Responsibility and Business Logic Patterns | Verbatim | Kept beside `M3` force choice. |
| `M5` | Responsibility and Business Logic Patterns | Verbatim | Promoted by `N3`. |
| `M6` | Presentation, Integration, and Distribution | Verbatim | Repaired canonical wording kept exact. |
| `M7` | Persistence, Identity, and State | Verbatim | Promoted by `N4`. |
| `M8` | Persistence, Identity, and State | Verbatim | Promoted by `N5`. |
| `M9` | Persistence, Identity, and State | Verbatim | Repaired canonical wording kept exact. |
| `M10` | Transactions and Concurrency | Verbatim | Promoted by `N5`. |
| `M11` | Transactions and Concurrency | Verbatim | Repaired canonical wording kept beside `M10`. |
| `M12` | Presentation, Integration, and Distribution | Verbatim | Co-located with boundary behavior. |
| `M13` | Presentation, Integration, and Distribution | Verbatim | Co-located with DTO and remote rules. |
| `M14` | Persistence, Identity, and State | Verbatim | Session-state choice kept with state ownership. |
| `M15` | Persistence, Identity, and State | Verbatim | Repaired canonical wording kept exact. |
| `M16` | Presentation, Integration, and Distribution | Verbatim | Promoted by `N7`. |
| `M17` | Responsibility and Business Logic Patterns | Verbatim | Source order retained inside the implementation concern. |
| `M18` | Testing | Verbatim | Repaired source qualifier preserved. |
| `M19` | Responsibility and Business Logic Patterns | Verbatim | Repaired trigger follows placement rules. |
| `M20` | Responsibility and Business Logic Patterns | Verbatim | Promoted by `N9`. |
| `M21` | Responsibility and Business Logic Patterns | Verbatim | Promoted by `N10` and kept near `M3-M4`. |
| `M22` | Persistence, Identity, and State | Verbatim | Promoted by `N11`. |
| `M23` | Persistence, Identity, and State | Verbatim | Repaired centralization trigger kept with persistence choices. |
| `M24` | Persistence, Identity, and State | Verbatim | Promoted by `N12` and kept beside `M8`. |
| `M25` | Transactions and Concurrency | Verbatim | Repaired lock/long-workflow split kept exact. |
| `M26` | Presentation, Integration, and Distribution | Verbatim | Promoted by `N13`. |
| `M27` | Persistence, Identity, and State | Verbatim | Repaired session trigger kept with `M14`. |
| `M28` | Responsibility and Business Logic Patterns | Verbatim | Overall forbidden-pattern blocker closes the concern. |

## Wording Fidelity

- Verbatim primary bias: yes; exact repaired mini text.
- Verbatim mini rules: yes; all 28 rules match as an unordered exact-text multiset.
- Verbatim final checklist and order: yes; all nine repaired checklist items match in order.
- Documented exceptions: none between the repaired canonical mini and `SKILL.md`. Source repairs are recorded above and in traceability before package generation.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: the description states invocation ownership, headings group canonical guidance, router prose controls loading, and index predicates route to source-stated pattern forces. None adds a technical mechanism, default, guarantee, failure mode, or exception.

## Size Exception

The canonical mini is 1,167 words, already above the 500-word target. `SKILL.md` is 1,284 words and 73 lines, for 117 words of packaging overhead. The active body therefore preserves the complete mini rather than compressing it during conversion; overhead remains below the 150-word target and the 100-line limit passes.

## Evaluation Cases

The seven original raw fixtures remain frozen. E4 and E6 were rejected before execution and preserved unchanged as pre-run diagnostics; separately named E4b and E6b replacements were frozen afterward. Independent corrected-catalog review approved all seven active contracts, and the resulting 11-record behavioral matrix is recorded below.

### E1: Direct pattern review

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/direct-pattern-review.md`
- Fixture SHA-256: `196e516d72d4740968a5b7442a707413cb990b929ab31d5cf8829f3a7bae9537`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: choose the smallest fitting business-logic, persistence, transaction, and remote-boundary patterns by their forces and assign responsibility ownership.
- Neighbor ownership: DDD may become relevant if exemptions and approvals become a model-discovery problem, but this fixture asks for the prior enterprise pattern choice; DDIA may own remote-delivery semantics only if expanded beyond the stated boundary.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-1`, `green-batch4-2`, and `green-batch4-3`; all selected Patterns of Enterprise Application Architecture, with run 1 focused and runs 2-3 ordinary
- Package fidelity trace: `M1`, `M3-M7`, `M10`, `M13`, `M16-M18`, `N1-N4`, `N7`
- Attribution review: `PASS`; the source backs the Domain Model/Service Layer, Repository/Data Mapper, Unit of Work/transaction, Remote Facade/DTO, and responsibility-placement advice, while async handoff, pending state, outbox-style reliability, retries, reconciliation, and concrete policy types remain identified as general solver additions
- Behavioral result: `pass`; required inclusion and materially correct application are `3/3`
- Diagnostics: run 1 is a coherent nonblocking `8/19` focused over-read; runs 2-3 resolve the same fixture from `SKILL.md` alone; all three records contain only the shell-snapshot cleanup warning

### E2: Distinctive unnamed review

- Class: recognition
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/distinctive-unnamed-review.md`
- Fixture SHA-256: `231196d81d61306de28c4d61386dc6d52cc4629068036383499f0ffbefb173fa`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: identify collapsed controller, SQL, transaction, domain, and remote responsibilities and choose force-fit business-logic, data-access, Service Layer, and coarse remote patterns without assuming DDD commitment.
- Neighbor ownership: DDD is secondary because rich modeling is only future pressure; Clean Architecture dependency direction and Code Complete construction are not the central requested choice.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-1`, `green-batch4-2`, and `green-batch4-3`; all selected Patterns of Enterprise Application Architecture in ordinary mode, and run 2 additionally selected Clean Architecture
- Package fidelity trace: `M1-M7`, `M10`, `M12-M13`, `M16`, `M19-M23`, `M26`, `M28`, `N1-N4`, `N6-N11`, `N13`
- Attribution review: `PASS`; the source backs the Transaction Script/Service Layer, bounded persistence boundary, explicit local transaction, coarse Remote Facade, and responsibility-level testing advice, while Clean Architecture independently backs run 2's use-case boundary and replaceable gateway and the asynchronous delivery mechanisms remain general additions
- Behavioral result: `pass`; unnamed discovery and materially correct application are `3/3`
- Diagnostics: the unnamed fixture does not reveal the target skill, book, or lens name; Clean Architecture is an allowed source-backed extra in run 2; all three records contain only the shell-snapshot cleanup warning

### E3: Ordinary customer credit

- Class: application
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/ordinary-customer-credit.md`
- Fixture SHA-256: `d44659ce0adf9b5dcd41c5b935a55283e6afd9fe8fd4849d4165e6bd2975cb76`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: keep a simple local operation simple while placing validation, workflow, transaction, persistence, response mapping, and responsibility-level tests explicitly.
- Neighbor ownership: DDD investment is not central because lifecycle growth is explicitly absent; Code Complete may contribute construction detail but does not own the pattern-fit decision.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-1`; selected Patterns of Enterprise Application Architecture in ordinary mode
- Package fidelity trace: `M1`, `M3-M7`, `M10`, `M12`, `M17-M18`, `N1-N4`, `N6`
- Attribution review: `PASS`; the source backs the small transaction-script Service Layer, repositories, explicit customer/audit transaction, boundary DTO, and responsibility-aligned tests, while concrete audit columns and locking/update syntax remain general additions
- Behavioral result: `pass`; the answer keeps the local operation bounded and applies the intended simple-flow pattern choice
- Diagnostics: ordinary disclosure passes; `FOR UPDATE` is stronger than the fixture proves necessary and remains conditional on expected contention and justified cost, while the guarded-update alternative prevents material error; the record contains only the shell-snapshot cleanup warning

### E4: Focused inheritance mapping

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/focused-inheritance-mapping.md`
- Fixture SHA-256: `99f5fa7b91a7a5ab1decbe63888444af1bb2a227e27f1b4d91274b0fdd3667ce`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: choose among Single Table, Class Table, and Concrete Table Inheritance from nullable-column simplicity, normalized join complexity, and duplication pressure.
- Neighbor ownership: DDD may own whether identity/lifecycle justify the hierarchy, but the fixture fixes the hierarchy and asks for relational mapping tradeoffs; DDIA storage internals are not central.
- Ownership review: REJECTED before execution; the fixture reveals the suspected compact-body omission and conversion rationale
- Reference expectation: focused
- Compact-body gap: `SKILL.md` names inheritance mapping but omits the source's concrete nullable-column, normalized-join, and concrete-table duplication tradeoffs.
- Intended index destinations: `Object-Relational Mapping Pattern Index`
- Runs: not run; rejected before execution as an invalid focused prompt
- Package fidelity trace: `M9`, `N4`, full heading `Object-Relational Mapping Pattern Index`
- Attribution review: not run; no solver answer exists, and workload/schema candidates remain fixture facts
- Behavioral result: not applicable; the rejected fixture was never run and produced no behavioral failure
- Diagnostics: pre-run invalid diagnostic preserved unchanged because the prompt discloses the compact-body gap; intended route remains `1/19` full sections

### E4b: Focused inheritance mapping replacement

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/focused-inheritance-mapping-v2.md`
- Fixture SHA-256: `351572e25b61059c65a5ab10308e80c76c2d442e9912f5d06ec71261af2db205`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: choose among Single Table, Class Table, and Concrete Table Inheritance from nullable-column simplicity, normalized join complexity, and duplication pressure.
- Neighbor ownership: DDD may own whether identity/lifecycle justify the hierarchy, but the fixture fixes the hierarchy and asks only for relational inheritance mapping tradeoffs; DDIA storage semantics are not central.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: focused
- Compact-body gap: `SKILL.md` names inheritance mapping but omits the source's concrete nullable-column, normalized-join, and concrete-table duplication tradeoffs.
- Intended index destinations: `Object-Relational Mapping Pattern Index`
- Runs: `green-batch4-1`; selected Patterns of Enterprise Application Architecture and read only `Object-Relational Mapping Pattern Index` in focused mode
- Package fidelity trace: `M9`, `N4`, full heading `Object-Relational Mapping Pattern Index`
- Attribution review: `PASS`; the answer accurately retrieves and attributes the source's nullable-column, normalized-data/join-complexity, and concrete-table duplication forces, while the workload and schema candidates remain fixture facts
- Behavioral result: `pass`; required inclusion, concrete mapping-detail retrieval, and focused disclosure all pass
- Diagnostics: replacement asks for the smallest applicable packaged source section without revealing the suspected omission, conversion rationale, target skill, book, or lens name; the one-section read is bounded; only the shell-snapshot cleanup warning remains

### E5: Comprehensive claims audit

- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/comprehensive-claims-audit.md`
- Fixture SHA-256: `3d4e5f1e92b8922fbbed7f85e87b659fcd0a72665dca39bea9b51dca939b98c6`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: apply the complete catalog across every source concern while selecting staged, force-fit corrections rather than a rewrite or indiscriminate pattern stack.
- Neighbor ownership: Clean Architecture, DDD, DDIA, and Code Complete may add compatible guidance only where their distinct objectives become central; the requested exhaustive enterprise pattern catalog remains the target ownership.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: comprehensive
- Runs: `green-batch4-1`; selected Patterns of Enterprise Application Architecture and read `full.md` end to end in comprehensive mode
- Package fidelity trace: `M1-M28`, `N1-N13`, full reference `*`
- Attribution review: `PASS`; the blocker classifications and major pattern choices trace to the source, the supplied design inventory remains fixture data, and Aggregate vocabulary, concrete use-case names, and stale-session mechanisms remain general additions
- Behavioral result: `pass`; exhaustive application and comprehensive retrieval both pass
- Diagnostics: the unnamed disclosure fixture requires the complete applicable packaged reference without naming a skill, book, or lens; no stderr warning, attribution issue, or disclosure issue remains

### E6: Nano pressure ORM capture

- Class: pressure
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/nano-pressure-orm-capture.md`
- Fixture SHA-256: `e61f4006a2c5a84618df52fb00f1d13c934ed5dd40e497651aa49a46ab68951c`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: resist schedule and sunk-cost pressure to trust ORM-shaped responsibility, hidden lazy loading, ad hoc remote calls, and unclear transaction outcomes while still choosing the smallest earned correction.
- Neighbor ownership: the frozen prompt's demonstrated partial remote reservations, whole-endpoint retry, and before-shipping decision independently activate DDIA cross-system semantics and Release It production-failure concerns, so the target-only required set cannot receive an ownership PASS.
- Ownership review: REJECTED before execution; target-only ownership is not defensible against the live catalog
- Reference expectation: ordinary
- Runs: not run; rejected before execution as an invalid target-only ownership contract
- Package fidelity trace: `M1-M8`, `M10`, `M12-M13`, `M16`, `M19-M24`, `M26`, `M28`, `N1-N13`
- Attribution review: not run; no solver answer exists, and partial reservations/retries remain fixture facts
- Behavioral result: not applicable; the rejected fixture was never run and produced no behavioral failure
- Diagnostics: pre-run ownership-rejected diagnostic preserved with its original target-only required set and hash; no reassignment or broadened required set was applied

### E6b: Nano pressure ORM capture replacement

- Class: pressure
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/nano-pressure-orm-capture-v2.md`
- Fixture SHA-256: `e0b4285296d79d773aacbf4fb67286f94dc31c80dfa1ee9ebcd6d9411e989e63`
- Required skills: `{patterns-of-enterprise-application-architecture}`
- Distinctive judgment: resist schedule pressure and ORM/schema capture by choosing the smallest force-fit business-logic, Service Layer, persistence, transaction, loading, and presentation correction for a local operation.
- Neighbor ownership: the fixture fixes one local database transaction and excludes external calls, asynchronous work, retries, and long-running workflow, so DDIA cross-system semantics and Release It production-failure decisions are not independently central; DDD remains secondary until richer model discovery is requested.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-1`; selected Patterns of Enterprise Application Architecture in ordinary mode
- Package fidelity trace: `M1-M5`, `M7-M8`, `M10`, `M12`, `M17`, `M19-M24`, `M28`, `N1-N6`, `N8-N12`
- Attribution review: `PASS`; the source backs rejecting controller business logic, generic-CRUD/loading opacity, and ORM-driven responsibility, introducing a real Service Layer operation, making loading explicit, and deferring unearned richer patterns, while concrete ORM fetch choices remain general additions
- Behavioral result: `pass`; the answer applies the smallest-earned-pattern judgment under schedule pressure without importing distributed-system concerns
- Diagnostics: replacement keeps ORM/schema/pattern capture central without independently requiring distributed-data or production-failure guidance; the Transaction Script shape is consistent even though it is not named; only the shell-snapshot cleanup warning remains

### E7: Compatible distributed order flow

- Class: application
- Prompt or artifact: `_skill-workbench/evaluations/cases/patterns-of-enterprise-application-architecture/compatible-distributed-order-flow.md`
- Fixture SHA-256: `f31a34fcc9b0b7cda31b78996189a927003c9951c33b54d470e6c3dc130383a1`
- Required skills: `{patterns-of-enterprise-application-architecture, designing-data-intensive-applications}`
- Distinctive judgment: Patterns of Enterprise Application Architecture owns Service Layer, business-logic, Repository/Data Mapper/Unit of Work, transaction, DTO, and remote-boundary placement; DDIA independently owns authoritative records, idempotency, ordering scope, schema evolution, projection rebuild/repair, and partial-success data semantics.
- Neighbor ownership: DDD is not committed and Clean Architecture dependency direction is secondary; both required skills contribute separate central decisions rather than shared vocabulary.
- Ownership review: PASS - independent corrected Batch 4 catalog audit against 13-skill snapshot `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`
- Reference expectation: ordinary
- Runs: `green-batch4-1`; selected required Patterns of Enterprise Application Architecture and Designing Data-Intensive Applications; the target read 11 bounded sections and DDIA read `full.md`, making the overall mode comprehensive
- Package fidelity trace: target `M1`, `M3-M8`, `M10`, `M13`, `M16-M18`, `M20`, `M23-M26`, `N1-N7`, `N9`, `N12-N13`; DDIA package traces are reviewed by its owner
- Attribution review: `PASS`; the target source independently backs application-pattern placement while DDIA backs authority, idempotency, ordering, schema evolution, projection repair, and partial-success semantics; exact delivery schemas, status codes, and reconciliation mechanisms remain general design choices
- Behavioral result: `pass`; both required skills contribute materially distinct guidance and no attribution is crossed
- Diagnostics: coherent nonblocking high-context over-read (`11/19` target sections plus DDIA `*`); compatible overlap permits additional relevant selections; only the shell-snapshot cleanup warning remains

## Independent Review

- Reviewer: `.superpowers/sdd/task-2-review.md` rejected the pre-repair package; `.superpowers/sdd/task-2-rereview.md` and `task-2-rereview-final.md` close all findings with a final `PASS`.
- Catalog snapshot: `PASS - FREEZE`; `.superpowers/sdd/catalog-review-final.md` independently approved all 21 active contracts against the corrected 13-description payload, 6,335 bytes, SHA-256 `5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`.
- Semantic verdict: `PASS`; source/package fidelity and all seven active fixture-ownership contracts, including E4b and E6b, are independently approved.
- Unsupported or altered guidance: none remain. All six source/package defects were repaired; the E4 record-placement correction was independently verified.

## Validation Evidence

- Structural validation: `rtk python3 _skill-workbench/scripts/validate_conversion.py patterns-of-enterprise-application-architecture` returned `PASS`: 73-line, 1,284-word `SKILL.md`, 117 words beyond mini, 28 mini rules, 13 nano rules, and 19 indexed full-reference sections.
- Official skill validation: `rtk uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/patterns-of-enterprise-application-architecture` returned `Skill is valid!` with exit 0.
- Full-reference equality: `cmp` passed; canonical and packaged SHA-256 are `e7f30e7d65005924ec29cc0c6f032aedd0b1bffa22223d5386c5a3140cd76af0`
- Index validation: the repository validator confirmed all 19 headings, anchors, order, heading-to-last-nonempty ranges, and direct links. An initial range-only failure exposed that nonblank horizontal separators belong to preceding sections; ranges were corrected and the same gate passed.
- Wording fidelity: `check_rule_wording.py` returned exact primary bias, 28/28 exact rule matches, no missing or added rules, and exact nine-item checklist wording/order.
- Evaluation contracts: `validate_evaluation_contracts.py` returned `PASS: durable required-skill and versioned evaluation contracts are valid`; all nine original/replacement fixture hashes match.
- Public/workbench equality: `cmp` passed for both mini and nano copies.
- Whitespace: scoped `git diff --check` passed, and the explicit trailing-whitespace/final-newline scan passed all 23 Task 2 artifact files.
- Invocation evaluation: direct recognition `3/3`; distinctive unnamed recognition `3/3`; all six valid records include the target skill
- Application evaluation: `11/11` valid active records include every required skill and apply distinctive source guidance; disclosure modes are ordinary `7`, focused `2`, and comprehensive `2`
- Remaining risks: preserve the two coherent over-reads, one allowed Clean Architecture extra, conditional pessimistic-lock option, general delivery additions, ten shell-snapshot cleanup warnings, and inactive no-output E4/E6 diagnostics.

## Verdicts

- Source/package verdict: PASS; independent post-repair semantic review and deterministic fidelity checks pass
- Original behavioral observation: PASS; the first valid active Batch 4 matrix completed `11/11`, with direct and unnamed discovery `3/3` each, all required sets included, and no valid first-run miss to preserve
- Current-state gate: PASS; source/package, corrected catalog ownership, `11/11` behavioral application, and progressive-disclosure review pass
- Residual diagnostics: preserve direct run 1's `8/19` target over-read, E7's `11/19` target plus full-DDIA over-read, the source-backed Clean Architecture extra in E2 run 2, E3's conditional pessimistic-lock option, general outbox/retry/reconciliation additions, ten shell-snapshot cleanup warnings, and the inactive no-output E4/E6 diagnostics
