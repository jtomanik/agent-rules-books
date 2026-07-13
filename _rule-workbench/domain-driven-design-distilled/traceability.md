# OBEY Domain-Driven Design Distilled by Vaughn Vernon

Canonical full source: [full.md](full.md)

## Compression decisions

- Repaired after complete mini/nano-to-full reverse tracing on 2026-07-13.
- These were book-specific misses: the existing process already requires exact activation scope, source-supported modalities and defaults, reverse tracing of every retained detail, and honest dispositions for merged or omitted rules.
- The source uses explicit default modality, including smaller Aggregate boundaries and eventual consistency across Aggregates. These remain active because they are not verified agent defaults eligible for omission under the process; known failures around fake DDD, framework-first design, unclear contexts, primitive obsession, service-centric models, overgrown Aggregates, and integration leakage justify retaining operational rules that may look human-obvious.
- Both activation statements now use the source threshold exactly: domain complexity, language ambiguity, business differentiation, or integration risk must justify the modeling effort.
- `mini.md` preserves the conditional strategic sequence separately from the default code-generation order. Both sequences are intentionally lost from nano, where the higher-salience selective-investment and boundary rules remain.
- Bounded Context ownership is limited to language, rules, and model semantics. Code reflects context boundaries; integration contracts are owned deliberately; domain tests use the local Ubiquitous Language. Tests and integration contracts are not assigned to context ownership.
- All nine context relationship patterns and their applicability conditions are retained in `M6`. Nano retains only Conformist's cheaper-and-safer adoption condition in `N14`; the other eight named patterns and their pattern-specific conditions are intentionally lost. Shared Kernel joint ownership and tests remain specific to that relationship, not a general split or translation criterion.
- Foreign-model translation applies where meanings differ, while Conformist adoption remains valid when adopting the upstream model is cheaper and safer than translation. Both are distinct from isolating screen/UI, framework, REST/transport, and persistence/database shapes. `UI` and `database` are plain-language labels entailed by the source's screen and persistence mechanics; unsupported API and permissions examples were removed.
- The former audited nano accelerated-modeling item is intentionally omitted: Event Storming or similar collaborative modeling, scenario and acceptance-test validation, modeling spikes, domain-expert involvement, timeboxing, and modeling-debt tracking retain their separate source purposes in `M17` and are all intentionally lost from nano.
- The former generic delivery-pressure trigger was removed as unsupported. The former final release gate requiring a bundle of modeling artifacts before shipping was removed; the replacement checklist only restates model validation, timeboxing, and conditional debt tracking.
- `M1` through `M18` remain stable. New `M19` preserves the separate code-generation default, former triggers `M19` through `M28` become `M20` through `M29`, and the unsupported former `M29` delivery-pressure trigger has no replacement.
- Re-audit repaired `M21`, `M26`, and `M27` so their conditions no longer share over-broad consequences: model reassessment is common but strategic scope review is conditional; multi-Aggregate transactions differ from whole-graph requests; duplicated controller orchestration differs from misplaced business decisions.
- Nano was manually reprioritized from 17 rules to eight high-salience bullets carrying 14 retained mechanisms. Surviving audited IDs `N2`-`N4`, `N6`-`N10`, and `N12`-`N17` remain stable and map individual clauses inside merged bullets; omitted `N1`, `N5`, and `N11` are not reused. The full strategic sequence, the other eight named relationship patterns, detailed integration styles, detailed testing, and accelerated-modeling rules are intentionally lost rather than compressed into weakened summaries.

## Activation and primary bias

- Mini activation: modeling effort is justified by domain complexity, language ambiguity, business differentiation, or integration risk. Source: `Adoption Fit and Modeling Investment` (38-45).
- Nano activation: the same technical threshold; `Use as compact DDD guidance` is packaging context only. Source: `Adoption Fit and Modeling Investment` (38-45).
- Mini primary bias: use DDD where it clarifies complex business software, avoid ritual, and use the smallest effective set that models business meaning while delivering results. Source: `Purpose` (3-16), `Primary Directive` (20-35).
- Nano primary bias: selective, serious DDD for real complexity with the smallest effective practices, not ritual. Source: `Purpose` (3-16), `Primary Directive` (20-35), `Final Instruction` (308-317).

## Mini mapping

Decision rules:

- `M1` Preserve the source's when-uncertain strategic sequence: capability or subdomain, subdomain class, Bounded Context, local Ubiquitous Language, then only tactical patterns that earn their cost. Source: `Primary Directive` (20-35).
- `M2` Put the most design effort into the Core Domain, keep Supporting and Generic Subdomains simpler unless complexity proves otherwise, and let business drivers allocate modeling effort. Source: `Adoption Fit and Modeling Investment` (38-45), `Start with Subdomains` (50-60).
- `M3` Avoid full tactical DDD for simple CRUD, Generic Subdomains, and mainly technical problems; permit simple services and data structures, strengthen the model as invariants, lifecycle, and language complexity rise, and improve incrementally rather than through massive overhaul. Source: `Adoption Fit and Modeling Investment` (38-45), `Practicality Rules` (219-230).
- `M4` Put every meaningful model in a Bounded Context that owns its language, rules, and model semantics, with code structure reflecting the boundary. Source: `Define Bounded Contexts Early` (61-66).
- `M5` Treat the same term across contexts as potentially different, translate where meanings differ, and reject shared classes or imported foreign language with divergent meaning. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Ubiquitous Language Rules` (112-124).
- `M6` Retain every context relationship applicability condition: Partnership, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open Host Service, Published Language, Separate Ways, and Big Ball of Mud containment. Source: `Context Relationship Rules` (80-99).
- `M7` Retain RPC coupling, latency, versioning, and failure conditions; REST representation boundaries; messaging fit, lag, duplicate, and ordering conditions; and the Domain Event payload-versus-query-back choice. Source: `Integration Style Rules` (101-109).
- `M8` Own integration contracts deliberately, keep them separate from internal models, and test translations at context boundaries. Source: `Use Context Mapping` (67-77), `Integration Style Rules` (101-109).
- `M9` Use current-context terms consistently in code, tests, Commands, Domain Events, and conversations; preserve one term per concept, rename with improved understanding, and make domain tests read in the Ubiquitous Language. Source: `Ubiquitous Language Rules` (112-124), `Testing Rules` (281-288).
- `M10` Use Entities when identity and lifecycle matter; preserve mandatory explicit identity and protected transitions, the default against unrestricted state changes, and valid/invalid transition tests. Source: `Entities` (129-136), `Testing Rules` (281-288).
- `M11` Use Value Objects aggressively when primitives hide meaning; preserve immutability as a default, self-validation, domain-language readability, and validation/behavior tests. Source: `Value Objects` (137-144), `Testing Rules` (281-288).
- `M12` Use Aggregates only where invariants require a consistency boundary; keep them small, root-protected, free of directly exposed mutable children, identity-referenced, and graph-limited; default to eventual consistency across Aggregates and usually one Aggregate per transaction; test valid and invalid transitions. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174), `Testing Rules` (281-288).
- `M13` Use Domain Events for meaningful past-tense facts that clarify collaboration or integration, not trivial field-change noise. Source: `Domain Events` (154-160).
- `M14` Keep Application Services in use-case orchestration, thin enough for the model to carry meaning, and test them for orchestration rather than all domain rules. Source: `Application Service Rules` (177-188), `Testing Rules` (281-288).
- `M15` Keep framework, persistence, REST, transport, and other technology concerns out of the domain model; prevent persistence from defining Aggregates and translate transport and integration data at the boundary. Source: `Architecture and Infrastructure Rules` (191-202).
- `M16` Make code teach the model through business terms and explicit assumptions; expose richer concepts instead of unexplained statuses, flags, enums, booleans, or generic helpers/utilities carrying domain decisions. Source: `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216).
- `M17` Preserve each accelerated-modeling purpose separately: Event Storming for unclear workflow/events/Commands/policies/team language; scenarios and acceptance tests for real-business-behavior validation; spikes for model-shape uncertainty; debt tracking for known imperfect code/language intentionally deferred; expert involvement in walkthroughs, terminology, and acceptance criteria; and timeboxing to serve implementation. Source: `Adoption Fit and Modeling Investment` (38-45), `Accelerated Modeling and Project Rules` (233-242).
- `M18` Estimate DDD work from modeling uncertainty, integration risk, and implementation cost, and treat team skill and expert access as constraints on sustainable ceremony. Source: `Accelerated Modeling and Project Rules` (233-242).
- `M19` Preserve the separate default code-generation order from subdomain and context through local language, tactical concept choice, smallest fitting pattern, infrastructure isolation, and explicit context translation. Source: `Code Generation Rules` (245-260).

Trigger rules:

- `M20` Fuzzy, generic, overloaded, or imported language triggers local Ubiquitous Language refinement and foreign-term translation. Source: `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216).
- `M21` Core-business drift, code-language mismatch, or Supporting complexity hiding the Core Domain always triggers model reassessment; subdomain classification, Bounded Context boundaries, and modeling investment are revisited only when the affected scope calls them into question. Source: `Adoption Fit and Modeling Investment` (38-45).
- `M22` One model spreading across billing, identity, catalog, fulfillment, and support triggers splitting or translation instead of shared domain classes. Source: `Use Context Mapping` (67-77), `Review Rules` (264-278).
- `M23` A foreign model defining local language triggers translation; a screen/UI, framework, REST/transport representation, or persistence/database shape defining the domain triggers technology isolation. `UI` is entailed by the source's screen-shaped Aggregate anti-pattern; `database` is entailed by persistence-first modeling and persistence defining the model. Source: `Use Context Mapping` (67-77), `Aggregate Minimalism Rules` (162-174), `Architecture and Infrastructure Rules` (191-202).
- `M24` Shared Kernel requires a small stable overlap, joint ownership, tests, and governance. Source: `Context Relationship Rules` (80-99).
- `M25` A claimed Anticorruption Layer requires actual translation. Source: `Context Relationship Rules` (80-99).
- `M26` A transaction changing several Aggregate roots triggers consistency-boundary review, the usual one-Aggregate-per-transaction consequence, and eventual consistency across Aggregates as the default. Separately, a request loading and mutating a whole graph triggers rejection of navigation-shaped boundaries and restoration of smaller identity-referenced Aggregates. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174).
- `M27` Duplicated controller orchestration triggers restoration of Application Service coordination. Separately, helpers, services, or transport-shaped Application Services carrying business decisions trigger moving those decisions into the domain model or naming the missing concept. Source: `Application Service Rules` (177-188), `Collaboration Rules` (205-216), `Review Rules` (264-278).
- `M28` Vague, command-like, trivial, or field-change Domain Events trigger redesign as meaningful past-tense facts or removal; command-like is the clearly entailed opposite of the source's completed past-tense fact. Source: `Domain Events` (154-160), `Review Rules` (264-278).
- `M29` Primitives, flags, status codes, enums, or booleans carrying domain rules trigger a richer concept or Value Object. Source: `Value Objects` (137-144), `Collaboration Rules` (205-216), `Review Rules` (264-278).

Final checklist:

- Subdomain and Core Domain investment restates `M2` and `M3`.
- Explicit context and condition-specific neighboring relationship restates `M4` and `M6`.
- Local language in code and tests restates `M9`.
- Deliberate contract ownership and translation tests restates `M5` and `M8`.
- Tactical patterns earning their cost and genuinely helping restates `M1`, `M3`, and the source `Review Checklist` (291-304).
- Entity/Value Object modalities and tests restates `M10` and `M11`.
- Aggregate shape and eventual-consistency default restates `M12` and `M26`.
- Application Service orchestration and testing restates `M14` and `M27`.
- Technology isolation restates `M15` and `M23`.
- Model validation, timeboxing, and conditional debt tracking restates `M17`; it does not require every modeling artifact before release.

## Nano mapping

Decision rules:

- `N2` Focus design effort on the Core Domain and keep Supporting and Generic work simpler unless complexity proves otherwise. Do not apply full tactical DDD to simple CRUD, Generic Subdomains, or mainly technical problems. Strengthen incrementally as invariants, lifecycle, or language complexity rise, and require tactical patterns to earn their cost. Source: `Adoption Fit and Modeling Investment` (38-45), `Start with Subdomains` (50-60), `Practicality Rules` (219-230).
- `N3` Put every meaningful model in an explicit Bounded Context that owns language, rules, and model semantics, with code reflecting the boundary. Source: `Define Bounded Contexts Early` (61-66).
- `N4` Use local terms, translate where meanings differ, and reject shared domain classes with divergent meanings. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Ubiquitous Language Rules` (112-124).
- `N6` Translate transport and integration data at boundaries and keep integration contracts separate from internal models. Source: `Integration Style Rules` (101-109), `Architecture and Infrastructure Rules` (191-202).
- `N7` Preserve exact Entity and Value Object applicability, mandatory Entity identity and protected transitions, the default against exposing unrestricted Entity changes, aggressive Value Object use, default immutability, self-validation, and domain-language readability. Source: `Entities` (129-136), `Value Objects` (137-144).
- `N8` Preserve invariant-driven Aggregate applicability, mandatory small root-protected boundaries and identity references, and the explicit defaults to smaller boundaries and eventual consistency across Aggregates. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174).
- `N9` Keep business decisions in the domain model. Application Services coordinate use cases and must not be shaped only by transport or become the real domain model. Source: `Application Service Rules` (177-188).
- `N10` Keep technology concerns out of the domain model. Source: `Architecture and Infrastructure Rules` (191-202).

Trigger rules:

- `N12` Fuzzy, overloaded, or imported language triggers local refinement or foreign-language translation. Source: `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216).
- `N13` One model absorbing unrelated concerns triggers subdomain and Bounded Context boundary review and the prohibition on reusing one model across distinct business concerns; translation is conditioned only on meanings differing, not on ownership differences. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Review Rules` (264-278).
- `N14` Foreign models are translated where meanings differ unless Conformist adoption of the upstream model is cheaper and safer than translation; screen/UI, framework, REST/transport, or persistence/database shape driving the domain model instead triggers technology isolation. Source: `Use Context Mapping` (67-77), `Context Relationship Rules` (80-99), `Aggregate Minimalism Rules` (162-174), `Architecture and Infrastructure Rules` (191-202).
- `N15` A transaction changing several Aggregates triggers consistency-boundary review, the usual one-Aggregate consequence, and eventual consistency across Aggregates as the default. Separately, a request loading and mutating a whole graph triggers restoration of smaller identity-referenced Aggregates. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174).
- `N16` Helpers or services carrying business decisions trigger moving them into the model or naming the missing concept. Duplicated controller orchestration and its distinct Application Service remedy are intentionally lost from nano. Source: `Ubiquitous Language Rules` (112-124), `Application Service Rules` (177-188), `Collaboration Rules` (205-216).
- `N17` Vague, command-like, trivial, or noisy field-change Domain Events trigger redesign as meaningful past-tense facts or removal. Source: `Domain Events` (154-160).

Final checklist:

- Justified DDD investment, Core Domain focus, and tactical cost restate the activation rule and `N2`.
- Explicit context, local language, and conditionally warranted boundary changes restate `N3`, `N4`, `N12`, and `N13`.
- Entity/Value Object modalities and Aggregate boundaries/defaults restate `N7`, `N8`, and `N15`.
- Meaning-conditioned foreign-model translation, condition-specific Conformist adoption, technology isolation, and contract separation restate `N6`, `N10`, and `N14`.
- Domain decisions, Application Service coordination, and meaningful Domain Events restate `N9`, `N16`, and `N17`.

## Section coverage review

- `Purpose` (3-16): covered by `M1`, `M2`, `M3`, `M4`, `M9`, `M15`, `M17`, `N2`, `N3`, `N4`, `N9`, and `N10`, plus both primary-bias statements. The standalone binding-policy declaration is intentionally lost; rule-specific modalities are retained where applicable.
- `Primary Directive` (20-35): covered by mini primary bias, `M1`, `M3`, and `N2`. The full when-uncertain sequence is intentionally lost from nano.
- `Adoption Fit and Modeling Investment` (38-45): covered by both activation statements, `M2`, `M3`, `M17`, `M21`, and `N2`. Scenario and acceptance-test validation is intentionally lost from nano and remains covered by `M17`.
- `Strategic Rules / Start with Subdomains` (48-60): covered by `M1`, `M2`, `M19`, and `N2`.
- `Strategic Rules / Define Bounded Contexts Early` (61-66): covered by `M4`, `M5`, `N3`, and `N4`; tests and integration contracts are not attributed to context ownership.
- `Strategic Rules / Use Context Mapping` (67-77): covered by `M5`, `M6`, `M8`, `M22`, `M23`, `M25`, `N4`, `N6`, `N13`, and `N14`.
- `Context Relationship Rules` (80-99): every pattern condition is covered by `M6`; Shared Kernel and Anticorruption Layer safeguards are repeated as `M24` and `M25`. Nano retains Conformist's cheaper-and-safer adoption condition in `N14`; the other eight named patterns and their conditions are intentionally lost from nano.
- `Integration Style Rules` (101-109): every integration-style rule is covered by `M7` and `M8`. Nano keeps only boundary data translation and contract separation in `N6`; RPC/REST/messaging conditions, Domain Event payload versus query-back, and translation testing are intentionally lost from nano.
- `Ubiquitous Language Rules` (112-124): covered by `M5`, `M9`, `M16`, `M20`, `N4`, and `N12`.
- `Tactical Pattern Rules / Entities` (129-136): every modality and default is covered by `M10` and `N7`. Entity transition testing is intentionally lost from nano.
- `Tactical Pattern Rules / Value Objects` (137-144): every modality and default is covered by `M11` and `N7`; the broader flag/status/enum/boolean trigger remains in `M29` and is intentionally lost from nano. Value Object testing is intentionally lost from nano.
- `Tactical Pattern Rules / Aggregates` (145-153): covered by `M12`, `M26`, `N8`, and `N15`.
- `Tactical Pattern Rules / Domain Events` (154-160): covered by `M13`, `M28`, and `N17`. Nano retains the high-risk misuse trigger; the positive collaboration/integration applicability rule is intentionally lost from nano.
- `Aggregate Minimalism Rules` (162-174): covered by `M12`, `M23`, `M26`, `N8`, `N14`, and `N15`; one-transaction and one-request conditions have separate consequences, while smaller boundaries and eventual consistency across Aggregates remain explicit defaults.
- `Application Service Rules` (177-188): covered by `M14`, `M27`, `N9`, and `N16`. Duplicated controller orchestration and its Application Service remedy are intentionally lost from nano; misplaced business decisions remain covered by `N16`.
- `Architecture and Infrastructure Rules` (191-202): covered by `M15`, `M23`, `N6`, `N10`, and `N14`; technology isolation is not mislabeled as foreign-model translation.
- `Collaboration Rules` (205-216): covered by `M9`, `M16`, `M20`, `M27`, `M29`, `N4`, `N12`, and `N16`.
- `Practicality Rules` (219-230): every rule and anti-pattern is covered by `M1`, `M2`, `M3`, and `N2`; incremental improvement and the tactical-pattern cost condition are explicit.
- `Accelerated Modeling and Project Rules` (233-242): Event Storming or similar collaborative modeling, scenario/acceptance-test validation, modeling spikes, domain-expert involvement, timeboxing, modeling-debt tracking, estimation, and team constraints are covered by `M17` and `M18` and intentionally lost from nano.
- `Code Generation Rules` (245-260): the complete default order is covered by `M19` and intentionally lost from nano. Nano keeps only high-risk avoidance effects through `N2`, `N3`, `N4`, `N9`, `N10`, and `N16`.
- `Review Rules` (264-278): covered by `M2`, `M3`, `M4`, `M5`, `M10`, `M11`, `M12`, `M14`, `M22`, `M23`, `M25`, `M27`, `M29`, `N2`, `N3`, `N4`, `N7`, `N8`, `N9`, `N13`, `N14`, `N15`, and `N16`; the long list is merged into decisions, triggers, and checklists without importing permissions or APIs.
- `Testing Rules` (281-288): local-language tests are covered by `M9`; Value Object validation/behavior by `M11`; Entity/Aggregate valid and invalid transitions by `M10` and `M12`; Application Service orchestration by `M14`; context translation by `M8`. Every detailed testing rule is intentionally lost from nano.
- `Review Checklist` (291-304): covered by `M1`, `M2`, `M3`, `M4`, `M9`, `M11`, `M12`, `M14`, `M15`, `N2`, `N3`, `N4`, `N7`, `N8`, `N9`, `N10`, and both final checklists. The source's revise-before-shipping instruction applies to its own checklist and does not support a new all-artifacts release gate.
- `Final Instruction` (308-317): covered by both primary-bias statements, `M1`, `M3`, `M4`, `M9`, `M15`, `N2`, `N3`, `N4`, `N9`, and `N10`.
