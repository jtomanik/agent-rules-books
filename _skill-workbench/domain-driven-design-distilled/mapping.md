# Domain-Driven Design Distilled Skill Mapping

## Scope

- Distinctive lens: choose the smallest effective DDD investment, concentrate modeling effort on the Core Domain, and make every tactical pattern earn its cost instead of turning DDD into ceremony.
- Intended invocation: select when domain complexity, language ambiguity, business differentiation, or integration risk makes subdomain investment, Bounded Context boundaries, Ubiquitous Language meaning, or tactical-pattern cost central to the task.
- Closest neighboring skills: `domain-driven-design` owns deeper model discovery, knowledge crunching, and the fuller Evans strategic vocabulary; `implementing-domain-driven-design` owns detailed implementation mechanics after context and model commitment. `designing-data-intensive-applications` co-invokes when source-of-truth, replay, ordering, schema, durability, or distributed consistency semantics are independently central. `clean-architecture` owns policy/detail dependency direction, while `refactoring` and `working-effectively-with-legacy-code` own their respective safe-change constraints.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`. The description uses a positive centrality threshold and preserves the canonical four-part adoption condition.
- Canonical inputs: independently accepted repaired full, mini, nano, and traceability files present in the shared worktree on 2026-07-13. Compatibility prose is used only for catalog boundaries where it cites an older pre-repair mini; package guidance comes only from the assigned repaired canonical inputs.

## Repair History

- 2026-07-13 independent source re-review: PASS for the repaired Domain-Driven Design Distilled full, mini, nano, and traceability inputs.
- Package regeneration: updated the nano dispositions for meaning-conditioned translation, the Conformist cheaper-and-safer exception, distinct-concern model reuse, and the repaired nano checklist; removed the unsupported `N17` final-check disposition while retaining its early-guidance role.
- Catalog correction: changed the Implementing Domain-Driven Design boundary from `after DDD boundaries are chosen` to `after context and model commitment` in the live description and its mapping records.
- Reference correction: replaced the Collaboration router's over-broad `richer types` mechanism with source-faithful routing to an explicit richer concept without requiring type creation for every fuzzy concept.
- Preserved artifacts: mini-derived guidance, primary bias, final checklist, full reference, and all seven frozen case contracts are unchanged; behavioral runs were pending at this repair checkpoint and are recorded under `Evaluation Cases` below.
- Catalog effect: the description edit invalidates the prior Batch 3 catalog freeze. Parent reconciliation and a new explicit freeze are required before behavioral execution.

## Description Branches

Candidate description (489 characters):

> Domain-Driven Design Distilled guidance for the smallest effective DDD investment and anti-ceremony selectivity. Use when domain complexity, language ambiguity, business differentiation, or integration risk makes subdomain investment, Bounded Context boundaries, Ubiquitous Language meaning, or whether tactical patterns earn their cost central. Domain-Driven Design owns deeper model discovery; Implementing Domain-Driven Design owns detailed mechanics after context and model commitment.

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Selective investment lens | `smallest effective DDD investment and anti-ceremony selectivity` | Fuller DDD vocabulary or implementation machinery without first establishing that its modeling cost is warranted. |
| Canonical adoption threshold | `domain complexity, language ambiguity, business differentiation, or integration risk` plus `central` | Generic coding, CRUD, database, integration, or architecture work where no DDD modeling decision is central. |
| Strategic boundary decision | `subdomain investment, Bounded Context boundaries, Ubiquitous Language meaning` | Clean Architecture policy direction, local Clean Code naming, and DDIA data ownership unless domain meaning and context ownership are also central. |
| Tactical cost decision | `whether tactical patterns earn their cost` | Implementing DDD mechanics after a tactical DDD commitment has already been made. |
| DDD neighbor split | `Domain-Driven Design owns deeper model discovery; Implementing Domain-Driven Design owns detailed mechanics after context and model commitment` | Evans-style model discovery and IDDD mechanics after context and model commitment, while retaining Distilled as the selectivity gate. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Use Domain-Driven Design Distilled to choose the smallest effective DDD investment across a differentiating returns policy, commodity carrier integration, and CRUD preferences." | `domain-driven-design-distilled` | Direct invocation plus Core, Supporting, and Generic investment and tactical-cost decisions. |
| "Billing, Identity, and Fulfillment use Customer and active differently; prevent a canonical shared model from collapsing those meanings." | `domain-driven-design-distilled` | Unnamed distinctive Ubiquitous Language, Bounded Context, and translation pressure. |
| "A vendor controls taxonomy IDs that merchandisers reject; choose the relationship and translation boundary without a complete model audit." | `domain-driven-design-distilled` | Focused context relationship, local language, and integration-style decision. |
| "Billing and Ledger mean posted differently, while an at-least-once event must be replayable and duplicate-safe." | `domain-driven-design-distilled` plus `designing-data-intensive-applications` | Context meaning and translation are central alongside replay, idempotency, ordering, retention, and rebuild semantics. |
| "Work with experts and refactor the pricing model toward deeper insight about a previously unnamed eligibility concept." | `domain-driven-design` | Deeper model discovery and knowledge crunching are the objective, not the smallest DDD investment gate. |
| "Implement the already chosen Bounded Context with Repositories, Domain Events, projections, CQRS, package structure, and integration adapters." | `implementing-domain-driven-design` | Context and model commitment are already established, so detailed implementation mechanics belong to IDDD and Distilled's selection decision is closed. |
| "Move pricing policy out of Prisma and Express while keeping the supplied model and transaction semantics unchanged." | `clean-architecture`, optionally `refactoring` | Policy/detail direction is central; no open subdomain, language, context, or tactical-cost decision is stated. |
| "Make this outbox consumer duplicate-safe and replayable after an unknown commit outcome." | `designing-data-intensive-applications` | Distributed data semantics are central without an independent domain-language or DDD investment decision. |

## Nano Mapping

The current nano contains eight physical bullets, so the deterministic validator requires ordinal rows `N1` through `N8` below. The repaired traceability intentionally retains fourteen stable clause IDs across those merged bullets and retires `N1`, `N5`, and `N11`; the following `Canonical Nano Traceability Mapping` records that source truth separately.

| ID | Canonical traceability IDs | Skill role | Destination | Notes |
| --- | --- | --- | --- | --- |
| `N1` | `N2` | description, early-guidance, final-check | Description selectivity and cost branches; `Investment, Subdomains, and Contexts`; final checklist | Physical decision bullet 1 promotes complete `M2` and `M3` instead of creating a shortened active rule. |
| `N2` | `N3`, `N4`, `N12` | description, early-guidance, reference-router, final-check | Description context/language branch; first two concern groups; focused router; final checklist | Physical decision bullet 2 promotes complete context ownership, language, translation, and language-trigger rules. |
| `N3` | `N7` | early-guidance, final-check | `Tactical Patterns and Consistency`; final checklist | Physical decision bullet 3 promotes complete Entity and Value Object rules `M10` and `M11`. |
| `N4` | `N8`, `N15` | early-guidance, reference-router, final-check | `Tactical Patterns and Consistency`; focused router; final checklist | Physical decision bullet 4 keeps Aggregate applicability, boundaries, references, defaults, transaction review, and whole-graph trigger whole through `M12` and `M26`. |
| `N5` | `N9`, `N16` | early-guidance, final-check | `Domain Behavior and Technology Boundaries`; final checklist | Physical decision bullet 5 promotes complete Application Service and misplaced-decision guidance `M14` and `M27`. |
| `N6` | `N6`, `N10`, `N14` | description, early-guidance, reference-router, final-check | Description integration-risk branch; investment/context, language/integration, and technology-boundary groups; focused router; final checklist | Physical decision bullet 6 preserves translation where meanings differ, Conformist adoption when cheaper and safer, transport/integration boundary translation, contract separation, and technology isolation through `M5`, `M6`, `M8`, `M15`, and `M23`. |
| `N7` | `N13` | early-guidance, reference-router, final-check | `Investment, Subdomains, and Contexts`; focused router; final checklist | Physical trigger bullet 1 promotes `M4`, `M5`, and `M22`: review boundaries, prohibit one model across distinct business concerns, and translate only where meanings differ. |
| `N8` | `N17` | early-guidance | `Tactical Patterns and Consistency` | Physical trigger bullet 2 promotes the complete Domain Event applicability and redesign/removal guidance in `M13` and `M28`; the packaged mini checklist has no corresponding final check. |

## Canonical Nano Traceability Mapping

| ID | Skill role | Destination | Complete mini guidance promoted | Notes |
| --- | --- | --- | --- | --- |
| `N1` | not-used | None | None | Retired by the repaired traceability and intentionally not reused. |
| `N2` | description, early-guidance, final-check | Description selectivity/cost branches; `Investment, Subdomains, and Contexts`; final checklist | `M2`, `M3` | Core investment, simpler Supporting/Generic work, and earned tactical cost lead the skill. |
| `N3` | description, early-guidance, final-check | Description Bounded Context branch; `Investment, Subdomains, and Contexts`; final checklist | `M4` | Promotes complete context ownership and code-boundary wording. |
| `N4` | description, early-guidance, final-check | Description Ubiquitous Language branch; first two concern groups; final checklist | `M5`, `M9` | Keeps local terms and translation beside context meaning. |
| `N5` | not-used | None | None | Retired by the repaired traceability and intentionally not reused. |
| `N6` | description, early-guidance, reference-router, final-check | Description integration-risk branch; language/integration and technology-boundary groups; focused router; final checklist | `M8`, `M15` | Transport and integration data stay translated at boundaries, contracts stay separate from internal models, and the packaged checklist retains contract separation. |
| `N7` | early-guidance, final-check | `Tactical Patterns and Consistency`; final checklist | `M10`, `M11` | Entity and Value Object modalities remain unsplit. |
| `N8` | early-guidance, reference-router, final-check | `Tactical Patterns and Consistency`; focused router; final checklist | `M12` | Aggregate applicability, shape, references, defaults, and tests remain one rule. |
| `N9` | early-guidance, final-check | `Domain Behavior and Technology Boundaries`; final checklist | `M14` | Application Service coordination stays separate from domain decisions. |
| `N10` | early-guidance, reference-router, final-check | `Domain Behavior and Technology Boundaries`; focused router; final checklist | `M15` | Technology isolation stays attached to complete architecture guidance. |
| `N11` | not-used | None | None | Retired by the repaired traceability and intentionally not reused. |
| `N12` | early-guidance, reference-router, final-check | `Language, Relationships, and Integration`; focused router; final checklist | `M20` | The full fuzzy, generic, overloaded, or imported language trigger is retained. |
| `N13` | early-guidance, reference-router, final-check | `Investment, Subdomains, and Contexts`; focused router; final checklist | `M4`, `M5`, `M22` | Boundary review and the prohibition on one model across distinct business concerns remain explicit; translation is conditioned only on meanings differing, not on ownership differences. |
| `N14` | early-guidance, reference-router, final-check | Investment/context, language/integration, and technology-boundary groups; focused router; final checklist | `M5`, `M6`, `M15`, `M23` | Foreign models are translated where meanings differ unless Conformist adoption is cheaper and safer; technology-shaped models still trigger isolation rather than translation. |
| `N15` | early-guidance, reference-router, final-check | `Tactical Patterns and Consistency`; focused router; final checklist | `M26` | Multi-Aggregate transactions remain distinct from whole-graph requests. |
| `N16` | early-guidance, final-check | `Domain Behavior and Technology Boundaries`; final checklist | `M27` | Misplaced decisions remain distinct from duplicated controller orchestration. |
| `N17` | early-guidance | `Tactical Patterns and Consistency` | `M13`, `M28` | Positive Domain Event applicability and misuse trigger remain colocated; no `final-check` role is claimed because the packaged mini checklist contains no meaningful, past-tense, or noise check for Domain Events. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Investment, Subdomains, and Contexts` | Moved verbatim | Leads with the conditional strategic sequence. Source: `Primary Directive`. |
| `M2` | `Investment, Subdomains, and Contexts` | Moved verbatim | Keeps Core investment and Supporting/Generic simplicity together. Source: `Adoption Fit and Modeling Investment`; `Strategic Rules`. |
| `M3` | `Investment, Subdomains, and Contexts` | Moved verbatim | Keeps the anti-ceremony gate, simple structures, rising-complexity trigger, and incremental strengthening whole. Source: `Adoption Fit and Modeling Investment`; `Practicality Rules`. |
| `M4` | `Investment, Subdomains, and Contexts` | Moved verbatim | Establishes Bounded Context ownership before relationship and tactical choices. Source: `Strategic Rules`. |
| `M5` | `Investment, Subdomains, and Contexts` | Moved verbatim | Stays with context boundaries and the shared-model trigger `M22`. Source: `Strategic Rules`; `Ubiquitous Language Rules`. |
| `M6` | `Language, Relationships, and Integration` | Moved verbatim | Keeps all nine relationship patterns and applicability conditions in one rule. Source: `Context Relationship Rules`. |
| `M7` | `Language, Relationships, and Integration` | Moved verbatim | Keeps RPC, REST, messaging, and event payload/query-back conditions together. Source: `Integration Style Rules`. |
| `M8` | `Language, Relationships, and Integration` | Moved verbatim | Co-locates contract ownership, model separation, and translation tests. Source: `Strategic Rules`; `Integration Style Rules`. |
| `M9` | `Language, Relationships, and Integration` | Moved verbatim | Promoted by nano language salience and placed beside the complete fuzzy-language trigger `M20`. Source: `Ubiquitous Language Rules`; `Testing Rules`. |
| `M10` | `Tactical Patterns and Consistency` | Moved verbatim | Entity applicability, modalities, and transition tests remain complete. Source: `Tactical Pattern Rules`; `Testing Rules`. |
| `M11` | `Tactical Patterns and Consistency` | Moved verbatim | Value Object applicability, defaults, behavior, and tests remain complete and sit beside `M29`. Source: `Tactical Pattern Rules`; `Testing Rules`. |
| `M12` | `Tactical Patterns and Consistency` | Moved verbatim | Aggregate applicability, size, root protection, identity references, consistency default, transaction norm, and tests remain complete beside `M26`. Source: `Tactical Pattern Rules`; `Aggregate Minimalism Rules`; `Testing Rules`. |
| `M13` | `Tactical Patterns and Consistency` | Moved verbatim | Positive Domain Event applicability sits beside misuse trigger `M28`. Source: `Tactical Pattern Rules`. |
| `M14` | `Domain Behavior and Technology Boundaries` | Moved verbatim | Application Service coordination, domain ownership, thinness, and tests remain complete beside `M27`. Source: `Application Service Rules`; `Testing Rules`. |
| `M15` | `Domain Behavior and Technology Boundaries` | Moved verbatim | Technology isolation and boundary translation remain complete beside `M23`. Source: `Architecture and Infrastructure Rules`. |
| `M16` | `Domain Behavior and Technology Boundaries` | Moved verbatim | Rich domain concepts and model-teaching code close the concern group. Source: `Ubiquitous Language Rules`; `Collaboration Rules`. |
| `M17` | `Collaborative Modeling and Delivery` | Moved verbatim | Preserves each collaborative modeling, validation, spike, debt, expert, and timeboxing condition without merging purposes. Source: `Adoption Fit and Modeling Investment`; `Accelerated Modeling and Project Rules`. |
| `M18` | `Collaborative Modeling and Delivery` | Moved verbatim | Keeps estimation inputs and sustainable-ceremony constraints together. Source: `Accelerated Modeling and Project Rules`. |
| `M19` | `Collaborative Modeling and Delivery` | Moved verbatim | Preserves the separate default code-generation order after strategic and tactical guidance. Source: `Code Generation Rules`. |
| `M20` | `Language, Relationships, and Integration` | Moved verbatim | Placed directly after `M9` to bind fuzzy or imported language to local refinement and translation. Source: `Ubiquitous Language Rules`; `Collaboration Rules`. |
| `M21` | `Investment, Subdomains, and Contexts` | Moved verbatim | Keeps unconditional reassessment distinct from conditional strategic scope review. Source: `Adoption Fit and Modeling Investment`. |
| `M22` | `Investment, Subdomains, and Contexts` | Moved verbatim | Placed after context ownership and meaning to reject one shared model where concerns diverge. Source: `Strategic Rules`; `Review Rules`. |
| `M23` | `Domain Behavior and Technology Boundaries` | Moved verbatim | Separates foreign-language translation from screen, framework, transport, and persistence isolation. Source: `Strategic Rules`; `Aggregate Minimalism Rules`; `Architecture and Infrastructure Rules`. |
| `M24` | `Language, Relationships, and Integration` | Moved verbatim | Placed after the complete relationship rule as the Shared Kernel governance guard. Source: `Context Relationship Rules`. |
| `M25` | `Language, Relationships, and Integration` | Moved verbatim | Placed after Shared Kernel as the Anticorruption Layer translation guard. Source: `Context Relationship Rules`. |
| `M26` | `Tactical Patterns and Consistency` | Moved verbatim | Placed after `M12`; multi-root transaction review remains separate from whole-graph request correction. Source: `Tactical Pattern Rules`; `Aggregate Minimalism Rules`. |
| `M27` | `Domain Behavior and Technology Boundaries` | Moved verbatim | Placed after `M14`; controller orchestration and misplaced business decisions keep distinct remedies. Source: `Application Service Rules`; `Collaboration Rules`; `Review Rules`. |
| `M28` | `Tactical Patterns and Consistency` | Moved verbatim | Placed after `M13` as the complete Domain Event misuse trigger. Source: `Tactical Pattern Rules`; `Review Rules`. |
| `M29` | `Tactical Patterns and Consistency` | Moved verbatim | Placed after `M11` to bind primitive and flag pressure to the richer concept or Value Object response. Source: `Tactical Pattern Rules`; `Collaboration Rules`; `Review Rules`. |

## Wording Fidelity

- Verbatim primary bias: exact.
- Verbatim mini rules: all 29 decision and trigger rules are moved whole and exact; no rule is added, omitted, merged, split, or reworded.
- Verbatim final checklist and order: all ten items are exact and remain in canonical order.
- Documented exceptions: none.
- Reordering: nano-salient selective investment and boundaries lead; complete rules are colocated with their triggers and guards as recorded in the Mini Mapping.
- Reverse trace: every retained mini and repaired nano detail is supported by the full headings named in traceability and repeated in the mapping notes. Repaired `N6`, `N13`, and `N14` preserve meaning-conditioned translation, Conformist's cheaper-and-safer exception, distinct-concern model reuse, transport/integration boundary translation, and technology isolation without adding nano text as a second active rule.
- Nano final-check disposition: the repaired nano checklist effects for `N6`, `N13`, and `N14` route to existing mini checklist items. `N17` remains early guidance only because no mini checklist item checks Domain Event meaning, past-tense naming, or noise.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Catalog prose: the 489-character description encodes the canonical activation threshold, smallest-effective-investment lens, tactical-cost branch, and compatibility-supported neighbor split. It adds no DDD mechanism or application sequence.
- Concern headings: `Investment, Subdomains, and Contexts`, `Language, Relationships, and Integration`, `Tactical Patterns and Consistency`, `Domain Behavior and Technology Boundaries`, and `Collaborative Modeling and Delivery` only group verbatim canonical rules.
- Newly authored packaging directives: the Reference Router's ordinary branch says to stop with `SKILL.md` when it resolves the bounded DDD question; its focused branch routes an explicit dispute, demonstrated modeling hotspot, or one bounded unresolved source question through `references/index.md` to the smallest named full sections; its comprehensive branch requires end-to-end `full.md` for a complete lens or several independent concern families. These are progressive-disclosure controls required by `_skill-workbench/PROCESS.md`, not DDD advice.
- Reference index: the introductory router and nineteen manually authored `Read when` cells select canonical H2 sections only. Each cell is bounded to concepts present in its linked section and introduces no new mechanism, default, guarantee, failure mode, or preference.
- UI metadata: `short_description` is discovery-only; the default prompt explicitly invokes `$domain-driven-design-distilled` and requests the canonical smallest-effective-investment lens.
- Review: frontmatter, headings, routing prose, index prose, and UI metadata organize discovery and loading only; no unsupported technical rule was found.

## Size Exception

- Canonical mini: 1,316 words.
- `SKILL.md`: 1,458 words across 75 lines.
- Packaging overhead: 142 words, within the 150-word target.
- Description: 489 characters.
- Decision: retain a source-driven skill-size exception because the canonical mini already exceeds the 500-word target and every mini rule is required for complete ordinary use. No packaging-overhead exception is needed, and canonical guidance must not be paraphrased to reduce the source size.

## Evaluation Cases

These seven durable contracts were recorded before any behavioral execution. Their repository fixtures remained frozen through Batch 3 execution. The repaired description invalidated the prior catalog freeze; the parent subsequently reconciled all ten descriptions and recorded a new batch freeze before execution.

### E1: Direct Smallest DDD Investment

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/direct-smallest-ddd-investment.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: direct book-name and distinctive smallest-effective-investment case; extra relevant selections are permitted.
- Reference expectation: `ordinary`.
- Relevant sections: not applicable; `SKILL.md` contains the complete selective-investment, subdomain, context, language, and tactical-cost guidance.
- Runs:
  - Invalid environment record: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-1.json`; thread `019f5c4a-32fd-7ef1-9dcb-7114427fde4a`; `exit_code=1`, `result=null`, no selected/files/sections/mode evidence. Preserved and excluded from acceptance after the parent diagnosed the then-unsupported response-schema `uniqueItems` keyword.
  - Invalid environment retry: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-retry-1.json`; thread `019f5c4a-aecc-7f80-bff5-85c87b1a09cb`; `exit_code=1`, `result=null`, no selected/files/sections/mode evidence. Preserved and excluded from acceptance for the same endpoint-schema failure.
  - Counted run 1 replacement: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-valid-1.json`; thread `019f5c50-38d4-7213-8527-b9a0076ec19b`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`; sections `[]`; mode `ordinary`.
  - Invalid run 2 record: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-2.json`; thread `019f5c50-bbb1-78c1-9fa4-0bcf652941e7`; selected `{domain-driven-design-distilled}`; consulted `/Users/jakubtomanik/github/agent-rules-books/.agents/skills/domain-driven-design-distilled/SKILL.md` and `/Users/jakubtomanik/github/agent-rules-books/.agents/skills/domain-driven-design-distilled/references/index.md`; sections `[]`; reported mode `ordinary`; integrity error `reference_mode ordinary requires SKILL.md files and no references`. Preserved and excluded from acceptance.
  - Counted run 2 replacement: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-retry-2.json`; thread `019f5c51-e7b2-76d1-bd65-a91d6f5b4264`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`; sections `[]`; mode `ordinary`.
  - Counted run 3: `_skill-workbench/evaluations/results/domain-driven-design-distilled/direct-smallest-ddd-investment/green-batch3-3.json`; thread `019f5c52-cf52-79f1-856b-b839679f3026`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`; sections `[]`; mode `ordinary`.
- Required-subset result: pass in all three counted runs; `{domain-driven-design-distilled}` was included each time.
- Package fidelity trace: `M1-M6`, `M17-M19`, `N2-N4`, and the final checklist.
- Attribution review: supported. The counted answers applied Core/Supporting/Generic investment, explicit contexts and local language, meaning-conditioned translation, small consistency boundaries, and earned tactical cost from the package. Candidate concept names, team-boundary suggestions, and adapter/workflow details were solver application or general engineering judgment and are not credited to the book.
- Conversion result: pass.
- Diagnostics: all three counted runs stayed target-only and `SKILL.md`-only. The run 2 index-only over-read was internally inconsistent and was replaced once rather than counted. Run 3 retained transient model-refresh and shell-snapshot cleanup stderr, but `exit_code=0`, `codex_errors=[]`, integrity passed, and the valid result was not rerun.

### E2: Unnamed Customer Meaning Collision

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/unnamed-customer-meaning-collision.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: unnamed distinctive discovery case for conflicting context-local meanings; extra relevant selections are permitted.
- Reference expectation: `ordinary`.
- Relevant sections: not applicable; `SKILL.md` contains context ownership, local language, translation, and shared-model guidance.
- Runs:
  - Counted run 1: `_skill-workbench/evaluations/results/domain-driven-design-distilled/unnamed-customer-meaning-collision/green-batch3-1.json`; thread `019f5c53-9e13-7453-8d09-7a56419f254b`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`; sections `[]`; mode `ordinary`.
  - Counted run 2: `_skill-workbench/evaluations/results/domain-driven-design-distilled/unnamed-customer-meaning-collision/green-batch3-2.json`; thread `019f5c54-0fae-7662-8f38-e8621285c5df`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/domain-driven-design-distilled/references/index.md`, and `.agents/skills/domain-driven-design-distilled/references/full.md`; sections `{domain-driven-design-distilled: [Strategic Rules, Context Relationship Rules, Integration Style Rules, Ubiquitous Language Rules, Architecture and Infrastructure Rules]}`; mode `focused`.
  - Counted run 3: `_skill-workbench/evaluations/results/domain-driven-design-distilled/unnamed-customer-meaning-collision/green-batch3-3.json`; thread `019f5c54-ca77-7a31-9238-d9643303a4d0`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`; sections `[]`; mode `ordinary`.
- Required-subset result: pass in all three runs; `{domain-driven-design-distilled}` was included each time.
- Package fidelity trace: `M4`, `M5`, `M8`, `M9`, `M20`, `M22`, `M23`, `N3`, `N4`, `N12-N14`.
- Attribution review: supported. All runs rejected the shared domain class because meanings differ and kept context-local language plus explicit translation. Suggested neutral correlation records, field names, event names, and the run 1 ban on unqualified cross-team terms are solver-added application details, not book guidance.
- Conversion result: pass.
- Diagnostics: runs 1 and 3 were ordinary. Run 2 over-read five of nineteen target full sections despite an ordinary expectation; the sections form a coherent language/boundary/integration family, the other two runs remained `SKILL.md`-only, and manual review found diagnostic over-reading rather than material tier collapse. No run inferred translation from ownership difference alone.

### E3: Ordinary Smallest Honest Order Model

- Class: application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/ordinary-smallest-honest-order-model.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: ordinary tactical selectivity and Aggregate-boundary case; extra relevant selections are permitted.
- Reference expectation: `ordinary`.
- Relevant sections: not applicable; `SKILL.md` contains the required Value Object, Aggregate, transaction, identity-reference, Application Service, and technology-boundary guidance.
- Runs: counted run 1 is `_skill-workbench/evaluations/results/domain-driven-design-distilled/ordinary-smallest-honest-order-model/green-batch3-1.json`; thread `019f5c55-a5b5-7e01-8253-08ca5c79a11c`; selected `{domain-driven-design-distilled, implementing-domain-driven-design}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md` and `.agents/skills/implementing-domain-driven-design/SKILL.md`; sections `[]`; mode `ordinary`.
- Required-subset result: pass; `{domain-driven-design-distilled}` is a subset of the selected set.
- Package fidelity trace: `M3`, `M11`, `M12`, `M14-M16`, `M26`, `M27`, `M29`, `N2`, `N7-N10`, `N15`, `N16`.
- Attribution review: supported. The target package supports Money as a Value Object, a small Order Aggregate around its local invariant, identity references to other Aggregates, one local transaction, and Application Service coordination. Ports, translated local records, follow-up commands/events, and the concrete TypeScript shape are solver/Implementing DDD application details and are not credited to Distilled.
- Conversion result: pass.
- Diagnostics: the answer modeled Money and the local Order invariant without absorbing Payment or Inventory graphs. `implementing-domain-driven-design` was an allowed extra selection; both skills stayed body-only, so ordinary disclosure remained intact.

### E4: Focused Vendor Taxonomy Integration

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/focused-vendor-taxonomy-integration.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: bounded dispute about context relationship, translation responsibility, and integration style; extra relevant selections are permitted.
- Reference expectation: `focused`.
- Relevant sections: context relationship applicability, local-language protection, RPC and messaging conditions, event payload versus query-back, contract separation, and boundary translation. Likely H2 sources are `Strategic Rules`, `Context Relationship Rules`, `Integration Style Rules`, `Ubiquitous Language Rules`, and `Architecture and Infrastructure Rules`; exact section selection is not required.
- Runs:
  - Invalid original: `_skill-workbench/evaluations/results/domain-driven-design-distilled/focused-vendor-taxonomy-integration/green-batch3-1.json`; thread `019f5c56-6116-77a3-a995-93b9029ba1a8`; selected `{domain-driven-design-distilled, designing-data-intensive-applications, implementing-domain-driven-design}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/domain-driven-design-distilled/references/index.md`, `.agents/skills/domain-driven-design-distilled/references/full.md`, `.agents/skills/designing-data-intensive-applications/SKILL.md`, `.agents/skills/designing-data-intensive-applications/references/index.md`, `.agents/skills/designing-data-intensive-applications/references/full.md`, `.agents/skills/implementing-domain-driven-design/SKILL.md`, and `.agents/skills/implementing-domain-driven-design/references/index.md`; sections `{domain-driven-design-distilled: [Context Relationship Rules, Integration Style Rules, Ubiquitous Language Rules], designing-data-intensive-applications: [Event, Log, and Stream Rules, Schema Evolution Rules, Encoding and Data Flow Rules, API and Service Boundary Rules]}`; mode `focused`; integrity error `reference_mode focused requires SKILL.md, index.md, and full.md` because the Implementing DDD index read had no matching full read/section record. Preserved and excluded from acceptance.
  - Counted retry: `_skill-workbench/evaluations/results/domain-driven-design-distilled/focused-vendor-taxonomy-integration/green-batch3-retry-1.json`; thread `019f5c57-968e-7332-946f-fcaf6f53c6da`; selected `{domain-driven-design-distilled, implementing-domain-driven-design, designing-data-intensive-applications}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/domain-driven-design-distilled/references/index.md`, `.agents/skills/domain-driven-design-distilled/references/full.md`, `.agents/skills/implementing-domain-driven-design/SKILL.md`, `.agents/skills/implementing-domain-driven-design/references/index.md`, `.agents/skills/implementing-domain-driven-design/references/full.md`, `.agents/skills/designing-data-intensive-applications/SKILL.md`, `.agents/skills/designing-data-intensive-applications/references/index.md`, and `.agents/skills/designing-data-intensive-applications/references/full.md`; sections `{domain-driven-design-distilled: [Context Relationship Rules, Integration Style Rules], implementing-domain-driven-design: [Context Integration Rules], designing-data-intensive-applications: [Event, Log, and Stream Rules, API and Service Boundary Rules]}`; mode `focused`.
- Required-subset result: pass in the counted retry; `{domain-driven-design-distilled}` is a subset of the selected set.
- Package fidelity trace: `M5-M9`, `M15`, `M20`, `M23-M25`, `N4`, `N6`, `N10`, `N12`, `N14`, plus the named full headings.
- Attribution review: supported. Distilled supports the Anticorruption Layer decision, local-language protection, Conformist's cheaper-and-safer condition, RPC/messaging conditions, event payload versus query-back, and contract translation. Source-of-truth phrasing plus timestamp, version, and correlation suggestions are DDIA/general application details and are not credited to Distilled.
- Conversion result: pass.
- Diagnostics: the counted run over-selected Implementing DDD and DDIA, which was permitted and produced compatible advice. The target read two of nineteen sections, Implementing DDD one of nineteen, and DDIA two of twenty-six; each subset was bounded to the stated dispute, so no tier collapse occurred. Conformist was rejected because the fixture made local-language corruption concrete, not because translation was treated as universal.

### E5: Comprehensive Order-to-Cash Audit

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/comprehensive-order-to-cash-audit.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: explicit complete-lens request; extra relevant selections are permitted.
- Reference expectation: `comprehensive`.
- Relevant sections: all nineteen H2 sections in `references/full.md`, read end to end.
- Runs: counted run 1 is `_skill-workbench/evaluations/results/domain-driven-design-distilled/comprehensive-order-to-cash-audit/green-batch3-1.json`; thread `019f5c58-ccbb-79e0-bc87-b0ae2d85111b`; selected `{domain-driven-design-distilled}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/domain-driven-design-distilled/references/index.md`, and `.agents/skills/domain-driven-design-distilled/references/full.md`; sections `{domain-driven-design-distilled: [*]}`; mode `comprehensive`.
- Required-subset result: pass; `{domain-driven-design-distilled}` was selected.
- Package fidelity trace: `M1-M29`, all active nano traceability IDs, all nineteen full headings, and the final checklist.
- Attribution review: supported. The answer used the package's complete investment, context, relationship, language, tactical-pattern, technology-boundary, collaboration, and delivery guidance. Specific team ownership, proposed context split, integration topology, payment deferral, and contention language are solver application/general judgment and are not credited to the book.
- Conversion result: pass.
- Diagnostics: the explicit complete-lens request reached an end-to-end `full.md` read and selected no extra skill. Recommendations remained proportionate to Core, Supporting, and Generic value; comprehensive disclosure worked as designed.

### E6: Shared Model and Transaction Pressure

- Class: pressure and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/pressure-shared-model-transaction.md`
- Required skills: `{domain-driven-design-distilled}`
- Selection notes: schedule, authority, and sunk-cost pressure tests the early selectivity, context, and Aggregate rules; extra relevant selections are permitted.
- Reference expectation: `ordinary`.
- Relevant sections: not applicable; `SKILL.md` contains the complete pressure-relevant guidance.
- Runs: counted run 1 is `_skill-workbench/evaluations/results/domain-driven-design-distilled/pressure-shared-model-transaction/green-batch3-1.json`; thread `019f5c88-c731-77c0-af49-ccae5678a2d4`; selected `{domain-driven-design-distilled, implementing-domain-driven-design}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md` and `.agents/skills/implementing-domain-driven-design/SKILL.md`; sections `[]`; mode `ordinary`.
- Required-subset result: pass; `{domain-driven-design-distilled}` is a subset of the selected set.
- Package fidelity trace: `M1-M5`, `M12`, `M19`, `M21`, `M22`, `M26`, `N2-N4`, `N8`, `N13`, `N15`, and the final checklist.
- Attribution review: supported. The target package supports separating the Core Pricing context now, keeping Supporting/Generic work simpler, rejecting one shared model and multi-root transaction, retaining physical storage as an isolated implementation detail, and requiring tactical cost justification. The outbox, event-sourcing and saga/process-manager discussion, repository-interface choice, and generated-schema containment tactics are solver/Implementing DDD general knowledge and are not credited to Distilled.
- Conversion result: pass.
- Diagnostics: the answer protected the deadline without a big-bang persistence rewrite and did not add rich DDD to Notifications. `implementing-domain-driven-design` was an allowed extra selection; both selected skills remained `SKILL.md`-only, so no over-reading or tier collapse occurred.

### E7: DDIA-Compatible Meaning and Replay Overlap

- Class: compatible overlap and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design-distilled/ddia-compatible-overlap.md`
- Required skills: `{domain-driven-design-distilled, designing-data-intensive-applications}`
- Selection notes: both context-local meaning/translation and distributed replay, idempotency, ordering, schema, retention, and rebuild semantics are central; extra relevant selections are permitted.
- Reference expectation: `ordinary` for the target skill; DDIA disclosure is recorded independently by its solver evidence.
- Relevant sections: not applicable for the target skill unless one bounded DDD source dispute remains after applying `SKILL.md`.
- Runs: counted run 1 is `_skill-workbench/evaluations/results/domain-driven-design-distilled/ddia-compatible-overlap/green-batch3-1.json`; thread `019f5c89-b7ad-7a23-9ba9-2521a0bc7908`; selected `{domain-driven-design-distilled, designing-data-intensive-applications}`; consulted `.agents/skills/domain-driven-design-distilled/SKILL.md`, `.agents/skills/domain-driven-design-distilled/references/index.md`, `.agents/skills/domain-driven-design-distilled/references/full.md`, `.agents/skills/designing-data-intensive-applications/SKILL.md`, `.agents/skills/designing-data-intensive-applications/references/index.md`, and `.agents/skills/designing-data-intensive-applications/references/full.md`; sections `{domain-driven-design-distilled: [Strategic Rules, Context Relationship Rules, Integration Style Rules], designing-data-intensive-applications: [Idempotency and Replay Rules, Ordering Rules, Event, Log, and Stream Rules, Schema Evolution Rules, Encoding and Data Flow Rules, Derived Data Rules, Distributed Fault, Clock, and Consensus Rules, Batch and Stream Processing Rules]}`; mode `focused`.
- Required-subset result: pass; `{domain-driven-design-distilled, designing-data-intensive-applications}` exactly equals the selected set.
- Package fidelity trace: target `M4-M9`, `M13`, `M15`, `M20`, `M23`, `M28`, `N3`, `N4`, `N6`, `N12`, `N14`, `N17`; DDIA package fidelity is reviewed against its own mapping.
- Attribution review: supported. Distilled supports separate meanings for `posted`, context-local language, published contracts, and translation; DDIA supports source-of-truth, duplicate/replay/order, schema evolution, checkpoint, retention, and rebuild contracts. Exact envelope fields, database uniqueness, replay-log implementation options, and example command/event names are solver/DDIA application details and are not credited to Distilled.
- Conversion result: pass.
- Diagnostics: the required overlap was selected exactly and the two lenses remained distinct. The target over-read three of nineteen sections despite its ordinary expectation; DDIA read eight of twenty-six sections, approaching one-third and spanning several concern families. Manual review found both subsets coherent with this explicitly multi-concern fixture, so these are diagnostic over-reading cases, not material tier collapse.

## Independent Review

- Reviewer: independent source/package review completed outside the converter; the same reviewer re-traced the regenerated package and returned `PASS` with no P1/P2/P3 semantic findings.
- Catalog snapshot: all ten live project book-skill descriptions were reviewed together again after repair. The three DDD roles remain smallest-investment/selectivity for this skill, strategic discovery and deeper-model development for `domain-driven-design`, and implementation mechanics after context and model commitment for `implementing-domain-driven-design`.
- Catalog freeze: the complete ten-skill catalog was re-frozen for Batch 3 behavioral evaluation as of 2026-07-13. The description repair did not change any frozen fixture's required target set; behavioral execution proceeded only after independent package acceptance.
- Semantic verdict: independently accepted. The repaired canonical source and regenerated package preserve exact mini guidance and full-reference bytes while correcting nano dispositions and index routing.
- Unsupported or altered guidance: the unsupported `N17` final-check claim and over-broad `richer types` routing mechanism were removed. No nano wording was added as a second active rule.

## Validation Evidence

- Source re-review: independently reported `PASS` for the repaired canonical source before package regeneration.
- Structural validation: `python3 _skill-workbench/scripts/validate_conversion.py domain-driven-design-distilled` passed: `SKILL.md 75 lines; 1458 words (142 beyond mini); 29 mini rules and 8 nano rules mapped; 19 full-reference sections indexed`.
- Wording validation: `python3 _skill-workbench/scripts/check_rule_wording.py --mini domain-driven-design-distilled/domain-driven-design-distilled.mini.md --skill .agents/skills/domain-driven-design-distilled/SKILL.md` passed with `29/29` exact mini-rule matches, exact primary bias, exact final checklist wording and order, and zero missing, added, or reworded rules.
- Repair-specific nano validation: both physical `N8`/`N17` and canonical `N17` roles are exactly `early-guidance`; repaired Conformist and meanings-differ qualifiers are recorded for `N6`, `N13`, and `N14`; no nano wording was added as a second active rule.
- Official skill validation: `uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/domain-driven-design-distilled` passed with `Skill is valid!`. The previously used `/Users/jakubtomanik/.codex/skills/.system/skill-creator/scripts/quick_validate.py` path is absent on this machine.
- Full-reference equality: `cmp` exited `0`; SHA-256 is `d665da3c697df36fe04f8bb266381e5b40d158aad5283c1d233d4c47319e5b1c` for both canonical full and `references/full.md`.
- Index validation: repository validation and a source-derived standalone assertion confirmed all nineteen H2 headings, anchors, source order, and last-nonempty line ranges exactly match `full.md`; the Collaboration row uses `richer concept` routing without a type-creation requirement.
- Metadata and links: repository and official validation passed the two-key frontmatter, 489-character description, one-level reference links, quoted UI fields, 25-64 character short description, exact `$domain-driven-design-distilled` prompt token, and explicit `allow_implicit_invocation: true` policy.
- Evaluation-contract validation: `python3 _skill-workbench/scripts/validate_evaluation_contracts.py` passed with `every durable evaluation case names only live required skills`.
- Frozen-fixture audit: before execution, all seven repository-relative fixture paths matched exactly, all seven `Runs` values were `pending`, and required sets were six target-only cases plus one target-and-DDIA case. Post-execution SHA-256 values remain `bd4f75e0bd0cde74ca27a16427130f1171ced430af1488d532c4bb1037137493` (E1), `05b23f1934f2473d70822bdfd1f2d56ec62bb9fe263a1be25403bd402fd22f8c` (E2), `b8881eda78b71a4dd0b61067a4c9eeb3477a85f3c1d973765c076d223368f901` (E3), `661a838be12a8026dfd32e1110b5b3472cecbd0455de567cadbf7fdbd4f1c3b6` (E4), `5af61604bf76006c4352096a5755f3f5f6033161feba5b1c5398c4b7caa509b8` (E5), `eb6ec0e19402968251a55629034ed358070d25671173a92ddf42b317cbf75ab6` (E6), and `842d0253b075b141891d17b8ed9dcd2766f9d1f54916f5dce9dd3928fd974bba` (E7).
- Whitespace validation: `git diff --check` exited `0` for tracked shared-checkout changes; a separate scoped audit confirmed final newlines and no trailing whitespace in all five assigned files, including the untracked package and mapping.
- Behavioral configuration: all fifteen retained records use `model=gpt-5.4`, `ignore_user_config=true`, `ephemeral=true`, `sandbox=read-only`, `green_workspace=/Users/jakubtomanik/github/agent-rules-books`, and the same temporary project-skill-free baseline configuration. All eleven counted records have `exit_code=0`, `codex_errors=[]`, empty integrity errors, and empty selection errors.
- Behavioral result integrity: fifteen JSON records were retained and parsed. Eleven valid records count toward the eleven-run matrix. Two pre-fix environment records have `exit_code=1` and `result=null`; two later records have result-trace integrity errors and were each replaced once. Invalid records remain preserved but do not count. No counted record has a required-subset miss.
- Invocation evaluation: passed. The three counted direct runs and all three unnamed runs included `domain-driven-design-distilled`; extra selections were absent in those six discovery runs.
- Application evaluation: passed. E3-E7 included every required skill, applied the target guidance without unsupported book attribution, and showed ordinary, focused, and comprehensive access without material tier collapse.
- Progressive-disclosure review: E1 counted runs, E3, and E6 were body-only ordinary; E4 used bounded focused sections; E5 read the target full reference end to end. E2 run 2 and E7 over-read diagnostically, but manual review found no collapsed tier. E7's DDIA read covered eight of twenty-six sections because the fixture explicitly combined replay, ordering, schema, retention, projection, and rebuild concerns.
- Selection diagnostics: three of eleven counted records selected permitted extras: E3 added `implementing-domain-driven-design`, E4 added `implementing-domain-driven-design` and `designing-data-intensive-applications`, and E6 added `implementing-domain-driven-design`. E7 selected exactly its two required skills. No extra selection produced contradictory advice.
- Attribution review: passed. Source-backed Distilled guidance remained distinguishable from solver-added implementation examples and general engineering judgment. Outbox, event-sourcing, saga/process-manager, exact envelope, unique-constraint, correlation-record, ownership, and concrete topology suggestions are not credited to Domain-Driven Design Distilled.
- Remaining risks: E2 and E7 retain non-blocking over-reading diagnostics, and three counted cases retain permitted over-selection diagnostics. Any later description drift invalidates the catalog freeze and requires contract validation plus reruns of affected positive cases.
