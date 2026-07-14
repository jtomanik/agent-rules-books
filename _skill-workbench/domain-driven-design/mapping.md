# Domain-Driven Design Skill Mapping

## Scope

- Distinctive lens: discover and evolve an implementation-driving domain model through expert language, code, scenarios, and refactoring; keep that model coherent inside explicit Bounded Contexts and direct strategic attention toward the Core Domain.
- Intended invocation: select when business complexity makes Ubiquitous Language conflict, missing concepts, lifecycle rules, Bounded Context or Context Map choices, Core Domain focus, or deeper-model pressure central to the task. Mere use of DDD nouns is insufficient.
- Closest neighboring skills: `domain-driven-design-distilled` owns the smallest-investment and selectivity gate; `implementing-domain-driven-design` owns post-boundary implementation mechanics once the DDD direction is settled. `designing-data-intensive-applications` may co-invoke for distributed data semantics, while `clean-architecture` may co-invoke for policy/detail dependency direction.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`. The description uses a positive business-complexity threshold and gives the Evans skill a discovery/evolution role rather than treating all domain code as a trigger.

## Source Fidelity Inventory

- Canonical full: `domain-driven-design/domain-driven-design.md`, 979 lines, 6,228 words, SHA-256 `de806ceb828df4408e452361ab587d81f213443ad057017b1f6bed2334d5aaa6` at the authoring snapshot.
- Repaired mini: `domain-driven-design/domain-driven-design.mini.md`, 48 lines, 1,061 words, 15 decision rules, 9 trigger rules, and 6 final checks, SHA-256 `32a4648a3e6bf8e63aa8057d7729419ed65abf0fb2be148cb58374a794b5a91f`.
- Repaired nano: `domain-driven-design/domain-driven-design.nano.md`, 39 lines, 488 words, 10 decision rules, 5 trigger rules, and 6 final checks, SHA-256 `e7dc63e35a2e735224519cfa4c1b281812d7cfdfe9ca83fbe2c3af0252b607a7`.
- Traceability: `_rule-workbench/domain-driven-design/traceability.md`, 118 lines, SHA-256 `60681286b4999c4e89fce515f0d3bcb29d7bcea2a8a0baf4901f4e29bb6ca7cf`; it maps every retained mini and nano detail to the current 38-section full rule and records intentional omissions.
- Reverse-trace review: the converter checked the repaired mini and nano mechanisms, qualifiers, exceptions, and relationship-pattern conditions against the cited full sections. No unsupported compressed-source detail was found, so no source repair was requested or performed in this write scope.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Evans discovery and evolution | `discovering and evolving an implementation-driving domain model` | Generic architecture or code organization that does not need expert language, model feedback, or deeper insight. |
| Language, lifecycle, and context pressure | `Ubiquitous Language conflicts, missing domain concepts, lifecycle rules, Bounded Context or Context Map decisions` | Clean Architecture dependency direction and local Clean Code naming when no domain-model boundary or meaning is disputed. |
| Strategic focus and deeper-model pressure | `Core Domain focus, or deeper-model pressure from awkward procedural behavior` | Ordinary tactical implementation and generic construction coordination. |
| Positive threshold and DDD neighbor ownership | `business complexity makes ... central` plus the Distilled and Implementing DDD ownership clauses | `domain-driven-design-distilled` for the smallest justified DDD investment and `implementing-domain-driven-design` for mechanics after boundaries and language are settled. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Use Eric Evans's Domain-Driven Design lens to review conflicting Quote and Customer meanings across Sales, Pricing, and Billing." | `domain-driven-design` | Direct Evans retrieval plus Ubiquitous Language, Bounded Context, and Context Map decisions. |
| "Three teams use Customer and active differently but are being forced onto one shared class." | `domain-driven-design` | An unnamed model-language collision across contexts is central. |
| "A generic pricing engine has accumulated status checks and cannot express negotiated-agreement concepts." | `domain-driven-design` | Awkward procedural behavior and missing concepts create deeper-model pressure. |
| "Decide whether a simple internal CRUD screen needs any tactical DDD and choose the smallest justified investment." | `domain-driven-design-distilled` | The selectivity and minimum-investment gate is central, not Evans-style deeper-model discovery. |
| "The Bounded Contexts and language are agreed; implement Aggregate persistence, Domain Events, projections, and application services." | `implementing-domain-driven-design` | Post-boundary implementation mechanics are central. |
| "Ordering and Billing mean status differently, and an at-least-once event can duplicate ledger writes." | `domain-driven-design` plus `designing-data-intensive-applications` | Context meaning and distributed event correctness are independent central concerns. |
| "Move pricing policy out of Prisma and Express while clarifying the Pricing model's language." | `domain-driven-design` plus `clean-architecture` | Model meaning and policy/detail dependency direction are independently central. |
| "Rename and extract a fully specified local helper without changing behavior or domain meaning." | `refactoring`, optionally `clean-code` | Structural and local-readability concerns are central; no domain-model discovery decision exists. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance, final-check | Description implementation-driving-model branch; `Model Discovery, Language, and Deeper Insight`; final checklist | Promotes complete `M2` and its final check rather than adding a shortened alignment rule. |
| `N2` | description, early-guidance, final-check | Description awkward-procedural branch; `Model-Driven Implementation`; final checklist | Promotes complete `M3` and `M17`, preserving the model-driven complexity condition and Smart UI exception. |
| `N3` | description, early-guidance, reference-router | Description missing-concepts and context branch; opening rules in the first two concern groups; focused router | Promotes complete `M1`, `M6`, and `M16` without duplicating the required pre-code ordering. |
| `N4` | early-guidance, final-check | `Model-Driven Implementation`; final checklist | Promotes complete `M4`, including tactical applicability and Value Object qualifiers. |
| `N5` | early-guidance, final-check | `Model-Driven Implementation`; final checklist | Promotes complete `M5`, retaining immediate consistency, root mutation, identity references, and the stronger-consistency exception. |
| `N6` | early-guidance, final-check | `Model-Driven Implementation`; final checklist | Preserves Factory/direct-constructor and Repository/model-first choices through complete `M5` and `M6`. |
| `N7` | description, early-guidance, reference-router, final-check | Description Bounded Context and Context Map branch; `Bounded Contexts and Integration`; focused router; final checklist | Promotes complete `M9`, `M10`, and `M22` rather than a second context-boundary rule. |
| `N8` | description, early-guidance, final-check | Description Core Domain branch; `Core Domain and Strategic Structure`; final checklist | Promotes complete `M11` and `M24`. |
| `N9` | description, early-guidance, reference-router | Description deeper-model branch; `Model Discovery, Language, and Deeper Insight`; focused router | Promotes complete `M7` and `M21`, retaining explanatory gain, migration cost, behavior preservation, and incremental movement. |
| `N10` | early-guidance, final-check | `Model Tests`; final checklist | Promotes complete `M14` and `M23` without adding a second testing rule. |
| `N11` | description, early-guidance, reference-router, final-check | Description Ubiquitous Language branch; `Model Discovery, Language, and Deeper Insight`; focused router; final checklist | Promotes complete `M16`, including the within-context and cross-context distinction. |
| `N12` | description, early-guidance, reference-router | Description awkward-procedural branch; `Model-Driven Implementation`; focused router | Promotes complete `M17` with its model-driven complexity threshold and named destinations. |
| `N13` | early-guidance, reference-router | `Bounded Contexts and Integration`; focused router | Promotes complete `M19` so Aggregate and context review remains tied to an observed sprawling change. |
| `N14` | early-guidance, reference-router, final-check | `Bounded Contexts and Integration`; focused router; final checklist | Promotes complete `M10`, `M18`, and `M22`, including Conformist and real-translation Anticorruption Layer conditions. |
| `N15` | description, early-guidance, reference-router, final-check | Description Core Domain branch; `Core Domain and Strategic Structure`; focused router; final checklist | Promotes complete `M11` and `M24` without restating the distillation trigger. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Leads with model usefulness, implementation expression, and iterative discovery. |
| `M2` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Co-located with the terminology trigger `M16`. |
| `M3` | `Model-Driven Implementation` | Moved verbatim | Co-located with the procedural-business-rule trigger `M17`. |
| `M4` | `Model-Driven Implementation` | Moved verbatim | Keeps all tactical applicability and Value Object qualifiers in one authoritative rule. |
| `M5` | `Model-Driven Implementation` | Moved verbatim | Co-located with the creation, reconstitution, mutation, and persistence trigger `M20`. |
| `M6` | `Model-Driven Implementation` | Moved verbatim | Opens the concern group because nano gives the pre-code identification order high salience. |
| `M7` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Co-located with the deeper-model trigger `M21`. |
| `M8` | `Model-Driven Implementation` | Moved verbatim | Keeps model-user interface guidance beside tactical and model-first implementation choices. |
| `M9` | `Bounded Contexts and Integration` | Moved verbatim | Leads explicit context ownership and model-integrity guidance. |
| `M10` | `Bounded Contexts and Integration` | Moved verbatim | Co-located with the integration trigger `M22`; all seven relationship conditions remain intact. |
| `M11` | `Core Domain and Strategic Structure` | Moved verbatim | Co-located with the Core Domain obscurity trigger `M24`. |
| `M12` | `Core Domain and Strategic Structure` | Moved verbatim | Remains subordinate to Bounded Context models and follows strategic priority. |
| `M13` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Keeps pattern and prior-art use subordinate to current model clarity and language. |
| `M14` | `Model Tests` | Moved verbatim | Leads the dedicated validation concern. |
| `M15` | `Core Domain and Strategic Structure` | Moved verbatim | Keeps major strategy tied to implementation-aware domain participation. |
| `M16` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Placed directly after `M2` to bind language alignment to its trigger and cross-context exception. |
| `M17` | `Model-Driven Implementation` | Moved verbatim | Placed directly after `M3` to bind behavior placement to observed procedural leakage. |
| `M18` | `Bounded Contexts and Integration` | Moved verbatim | Co-locates technical-representation isolation and real Anticorruption Layer translation with boundary guidance. |
| `M19` | `Bounded Contexts and Integration` | Moved verbatim | Keeps Module, Aggregate, consistency, and context reassessment together. |
| `M20` | `Model-Driven Implementation` | Moved verbatim | Placed directly after `M5` to bind creation and persistence symptoms to their tactical repair. |
| `M21` | `Model Discovery, Language, and Deeper Insight` | Moved verbatim | Placed directly after `M7` to bind hard-to-explain behavior to deeper-model search. |
| `M22` | `Bounded Contexts and Integration` | Moved verbatim | Placed directly after `M10` to bind integration symptoms to relationship choice, translation, and tests. |
| `M23` | `Model Tests` | Moved verbatim | Co-located with complete domain-language test priorities in `M14`. |
| `M24` | `Core Domain and Strategic Structure` | Moved verbatim | Placed directly after `M11` to bind obscuring mechanisms to Core Domain distillation. |

## Wording Fidelity

- Verbatim primary bias: exact; the complete canonical mini text appears under `Primary Bias`.
- Verbatim mini rules: 24/24 exact. Every decision and trigger bullet is moved whole; none is added, omitted, merged, split, or reworded.
- Verbatim final checklist and order: 6/6 exact and in canonical order.
- Documented exceptions: none.
- Reordering inventory: `M6` opens model-driven implementation because of `N3`; `M7/M21`, `M2/M16`, `M3/M17`, `M5/M20`, `M10/M22`, `M11/M24`, and `M14/M23` are paired to co-locate each rule with its trigger or final pressure. All other moves place complete rules under book-specific concerns without semantic change.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Description inventory: the exact 469-character description is catalog-routing prose. Its Evans discovery/evolution branch traces to `M1`, `M7`, `M21`, `N3`, and `N9`; language, lifecycle, and context branches trace to `M2`, `M9`, `M16`, `N1`, `N7`, and `N11`; Core Domain traces to `M11`, `M24`, `N8`, and `N15`. The Distilled and Implementing DDD boundary clauses trace to the reviewed compatibility documents and add no model-design rule.
- Concern-heading inventory: `Model Discovery, Language, and Deeper Insight`, `Model-Driven Implementation`, `Bounded Contexts and Integration`, `Core Domain and Strategic Structure`, and `Model Tests` only group verbatim mini guidance.
- Ordinary loading directive: stop at `SKILL.md` when it resolves the modeling question. This is a progressive-disclosure condition, not technical guidance.
- Focused loading directive: eight source-backed labels link common modeling questions directly to canonical full headings; every other bounded source question uses the exhaustive index.
- Comprehensive loading directive: an explicit comprehensive DDD audit or complete Evans lens reads `references/full.md` end to end. This implements the repository loading contract.
- Index inventory: all 38 `Read when` cells are manually authored routing summaries tied to their same-named canonical H2 sections. `references/index.md` remains their single source of truth; this mapping does not duplicate the row set.
- Review: frontmatter, concern headings, loading transitions, index routing, and metadata add no technical mechanism, default, guarantee, example, failure mode, or preference beyond the canonical source.

## Size Exception

- Canonical mini: 1,061 words.
- `SKILL.md`: 1,230 words across 75 lines.
- Packaging overhead: 169 words, within the documented 151-200 allowance.
- Description: 469 characters.
- Decision: retain a source-driven exception to the 500-word skill target because the repaired canonical mini already exceeds it and all 24 rules plus the six-item final checklist are required for complete ordinary use. The 19-word soft-target overage provides eight direct focused routes without duplicating the exhaustive index; canonical guidance was not compressed.

## Evaluation Cases

These seven durable cases are frozen before behavioral execution. Each required set is a minimum inclusion set, and extra selections are permitted. Batch 3 executed against the reconciled frozen catalog; no fixture, description, or package file changed during this lane.

- Batch 3 common runtime: `mode=green`, `model=gpt-5.4`, `codex_version=codex-cli 0.144.1`, `ignore_user_config=true`, `ephemeral=true`, `sandbox=read-only`, `green_workspace=/Users/jakubtomanik/github/agent-rules-books`, and `baseline_workspace=temporary directory without project skills`.
- Planned evidence accounting: 11 planned run slots produced structured records with `exit_code=0`, `codex_errors=[]`, and `integrity_errors=[]`. Five runner invocations returned nonzero only after recording a valid structured result with a required-skill selection miss. Two additional pre-fix direct-run artifacts are retained with `exit_code=1` and `result=null`.

### E1: Direct Evans pricing brief

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/direct-evans-pricing-brief.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: direct Evans invocation; extra relevant selections are permitted.
- Reference expectation: ordinary.
- Relevant sections: normal-use model, language, context, relationship, and Core Domain guidance in `SKILL.md`; no full-reference read is required.
- Case SHA-256: `5ec5dbf71bcf410bb48239216f6a5b7d65ae6e8c614df5e8874e4479da3141fb`; every artifact below matches the frozen fixture and common runtime configuration.
- Runs:
  - Pre-fix attempt: `_skill-workbench/evaluations/results/domain-driven-design/direct-evans-pricing-brief/green-batch3-1.json`; thread `019f5c4a-2522-73a3-8b7f-3e31842f630d`; `exit_code=1`, `result=null`, no selection or read evidence.
  - Pre-fix retry: `_skill-workbench/evaluations/results/domain-driven-design/direct-evans-pricing-brief/green-batch3-retry-1.json`; thread `019f5c4a-75e7-7aa0-8aad-0a477cd33618`; `exit_code=1`, `result=null`, no selection or read evidence.
  - Run 1: `_skill-workbench/evaluations/results/domain-driven-design/direct-evans-pricing-brief/green-batch3-valid-1.json`; thread `019f5c4e-c76c-7ac0-ad71-3e52360d4e96`; selected `{domain-driven-design}`; consulted `{.agents/skills/domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
  - Run 2: `_skill-workbench/evaluations/results/domain-driven-design/direct-evans-pricing-brief/green-batch3-2.json`; thread `019f5c50-32b4-7853-a8a4-d7b5d3b856df`; selected `{domain-driven-design}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/domain-driven-design/references/index.md, .agents/skills/domain-driven-design/references/full.md}`; sections `{domain-driven-design: [Making Implicit Concepts Explicit, Ubiquitous Language, Bounded Contexts, Model Integrity Patterns]}`; mode `focused`; required subset `pass`.
  - Run 3: `_skill-workbench/evaluations/results/domain-driven-design/direct-evans-pricing-brief/green-batch3-3.json`; thread `019f5c51-45af-7f83-ad82-04e514ed39e1`; selected `{domain-driven-design}`; consulted `{/Users/jakubtomanik/github/agent-rules-books/.agents/skills/domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
- Package fidelity trace: `M1-M2`, `M6-M11`, `M15-M16`, `M18-M22`, `N1`, `N3`, `N7-N9`, `N11`, and `N14-N15`.
- Attribution review: supported. The context, language, lifecycle, translation, relationship, and Core Domain judgments trace to the accepted package. Concrete proposed names and the event-storming/domain-workshop tactic are solver-added application choices, not credited as canonical book rules.
- Conversion result: pass; all three planned runs include the required skill and no DDD disclosure tier materially collapses.
- Diagnostics: the first attempt and its retry were invalid environment records caused by the then-unsupported output-schema `uniqueItems` keyword; both are retained and excluded from the 11 planned acceptance records. Run 2 over-read four coherent sections, `4/38` of the DDD reference, despite an ordinary expectation; this is bounded diagnostic over-reading, not tier collapse.

### E2: Unnamed Customer language collision

- Class: recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/unnamed-customer-language-collision.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: unnamed distinctive discovery; additional relevant skills are permitted.
- Reference expectation: ordinary.
- Relevant sections: Ubiquitous Language, Bounded Context ownership, explicit translation, and avoidance of one shared model, all represented in `SKILL.md`.
- Case SHA-256: `b914d0a5d83b0da17369373165be596bc25188a006369490e5f0585205c45971`; every run matches the frozen fixture and common runtime configuration.
- Runs:
  - Run 1: `_skill-workbench/evaluations/results/domain-driven-design/unnamed-customer-language-collision/green-batch3-1.json`; thread `019f5c52-4f30-7d91-8917-3c0ccaa5e8fb`; selected `{domain-driven-design-distilled, domain-driven-design}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md, .agents/skills/domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
  - Run 2: `_skill-workbench/evaluations/results/domain-driven-design/unnamed-customer-language-collision/green-batch3-2.json`; thread `019f5c53-23fc-72b0-b69a-ff5cd1a5806e`; selected `{domain-driven-design-distilled}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
  - Run 3: `_skill-workbench/evaluations/results/domain-driven-design/unnamed-customer-language-collision/green-batch3-3.json`; thread `019f5c53-e1a4-7fa3-80fb-5c510a2b7071`; selected `{domain-driven-design-distilled}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: `M2`, `M9-M10`, `M16`, `M18`, `M22`, `N1`, `N7`, `N11`, and `N14`.
- Attribution review: run 1 is supported by the accepted DDD package. Runs 2 and 3 did not consult that package, so their otherwise compatible language/context advice cannot be credited to it. Illustrative local type, event, and contract names are solver additions; no answer falsely states that Evans prescribes them.
- Conversion result: fail; required-subset discovery passes `1/3`, below the mandatory `3/3` unnamed threshold.
- Diagnostics: run 1 has permitted over-selection of `domain-driven-design-distilled`; runs 2 and 3 select that sibling instead of the required Evans skill. All three remain SKILL-only ordinary traces, so there is no reference over-read or tier collapse.

### E3: Ordinary pricing policy model

- Class: application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/ordinary-pricing-policy-model.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: bounded local modeling case; service-boundary and infrastructure redesign are explicitly out of scope.
- Reference expectation: ordinary.
- Relevant sections: explicit concepts, model-user design, domain-language examples and tests, and deeper-model feedback in `SKILL.md`.
- Case SHA-256: `02bc9472a80849f036e0b51a2fc25eabf261d5254a997bca805ebeaa6aff4f1f`; the run matches the frozen fixture and common runtime configuration.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/ordinary-pricing-policy-model/green-batch3-1.json`; thread `019f5c54-ac35-7eb3-9619-38b108504a66`; selected `{domain-driven-design-distilled}`; consulted `{/Users/jakubtomanik/github/agent-rules-books/.agents/skills/domain-driven-design-distilled/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: `M1`, `M4`, `M7-M8`, `M13-M14`, `M17`, `M21`, `M23`, `N3-N4`, `N9-N10`, and `N12`.
- Attribution review: the DDD package was not consulted, so the explicit-concept analysis and concrete TypeScript model cannot be credited to the Evans conversion. They are Distilled/general-solver application choices, and the answer makes no false Evans attribution.
- Conversion result: fail; required-subset discovery passes `0/1`.
- Diagnostics: the ordinary trace itself is SKILL-only and does not over-read, but it exercises the sibling package rather than the required one; DDD ordinary application therefore remains unproven in this case.

### E4: Focused legacy ERP integration

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/focused-legacy-erp-integration.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: one bounded context-relationship and translation dispute; do not broaden into a full audit.
- Reference expectation: focused.
- Relevant sections: the semantic target is relationship-pattern fit, translation ownership, protocol publication, and boundary testing; likely headings include `Bounded Contexts`, `Model Integrity Patterns`, `Translation at Boundaries`, and `Testing Rules`, without requiring an exact set.
- Case SHA-256: `5d99cd1a6554c338ef91d582a6d236f6de0e77c5e2ab78a94554eb851c86789f`; the run matches the frozen fixture and common runtime configuration.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/focused-legacy-erp-integration/green-batch3-1.json`; thread `019f5c55-aed2-7772-a53e-f3087bffd811`; selected `{domain-driven-design-distilled, implementing-domain-driven-design}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md, .agents/skills/implementing-domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: `M9-M10`, `M18`, `M22-M23`, `N7`, `N10`, and `N14`, plus the named full headings.
- Attribution review: the response's Conformist, Published Language, translation, and boundary-test advice is compatible with the accepted DDD package, but this run consulted only Distilled and Implementing DDD. It is not evidence of Evans-package application and contains no false Evans attribution.
- Conversion result: fail; required-subset discovery passes `0/1`, so the intended focused retrieval is not demonstrated.
- Diagnostics: the expected DDD focused route was never entered. That is a selection miss, not evidence that the DDD tier itself collapsed; no reference files were read.

### E5: Comprehensive multi-context audit

- Class: retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/comprehensive-multi-context-audit.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: explicit complete Evans-style audit; extra relevant selections are permitted.
- Reference expectation: comprehensive.
- Relevant sections: all 38 full-reference H2 sections, recorded as `*` after an end-to-end read.
- Case SHA-256: `69e426c19b4508f2473ff1d4327e22433535989d3a34aa5ad5d38fedbea4855b`; the run matches the frozen fixture and common runtime configuration.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/comprehensive-multi-context-audit/green-batch3-1.json`; thread `019f5c56-a5e0-7280-9456-77b1c32e7564`; selected `{domain-driven-design}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/domain-driven-design/references/full.md}`; sections `{domain-driven-design: [*]}`; mode `comprehensive`; required subset `pass`.
- Package fidelity trace: every `M*`, `N*`, final-checklist item, and full heading.
- Attribution review: supported. The explicitly attributed DDD claims about context-local language, explicit domain concepts, model discovery, aggregate/invariant boundaries, strategic focus, translations, domain tests, and iterative refactoring are present in the accepted package. Insurance-specific context names, lifecycle questions, integration choices, and thin-slice sequencing are solver application judgment rather than added book rules.
- Conversion result: pass; required-subset discovery passes `1/1` and the explicit comprehensive request reaches the full reference end to end.
- Diagnostics: no over-selection or disclosure anomaly. The `*` section record and `comprehensive` mode are internally consistent.

### E6: Generic pricing engine pressure

- Class: pressure and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/pressure-generic-pricing-engine.md`.
- Required skills: `{domain-driven-design}`.
- Selection notes: unnamed discovery under deadline, authority, and sunk-cost pressure; extra relevant selections are permitted.
- Reference expectation: ordinary.
- Relevant sections: deeper-model pressure, missing concepts, language collision, safe incremental migration, and domain-expert examples are complete in `SKILL.md`.
- Case SHA-256: `1d40b8eaf3f8ef82f10abed636b4dcc42fdae770703029ee6875eabde5dbdb64`; the run matches the frozen fixture and common runtime configuration.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-generic-pricing-engine/green-batch3-1.json`; thread `019f5c57-ff5e-7f40-bcf6-23e3980fced6`; selected `{domain-driven-design-distilled, implementing-domain-driven-design, clean-architecture}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md, .agents/skills/implementing-domain-driven-design/SKILL.md, .agents/skills/clean-architecture/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: `M1-M2`, `M7`, `M14-M16`, `M21`, `M23`, `N1`, `N3`, `N9-N11`, and the final checklist.
- Attribution review: the bounded migration, missing-concept, domain-example, and no-big-bang recommendations align with the accepted DDD package, but the target package was not consulted and receives no credit. Feature flags, concrete use-case shapes, and checkpoint mechanics are solver/neighbor guidance, not claimed as Evans rules.
- Conversion result: fail; required-subset discovery passes `0/1`.
- Diagnostics: deadline, authority, and sunk-cost pressure selected three neighboring skills but not the required Evans skill. The answer avoided both another generic branch and a big-bang rewrite, yet answer quality does not repair the discovery miss.

### E7: DDIA-compatible overlap

- Class: compatible overlap application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/ddia-compatible-overlap.md`.
- Required skills: `{domain-driven-design, designing-data-intensive-applications}`.
- Selection notes: both model meaning across Ordering and Billing and distributed event correctness are central; extra relevant selections are permitted.
- Reference expectation: ordinary for both skills unless one bounded source question remains unresolved.
- Relevant sections: DDD context language, relationship, translation, and boundary tests together with DDIA ownership, write/event durability, duplicate/replay/order safety, schema evolution, and rebuildability.
- Case SHA-256: `61d9f2de85fe4cc134d08ff0ebdec6c0570f0cb4c0db12fb4d25589b36e77cd3`; the run matches the frozen fixture and common runtime configuration.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/ddia-compatible-overlap/green-batch3-1.json`; thread `019f5c58-d4c1-7832-bfca-93087bf3089d`; selected `{domain-driven-design, designing-data-intensive-applications}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/domain-driven-design/references/index.md, .agents/skills/domain-driven-design/references/full.md, .agents/skills/designing-data-intensive-applications/SKILL.md, .agents/skills/designing-data-intensive-applications/references/index.md, .agents/skills/designing-data-intensive-applications/references/full.md}`; sections `{domain-driven-design: [Bounded Contexts, Strategic Design, Model Integrity Patterns, Translation at Boundaries], designing-data-intensive-applications: [Reliability Rules, Scalability and Maintainability Rules, Data Model and Storage Rules, Query Model and Data Shape Rules, Storage Engine and Indexing Rules, Consistency Rules, Idempotency and Replay Rules, Ordering Rules, Event, Log, and Stream Rules, Schema Evolution Rules, Partitioning and Locality Rules, Replication Rules, Transaction Rules, Derived Data Rules]}`; mode `focused`; required subset `pass`.
- Package fidelity trace: DDD `M2`, `M9-M10`, `M14`, `M18`, `M22-M23`, `N1`, `N7`, `N10-N11`, and `N14`; DDIA package fidelity remains owned by its mapping.
- Attribution review: supported and separated. DDD supplies context-specific meaning, explicit relationships, translation, and boundary testing; DDIA supplies durability, replay, ordering, schema-evolution, and rebuildability pressure. Transactional outbox, concrete event names, event IDs, aggregate versions, dedupe constraints, and retention choices are solver implementation recommendations, not credited as Evans rules.
- Conversion result: fail for this case's disclosure contract: required-subset discovery passes `1/1` and the DDD component remains bounded, but the neighboring DDIA focused tier materially collapses.
- Diagnostics: DDD reads four coherent boundary sections, `4/38`, which is diagnostic over-reading from an ordinary expectation but remains bounded. DDIA reads `14/26` sections, about `54%`, spanning storage, query shape, indexing, consistency, replay, ordering, streams, schema, partitioning, replication, transactions, and derived data; that is material tier collapse rather than a small relevant expansion. The selected set contains exactly the two required skills, with no additional over-selection.

## Post-Run Contract Audit And Replacement Cases

The original `6/11` observation remains immutable evidence, but an independent post-run ownership audit found that E2, E3, and E4 do not isolate this skill's catalog role. E2 duplicates Distilled's language-boundary case, E3 explicitly asks for the smallest model improvement owned by Distilled's investment gate, and E4 combines Distilled relationship selection with Implementing DDD translation mechanics. Those records remain catalog diagnostics and are not repurposed as sibling acceptance evidence. The audit found no description defect and prohibited tuning the 469-character description to those misclassified cases.

The same audit classified E6 as a correctly owned but single stochastic miss because its overloaded language, accumulated procedural branches, missing expert examples, and deeper-model pressure match the current description directly. Two fresh repetitions are frozen below before execution. Another miss requires a replacement pressure case centered on actual deeper-model discovery before any description edit is considered.

Manual review also supersedes the initial E7 tier-collapse judgment. The target's `4/38` read is bounded. DDIA read `14/26` sections, but ten are directly relevant to the multi-concern fixture, the record remained focused rather than comprehensive, and the answer did not apply the four unnecessary sections. E7 is therefore a required-subset pass with a broad-focused-read diagnostic, not an automatic disclosure failure under the one-third review rule.

### R1: Unnamed Deeper Reservation Model

- Class: distinctive unnamed recognition and ordinary application; three runs required.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/unnamed-deeper-reservation-model.md`.
- Fixture SHA-256: `cb5fdef5c6d55193e7e9eff10f45c9ac9e408cbe0579eab13558297a1a68ed29`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Ownership: modeling investment is already settled, implementation mechanics are excluded, and the task requires expert-language distinctions, missing concepts, explanatory gain, falsifying scenarios, and incremental deeper-model evolution.
- Reference expectation: ordinary; `SKILL.md` contains the required deeper-model, explicit-concept, scenario, and safe-refactoring guidance.
- Runs:
  - Run 1 is `_skill-workbench/evaluations/results/domain-driven-design/unnamed-deeper-reservation-model/green-batch3-contract-final-1.json`; thread `019f5cae-cb21-75d3-927f-94d2bd3d0d72`; selected `{domain-driven-design, implementing-domain-driven-design, refactoring}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/implementing-domain-driven-design/SKILL.md, .agents/skills/refactoring/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
  - Run 2 is `_skill-workbench/evaluations/results/domain-driven-design/unnamed-deeper-reservation-model/green-batch3-contract-final-2.json`; thread `019f5caf-cc7a-7b81-8dae-933af78ad622`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/implementing-domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
  - Run 3 is `_skill-workbench/evaluations/results/domain-driven-design/unnamed-deeper-reservation-model/green-batch3-contract-final-3.json`; thread `019f5caf-cc7a-7c41-90b8-f42c34cbbfad`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted `{/Users/jakubtomanik/github/agent-rules-books/.agents/skills/domain-driven-design/SKILL.md, /Users/jakubtomanik/github/agent-rules-books/.agents/skills/implementing-domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
- Package fidelity trace: DDD `M1-M2`, `M7-M8`, `M14`, `M16`, `M21`, `M23`, `N1`, `N3`, `N9-N12`, and the model-language and model-test final checks.
- Attribution review: supported only at the package-guidance level. DDD supports recognizing overloaded lifecycle language, making the hold and commitment concepts explicit, testing them through expert-language scenarios, comparing explanatory gain with migration cost, and moving incrementally while preserving behavior. `CapacityHold`, `Commitment`, the exact state variants and reason vocabularies, the Aggregate shape, and the ordered migration steps are solver application choices, with neighboring implementation and refactoring guidance also consulted; they are not credited as Evans rules.
- Conversion result: pass; distinctive unnamed required-subset discovery passes `3/3`.
- Diagnostics: ordinary disclosure is intact in all three runs. Every selected package remained at `SKILL.md` only, no reference file was read, and the additional relevant selections are permitted by the frozen contract.

### R2: Ordinary Committed Claims Model

- Class: ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/ordinary-committed-claims-model.md`.
- Fixture SHA-256: `71ac80a7feb40158a23fa82499e66e6e439caac6e08211d8d258537746eec2b4`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Ownership: context and DDD investment are settled; the flag bundle hides distinct domain decisions and the task asks for implementation-driving model evolution, domain-language feedback, and safe migration rather than tactical mechanics.
- Reference expectation: ordinary; `SKILL.md` should resolve the bounded model evolution without references.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/ordinary-committed-claims-model/green-batch3-contract-final-1.json`; thread `019f5caf-cc60-7452-836d-32ea1905bd02`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted `{.agents/skills/domain-driven-design/SKILL.md, .agents/skills/implementing-domain-driven-design/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `pass`.
- Package fidelity trace: DDD `M1-M2`, `M4`, `M7-M8`, `M14`, `M16`, `M21`, `M23`, `N1`, `N3-N4`, `N9-N12`, and the model-language and model-test final checks.
- Attribution review: DDD supports replacing opaque flags with implementation-driving concepts, keeping specialist language explicit, validating distinctions with domain-language tests, and migrating in behavior-preserving increments. The five TypeScript unions, `Claim` API, exact specialist questions, characterization sequence, and choice to retain one Aggregate root are solver or neighboring-skill application decisions, not book rules.
- Conversion result: pass; ordinary required-subset discovery passes `1/1`.
- Diagnostics: ordinary disclosure is intact. Both selected packages remained at `SKILL.md` only, the DDD body resolved the modeling question without references, and the extra Implementing DDD selection is permitted.

### R3: Focused Hidden Fulfillment Concept

- Class: focused retrieval and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/focused-hidden-fulfillment-concept.md`.
- Fixture SHA-256: `ccc4ce6be7528b8d7fae1b030cd2ab88c77242ac9030b4472468767f4274f70c`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Ownership: the bounded dispute asks whether awkward status language hides a missing concept, what explanatory gain warrants a deeper model, and which scenarios could falsify it.
- Reference expectation: focused; use the index and the smallest coherent set around `Knowledge Crunching and Deep Models`, `Breakthrough and Deeper Insight`, or `Making Implicit Concepts Explicit`.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/focused-hidden-fulfillment-concept/green-batch3-contract-final-1.json`; thread `019f5cb1-20a4-7fa3-b070-b195675a5a22`; selected `{domain-driven-design-distilled}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md, .agents/skills/domain-driven-design-distilled/references/index.md, .agents/skills/domain-driven-design-distilled/references/full.md}`; sections `{domain-driven-design-distilled: [Ubiquitous Language Rules, Tactical Pattern Rules, Aggregate Minimalism Rules, Application Service Rules, Architecture and Infrastructure Rules, Collaboration Rules, Practicality Rules, Accelerated Modeling and Project Rules, Code Generation Rules, Review Rules, Testing Rules, Review Checklist, Final Instruction]}`; mode `focused`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: the DDD target trace would be `M1-M2`, `M7`, `M14`, `M16`, `M21`, `M23`, `N1`, `N3`, and `N9-N11`, plus the three named full headings, but the target package was not consulted. The selected Distilled package supplies only its own local-language, richer-concept, scenario, and incremental-strengthening guidance.
- Attribution review: the response is compatible with DDD's missing-concept and deeper-model guidance, but DDD receives no application credit because it was not consulted. Distilled supports rejecting an overloaded status, using local domain language, validating behavior with scenarios, and strengthening a model incrementally. `allocationCommitment`, `supplyAssignment`, `PROPOSED`/`RESERVED`, the event names, the three falsifying scenarios, and the migration path are solver application choices, not credited to either book as authored rules.
- Conversion result: fail; focused required-subset discovery passes `0/1`, so the intended DDD focused route remains unproven.
- Diagnostics: the selected sibling's focused read covers `13/19` full-reference H2 sections, about `68%`, and spans tactical patterns, Aggregates, application services, architecture, collaboration, delivery, code generation, review, and testing. The bounded answer uses only a much smaller subset of those concern families, so manual review classifies this as material tier collapse in Distilled. It is not evidence that DDD's own focused router collapsed because that package was never entered.

### R4: Generic Pricing Engine Repetitions

- Class: repeated diagnosis of the correctly owned E6 pressure case.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/pressure-generic-pricing-engine.md`.
- Fixture SHA-256: `1d40b8eaf3f8ef82f10abed636b4dcc42fdae770703029ee6875eabde5dbdb64`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Reference expectation: ordinary.
- Runs:
  - Run 2 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-generic-pricing-engine/green-batch3-diagnostic-2.json`; thread `019f5cb1-22b2-7573-8289-46b55a23b67a`; selected `{domain-driven-design-distilled}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
  - Run 3 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-generic-pricing-engine/green-batch3-diagnostic-3.json`; thread `019f5cb1-21bf-75d1-b1f4-98285fd337ed`; selected `{domain-driven-design-distilled, clean-architecture}`; consulted `{.agents/skills/domain-driven-design-distilled/SKILL.md, .agents/skills/clean-architecture/SKILL.md}`; sections `[]`; mode `ordinary`; required subset `fail`, with `required project skill not selected: domain-driven-design`.
- Package fidelity trace: the DDD target trace remains E6's `M1-M2`, `M7`, `M14-M16`, `M21`, `M23`, `N1`, `N3`, `N9-N11`, and the final checklist, but neither repetition consulted the target package.
- Attribution review: both answers align with DDD concerns about overloaded language, missing concepts, expert examples, and incremental change, but no such guidance is credited to DDD because it was not consulted. Distilled supports selective incremental strengthening, explicit concepts, local language, and expert scenarios; Clean Architecture contributes boundary direction in run 3. The named agreement types, thin-slice orchestration, feature flag, manual-review fallback, numeric timeboxes and example counts, and post-Friday checkpoints are solver or neighboring-skill choices rather than Evans guidance.
- Conversion result: fail; the two repetitions pass required-subset discovery `0/2`, and the correctly owned pressure case is now `0/3` including preserved E6 run 1.
- Diagnostics: both repetitions are valid selection misses with clean structured-result integrity, not environment or harness failures, so neither was retried. Ordinary disclosure remains intact for the packages that were selected because no references were read. Because either miss triggers the frozen stop rule, the pressure case needs replacement with a newly frozen deeper-model-discovery fixture before any description work.

### R5: Focused Competing Allocation Models

- Class: focused retrieval and application; one run required.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/focused-competing-allocation-models.md`.
- Fixture SHA-256: `f7332e27aaaa6555b2d6eb8825b0497939dc7b38fb796884581ae4a6e6150e8f`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Ownership: the Allocation context and commitment to model-driven design are settled. The task requires choosing between two implementation-driving models by explanatory power, making an implicit concept explicit, trying domain-language experiments that can falsify the choice, and balancing explanatory gain against behavior-preserving migration cost. Selectivity and tactical implementation mechanics are explicitly outside the central decision.
- Reference expectation: focused; use the index and the smallest coherent set around `Knowledge Crunching and Deep Models`, `Breakthrough and Deeper Insight`, `Making Implicit Concepts Explicit`, and `Refactoring Toward Deeper Insight`.
- Runs: run 1 is `_skill-workbench/evaluations/results/domain-driven-design/focused-competing-allocation-models/green-batch3-contract-final-1.json`; thread `019f5ccf-7e21-7ad2-b87d-e89187ea59a1`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted both selected `SKILL.md` files; sections `[]`; mode `ordinary`; `exit_code: 0`; empty selection, integrity, and Codex errors; required subset `pass`.
- Package fidelity trace: DDD `M1-M2`, `M7-M8`, `M14`, `M16`, `M21`, `M23`, `N1`, `N3`, `N9-N12`, the four named full headings, and the model-language and model-test final checks.
- Attribution review: DDD supports deeper-model search, making implicit concepts explicit, comparing explanatory gain with migration cost, using expert conversation and domain scenarios to test a model, and preserving behavior through incremental migration. Choosing Candidate B, treating allocation as a reconciliation policy, the two concrete falsification exercises, the compatibility facade, projections, events, and migration order are fixture application or solver choices, not Evans rules. `SupplyPromise` and `CapacityReservation` originate in the fixture.
- Conversion result: pass; corrected focused-case ownership includes required DDD `1/1` with clean evidence.
- Diagnostics: the compact bodies fully resolved the question, so the passive result correctly remained ordinary instead of forcing a reference read. R5 adds no new focused-access evidence, but preserved direct run 2 already reaches `index.md` and four coherent DDD sections. The mistaken focused expectation is a fixture-design diagnostic, not a package disclosure failure.
- Frozen stop rule: any valid run that omits `domain-driven-design`, any unjustified comprehensive target read, or any answer that credits solver invention as source guidance fails the replacement case. Environment, harness, or evidence-integrity failures are preserved and replaced under the shared protocol; valid selection misses are not retried.

### R6: Pressure Committed Service Recovery Model

- Class: pressure recognition and ordinary application; three runs required to diagnose selection stability.
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/pressure-committed-service-recovery-model.md`.
- Fixture SHA-256: `78e2d20e22daf05a1c210e784f73ee798cb540168b436cbded7b37a5c17aad3a`.
- Required skills: `{domain-driven-design}`; additional relevant skills are permitted.
- Ownership: the Service Recovery context, modeling investment, and replacement commitment are settled. The deadline and sunk-cost pressure test whether the solver will preserve explicit specialist distinctions, develop a deeper implementation-driving model, test it against expert scenarios, and move one behavior-preserving vertical slice instead of adding another generic branch. Distilled's investment gate and Implementing DDD's tactical mechanics are not the primary decision.
- Reference expectation: ordinary; `SKILL.md` contains the required deeper-model, explicit-concept, domain-scenario, pressure-resistance, and incremental-change guidance.
- Runs:
  - Run 1 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-committed-service-recovery-model/green-batch3-contract-final-1.json`; thread `019f5ccf-45ad-7961-bf77-a15ba89a8874`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted both selected `SKILL.md` files; sections `[]`; mode `ordinary`; `exit_code: 0`; empty selection, integrity, and Codex errors; required subset `pass`.
  - Run 2 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-committed-service-recovery-model/green-batch3-contract-final-2.json`; thread `019f5cd0-4057-7691-af23-90a7e8f24847`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted both selected `SKILL.md` files; sections `[]`; mode `ordinary`; `exit_code: 0`; empty selection, integrity, and Codex errors; required subset `pass`.
  - Run 3 is `_skill-workbench/evaluations/results/domain-driven-design/pressure-committed-service-recovery-model/green-batch3-contract-final-3.json`; thread `019f5ccf-60b5-7fc0-8c7f-bcdedd426ec1`; selected `{domain-driven-design, implementing-domain-driven-design}`; consulted both selected `SKILL.md` files; sections `[]`; mode `ordinary`; `exit_code: 0`; empty selection, integrity, and Codex errors; required subset `pass`.
- Package fidelity trace: DDD `M1-M2`, `M7-M8`, `M14-M16`, `M21`, `M23`, `N1`, `N3`, `N9-N12`, and the model-language and model-test final checks.
- Attribution review: all three answers apply specialist language, explicit implementation-driving concepts, expert scenarios, resistance to another generic branch, and one behavior-preserving vertical slice under deadline pressure. Named Aggregates, Domain Services, cardinalities, exact invariants, adapters, handler reuse, operation names, pseudocode, and migration ordering are neighboring Implementing DDD guidance or solver hypotheses, not Evans rules. No answer falsely attributes them to the source or materially contradicts DDD guidance.
- Conversion result: pass; corrected pressure recognition includes required DDD `3/3` with clean evidence and ordinary disclosure.
- Diagnostics: every run also selected Implementing DDD, which is permitted and explains the tactical specificity. Runs 1 and 3 retain nonfatal shell-snapshot cleanup warnings in `stderr`; their `codex_errors` and integrity remain clean.
- Frozen stop rule: any valid run that omits `domain-driven-design`, any unjustified reference escalation, or any answer that credits solver invention as source guidance fails the replacement case. Environment, harness, or evidence-integrity failures are preserved and replaced under the shared protocol; valid selection misses are not retried.

R3 and R4 remain immutable failed diagnostics. A second ownership review after their results found that both still ask whether a deeper model is warranted instead of making the modeling commitment unambiguous. They therefore cannot establish or reject the current DDD package's focused and pressure acceptance. R5 and R6 are separately named, pre-run audited replacements; they do not overwrite, relax, or erase the earlier contracts or results.

## Independent Review

- Reviewer: independent final source-to-package review completed outside the converter after the batch catalog freeze; verdict `PASS` with no P1/P2/P3 findings.
- Catalog snapshot: all ten live project book-skill descriptions were reviewed together again after the Distilled description repair. The three DDD descriptions assign the smallest-investment/selectivity gate to `domain-driven-design-distilled`, strategic discovery and deeper-model development to this skill, and implementation mechanics after context and model commitment to `implementing-domain-driven-design`. The complete ten-skill catalog is frozen for Batch 3 behavioral evaluation as of 2026-07-13.
- DDD-family reconciliation: the current three descriptions use reciprocal ownership boundaries. Distilled claims the smallest effective DDD investment and gives deeper model discovery to this Evans skill; Implementing DDD claims mechanics after context/model commitment and gives strategic discovery and deeper-model development to this skill; this description gives those siblings the same selectivity and implementation roles. The repaired wording does not change any frozen fixture's required target set. Independent package acceptance remained unchanged during behavioral execution.
- Semantic verdict: independently accepted. The final package contains no unsupported strengthening, weakening, omission, or imported technical guidance.
- Unsupported or altered guidance: none found in the authored package. The repaired source snapshot and its traceability remain authoritative.
- Final behavioral reviewer: independent read-only review of R5 and all three R6 artifacts returned `PASS` with no P1/P2/P3 findings. Required subsets, fixture hashes, selected/consulted consistency, disclosure records, and attribution boundaries are clean.
- Post-map behavioral review: `FAIL` for RM1b required-skill inclusion in `2/2`; both ordinary answers selected sibling DDD skills but omitted `domain-driven-design`. RM2 and RM3b disclosure and all three attribution checks passed. This is a behavioral discovery failure, not a source/package-fidelity defect.

## Validation Evidence

- Structural validation: `rtk python3 _skill-workbench/scripts/validate_conversion.py domain-driven-design` returned `PASS domain-driven-design: SKILL.md 66 lines; 1202 words (141 beyond mini); 24 mini rules and 15 nano rules mapped; 38 full-reference sections indexed`.
- Official skill validation: `rtk uv run --with pyyaml /Users/jakubtomanik/personal-google/reference/codex/codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py .agents/skills/domain-driven-design` returned `Skill is valid!` with exit 0. The previously used installed-system path is absent on this machine.
- Full-reference equality: `rtk cmp -s domain-driven-design/domain-driven-design.md .agents/skills/domain-driven-design/references/full.md` returned exit 0. Both files have SHA-256 `de806ceb828df4408e452361ab587d81f213443ad057017b1f6bed2334d5aaa6`.
- Index validation: repository validation passes all 38 headings, GitHub anchors, source order, and heading-to-last-nonempty ranges. Both runtime references are linked directly from `SKILL.md`, and the index links `full.md`.
- Wording fidelity: `rtk python3 _skill-workbench/scripts/check_rule_wording.py --mini domain-driven-design/domain-driven-design.mini.md --skill .agents/skills/domain-driven-design/SKILL.md` reports 24 mini rules, 24 skill guidance rules, 24 exact matches, zero missing, zero added, exact primary bias, exact final-checklist wording/order, and `wording fidelity: exact`.
- Metadata and budget: frontmatter contains only `name` and `description`; the description is 469 characters; `agents/openai.yaml` has explicit implicit invocation, valid quoted interface fields, a 33-character short description, and exactly one `$domain-driven-design` token. Packaging overhead is 141 words.
- Evaluation contracts: `rtk python3 _skill-workbench/scripts/validate_evaluation_contracts.py` returned `PASS: every durable evaluation case names only live required skills`. Every original and separately named replacement fixture remains immutable at its recorded hash and required set.
- Behavioral result integrity: 13 JSON artifacts parse: 11 planned structured records plus two preserved pre-fix invalid attempts. All planned records have the expected case hash and common configuration, `exit_code=0`, `codex_errors=[]`, and `integrity_errors=[]`. Five planned records have only the recorded required-skill `selection_errors`; nonfatal plugin-catalog and shell-snapshot warnings remain in `stderr` where emitted.
- Invocation evaluation: `6/11` planned runs pass required-subset inclusion. Direct discovery passes `3/3`; unnamed discovery passes `1/3`; ordinary, focused, and pressure each pass `0/1`; comprehensive and DDIA overlap each pass `1/1`. The five misses are retained and were not rerun.
- Application evaluation: answer attribution was reviewed for all 11 planned records. No unsupported solver addition was credited as Evans guidance, but cases that did not consult the DDD package are not counted as package-application evidence.
- Historical matrix limitations: the initial `6/11` observation fails its then-assigned unnamed, ordinary, focused, and pressure contracts. Later ownership review reclassified E2-E4 and the generic pressure case as diagnostics rather than rewriting them. E7 is a required-subset pass with a broad-focused neighboring DDIA diagnostic, not automatic tier collapse. Any future description change still requires catalog-contract validation and affected positive-case reruns.

## 2026-07-13 Post-Retrofit Checkpoint

- Evidence integrity: all eleven retrofit artifacts match their frozen fixture hashes and common `gpt-5.4` GREEN configuration. Every record has `exit_code=0`, `codex_errors=[]`, and `integrity_errors=[]`; the three failed first-round runs are valid required-skill selection misses and remain preserved without retry.
- Historical accounting: the original `6/11` observation, E2-E4 ownership reclassification, E6/R4 misses, R3 miss, and E7 manual disclosure review remain unchanged above. R3 and R4 are failed diagnostics; R5 and R6 are separately frozen current-state replacements. Their counts are not flattened into one ratio.
- Current discovery and disclosure: direct DDD remains `3/3`; distinctive unnamed replacement is `3/3`; ordinary replacement is `1/1`; corrected competing-model selection is `1/1`; committed pressure selection is `3/3`; comprehensive remains `1/1`; and E7 remains a required-subset pass with a broad-focused-read diagnostic. Ordinary disclosure is demonstrated repeatedly. Preserved direct run 2 demonstrates bounded focused access through the index and four of 38 sections; R5 stayed ordinary because the compact body resolved it. The comprehensive control reads the full source.
- Attribution: independent final review found no P1/P2/P3 issue. No answer-level solver invention is credited as Evans guidance. Exact domain types, cardinalities, examples, migration sequences, adapters, operations, and implementation structures remain fixture content, solver hypotheses, or neighboring-skill choices.
- Checkpoint verdict: `PASS` for the then-current retrofit matrix. Source and package fidelity remained independently accepted and the corrected targets in that snapshot were included. This historical checkpoint is superseded for current behavioral invocation by RM1b below, whose post-map runs miss required DDD inclusion in `2/2`.

## Inline Reference Map Evaluation

### RM1: Ordinary Evans-model control

- Contract version: 2
- Class: application and disclosure
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/direct-evans-pricing-brief.md`
- Fixture SHA-256: `5ec5dbf71bcf410bb48239216f6a5b7d65ae6e8c614df5e8874e4479da3141fb`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Evolve context-local language and explicit concepts from domain evidence using the compact Evans guidance.
- Neighbor ownership: Distilled owns whether to invest and Implementing DDD owns committed mechanics; this fixture explicitly asks for Evans-style discovery and evolution.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture reveals the required source lens and cannot be reused unchanged.
- Reference expectation: ordinary
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: exact mini-derived model discovery, language, context, and deeper-insight guidance; router-only change
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM1b; the frozen fixture, hash, and required set remain unchanged

### RM1b: Ordinary hidden-commitment replacement

- Contract version: 2
- Class: application and disclosure
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/ordinary-hidden-commitment-model-v2.md`
- Fixture SHA-256: `0a304b5234ca179431864cd372649c930afa0215a3002f3e41bef5faf791df85`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Use domain-expert language and scenarios to make two materially different allocation commitments explicit, then evolve implementation and tests incrementally from the model.
- Neighbor ownership: Distilled's investment gate is already settled and Implementing DDD mechanics are secondary; the central judgment is discovering and expressing the missing concept.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, and the ordinary tier premise were accepted.
- Reference expectation: ordinary
- Runs: `green-inline-map-1` and `green-inline-map-recheck-1`; both reported `ordinary` with no reference sections, but neither selected required `domain-driven-design`
- Package fidelity trace: exact mini-derived model-discovery, language, missing-concept, and incremental-refactoring guidance
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance; answers remained source-compatible but were produced from sibling skills
- Behavioral result: fail; required target inclusion missed in `2/2`, and repetition does not erase the original miss
- Diagnostics: first run selected Distilled plus Implementing DDD; recheck added Refactoring but still omitted the required model-discovery skill

### RM2: Focused hidden-concept control

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/focused-hidden-fulfillment-concept.md`
- Fixture SHA-256: `ccc4ce6be7528b8d7fae1b030cd2ab88c77242ac9030b4472468767f4274f70c`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Decide whether overloaded state reveals a missing domain concept and test the proposed deeper model against scenarios.
- Neighbor ownership: Distilled's investment gate is already settled and Implementing DDD mechanics are out of scope; deeper model discovery is the Evans lens.
- Ownership review: REJECTED - post-run contract audit on 2026-07-14 found ordinary developer disagreement rather than an explicit source-interpretation dispute; the earlier independent review had recorded `PASS` under the mistaken broader interpretation.
- Reference expectation: focused
- Compact-body gap: invalid as recorded; the fixture disputes the model decision but does not state competing source propositions.
- Intended index destinations: `Knowledge Crunching and Deep Models` and `Making Implicit Concepts Explicit`
- Runs: `green-inline-map-1`; selected `domain-driven-design` and compatible `domain-driven-design-distilled`; `focused`; target read `Making Implicit Concepts Explicit`
- Package fidelity trace: the named canonical full headings
- Attribution review: not counted because the focused contract was invalid, although the answer contained no unsupported book attribution
- Behavioral result: not counted
- Diagnostics: preserve the one-section focused run as invalid-contract evidence; separately named source-dispute replacement RM2b supersedes it

### RM2b: Focused missing-concept source-dispute replacement

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/focused-missing-concept-source-dispute-v2.md`
- Fixture SHA-256: `21165bfd547c70d9c6b913554d10e375a4b3b5bb6774d69c30b0fd15d30e4ec7`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Resolve the exact rename-versus-missing-concept source proposition using deeper-model explanatory gain and implicit-concept criteria, then test it against domain-language scenarios.
- Neighbor ownership: Distilled's investment gate is settled and Implementing DDD mechanics remain secondary; deeper model discovery is central.
- Ownership review: PASS - independent pre-dispatch review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14 accepted blindness, DDD ownership, the explicit source dispute, focused tier, and exact two-section destination.
- Reference expectation: focused
- Compact-body gap: none; the fixture explicitly disputes whether source guidance supports a rename or requires an explicit missing concept when that distinction increases explanatory power and removes procedural special cases.
- Intended index destinations: `Knowledge Crunching and Deep Models` and `Making Implicit Concepts Explicit`
- Runs: `green-inline-map-contract-fix-1`; selected only `domain-driven-design`; reported `focused`; read intended `Knowledge Crunching and Deep Models` and `Making Implicit Concepts Explicit` plus relevant `Ubiquitous Language` and `Refactoring Rules`
- Package fidelity trace: canonical full headings `Knowledge Crunching and Deep Models` and `Making Implicit Concepts Explicit` plus unchanged mini-derived deeper-model guidance
- Attribution review: PASS - independent final result review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` found no unsupported book attribution
- Behavioral result: pass
- Diagnostics: two intended sections plus two bounded relevant sections passed; separately named source-dispute replacement supersedes post-run-rejected RM2

### RM3: Comprehensive Evans control

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/comprehensive-multi-context-audit.md`
- Fixture SHA-256: `69e426c19b4508f2473ff1d4327e22433535989d3a34aa5ad5d38fedbea4855b`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Apply the complete Evans model-discovery, strategic, tactical, and deeper-insight lens.
- Neighbor ownership: Related DDD skills may co-apply, but the explicit complete Evans request owns this control.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture exposes the required source lens and cannot be reused unchanged.
- Reference expectation: comprehensive
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: all canonical full headings
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM3b; the frozen fixture, hash, and required set remain unchanged

### RM3b: Comprehensive domain-model replacement

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/domain-driven-design/comprehensive-domain-model-audit-v2.md`
- Fixture SHA-256: `c56478a3d5ea9b92b2d24b7d277d5110631e6b7aa5a25d4a74e5d269efda4c70`
- Required skills: `{domain-driven-design}`
- Distinctive judgment: Apply the complete model-discovery, language, context, strategic, tactical, translation, supple-design, testing, and deeper-insight lens end to end.
- Neighbor ownership: Distilled and Implementing DDD may contribute investment or mechanics, but the explicit exhaustive domain-model objective makes this discovery-and-evolution skill central.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, and end-to-end comprehensive loading were accepted.
- Reference expectation: comprehensive
- Runs: `green-inline-map-1`; selected `domain-driven-design`, both neighboring DDD skills, and `clean-architecture`; all consulted references reported `sections=["*"]`, including the required target
- Package fidelity trace: all canonical full headings
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: permitted compatible overlap; required target inclusion and end-to-end access passed
