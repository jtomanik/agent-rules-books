# OBEY Domain-Driven Design Distilled by Vaughn Vernon

## When to use

Use as compact DDD guidance when domain complexity, language ambiguity, business differentiation, or integration risk justify the modeling effort.

## Primary bias to correct

Use DDD selectively, but seriously: model real business complexity with the smallest effective practices, and do not turn DDD into ritual.

## Decision rules

- Invest most in the Core Domain. Keep Supporting and Generic work simpler unless complexity proves otherwise. Do not apply full tactical DDD to simple CRUD, Generic Subdomains, or mainly technical problems. As invariants, lifecycle, or language complexity rise, strengthen incrementally. Tactical patterns must earn their cost.
- Every meaningful model lives in an explicit Bounded Context owning language, rules, and model semantics; code reflects the boundary. When language is fuzzy, overloaded, or imported, refine local terms or translate differing meanings; do not share divergent domain classes.
- Use Entities when identity and lifecycle matter: require explicit identity and protected transitions; no unrestricted state changes by default. Use Value Objects aggressively when primitives hide meaning: immutable by default, self-validating, and readable in domain language.
- Use Aggregates only for invariant consistency boundaries: keep them small, protect invariants through the root, reference others by identity, and default to eventual consistency across Aggregates. If one transaction would change several, review the boundary; it should usually change one. Separately, a request loading and mutating a whole graph requires smaller, identity-referenced Aggregates.
- Business decisions belong in the domain model. Application Services coordinate use cases and must not be shaped only by transport or become the real domain model. When helpers or services carry decisions, move them into the model or name the missing concept.
- Keep technology concerns out of the domain model. Translate foreign models where meanings differ, unless Conformist adoption of the upstream model is cheaper and safer than translation; isolate screen/UI, framework, REST/transport, or persistence/database shapes that drive the model. Translate transport/integration data at boundaries; keep contracts separate from internal models.

## Trigger rules

- When one model absorbs unrelated concerns, review subdomain and Bounded Context boundaries; do not reuse one model across distinct business concerns. Translate only where meanings differ.
- When Domain Events are vague, command-like, trivial, or noisy field changes, redesign as meaningful past-tense facts or remove.

## Final checklist

- DDD investment justified; Core Domain prioritized; tactical cost earned?
- Explicit context, local language, and warranted boundary changes?
- Entity identity and transitions protected; Value Objects immutable and self-validating; Aggregates small and eventually consistent by default?
- Foreign models translated where meanings differ, or Conformist adoption cheaper and safer than translation; technology isolated; contracts separate?
- Domain decisions modeled; Application Services coordinating; Domain Events meaningful?
