# OBEY Implementing Domain-Driven Design by Vaughn Vernon

## When to use

Use when tight context still needs DDD guardrails for context leakage, fake tactical patterns, Aggregate sprawl, and cross-context model coupling.

## Primary bias to correct

Local context, language, and invariants outrank reuse pressure, ORM convenience, object graph traversal, and framework or client shape.

## Decision rules

- Name the Bounded Context and local Ubiquitous Language before interpreting domain artifacts, persistence, or integrations.
- Across Bounded Contexts, use explicit identifiers, integration messages, and separate contract models; do not pass local Aggregates, share model classes by default, or share enums whose semantics differ.
- Keep Aggregates small and centered on immediate invariants; route invariant changes through the root, prevent external mutation, reference other Aggregates by identity, and keep cross-Aggregate coordination usually eventual.
- Use Entities for identity and lifecycle, rejecting passive ORM containers in behavior-rich domains; make Value Objects immutable by default and validate at construction; use Domain Services only for domain-significant operations that require multiple domain objects and fit no Entity or Value Object.
- Repositories reconstitute and persist Aggregate Roots. Application Services coordinate use cases rather than make the Domain Model's core decisions; they may own transaction boundaries and integration coordination.
- Publish meaningful business facts as past-tense Domain Events; use Event Sourcing only when the event sequence is the right persistence model.
- Use DTOs, projections, use-case queries, or adapters when client needs differ from Aggregate shape instead of exposing or reshaping domain internals; keep scope identifiers explicit where context or ownership affects invariants or access.

## Trigger rules

- When a term has multiple local meanings, changes meaning across contexts, or is a technical placeholder, use the context-local business term and rename code when understanding improves.
- When a transaction would modify multiple Aggregates, require a compelling reason rather than convenience; center boundaries on immediate invariants, reference other Aggregates by identity, and use events, policies, or process coordination when consistency can be eventual.
- When legacy or foreign models enter local domain code, use an Anticorruption Layer; when client or infrastructure shape pressures the domain, use an application-facing representation or technical mapping.
- When DDD vocabulary wraps CRUD services, generic Repositories, mutable graphs, or anemic models, model the real invariants and behavior or use a simpler pattern honestly.
- When reviewing DDD code, verify context, language, Aggregate boundary, translation, Repository shape, events-as-facts, and Application Service thinness before approving.

## Final checklist

- Named Bounded Context and exact local language?
- Separate cross-context contracts; no model sharing by default or shared enums with different semantics?
- Small invariant-centered Aggregates; root-mediated invariant changes, no external mutation, identity references, and a compelling reason for multi-Aggregate transactions?
- Behavior-bearing Entities in behavior-rich domains; Value Objects immutable by default; Domain Services limited to domain-significant operations that require multiple domain objects and fit no Entity or Value Object?
- Repositories reconstituting and persisting Aggregate Roots; Application Services coordinating use cases rather than making the Domain Model's core decisions, with transaction boundaries and integration coordination as responsibilities they may own?
- Meaningful past-tense Domain Events; Event Sourcing only when event history is the right persistence model?
- Anticorruption Layers for legacy or foreign models; application-facing representations when client needs differ from Aggregate shape; explicit scope identifiers where context or ownership affects invariants or access; technical mappings for infrastructure concerns?
