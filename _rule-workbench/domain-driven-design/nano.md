# OBEY Domain-Driven Design by Eric Evans

## When to use

Use as always-on DDD guidance when domain language, invariants, lifecycle, or integration boundaries affect implementation choices.

## Primary bias to correct

Generic plumbing and DDD terminology are not a domain model.

## Decision rules

- Keep model, code, tests, documents, and team language aligned inside each Bounded Context.
- When the domain is complex enough to need model-driven design, keep business behavior in model code and presentation, application coordination, infrastructure, and framework concerns outside it; reserve Smart UI for simple applications where rich abstraction, reuse, integration, and deep rules do not matter.
- Before writing domain code, identify in order the Bounded Context, domain term, tactical type, and invariants; refine fuzzy Ubiquitous Language and use only a model that solves the problem and can be implemented.
- Use Entities when identity, lifecycle, or continuity matters; Value Objects for attribute-defined concepts, immutable by default, valid at construction, and equal by value; Domain Services only for domain-significant operations with no natural Entity or Value Object home; Modules for model cohesion.
- Treat Aggregates as small immediate-consistency boundaries around invariants; route invariant-affecting changes through roots and reference other Aggregates by identity unless stronger consistency is required.
- Use Factories for complex or domain-significant creation, but use a direct constructor when creation is simple, intention-revealing, and exposes no complex invariants; use Repositories for Aggregate roots and design the model first and storage second.
- Define context boundaries and relationships explicitly before sharing terms, data, or behavior across systems.
- Protect the Core Domain from generic subdomains, reusable mechanisms, infrastructure, framework pressure, and foreign models.
- When a deeper model appears, compare explanatory gain with migration cost; preserve behavior in safe incremental steps, never a big-bang rewrite when incremental migration is possible, and make important constraints, policies, processes, and calculations explicit.
- Test invariants, invalid construction, lifecycle transitions, and boundary translations in the Ubiquitous Language.

## Trigger rules

- Fuzzy or inconsistent terms inside one Bounded Context trigger language refinement and code renaming; legitimate differences across contexts require explicit translation, not one shared language.
- In a domain complex enough for model-driven design, procedural business rules in orchestration, SQL, jobs, or serializers trigger moving behavior into the model.
- Sprawling transactions or cross-module changes trigger Aggregate and context-boundary review.
- Foreign or legacy model pressure requires a deliberate relationship: use an Anticorruption Layer only when real translation protects the local model; choose Conformist only when adopting upstream is cheaper than translating.
- Supporting mechanisms obscuring distinctive value trigger Core Domain distillation.

## Final checklist

- Where complexity warrants model-driven design, is behavior in the model?
- One language inside each context and explicit translation across contexts?
- Aggregate invariants protected through roots and Value Objects valid by construction?
- Integration relationship and translation explicit?
- Domain tests cover invalid states, context boundaries, and actual Anticorruption Layer translations?
- Core Domain still visible?
