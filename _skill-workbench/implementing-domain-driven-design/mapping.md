# Implementing Domain-Driven Design Skill Mapping

## Scope

- Distinctive lens: implementation-level DDD after the context and model commitment, with practical guidance for Bounded Contexts, local language, Aggregate consistency boundaries, tactical model objects, Repositories, Domain and Application Services, Domain Events, modules, translations, and client-facing projections.
- Intended invocation: select when one or more of those DDD implementation decisions or their characteristic failure modes are central to implementing, changing, or reviewing an already committed domain model. The presence of domain nouns, services, repositories, events, or a database alone is insufficient.
- Closest neighboring skills: `domain-driven-design-distilled` owns whether and where DDD earns its investment; `domain-driven-design` owns strategic discovery, Ubiquitous Language development, Context Mapping, and deeper model insight; `clean-architecture` owns policy/detail dependency direction; `designing-data-intensive-applications` owns distributed data correctness. `code-complete`, `clean-code`, `refactoring`, `working-effectively-with-legacy-code`, and `release-it` may co-apply only when their separate objective is independently central.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`. The description therefore requires a central, implementation-level DDD decision and names the two closest DDD boundaries before permitting compatible DDIA overlap.
- Candidate description: `Implementing Domain-Driven Design guidance for implementation-level DDD after context and model commitment. Use when Aggregate boundaries, Value Objects/Entities, Repositories, Domain or Application Services, Domain Events, modules, translations, projections, or renamed-CRUD/anemic-model correction is central. Distilled owns the DDD investment gate; Domain-Driven Design owns strategic discovery and deeper model development; DDIA co-applies only for central distributed-data semantics.`
- Candidate description length: 488 characters.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Post-commit implementation lens | `implementation-level DDD after context and model commitment` | `domain-driven-design-distilled` before the DDD investment decision and `domain-driven-design` while discovering language, contexts, or deeper model insight. |
| Tactical model implementation | `Aggregate boundaries, Value Objects/Entities, Repositories, Domain or Application Services, Domain Events` are central | Generic object, service, repository, event, or persistence work without an active DDD model and implementation decision. |
| Structural and boundary implementation | `modules, translations, projections` are central | `clean-architecture` dependency direction and ordinary package, adapter, query, or DTO work without Bounded Context or Aggregate pressure. |
| Characteristic implementation failure | `renamed-CRUD/anemic-model correction` is central | Local readability or construction concerns that do not require DDD tactical semantics. |
| Distributed-data overlap | `DDIA co-applies only for central distributed-data semantics` | Domain Events, projections, or multiple systems by themselves; DDIA joins only for authority, consistency, replay, ordering, schema evolution, repair, or comparable data contracts. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Use Implementing Domain-Driven Design to implement this approved Subscription context." | `implementing-domain-driven-design` | Direct retrieval plus implementation-level Aggregate, Repository, event, Application Service, module, and projection decisions. |
| "The Pricing context and language are approved; implement roots, invariants, Repository, event publication, translation, and quoting projection." | `implementing-domain-driven-design` | Distinctive unnamed post-commit DDD implementation. |
| "Should this simple CRUD support tool receive tactical DDD, and where is the smallest honest investment?" | `domain-driven-design-distilled`, not the target by default | The unresolved decision is whether DDD earns its cost, not how to implement a committed model. |
| "Discover the language collision, Context Map, and deeper model for pricing before choosing implementation mechanisms." | `domain-driven-design`, not the target by default | Strategic discovery and deeper modeling remain open. |
| "Implement OrderPlaced through a durable, replay-safe, versioned search projection with rebuild." | `implementing-domain-driven-design` plus `designing-data-intensive-applications` | Domain event/application boundaries and distributed replay, ordering, evolution, authority, and repair are independently central. |
| "Move pricing policy out of Prisma and Express while preserving the supplied local model." | `clean-architecture`, optionally `refactoring`, not the target unless a DDD implementation decision is also central | Policy/detail ownership is the unresolved decision; DDD vocabulary alone does not activate this skill. |
| "Implement and review a nontrivial feature across several ordinary construction concerns." | `code-complete`, not the target without committed DDD pressure | Broad construction coordination does not imply tactical DDD. |

## Source Fidelity Inventory

- Canonical full: `implementing-domain-driven-design/implementing-domain-driven-design.md`, SHA-256 `cd2c1d404f60720cebca17fcffed9d68d94b1eef4a13bed63a4f59f01db005ad`; copied only to `references/full.md`.
- Canonical mini: `implementing-domain-driven-design/implementing-domain-driven-design.mini.md`, SHA-256 `c6e289e1845713512a9749a42a497fa3745851ae1fb129762e66c8c92d5f3d80`; one primary bias, 28 decision/trigger rules, and 13 final-check items form the active semantic inventory.
- Canonical nano: `implementing-domain-driven-design/implementing-domain-driven-design.nano.md`, SHA-256 `613342311705b9bab66c3ac3b1f7f846d8a9f7d695bc7467c4abcd52d8c40bf6`; 12 items influence discovery, ordering, focused routing, or final checking without becoming duplicate active rules.
- Traceability: `_rule-workbench/implementing-domain-driven-design/traceability.md`, SHA-256 `91cc60007ffdca93bf3402c4d286952b7800dd69d13d8a4aa6e40c1574819d71`; every retained compressed detail was reverse-traced there before this conversion.
- Reference inventory: all 19 level-two canonical headings are represented once in `references/index.md`; the index is the only full-section `Read when` inventory.

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance, final-check | Post-commit description branch; `Context, Language, and Translation`; final checklist | Promotes complete `M1`, `M2`, and `M19` guidance rather than repeating the compressed nano rule. |
| `N2` | description, early-guidance, reference-router, final-check | Tactical and boundary description branches; `Context, Language, and Translation`; focused router; final checklist | Keeps cross-context identifiers, messages, contracts, model-sharing qualifiers, and semantic-enum boundary together through `M4` and `M20`. |
| `N3` | description, early-guidance, reference-router, final-check | Tactical description branch; `Aggregate Boundaries and Tactical Model`; focused router; final checklist | Promotes complete `M6`, `M7`, `M22`, and `M23` guidance without fragmenting root, identity, transaction, or eventual-coordination conditions. |
| `N4` | description, early-guidance, reference-router, final-check | Tactical description branch; `Aggregate Boundaries and Tactical Model`; focused router; final checklist | Promotes complete `M8-M10` rules so Entity, Value Object, and Domain Service predicates retain their qualifiers. |
| `N5` | description, early-guidance, reference-router, final-check | Tactical description branch; `Repositories, Events, and Application Coordination`; focused router; final checklist | Keeps Repository reconstitution/persistence, Aggregate-needs API guidance, malformed-design predicates, and Application Service decision/orchestration semantics complete through `M11`, `M14`, `M24`, and `M26`. |
| `N6` | description, early-guidance, reference-router, final-check | Tactical description branch; `Repositories, Events, and Application Coordination`; focused router; final checklist | Promotes complete Domain Event and Event Sourcing gates from `M12`, `M13`, and `M25`. |
| `N7` | description, early-guidance, reference-router, final-check | Structural description branch; `Modules, Representations, and Delivery`; focused router; final checklist | Promotes complete `M16` and `M27` representation pressure, including the conditions on command/query separation and scope identifiers. |
| `N8` | early-guidance, final-check | `Context, Language, and Translation`; final checklist | The full `M19` trigger stays beside context and language rules; its renaming effect is not duplicated in the description. |
| `N9` | early-guidance, reference-router, final-check | `Aggregate Boundaries and Tactical Model`; focused router; final checklist | The complete `M7` and `M22` rules retain the compelling-reason exception and eventual-consistency alternatives. |
| `N10` | description, early-guidance, reference-router, final-check | Structural and boundary description branches; context and representation concerns; focused router; final checklist | Keeps Anticorruption Layer, application-facing representation, and technical mapping conditions distinct through `M5`, `M21`, and `M27`. |
| `N11` | description, early-guidance, final-check | Characteristic-failure description branch; canonical primary bias; `Modeling Investment`; final checklist | Renamed CRUD and anemic-model pressure is front-loaded by the exact primary bias and description while complete simplicity rules remain in `M3` and `M28`. |
| `N12` | reference-router, final-check | Focused implementation-review route; final checklist | The review trigger routes to bounded full sections when needed; the canonical checklist performs the active scan without a duplicate rule bullet. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Context, Language, and Translation` | Moved verbatim | Leads normal use with explicit context before implementation artifacts. |
| `M2` | `Context, Language, and Translation` | Moved verbatim | Keeps local language, artifact coverage, and renaming together. |
| `M3` | `Modeling Investment` | Moved verbatim | Co-located with `M28` so Core Domain investment and simple-subdomain restraint remain one concern without becoming the Distilled activation gate. |
| `M4` | `Context, Language, and Translation` | Moved verbatim | Stays with context relationships and translation responsibility. |
| `M5` | `Context, Language, and Translation` | Moved verbatim | Stays beside the foreign-model trigger `M21`. |
| `M6` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Leads the Aggregate concern with immediate invariants and root discipline. |
| `M7` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Stays beside the boundary and multi-Aggregate transaction trigger `M22`. |
| `M8` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Keeps Entity identity, lifecycle, transitions, behavior, and behavior-rich qualifier intact. |
| `M9` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Keeps Value Object selection, examples, immutability qualifier, validation, equality, and invariant locality intact. |
| `M10` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Keeps Domain Service predicates, Transformation Service purpose, and technical-mapping boundary as one source rule. |
| `M11` | `Repositories, Events, and Application Coordination` | Moved verbatim | Preserves reconstitution and persistence, domain-oriented results instead of ORM rows, implementation rule exclusion, and the source's `should` wording for Aggregate-needs APIs; stays beside `M24`. |
| `M12` | `Repositories, Events, and Application Coordination` | Moved verbatim | Stays beside the event-shape trigger `M25`. |
| `M13` | `Repositories, Events, and Application Coordination` | Moved verbatim | Preserves the Event Sourcing persistence-model gate and stream evolution mechanisms. |
| `M14` | `Repositories, Events, and Application Coordination` | Moved verbatim | Stays beside the Application Service trigger `M26`, retaining `may own` rather than strengthening ownership. |
| `M15` | `Modules, Representations, and Delivery` | Moved verbatim | Keeps context-first and within-context ownership structure together. |
| `M16` | `Modules, Representations, and Delivery` | Moved verbatim | Keeps client representation, cross-context composition, conditional command/query split, and conditional scope identifiers whole. |
| `M17` | `Modules, Representations, and Delivery` | Moved verbatim | Preserves the canonical code-generation order as an implementation rule. |
| `M18` | `Modules, Representations, and Delivery` | Moved verbatim | Keeps direct domain and boundary testing as one concern. |
| `M19` | `Context, Language, and Translation` | Moved verbatim | Placed after context and language rules as their concrete ambiguity and placeholder trigger. |
| `M20` | `Context, Language, and Translation` | Moved verbatim | Placed with context relationships and contracts to keep three coupling symptoms and their replacement together. |
| `M21` | `Context, Language, and Translation` | Moved verbatim | Placed after `M5` and `M20` to distinguish ACL, application-facing representation, and technical mapping pressure. |
| `M22` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Placed after complete Aggregate rules to bind boundary changes and multi-Aggregate transactions to immediate invariants. |
| `M23` | `Aggregate Boundaries and Tactical Model` | Moved verbatim | Placed beside root discipline so external mutation remediation stays intention-revealing. |
| `M24` | `Repositories, Events, and Application Coordination` | Moved verbatim | Preserves the separate giant-generic and Repository-per-table-without-Aggregate-thinking predicates, ORM-row or persistence-entity leakage, misplaced business rules, and the source's `should` wording; stays beside `M11`. |
| `M25` | `Repositories, Events, and Application Coordination` | Moved verbatim | Placed beside `M12-M13` to restore model-local past-tense facts without inventing event mechanisms. |
| `M26` | `Repositories, Events, and Application Coordination` | Moved verbatim | Preserves the Domain Model's core-decision predicate, the `all branching business rules` qualifier, and duplicated-controller orchestration remediation; stays beside `M14`. |
| `M27` | `Modules, Representations, and Delivery` | Moved verbatim | Placed beside `M16` to bind client/query pressure to representations rather than Aggregate reshaping. |
| `M28` | `Modeling Investment` | Moved verbatim | Co-located with `M3` as the honest simple-versus-rich modeling trigger. |

## Wording Fidelity

- Verbatim primary bias: exact.
- Verbatim mini rules: all 28 decision and trigger rules are moved whole and exact; no rule is added, omitted, merged, or reworded.
- Verbatim final checklist and order: all 13 items are exact and remain in canonical order.
- Documented wording exceptions: none.
- Repaired-source regeneration: stale package text for `M11`, `M24`, and `M26` was replaced verbatim from the independently accepted repaired mini; no other mini rule or checklist item was changed.
- Non-obvious reordering: context/language/translation leads; Aggregate and tactical model follows; Repositories/events/Application Services form one concern; modules/representations/delivery remain together; `M3` and `M28` close the active guidance as one modeling-investment concern. Source-relative order is preserved inside each concern.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Catalog-routing directive: `Distilled owns the DDD investment gate; Domain-Driven Design owns strategic discovery and deeper model development; DDIA co-applies only for central distributed-data semantics.` This selects among book lenses, derives from the reviewed pairwise compatibility decisions, and adds no domain implementation rule.
- Progressive-disclosure directives: the four `Reference Router` paragraphs implement the repository's ordinary, focused, and comprehensive loading contract. They govern file reads, not software design.
- Index routing inventory: every `Read when` cell is manually authored from its same-named canonical full heading. The Client Representation and Scope Discipline row preserves separate predicates for client-shape representations, conditional command/query separation, conditional scope identifiers, and application/integration-layer cross-context composition. The rows describe source questions and symptoms; they do not prescribe a mechanism beyond the linked section.
- Review: concern headings, description branches, transitions, and routing prose organize canonical guidance only. No new technical mechanism, default, example, guarantee, failure mode, exception, or preference is attributed to the book.

## Repair History

- On 2026-07-13, independent acceptance of the repaired source superseded the prior package wording for `M11`, `M24`, and `M26` and exposed an over-broad Client Representation and Scope Discipline routing predicate.
- Regeneration replaced only those three active bullets verbatim and repaired the one index cell so each canonical condition governs only its own mechanism.
- At this repaired-source regeneration point, the 488-character description and byte-identical full reference remained unchanged. All seven durable case contracts remained unchanged and every run was still pending; no behavioral solver had run yet.
- The prior catalog freeze is invalidated. Parent reconciliation and a new freeze are required before behavioral evaluation.

## Size Exception

- Canonical mini: 1,511 words.
- `SKILL.md`: 1,678 words across 79 lines after the later router-only correction.
- Packaging overhead: 167 words, 17 above the 150-word soft target and within the documented 151-200 allowance.
- Description: 488 characters.
- Decision: retain the source-driven exception because the canonical mini already exceeds the 500-word target, all 28 rules and 13 checklist items are required for complete ordinary use, and the extra packaging preserves a narrow post-commit catalog boundary plus explicit ordinary/focused/comprehensive routing. Do not paraphrase canonical guidance to reduce the count.

## Evaluation Cases

The seven frozen fixtures below were recorded before behavioral execution. The reconciled ten-skill catalog was frozen before these Batch 3 runs. Extra skill selections are permitted under the current evaluation contract.

### E1: Direct Subscription Implementation

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/direct-subscription-implementation.md`.
- Fixture SHA-256: `764dfa6f65d2d27d613a86611892b42632439daa0ce126d79ad379f5059e61e7`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: direct book-name retrieval must include the target; additional independently relevant skills are permitted.
- Reference expectation: ordinary; the committed context and tactical implementation correction are covered by `SKILL.md`.
- Relevant sections: not applicable for expected ordinary use.
- Runs:
  - Preserved pre-fix failure: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-1.json`; thread `019f5c4a-edc3-7170-a7b2-e96d15f6366f`; `exit_code: 1`, `result: null`, empty recorded stderr, and no selection or disclosure evidence. The live endpoint rejected the then-current schema's unsupported `uniqueItems`; this artifact predates `codex_errors` preservation and is excluded from planned-run and acceptance counts.
  - Preserved pre-fix retry: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-retry-1.json`; thread `019f5c4b-370b-7320-8655-368005806043`; `exit_code: 1`, `result: null`, empty recorded stderr, and no selection or disclosure evidence. It failed for the same schema reason and is excluded from planned-run and acceptance counts.
  - Valid run 1 replacement: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-valid-1.json`; thread `019f5c50-347c-7981-acd3-a38921a095d7`; selected `{implementing-domain-driven-design}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
  - Run 2: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-2.json`; thread `019f5c51-ae04-78c3-94b2-f773a13fd447`; selected `{implementing-domain-driven-design}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md` and `.agents/skills/implementing-domain-driven-design/references/full.md`; sections `{implementing-domain-driven-design: [*]}`; `reference_mode: comprehensive`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
  - Run 3: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-3.json`; thread `019f5c53-1a02-7450-af4a-051a65f57b3a`; selected `{implementing-domain-driven-design}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/references/index.md`, and `.agents/skills/implementing-domain-driven-design/references/full.md`; sections `{implementing-domain-driven-design: [*]}`; `reference_mode: comprehensive`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: `M1-M2`, `M4-M18`, `M20-M27`, `N1-N7`, `N9-N10`, and `N12`.
- Attribution review: `PASS`. Aggregate boundaries, identity references, invariant-bearing behavior, Aggregate-oriented Repositories, Domain Events, Application Service coordination, context translation, modules, and the renewal-history projection trace to the accepted package. Outbox publication, optimistic concurrency, persistence uniqueness, idempotency, and compensation are solver-added implementation mechanisms; they are not credited to the book.
- Conversion result: `PASS` for E1 required-skill discovery and application under the subset contract.
- Diagnostics: valid run 1 stayed ordinary, but runs 2 and 3 read the target full reference end to end despite the ordinary expectation. These two comprehensive reads are explicit over-reading diagnostics. They do not establish material tier collapse because all three unnamed runs and the dedicated ordinary run stayed `SKILL.md`-only, the focused route remained bounded, and the comprehensive route remained reachable.

### E2: Unnamed Approved Pricing Implementation

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/unnamed-pricing-implementation.md`.
- Fixture SHA-256: `0ee9f694b31c685fb76af3f45c3e53ed083bf7456493a17b69f4e625547083fa`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: this is the distinctive unnamed implicit-invocation case; the approved context and language keep strategic discovery out of scope.
- Reference expectation: ordinary; the target body covers roots, identities, invariants, Repository shape, publication coordination, translation, modules, and projection pressure.
- Relevant sections: not applicable for expected ordinary use.
- Runs:
  - Run 1: `_skill-workbench/evaluations/results/implementing-domain-driven-design/unnamed-pricing-implementation/green-batch3-1.json`; thread `019f5c54-e9bf-72b0-9afb-031efc7bc62f`; selected `{domain-driven-design, implementing-domain-driven-design, clean-architecture}`; consulted `.agents/skills/domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/SKILL.md`, and `.agents/skills/clean-architecture/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
  - Run 2: `_skill-workbench/evaluations/results/implementing-domain-driven-design/unnamed-pricing-implementation/green-batch3-2.json`; thread `019f5c56-9f64-7613-be70-2a702b50f04d`; selected `{implementing-domain-driven-design, clean-architecture}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md` and `.agents/skills/clean-architecture/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
  - Run 3: `_skill-workbench/evaluations/results/implementing-domain-driven-design/unnamed-pricing-implementation/green-batch3-3.json`; thread `019f5c58-0edc-7d62-b4b4-077bbf5f60ed`; selected `{domain-driven-design, implementing-domain-driven-design, clean-architecture}`; consulted `.agents/skills/domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/SKILL.md`, and `.agents/skills/clean-architecture/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: `M1-M2`, `M4`, `M6-M7`, `M9`, `M11-M12`, `M14-M17`, `M20-M21`, `M27`, and `N1-N7`, `N10`, `N12`.
- Attribution review: `PASS`. Roots, identities, Value Objects, invariant placement, reconstitution, Aggregate-shaped Repository, publication coordination, context translation, modules, and quoting projection trace to the target package. Database uniqueness, optimistic concurrency, outbox, idempotent/rebuildable projection behavior, and strict dependency-direction details are solver or selected-neighbor additions and are not credited to Implementing DDD.
- Conversion result: `PASS`; distinctive unnamed discovery included the target in all `3/3` runs.
- Diagnostics: all three runs over-selected `clean-architecture`; runs 1 and 3 also selected `domain-driven-design`. The answers did not reopen strategic discovery or contradict the approved context, and every run remained ordinary, so the extra selections are context-cost diagnostics only.

### E3: Ordinary Anemic Billing Correction

- Class: application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/ordinary-anemic-billing-model.md`.
- Fixture SHA-256: `d44e7c735e824b771d28c75d37b45172b6c9d634a14da3328fb6ba4508c340ae`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: bounded implementation correction with accepted context and terminology; no strategic redesign is requested.
- Reference expectation: ordinary; `SKILL.md` is sufficient and should stop disclosure.
- Relevant sections: not applicable for expected ordinary use.
- Runs: `_skill-workbench/evaluations/results/implementing-domain-driven-design/ordinary-anemic-billing-model/green-batch3-1.json`; thread `019f5c59-7f38-7051-a599-6297de3aa67e`; selected `{implementing-domain-driven-design}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: `M6`, `M8-M9`, `M11-M12`, `M14`, `M23-M26`, `N3-N6`, and `N11-N12`.
- Attribution review: `PASS`. The bounded correction moves issuance invariants into the `Invoice` Aggregate, introduces domain values, replaces generic row access with an Aggregate Repository, emits `InvoiceIssued`, and leaves transaction/publication coordination in the application service, all from active package guidance.
- Conversion result: `PASS`.
- Diagnostics: target-only selection and `SKILL.md`-only use provide the dedicated ordinary-tier success evidence; no over-read or material unsupported attribution was observed.

### E4: Focused Claim Dashboard Repository Dispute

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/focused-claim-dashboard-query.md`.
- Fixture SHA-256: `f0e0e555ae7db0a61a75fb7f04879b6b205dbce2292e74de00e9a7d16668c532`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: the prompt explicitly bounds the dispute and forbids a complete Claims audit.
- Reference expectation: focused; use the index to select the smallest source subset.
- Relevant sections: Repository semantics and client/query representation, principally `Repository Rules` and `Client Representation and Scope Discipline`; no exact section set is required.
- Runs: `_skill-workbench/evaluations/results/implementing-domain-driven-design/focused-claim-dashboard-query/green-batch3-1.json`; thread `019f5c89-1bd6-7223-8bfd-65955e6439f4`; selected `{implementing-domain-driven-design, clean-architecture}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/references/index.md`, `.agents/skills/implementing-domain-driven-design/references/full.md`, `.agents/skills/clean-architecture/SKILL.md`, `.agents/skills/clean-architecture/references/index.md`, and `.agents/skills/clean-architecture/references/full.md`; sections `{implementing-domain-driven-design: [Repository Rules, Client Representation and Scope Discipline], clean-architecture: [Required Layer Responsibilities]}`; `reference_mode: focused`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: `M11`, `M16`, `M24`, `M27`, `N5`, `N7`, `N12`, and the two named full headings.
- Attribution review: `PASS`. The Repository-versus-query decision and application-facing read representation trace directly to the two target headings; outer-adapter ownership is consistent with the separately selected Clean Architecture heading and is not credited to Implementing DDD.
- Conversion result: `PASS`.
- Diagnostics: the target read exactly the two semantically expected headings, and the neighboring skill read one coherent heading. The extra `clean-architecture` selection is diagnostic; the bounded retrieval is far below the target's one-third manual-review threshold and shows no tier collapse.

### E5: Comprehensive Marketplace Implementation Audit

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/comprehensive-marketplace-implementation.md`.
- Fixture SHA-256: `6e31bf7a5c155143db4e0cd61c18773f3d3e6281cbde9e41ac48e2fb8fefaad6`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: explicit complete Implementing DDD audit; additional relevant skills remain permitted.
- Reference expectation: comprehensive; read `references/full.md` end to end and record `*`.
- Relevant sections: all 19 level-two headings.
- Runs: `_skill-workbench/evaluations/results/implementing-domain-driven-design/comprehensive-marketplace-implementation/green-batch3-1.json`; thread `019f5c8a-0114-70e2-84df-6b89d2741222`; selected `{implementing-domain-driven-design}`; consulted `/Users/jakubtomanik/github/agent-rules-books/.agents/skills/implementing-domain-driven-design/SKILL.md` and `/Users/jakubtomanik/github/agent-rules-books/.agents/skills/implementing-domain-driven-design/references/full.md`; sections `{implementing-domain-driven-design: [*]}`; `reference_mode: comprehensive`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: every `M*`, `N*`, checklist item, and full heading.
- Attribution review: `PASS`. The end-to-end findings cover context-local models, small Aggregates, behavior-rich objects, Aggregate Repositories, meaningful events, thin Application Services, context-first modules, ACL translation, and read projections supported across the complete accepted reference. Process-manager wording is a solver-level implementation label rather than a new book rule.
- Conversion result: `PASS`.
- Diagnostics: target-only selection and `[*]` provide the required comprehensive-tier evidence; reading `full.md` directly without the index is valid for an end-to-end route.

### E6: Aggregate Boundary Under Deadline Pressure

- Class: pressure and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/pressure-cross-aggregate-transaction.md`.
- Fixture SHA-256: `0dd792df09684c2bb2b5dff43a1bfa9bfd6ee3445d43ce21fa4923e60eca5490`.
- Required skills: `{implementing-domain-driven-design}`.
- Selection notes: schedule, sunk-cost, and authority pressure test the nano-prioritized context, Aggregate, identity, transaction, integration, and Application Service guardrails without inviting a rewrite.
- Reference expectation: ordinary; the complete mini-derived body supplies the bounded correction.
- Relevant sections: not applicable for expected ordinary use.
- Runs: `_skill-workbench/evaluations/results/implementing-domain-driven-design/pressure-cross-aggregate-transaction/green-batch3-1.json`; thread `019f5c8b-0d67-75f0-8a3f-52421162a8ed`; selected `{implementing-domain-driven-design, domain-driven-design-distilled, designing-data-intensive-applications}`; consulted `.agents/skills/implementing-domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/references/index.md`, `.agents/skills/implementing-domain-driven-design/references/full.md`, `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/designing-data-intensive-applications/SKILL.md`, `.agents/skills/designing-data-intensive-applications/references/index.md`, and `.agents/skills/designing-data-intensive-applications/references/full.md`; sections `{implementing-domain-driven-design: [Aggregate Rules of Thumb, Domain Event Rules, Application Service Rules, Context Integration Rules, Final Instruction], designing-data-intensive-applications: [Reliability Rules, Consistency Rules, Idempotency and Replay Rules, Event, Log, and Stream Rules, Transaction Rules, API and Service Boundary Rules, Schema Evolution Rules]}`; `reference_mode: focused`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Package fidelity trace: `M4-M7`, `M14`, `M20-M23`, `M26`, `N2-N3`, `N5`, `N9-N10`, and `N12`.
- Attribution review: `PASS` with answer-level diagnostics. The local Order transaction, identity references, explicit integration messages, application coordination, foreign-status translation, and bounded change trace to the target package. Outbox guarantees, process-manager/result-message mechanics, retries, and compensation are solver or DDIA additions and are not credited to Implementing DDD.
- Conversion result: `PASS`; the answer preserves the case-specific one-Order transaction without restating the source default as an exceptionless universal rule and proposes a bounded change rather than a rewrite.
- Diagnostics: over-selected Distilled and DDIA and over-read relative to the ordinary expectation. The target's five coherent headings are `5/19` (26.3%), below the one-third review threshold; the seven DDIA headings widen context cost but address the separately selected cross-system coordination lens. This is diagnostic over-reading, not material target-tier collapse.

### E7: DDIA-Compatible Durable Order Projection

- Class: compatible-overlap application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/implementing-domain-driven-design/ddia-compatible-overlap.md`.
- Fixture SHA-256: `7667de0a361a4be83bd3f5560d811240b24c6d6ed4c707de4fb05d7ad07985bd`.
- Required skills: `{implementing-domain-driven-design, designing-data-intensive-applications}`.
- Selection notes: the target owns Domain Event construction, Application Service boundaries, translation, and read representation; DDIA independently owns authority, idempotency, ordering, schema evolution, lag, rebuild, and repair semantics.
- Reference expectation: ordinary for both skill bodies unless one bounded source question remains unresolved; extra focused retrieval is diagnostic and must remain materially bounded.
- Relevant sections: target concerns include `Domain Event Rules`, `Application Service Rules`, and `Client Representation and Scope Discipline`; DDIA sections are recorded by its own package evidence if consulted.
- Runs: `_skill-workbench/evaluations/results/implementing-domain-driven-design/ddia-compatible-overlap/green-batch3-1.json`; thread `019f5c8c-ab09-7180-9661-4d994ae0503c`; selected `{clean-architecture, designing-data-intensive-applications}`; consulted `.agents/skills/clean-architecture/SKILL.md` and `.agents/skills/designing-data-intensive-applications/SKILL.md`; no full-reference sections; `reference_mode: ordinary`; recorded child `exit_code: 0`, no integrity or Codex errors; runner command returned 1 with `selection_errors: [required project skill not selected: implementing-domain-driven-design]`; required subset `FAIL` because `{implementing-domain-driven-design, designing-data-intensive-applications}` is not a subset of the selected set.
- Package fidelity trace: `M12`, `M14`, `M16`, `M25-M27`, `N5-N7`, `N10`, `N12`, and the three named target headings.
- Attribution review: no target-package attribution can be accepted because `implementing-domain-driven-design/SKILL.md` was not consulted. The answer's domain-event/application-boundary material is general or Clean Architecture reasoning, while idempotency, ordering, schema evolution, lag, checkpoint, rebuild, and repair mechanisms are DDIA or solver knowledge; none is credited to Implementing DDD.
- Conversion result: `FAIL` for required-skill discovery. The answer is substantively useful, but it does not provide behavioral evidence for the target package.
- Diagnostics: `clean-architecture` is an extra selection and is permitted, but the missing target is a positive-case selection miss. The valid record was preserved and not rerun.

## Behavioral Evaluation Summary

- Execution accounting: exactly 11 valid planned observations were counted: E1 valid replacement plus runs 2/3, E2 runs 1/2/3, and E3-E7 run 1. The two preserved pre-fix E1 schema failures are retained evidence but are excluded from planned-run and acceptance counts. An interrupted focused attempt produced no file and is not a record.
- Common configuration: all 11 valid records use model `gpt-5.4`, `codex-cli 0.144.1`, `ignore_user_config: true`, `ephemeral: true`, `sandbox: read-only`, and GREEN workspace `/Users/jakubtomanik/github/agent-rules-books`; all case hashes match the seven frozen fixture hashes.
- Integrity: all 13 JSON artifacts parse and have unique thread IDs. The 11 valid records have `exit_code: 0`, empty `integrity_errors`, and empty `codex_errors`. The two excluded pre-fix artifacts have `exit_code: 1` and `result: null` because the endpoint rejected unsupported schema keyword `uniqueItems`.
- Required-subset acceptance: `10/11`. E1-E6 pass every required subset. E7 selected DDIA but missed `implementing-domain-driven-design`.
- Over-selection: `6/11` valid records selected at least one extra skill: all three E2 runs, E4, E6, and E7. No answer-level contradiction caused by an extra selected skill was found.
- Disclosure: modes are 6 ordinary, 2 focused, and 3 comprehensive. Explicit over-reading occurred in E1 runs 2/3 (comprehensive instead of ordinary) and E6 (focused instead of ordinary). Among the eight ordinary-expected records that actually selected the target, five stayed ordinary, one was focused, and two were comprehensive. E2 remained ordinary `3/3`, E3 supplied a target-only ordinary success, E4 reached the exact bounded target detail, and E5 reached the full reference.
- Tier-collapse judgment: `NO MATERIAL TIER COLLAPSE` under `_skill-workbench/EVALUATION.md`. Ordinary work does not consistently trigger end-to-end reads; the focused router reaches the needed source detail; the comprehensive request reads `[*]`; and E6's target subset remains coherent and below one-third of the 19 headings. E1 runs 2/3 remain significant disclosure diagnostics and must not be erased or rerun.
- Behavioral verdict: source/package semantic acceptance remains unchanged, but Batch 3 behavioral acceptance is `FAIL (10/11)` because E7 misses one required skill. Do not tune the accepted package from these observations; rerun affected positive cases only after a future catalog-description change.

## Post-Behavior Router Retrofit

Independent behavioral review supersedes the initial no-material-collapse classification for E1. E1 is ordinary implementation work, while E5 is the explicit complete audit. The former comprehensive clause sent any decision spanning several concern families to the entire book, and E1 followed that route in two of three identical runs. This is a packaging-router defect, not source guidance.

The broad `decision spanning several independent concern families` trigger was removed from both `SKILL.md` and `references/index.md`. Comprehensive reading now requires a comprehensive implementation audit or an explicit request for the complete Implementing Domain-Driven Design lens. The description, canonical mini rules, full reference, index rows, and frozen fixtures remain unchanged. The package now has 1,678 words and 167 words of packaging overhead, still within the documented 151-200 allowance.

### Final-State Runs

All six valid final-state observations use model `gpt-5.4`, `codex-cli 0.144.1`, `ignore_user_config: true`, `ephemeral: true`, `sandbox: read-only`, and GREEN workspace `/Users/jakubtomanik/github/agent-rules-books`. The E1 and E7 case hashes remain `764dfa6f65d2d27d613a86611892b42632439daa0ce126d79ad379f5059e61e7` and `7667de0a361a4be83bd3f5560d811240b24c6d6ed4c707de4fb05d7ad07985bd` respectively.

E1 preserved one integrity failure before producing three valid final-state observations:

- Preserved integrity failure: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-router-final-1.json`; thread `019f5caf-eec2-7392-9385-af59fef6abcf`; selected `{implementing-domain-driven-design}`; consulted the target `SKILL.md` and `references/full.md`; reported all 19 level-two headings individually with `reference_mode: focused` but did not consult `references/index.md`; child `exit_code: 0`, no Codex or selection error, and integrity error `reference_mode focused requires SKILL.md, index.md, and full.md`. The runner returned 1. This is preserved process-boundary evidence and is excluded from behavioral counts.
- Final run 1 replacement: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-router-final-retry-1.json`; thread `019f5cb1-8057-73e3-9f59-11767bceaaca`; selected `{implementing-domain-driven-design}`; `reference_mode: focused`; target sections `{Aggregate Rules of Thumb, Entity and Value Object Rules, Repository Rules, Domain Event Rules, Application Service Rules, Module and Package Rules, Context Integration Rules, Client Representation and Scope Discipline}`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Final run 2: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-router-final-2.json`; thread `019f5cb3-0bdf-7b70-8d4e-77e6a1ce66cf`; selected `{implementing-domain-driven-design}`; `reference_mode: focused`; target sections `{Aggregate Rules of Thumb, Entity and Value Object Rules, Domain and Transformation Service Rules, Repository Rules, Domain Event Rules, Application Service Rules, Module and Package Rules, Context Integration Rules, Client Representation and Scope Discipline}`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Final run 3: `_skill-workbench/evaluations/results/implementing-domain-driven-design/direct-subscription-implementation/green-batch3-router-final-3.json`; thread `019f5cb4-6211-7f63-bfb4-7b4a48afbd81`; selected `{implementing-domain-driven-design}`; `reference_mode: ordinary`; no full-reference sections; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.

E1 includes the target `3/3`, selects no extra skill, and avoids an end-to-end full-reference read in all `3/3` valid final-state runs. The two focused reads cover `8/19` and `9/19` headings, so both exceed the one-third manual-review trigger. The sections are coherent with the case's explicitly requested Aggregate, identity, Repository, event, application-coordination, module, integration, and projection concerns; neither uses `[*]`, and the third run stops at `SKILL.md`. The specific comprehensive-trigger defect is corrected, with broad focused retrieval retained as a non-blocking disclosure diagnostic rather than classified as material tier collapse. E5 remains the existing comprehensive control: `_skill-workbench/evaluations/results/implementing-domain-driven-design/comprehensive-marketplace-implementation/green-batch3-1.json` selects only the target and records `reference_mode: comprehensive` with target sections `[*]`.

E7's original required-skill miss remains a valid historical failure and is not combined with later runs as a majority vote. Domain Event construction, Application Service boundaries, translation, and projection mechanics remain central alongside DDIA, and no required-set or description change is justified:

- Final run 1: `_skill-workbench/evaluations/results/implementing-domain-driven-design/ddia-compatible-overlap/green-batch3-router-final-1.json`; thread `019f5cb5-534d-7cc2-867d-9256152d4498`; selected `{clean-architecture, designing-data-intensive-applications, implementing-domain-driven-design}`; `reference_mode: ordinary`; no full-reference sections; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Final run 2: `_skill-workbench/evaluations/results/implementing-domain-driven-design/ddia-compatible-overlap/green-batch3-router-final-2.json`; thread `019f5cb6-d85f-7401-8016-c1e7499fac3a`; selected `{clean-architecture, implementing-domain-driven-design, designing-data-intensive-applications}`; `reference_mode: focused`; target sections `{Domain Event Rules, Application Service Rules, Module and Package Rules, Context Integration Rules, Client Representation and Scope Discipline}`; Clean Architecture sections `{Required Layer Responsibilities}`; DDIA sections `{Reliability Rules, Scalability and Maintainability Rules, Data Model and Storage Rules, Query Model and Data Shape Rules, Storage Engine and Indexing Rules, Consistency Rules, Idempotency and Replay Rules, Ordering Rules, Event, Log, and Stream Rules, Schema Evolution Rules, Derived Data Rules, Distributed Fault, Clock, and Consensus Rules, Batch and Stream Processing Rules, API and Service Boundary Rules, Review Rules, Forbidden Patterns, Code Generation Rules, Testing Rules}`; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.
- Final run 3: `_skill-workbench/evaluations/results/implementing-domain-driven-design/ddia-compatible-overlap/green-batch3-router-final-3.json`; thread `019f5cb8-a079-7fa1-a60b-5ac153afe6f2`; selected `{implementing-domain-driven-design, designing-data-intensive-applications, clean-architecture}`; `reference_mode: comprehensive`; DDIA sections `{[*]}`; the target and Clean Architecture remained `SKILL.md`-only; `exit_code: 0`, no integrity, Codex, or selection errors; required subset `PASS`.

E7 includes both required skills in every `3/3` final-state run; the extra `clean-architecture` selection is permitted. Run 2's 18-heading DDIA read and run 3's DDIA `[*]` read are explicit neighboring-skill over-reading diagnostics. Implementing DDD itself stays ordinary in runs 1 and 3 and reads five coherent sections in run 2. No final-state required-skill miss triggers catalog-description diagnosis.

### Current-State Verdict

- Frozen post-retrofit gate: `PASS`. E1 includes the target and avoids end-to-end target reads `3/3`; E7 includes both required skills `3/3`; E5 remains the comprehensive `[*]` control.
- Historical Batch 3 verdict: remains `FAIL (10/11)`. The original E7 miss and original E1 over-reads are retained exactly; the post-retrofit result is a separately named current-state classification, not a recomputed majority vote.
- Semantic verdict: unchanged and independently accepted. The router-only correction changes no canonical rule, description branch, full-reference content, fixture, or required-skill ownership.

## Independent Review

- Reviewer: independent repaired-source and final source-to-package reviews are `PASS`; the final package review reported no P1/P2/P3 findings. Batch 3 behavioral attribution review is complete for all 11 valid records.
- Catalog snapshot: all ten live project book-skill descriptions were reviewed together again after the Distilled description repair. The repaired DDD-family boundaries remain complementary, no frozen fixture's required target set changed, and the complete catalog is re-frozen for Batch 3 behavioral evaluation as of 2026-07-13.
- Semantic verdict: independently accepted. The repaired active wording is exact, the index predicates are source-supported, and the package adds no technical directive.
- Unsupported or altered package guidance: none found by converter reverse trace or independent package review. Behavioral answers add general or neighboring-skill mechanisms such as outbox, optimistic concurrency, persistence uniqueness, idempotency, compensation, checkpoints, and rebuild procedures; these are recorded as solver-level additions and are not attributed to the Implementing DDD source.

## Validation Evidence

- Structural validation: `python3 _skill-workbench/scripts/validate_conversion.py implementing-domain-driven-design` returned `PASS implementing-domain-driven-design: SKILL.md 79 lines; 1678 words (167 beyond mini); 28 mini rules and 12 nano rules mapped; 19 full-reference sections indexed`. It emitted the expected soft warning for 167 packaging words above the 150-word target; the hard 200-word maximum passes and the exception is documented above.
- Official skill validation: `uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/implementing-domain-driven-design` returned `Skill is valid!` with exit 0.
- Full-reference equality: `cmp` returned exit 0; canonical and packaged files both have SHA-256 `cd2c1d404f60720cebca17fcffed9d68d94b1eef4a13bed63a4f59f01db005ad`.
- Index and link validation: the explicit read-only check returned 19 headings, 19 index rows, valid GitHub anchors, valid heading-to-last-nonempty line ranges, valid source order, 24 valid direct package links, and nonempty `Read when` cells.
- Wording fidelity: `check_rule_wording.py` returned exit 0: 28 mini rules, 28 skill guidance rules, 28 exact wording matches, zero missing/reworded mini rules, zero added/reworded skill rules, exact primary bias, and exact final-check wording and order.
- Evaluation contracts: `python3 _skill-workbench/scripts/validate_evaluation_contracts.py` returned `PASS: every durable evaluation case names only live required skills`.
- Frozen fixture contracts: read-only audit found seven fixture files and seven `E1-E7` records. Every repository-relative fixture path appears exactly once. Six cases require `{implementing-domain-driven-design}` and the DDIA-compatible case requires `{implementing-domain-driven-design, designing-data-intensive-applications}`; all retained result hashes match those fixtures.
- Result integrity: the lane contains 20 preserved JSON artifacts with 20 unique non-null thread IDs: 17 valid behavioral records and three excluded process/integrity artifacts. The excluded records are the two pre-fix schema failures plus the post-router E1 focused-mode/index mismatch. All 17 valid records have `exit_code: 0` and empty integrity and Codex errors; 16 pass their required subsets, while the one valid selection miss is the preserved original E7 record.
- Post-retrofit execution: seven new artifacts preserve six valid final-state observations and one integrity failure. All six valid records pass their required subsets. Their modes are two ordinary, three focused, and one comprehensive; the comprehensive mode belongs to E7's DDIA `[*]` read, not an Implementing DDD end-to-end read.
- Scope and formatting: behavioral writes are limited to `_skill-workbench/evaluations/results/implementing-domain-driven-design/**` and this mapping. The canonical full, repaired mini/nano, traceability, skill package, descriptions, fixtures, shared scripts, schema, and batch result file were not edited by this lane.
- Invocation evaluation: historical direct discovery includes the target `3/3`, distinctive unnamed discovery includes it `3/3`, and the original DDIA-compatible overlap misses it `0/1`. Separately, current post-retrofit E1 includes the target `3/3` and current post-retrofit E7 includes both required skills `3/3`; these final-state runs do not erase or majority-vote the original E7 miss.
- Application evaluation: the historical E1-E6 source-attribution decisions and original E7 non-attribution remain unchanged. The post-retrofit runs are current routing and required-selection evidence; they do not replace the independent semantic verdict.
- Current-state behavioral verdict: the narrowly frozen post-retrofit gate is `PASS`, while the preserved original Batch 3 gate remains `FAIL (10/11)` and the semantic verdict remains independently accepted.
- Remaining risks: the original E7 required-skill miss remains a valid nondeterminism signal. E1 final runs 1/2 are focused over-reads at `8/19` and `9/19` headings despite avoiding end-to-end reads; E7 final run 2 reads 18 DDIA headings and run 3 reads DDIA `[*]`. E6's historical focused over-read also remains. General solver mechanisms must remain separated from book attribution. Any later description drift invalidates this behavioral snapshot and requires catalog-contract validation plus affected positive-case reruns.
