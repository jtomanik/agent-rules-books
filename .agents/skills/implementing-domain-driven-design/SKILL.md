---
name: implementing-domain-driven-design
description: Implementing Domain-Driven Design guidance for implementation-level DDD after context and model commitment. Use when Aggregate boundaries, Value Objects/Entities, Repositories, Domain or Application Services, Domain Events, modules, translations, projections, or renamed-CRUD/anemic-model correction is central. Distilled owns the DDD investment gate; Domain-Driven Design owns strategic discovery and deeper model development; DDIA co-applies only for central distributed-data semantics.
---

# Implementing Domain-Driven Design

## Primary Bias

Practical DDD is not renamed CRUD. Model the operational domain inside an explicit Bounded Context, with local language, small invariant boundaries, identity references across Aggregates, and explicit translation across context and infrastructure boundaries.

## Context, Language, and Translation

- Name the Bounded Context before interpreting terms, modules, services, repositories, events, APIs, persistence, or integrations; never force one global company model.
- Use the local Ubiquitous Language consistently: one concept gets one term inside the context, one term must not carry multiple meanings, code, tests, events, commands, repositories, services, and packages must speak that language, and code must be renamed when understanding improves.
- Make every context interaction explicit: show the relationship, translation responsibility, and upstream/downstream influence; do not let external, partner, or legacy models define the local model, and do not share model classes across contexts by default.
- Use an Anticorruption Layer when integrating with legacy systems or foreign models: translate their language into the local context's language, keep foreign schemas and statuses out of local domain objects, and own the translation explicitly.
- When one term carries multiple meanings inside a context, changes meaning across contexts, or remains a technical placeholder despite a real domain term, use the context-local business term and rename code when understanding improves.
- When code wants to import another context's domain package, share an enum across contexts with different semantics, or couple through another context's database, replace the coupling with explicit identifiers, integration messages, and separate contract models.
- When a legacy system or foreign model would define local domain code, add an Anticorruption Layer. When API, transport, persistence, infrastructure, or client shape pressures the domain model, use an application-facing representation or technical mapping boundary instead.

## Aggregate Boundaries and Tactical Model

- Treat Aggregates as immediate consistency boundaries: keep them small, expose only the root outside the Aggregate, route invariant-changing operations through the root, prevent external mutation of internal members, and expose intention-revealing behavior instead of arbitrary setters.
- Reference other Aggregates by identity, avoid loading large connected graphs by default, and modify one Aggregate per transaction unless there is a compelling reason not to; use events, policies, or process coordination when consistency can be eventual.
- Use Entities where identity and lifecycle matter; make their methods protect meaningful state transitions and express domain behavior rather than generic state changes, and do not leave them as passive ORM containers in behavior-rich domains.
- Use Value Objects aggressively where primitives hide meaning: model local identifiers, quantities, ranges, names, and descriptive whole values explicitly; make them immutable by default, validate them at construction, compare by value, and keep invariant enforcement near the concept.
- Use a Domain Service only for a domain-significant operation that requires multiple domain objects and fits no single Entity or Value Object; name it in the Ubiquitous Language, and do not move behavior into services to avoid modeling those objects. Use a Transformation Service when domain information must be transformed without assigning behavior to the wrong object; keep technical transformation, serialization, transport, and persistence mapping outside the domain model, and do not hide it behind a domain-sounding service name.
- When an Aggregate boundary changes, center it on invariants that must hold immediately. When one transaction would modify multiple Aggregates, require a compelling reason rather than convenience; use events, policies, or process coordination when consistency can be eventual.
- When external code mutates Aggregate internals or performs an invariant-changing operation outside the root, move that operation behind intention-revealing root behavior.

## Repositories, Events, and Application Coordination

- Provide Repositories for Aggregate Roots: define interfaces by domain or application needs, reconstitute and persist Aggregates, return domain objects or domain-oriented results instead of ORM rows, and keep business rules out of implementations. Repository APIs should reflect Aggregate access needs rather than generic table CRUD.
- Publish Domain Events for meaningful business facts; name them in the past tense, keep events and payloads local to the model rather than transport mechanics, and use them across Aggregates or contexts when immediate consistency is not required. Do not emit events for every property change or to compensate for missing Aggregate design.
- Use Event Sourcing only when the event sequence is the right persistence model; streams must match Aggregate identity and versioning, replay must be deterministic, event meaning changes need versioning, upcasters, or translators, and Domain Events alone are not a reason to choose it.
- Keep Application Services as use-case coordinators: load Aggregates, invoke domain behavior, persist results, and publish resulting events; they may own transaction boundaries and integration coordination, but must not contain core decision logic and must remain thin enough that the model matters.
- When Repository design becomes a giant generic abstraction or a Repository per table without Aggregate thinking, replace that design. When a Repository returns ORM rows or persistence-layer entities, return domain objects or domain-oriented results; when it enforces business rules, move those rules back to the model. Repository APIs should reflect Aggregate access needs rather than generic table CRUD.
- When events are emitted for every property change, named as commands, or carry framework request objects or persistence artifacts, restore meaningful business facts: use past-tense fact names and model-local payloads.
- When Application Services contain the Domain Model's core decision logic or all branching business rules, move those decisions into the Entity, Value Object, Aggregate, or qualifying Domain Service; when controllers duplicate Application Service orchestration, restore that use-case coordination to the Application Service.

## Modules, Representations, and Delivery

- Organize modules by Bounded Context first and by domain or use-case ownership within the context; avoid giant `shared` or `common` packages for domain concepts, and keep the model visible in the structure.
- Use DTOs, projections, use-case queries, rendition adapters, or mediators when client needs differ from Aggregate shape; expose application-facing representations rather than Aggregate internals, tailor them per client without reshaping the domain model, compose multiple Bounded Contexts at the application or integration layer rather than merging their models, keep command behavior separate from query models when consistency, performance, or representation needs justify it, and keep scope identifiers explicit where context or ownership affects invariants or access.
- When generating code, proceed in order: identify the context, state its language terms, classify the concept as an Entity, Value Object, Aggregate Root, Domain Event, Repository, or Application Service, define a conservative Aggregate boundary, use identity references, place local invariants, shape Aggregate-oriented Repositories and use-case services, then define context or infrastructure translations.
- Test domain behavior and boundaries directly: Aggregate invariants, valid and invalid state transitions, Value Object validation, Domain Events as outcomes, repositories as infrastructure, translation layers, and application-service orchestration.
- When client rendering, query speed, or representation needs pressure the model shape, use projections, DTOs, use-case queries, or adapters instead of enlarging or exposing Aggregates.

## Modeling Investment

- Protect the Core Domain from generic abstractions and vendor terms; spend richer modeling where competitive or operational complexity lives, keep supporting subdomains simpler, and avoid DDD ceremony for trivial CRUD.
- When a subdomain is simple CRUD, keep it simple; when invariants and lifecycle complexity appear, model them honestly instead of hiding them in services.

## Reference Map

Use this file alone when it resolves ordinary matched implementation work; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Aggregate consistency and transaction scope: [Aggregate Rules of Thumb](references/full.md#aggregate-rules-of-thumb)
- Identity and value semantics: [Entity and Value Object Rules](references/full.md#entity-and-value-object-rules)
- Aggregate persistence and query ownership: [Repository Rules](references/full.md#repository-rules)
- Event meaning, publication, or sourcing: [Domain Event Rules](references/full.md#domain-event-rules)
- Use-case coordination: [Application Service Rules](references/full.md#application-service-rules)
- Context translation and integration: [Context Integration Rules](references/full.md#context-integration-rules)
- Client and read representations: [Client Representation and Scope Discipline](references/full.md#client-representation-and-scope-discipline)
- Domain-boundary verification: [Testing Rules](references/full.md#testing-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For an explicit comprehensive DDD implementation audit or complete Implementing Domain-Driven Design lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Is the Bounded Context explicit before interpreting names, modules, events, repositories, APIs, persistence, or integrations?
- Does the code use one local term per concept across tests, commands, events, repositories, services, and packages?
- Is Core Domain effort protected while supporting or CRUD areas stay simpler?
- Are context relationships, translation responsibilities, upstream/downstream pressures, and cross-context contracts visible without sharing model classes by default or enums with different semantics?
- Are Aggregates small and centered on immediate invariants, with invariant-changing operations through roots, no external mutation of internals, identity references across boundaries, and one Aggregate per transaction unless a compelling reason requires otherwise?
- In behavior-rich domains, are Entities behavior-bearing rather than passive ORM containers, and are Value Objects immutable by default, validated at construction, value-equal, and explicit for meaningful values?
- Is each Domain Service limited to a domain-significant operation that requires multiple domain objects and fits no single Entity or Value Object, and is each Transformation Service limited to domain information that would otherwise be assigned to the wrong object?
- Are Repositories reconstituting and persisting Aggregate Roots through Aggregate-oriented interfaces rather than generic DAOs or ORM leaks?
- Are Domain Events meaningful past-tense facts, and is Event Sourcing used only when event history is the right persistence model?
- Are Application Services coordinating use cases instead of owning domain decisions, with transaction boundaries and integration coordination treated as responsibilities they may own rather than must own?
- Does package structure expose Bounded Context and model ownership rather than giant `shared` or `common` domain packages?
- Are legacy and foreign models translated through Anticorruption Layers, client needs handled through application-facing representations, and technical infrastructure mappings kept outside the domain model?
- Do tests cover Aggregate invariants and transitions, Value Objects, Domain Events as outcomes, Repository infrastructure, translation layers, and Application Service orchestration?
