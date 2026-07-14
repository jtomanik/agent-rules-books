---
name: domain-driven-design-distilled
description: Domain-Driven Design Distilled guidance for the smallest effective DDD investment and anti-ceremony selectivity. Use when domain complexity, language ambiguity, business differentiation, or integration risk makes subdomain investment, Bounded Context boundaries, Ubiquitous Language meaning, or whether tactical patterns earn their cost central. Domain-Driven Design owns deeper model discovery; Implementing Domain-Driven Design owns detailed mechanics after context and model commitment.
---

# Domain-Driven Design Distilled

## Primary Bias

Use DDD where it clarifies complex business software; do not turn it into ritual. Use the smallest effective set of DDD practices to model business meaning clearly and deliver results quickly.

## Investment, Subdomains, and Contexts

- When uncertain, identify the business capability or subdomain, classify it as Core, Supporting, or Generic, define the Bounded Context, use its local Ubiquitous Language, and apply only tactical patterns that earn their cost.
- Put the most design effort into the Core Domain. Keep Supporting and Generic Subdomains simpler unless complexity proves otherwise, and let business drivers decide where modeling effort goes.
- Do not apply full tactical DDD to simple CRUD, Generic Subdomains, or mainly technical problems. Let simple domains use simple services and data structures; as invariants, lifecycle, and language complexity rise, strengthen the model incrementally rather than through a massive design overhaul.
- Every meaningful model lives inside an explicit Bounded Context that owns its language, rules, and model semantics. Code structure must reflect context boundaries.
- Treat the same term in different Bounded Contexts as potentially different concepts. Translate where meanings differ; do not share domain classes with subtly different meanings or import foreign language without translation.
- When the Core business concern drifts, terms stop matching code, or Supporting complexity hides the Core Domain, reassess the model. Revisit subdomain classification, Bounded Context boundaries, or modeling investment only when the affected scope calls them into question.
- When one model spreads across billing, identity, catalog, fulfillment, and support, split or translate instead of reusing shared domain classes.

## Language, Relationships, and Integration

- Use terms from the current Bounded Context in code, tests, Commands, Domain Events, and conversations. One concept gets one term; one term must not carry multiple meanings inside one context; rename code when understanding improves. Domain tests must read in the Ubiquitous Language.
- When language is fuzzy, generic, overloaded, or imported from another context, sharpen the local Ubiquitous Language and translate foreign terms.
- Choose each context relationship for its actual condition: Partnership only when teams can coordinate closely and share planning burden; Shared Kernel only for a small stable overlap with joint ownership and tests; Customer/Supplier when the upstream team can plan for downstream needs; Conformist when adopting the upstream model is cheaper and safer than translation; Anticorruption Layer when a foreign model would corrupt the local language; Open Host Service when many clients need a stable protocol into one context; Published Language when multiple systems need a documented interchange model; Separate Ways when integration cost is higher than shared capability value; and Big Ball of Mud as a context to contain and translate around, not a model to spread.
- When using Shared Kernel, require a small stable overlap with joint ownership and tests; without governance, choose another relationship.
- When calling an integration an Anticorruption Layer, verify that translation exists.
- Use RPC only when request/response coupling, latency, versioning, and failure semantics are acceptable. Use REST resources as application-facing representations, not leaked Aggregate internals. Use messaging when asynchronous coordination fits the business process and consumers can handle lag, duplicates, and ordering limits. Decide whether Domain Events carry enough information for consumers or require query-back.
- Own integration contracts deliberately, keep them separate from internal models, and test translations at context boundaries.

## Tactical Patterns and Consistency

- Use Entities when identity and lifecycle matter. They must have explicit identity and protect meaningful state transitions; do not expose unrestricted state changes by default. Test Entities for valid and invalid transitions.
- Use Value Objects aggressively when a primitive hides meaning. They are immutable by default, validate themselves, and make code read in domain language. Test their validation and behavior.
- When a primitive, flag, status code, enum, or boolean carries domain rules, expose the richer concept or use a Value Object.
- Use Aggregates only where invariants require a consistency boundary. Keep them small, protect invariants through the Aggregate root, do not expose mutable children directly, reference other Aggregates by identity, and avoid large object graphs. Default to eventual consistency across Aggregates; one transaction should usually change one Aggregate. Test Aggregates for valid and invalid transitions.
- When one transaction would change several Aggregate roots, revisit the consistency boundary; one transaction should usually change one Aggregate, with eventual consistency across Aggregates as the default. Separately, when one request would load and mutate a whole graph, reject navigation convenience as a boundary and restore smaller, identity-referenced Aggregates.
- Use Domain Events for meaningful past-tense facts when they clarify collaboration or integration; do not publish trivial noise for every field change.
- When a Domain Event is vague, command-like, trivial, or emitted for every field change, redesign it as a meaningful past-tense fact or remove it.

## Domain Behavior and Technology Boundaries

- Application Services coordinate use cases: they load Aggregates, call domain behavior, save results, and trigger integration work. They must not become the real domain model and should stay thin enough that the model carries meaning. Test Application Services for orchestration, not for all domain rules.
- When controllers duplicate application orchestration, restore coordination through an Application Service. When helpers, services, or transport-shaped Application Services carry business decisions, move those decisions into the domain model or name the missing concept.
- Keep frameworks, persistence mechanics, REST resources, transport formats, and other technology concerns out of the domain model. Persist Aggregates without letting persistence define the model, and translate transport and integration data at the boundary.
- When a foreign model starts defining local language, translate it at the context boundary. When a screen or UI, framework, REST or transport representation, or persistence or database shape starts defining the domain model, isolate that technology concern instead.
- Prefer code that teaches the model: keep names close to real business terms, make domain assumptions explicit in names, tests, and events, and expose richer concepts instead of unexplained status codes, flags, enums, booleans, or generic helpers or utilities carrying domain decisions.

## Collaborative Modeling and Delivery

- Use Event Storming or similar collaborative modeling when workflow, events, Commands, policies, or team language are unclear. Use scenarios and acceptance tests to validate that the model expresses real business behavior. Use modeling spikes to reduce uncertainty before committing to a model shape. Track modeling debt when code and language are known to be imperfect but intentionally deferred. Involve domain experts in scenario walkthroughs, terminology decisions, and acceptance criteria. Timebox modeling so it improves implementation instead of becoming detached analysis.
- Estimate DDD work by modeling uncertainty, integration risk, and implementation cost, not only by feature count; treat team skill and access to domain experts as constraints on how much DDD ceremony the project can sustain.
- When generating code, use this default order: identify the subdomain; identify the Bounded Context; write names in its local Ubiquitous Language; decide whether each concept is an Entity, Value Object, Aggregate, Service, Repository, or Domain Event; choose the smallest tactical pattern that fits; isolate infrastructure at boundaries; keep context translation explicit.

## Reference Map

Use this file alone when it resolves the ordinary DDD investment or modeling question; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Whether DDD investment is justified: [Adoption Fit and Modeling Investment](references/full.md#adoption-fit-and-modeling-investment)
- Subdomains and strategic priority: [Strategic Rules](references/full.md#strategic-rules)
- Upstream/downstream relationship choice: [Context Relationship Rules](references/full.md#context-relationship-rules)
- RPC, messaging, and contract shape: [Integration Style Rules](references/full.md#integration-style-rules)
- Context-local terminology: [Ubiquitous Language Rules](references/full.md#ubiquitous-language-rules)
- Tactical pattern selection: [Tactical Pattern Rules](references/full.md#tactical-pattern-rules)
- Consistency boundary size: [Aggregate Minimalism Rules](references/full.md#aggregate-minimalism-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For any explicit comprehensive end-to-end DDD investment or modeling audit, or a request for the complete DDD Distilled lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Correct subdomain and Core Domain investment?
- Explicit Bounded Context and neighboring relationship chosen under its actual conditions?
- Ubiquitous Language visible in code, tests, Commands, Domain Events, and conversations?
- Integration contracts owned deliberately and translation tested where meanings differ?
- Tactical patterns used only when they earn their cost and genuinely help?
- Entities protecting transitions and Value Objects preserving validated domain meaning, with their specified tests?
- Aggregates small, root-protected, identity-referenced, and using eventual consistency across Aggregates by default?
- Application Services coordinating and tested for orchestration rather than owning domain rules?
- Framework, persistence, REST, transport, and other technology concerns kept out of the domain model?
- Model validated against real business behavior, any modeling work timeboxed, and known imperfect code or language tracked when intentionally deferred?
