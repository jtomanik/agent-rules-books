---
name: domain-driven-design
description: Evans-style Domain-Driven Design guidance for discovering and evolving an implementation-driving domain model. Use when business complexity makes Ubiquitous Language conflicts, missing domain concepts, lifecycle rules, Bounded Context or Context Map decisions, Core Domain focus, or deeper-model pressure from awkward procedural behavior central. DDD Distilled owns the smallest-investment/selectivity gate; Implementing DDD owns post-boundary implementation mechanics.
---

# Domain-Driven Design

## Primary Bias

Keep domain behavior, code, tests, documents, and team language aligned inside explicit Bounded Contexts. Do not let persistence, UI, frameworks, integration formats, or DDD vocabulary replace an implementation-driving model.

## Model Discovery, Language, and Deeper Insight

- Use a model only when it organizes domain knowledge, clarifies communication, and can be expressed in implementation; iterate through code, expert conversation, scenarios, and refactoring toward deeper insight.
- Refactor toward deeper domain insight, not only mechanical cleanliness. Compare explanatory gain with migration cost; preserve behavior and move in safe incremental steps, never a big-bang rewrite when incremental migration is possible. Make constraints, policies, processes, calculations, and allocation rules explicit when they carry domain meaning.
- When new behavior is hard to explain, test, or extend, search for a deeper model, missing implicit concept, or breakthrough refactoring instead of adding procedural branches.
- Maintain one Ubiquitous Language per Bounded Context across names, tests, documents, diagrams, planning, and feature discussion; keep explanatory models separate from the implementation model.
- When terminology is awkward, ambiguous, or inconsistent inside one Bounded Context, refine the Ubiquitous Language and rename code; preserve legitimate differences between contexts through explicit translation rather than forcing one shared language.
- Use analysis patterns, design patterns, specifications, industry formalisms, and prior art only when they clarify the current model and preserve domain language.

## Model-Driven Implementation

- Before writing domain code, identify in order the Bounded Context, domain term, tactical type, and invariants. Then design the model first and persistence second; preserve identity, Aggregate boundaries, Value Object semantics, and domain query criteria instead of exposing database structure. Start from delivery, persistence, schema, or REST shape only for a purely infrastructural task.
- When the domain is complex enough to need model-driven design, put business rules in the domain layer and keep UI, application coordination, infrastructure, persistence, messaging, and framework constraints outside the model or behind adapters; use Smart UI only for simple applications where rich domain abstraction, reuse, integration, and deep business rules are unimportant.
- When a domain is complex enough for model-driven design and controllers, services, scripts, SQL, jobs, or serializers carry business decisions, move rules into domain objects, Domain Services, Specifications, or explicit domain concepts.
- Use tactical patterns only for model meaning: Entities when identity, lifecycle, or continuity matters; Value Objects for meaningful concepts defined by attributes, immutable by default, valid at construction, equal by value, whose concept validation should live inside the Value Object and whose validation and side-effect-free operations must stay near the value itself; Domain Services for domain-significant operations with no natural Entity or Value Object home; Modules for conceptual cohesion and Bounded Context ownership.
- Use Aggregates as small immediate-consistency boundaries around invariants: route every invariant-affecting modification through the root, reference other Aggregates by identity unless stronger consistency is required, and align transactions with invariants. Use Factories for complex or domain-significant creation; use a direct constructor when creation is simple, intention-revealing, and exposes no complex invariants. Use Repositories only for Aggregate roots; do not let invalid or partially formed objects escape supported creation paths.
- When clients perform complex creation, persistence mapping, reconstitution, or arbitrary internal mutation, repair Factories, Repositories, Aggregate roots, and encapsulation.
- Design for model users: name operations by domain purpose, prefer side-effect-free functions for calculations and queries, separate commands from queries when side effects would surprise readers, make assertions explicit, and shape boundaries around conceptual contours.

## Bounded Contexts and Integration

- Identify a Bounded Context explicitly for every substantial domain area. Do not assume a term has the same meaning elsewhere; use context maps, tests, and active communication to protect model integrity.
- Choose context relationships by their conditions: Shared Kernel only for a small jointly governed subset; Customer/Supplier when upstream commits to downstream needs; Conformist only when adopting upstream is cheaper than translating; Anticorruption Layer when real translation protects the local model from foreign or legacy models; Separate Ways when integration costs more than shared capability is worth; Open Host Service for a stable integration protocol; Published Language for a documented exchange language. Replace legacy responsibilities incrementally through translations.
- When integrating models, choose an explicit context relationship and translation strategy; add a stable protocol or documented exchange language only when the chosen relationship calls for it. Test context boundaries, and where an Anticorruption Layer exists, test its translation.
- When UI, persistence, messaging, APIs, or frameworks shape concepts in a model-driven domain, isolate technical representations behind appropriate layers, adapters, or explicit mappings; use an Anticorruption Layer only when real translation protects the local model from a foreign or legacy model.
- When a change crosses unrelated modules, many objects, or multiple roots, reassess Module cohesion, Aggregate ownership, consistency timing, and context boundaries.

## Core Domain and Strategic Structure

- Distill and protect the Core Domain by strategic value. Keep generic subdomains, infrastructure, reusable mechanisms, and supporting details from consuming core-domain attention.
- When generic mechanisms, reusable frameworks, or supporting subdomains obscure distinctive value, distill the Core Domain or separate the mechanism.
- Add large-scale structure only when it reduces cognitive load across contexts; keep it domain-specific, evolvable, minimally restrictive, and subordinate to each Bounded Context's model.
- Make major strategic moves with people who understand both the implementation and the domain; architecture and framework guidance must serve application teams and domain goals.

## Model Tests

- Test the model in the Ubiquitous Language: prioritize domain tests for invariants, allowed and forbidden transitions, valid construction, specifications, application orchestration, and boundary translation before generic infrastructure checks.
- When changing invariants, lifecycle transitions, specifications, orchestration, or context translation, add domain-language tests that prove valid behavior and block invalid states.

## Reference Map

Use this file alone when it resolves the ordinary modeling question; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Awkward models or missing distinctions: [Knowledge Crunching and Deep Models](references/full.md#knowledge-crunching-and-deep-models)
- Hidden policies or concepts: [Making Implicit Concepts Explicit](references/full.md#making-implicit-concepts-explicit)
- Context-specific terminology: [Ubiquitous Language](references/full.md#ubiquitous-language)
- Model ownership boundaries: [Bounded Contexts](references/full.md#bounded-contexts)
- Context relationship patterns: [Model Integrity Patterns](references/full.md#model-integrity-patterns)
- Consistency and invariant boundaries: [Aggregates](references/full.md#aggregates)
- External-model isolation: [Translation at Boundaries](references/full.md#translation-at-boundaries)
- Incremental deeper-model recovery: [Refactoring Rules](references/full.md#refactoring-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For an explicit comprehensive DDD audit or complete Evans lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Where complexity warrants model-driven design, is domain behavior explicit in the model rather than hidden in delivery, persistence, or integration code?
- Do code, tests, documents, and conversations use one language inside each Bounded Context?
- Where tactical patterns are used, do they protect identity, value semantics, lifecycle, invariants, and responsibility instead of adding ceremony?
- Does every cross-context integration have an explicit relationship and translation strategy, with boundary tests?
- Do tests read like executable examples of the model and cover invalid transitions or construction?
- Is the Core Domain visible and protected from supporting complexity, generic mechanisms, infrastructure, and frameworks?
