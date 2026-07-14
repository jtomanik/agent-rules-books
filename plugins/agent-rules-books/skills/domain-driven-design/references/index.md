# Domain-Driven Design Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit disputed interpretation, demonstrated model hotspot, or one bounded source question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a complete Evans-style DDD audit or a decision spanning several independent concern families, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-17` | Decide whether business complexity calls for a precise domain model, shared language, explicit contexts, rich behavior, invariant protection, and infrastructure separation. |
| [Primary Directive](full.md#primary-directive) | `19-34` | Arbitrate a concrete choice between domain-model clarity and generic reuse, CRUD, persistence, delivery, framework, or short-term convenience. |
| [What DDD Means in This Repository](full.md#what-ddd-means-in-this-repository) | `36-56` | Distinguish model-driven design from DDD ceremony, passive entities, pattern saturation, or over-modeling a simple subdomain. |
| [Knowledge Crunching and Deep Models](full.md#knowledge-crunching-and-deep-models) | `58-79` | Awkward code, contradictory language, vague fields, or repeated conditionals suggest missing distinctions and require expert conversation and deeper modeling. |
| [Model-Driven Design](full.md#model-driven-design) | `81-101` | Resolve divergence between the model used in discussion and the names, behavior, tests, interfaces, or implementation that must express it. |
| [Breakthrough and Deeper Insight](full.md#breakthrough-and-deeper-insight) | `103-122` | Evaluate a breakthrough model by explanatory power, future rule expression, migration cost, and safe incremental behavior preservation. |
| [Making Implicit Concepts Explicit](full.md#making-implicit-concepts-explicit) | `124-142` | Hidden constraints, policies, or processes remain buried in flags, comments, branches, awkward APIs, regulations, or domain references. |
| [Ubiquitous Language](full.md#ubiquitous-language) | `144-165` | Names, tests, modules, and expert language use synonyms, vague technical terms, or one term for different concepts inside a context. |
| [Communication Artifacts](full.md#communication-artifacts) | `167-185` | Decide how examples, tests, glossaries, diagrams, and short documents should reinforce boundaries, invariants, lifecycle, and current domain language. |
| [Scenario Walkthroughs](full.md#scenario-walkthroughs) | `187-205` | A real business scenario exposes awkward collaboration, creation, lifecycle, translation, Aggregate, Module, or premature persistence optimization choices. |
| [Layered Architecture and Smart UI](full.md#layered-architecture-and-smart-ui) | `207-221` | Decide whether complexity warrants separated presentation, application, domain, and infrastructure concerns or whether a simple Smart UI is sufficient. |
| [Bounded Contexts](full.md#bounded-contexts) | `223-243` | A model or term crosses team or system ownership, a shared domain package is proposed, or local meaning needs explicit translation and context ownership. |
| [Strategic Design](full.md#strategic-design) | `245-267` | Allocate modeling investment among Core, supporting, and generic subdomains or make integration influence and translation ownership visible. |
| [Model Integrity Patterns](full.md#model-integrity-patterns) | `269-303` | Choose or evolve Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Separate Ways, Open Host Service, or Published Language relationships. |
| [Distillation](full.md#distillation) | `305-332` | Expose and protect strategic advantage using a vision, highlighted or segregated core, generic subdomain, cohesive mechanism, or abstract core. |
| [Large-Scale Structure](full.md#large-scale-structure) | `334-361` | A cross-context structure, metaphor, responsibility layering, knowledge level, component framework, or evolving order must reduce rather than freeze understanding. |
| [Strategic Decision Making](full.md#strategic-decision-making) | `363-384` | Establish ownership, implementation feedback, revisability, and team coordination for context maps, Core Domain, or large-scale structural choices. |
| [Entities](full.md#entities) | `386-412` | Identity, lifecycle, continuity, valid transitions, or intention-revealing behavior determines whether a concept is an Entity rather than a passive record. |
| [Value Objects](full.md#value-objects) | `414-441` | A meaningful attribute-defined concept needs immutability, valid construction, value equality, concept-owned validation, or replacement of raw primitives. |
| [Associations and Modules](full.md#associations-and-modules) | `443-468` | Object navigation obscures Aggregate boundaries or package structure fails to express conceptual cohesion and Bounded Context ownership. |
| [Aggregates](full.md#aggregates) | `470-494` | Define the smallest immediate-consistency boundary, root-only invariant changes, cross-Aggregate identity references, and transaction scope. |
| [Domain Services](full.md#domain-services) | `496-518` | A domain-significant operation has no natural Entity or Value Object home, or a technical helper or god service is being mislabeled as domain behavior. |
| [Explicit Concepts and Specifications](full.md#explicit-concepts-and-specifications) | `520-540` | Repeated conditions, named policies, constraints, or business processes need explicit concepts or composable Specifications distinct from persistence queries. |
| [Repositories](full.md#repositories) | `542-570` | Design Aggregate-root persistence, domain- or application-owned interfaces, intent-revealing queries, reconstitution, or protection from database-shaped contracts. |
| [Factories](full.md#factories) | `572-591` | Choose between direct construction and a Factory for complex or domain-significant valid creation, including separate storage reconstitution. |
| [Application Layer](full.md#application-layer) | `593-615` | Application services are taking domain decisions instead of coordinating Aggregate loading, behavior, persistence, transactions, and side effects. |
| [Infrastructure](full.md#infrastructure) | `617-631` | ORM, transport, messaging, cache, framework, or delivery constraints are shaping domain names, types, methods, or boundaries. |
| [Translation at Boundaries](full.md#translation-at-boundaries) | `633-651` | External IDs, statuses, schemas, transport forms, persistence records, or vendor language risk leaking into the local model. |
| [Supple Design](full.md#supple-design) | `653-679` | Refine intention-revealing interfaces, side-effect-free calculations, command-query separation, explicit assertions, conceptual contours, or readable declarative rules. |
| [Analysis and Model Patterns](full.md#analysis-and-model-patterns) | `681-706` | Evaluate industry formalisms, prior models, Strategy, Policy, Composite, or exploration work without overriding local language and implementation evidence. |
| [Code Generation Rules](full.md#code-generation-rules) | `708-757` | Translate settled context, language, tactical type, invariant, persistence, translation, implicit-concept, and strategic choices into generated code. |
| [Review Rules](full.md#review-rules) | `759-804` | Run a focused review for language, model, boundary, Aggregate, service, infrastructure, or strategic modeling problems. |
| [Testing Rules](full.md#testing-rules) | `806-834` | Design domain-language tests for invariants, transitions, valid construction, Specifications, orchestration, and context or Anticorruption Layer translation. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `836-885` | Classify passive models, Smart UI misuse, persistence-driven design, primitive obsession, shared-model sprawl, god services, invalid construction, fake DDD, or context-map blindness. |
| [Refactoring Rules](full.md#refactoring-rules) | `887-906` | Recover language, behavior, concepts, Aggregate or context boundaries, translation, and Core Domain clarity while preserving behavior incrementally. |
| [Output Expectations](full.md#output-expectations) | `908-941` | Determine the expected DDD content of an implementation, code review, or modification response. |
| [Review Checklist](full.md#review-checklist) | `943-968` | Run the canonical final scan over contexts, language, explicit concepts, tactical patterns, boundaries, translation, Core Domain, structure, and over-modeling. |
| [Final Instruction](full.md#final-instruction) | `970-979` | Arbitrate a final choice by sharper domain language, protected invariants, explicit contexts, meaningful types, and infrastructure subordination. |
