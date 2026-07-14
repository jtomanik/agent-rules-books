# OBEY Patterns of Enterprise Application Architecture by Martin Fowler

## When to use

Use when designing or reviewing enterprise application code that crosses presentation, application workflow, domain logic, persistence, transactions, concurrency, integration, session state, or remote boundaries.

## Primary bias to correct

Enterprise applications are not improved by inventing architecture for every feature or by letting the ORM, database schema, or transport shape choose the design. Use a small set of well-understood patterns to make responsibilities and boundaries explicit.

## Decision rules

- Make responsibility ownership explicit before naming patterns: presentation and transport, application workflow, domain logic, data source interaction, transaction management, concurrency control, and integration boundaries must not collapse into one class or layer.
- Use layering as the default organizing principle, but every layer must earn its cost by reducing coupling or clarifying responsibility; forbid lower layers from reaching into presentation concerns and reject pass-through layering theater.
- Choose the business logic pattern by force: Transaction Script for short independent simple flows, Table Module for table-centered set logic, and Domain Model for significant rules, invariants, identity, lifecycle, or collaboration.
- Let Transaction Scripts stay use-case focused, Table Modules stay honestly tabular, and Domain Models own rich behavior; escalate when duplication, lifecycle, or invariant complexity grows.
- Use a Service Layer to define application operations, coordinate use cases, own transaction boundaries and orchestration, expose an application-oriented API, and avoid absorbing all domain logic by default.
- At remote boundaries, use Remote Facade for coarse operations and translation; at process or layer boundaries, use DTOs for batching, translation, and explicit transport shape, not as domain models.
- Choose persistence patterns deliberately: repositories speak domain terms and hide query/mapping/storage details, Data Mappers keep SQL and record formats outside domain objects, gateways centralize record/table access, and Active Record is only for simple domains where persistence coupling is acceptable.
- Keep identity, write coordination, and loading behavior visible: use Identity Map where needed for one object per identity per scope, Unit of Work for one logical transactional commit, and Lazy Load only where hidden database or remote chatter will not surprise loops or serializers.
- Choose object-relational mappings by identity, lifecycle, query needs, schema shape, and serialization versioning; keep identity fields, foreign keys, association tables, dependent objects, embedded values, serialized values, inheritance mapping, metadata mapping, and query objects explicit rather than accidental.
- Design concurrency and transactions in the application workflow: optimistic locks detect conflicts and surface merge semantics, pessimistic locks require justified contention, transactions stay short, remote calls usually sit outside transactions, and helpers must not hide transaction ownership.
- Use Coarse-Grained Lock when related objects must be locked together to preserve a user-level edit; use Implicit Lock only when lock acquisition can remain reliably hidden without making concurrency invisible or transaction ownership and contention impossible to diagnose.
- Keep presentation code focused on input, rendering, routing, formatting, pagination, UI state, and transport; business rules stay out of controllers, views, templates, and presentation models.
- Access external systems through boundaries, translate partner formats into internal concepts, treat integration events and messages as boundary data, and do not let vendor payloads or serialization code shape internal domain design.
- Choose session state deliberately: client, server, or database session storage must account for integrity, security, scaling, cleanup, durability, server-farm sharing, and database load.
- Use base patterns only for concrete pressure: Gateway for external resources, Mapper for independent sides, Layer Supertype for real shared behavior, Separated Interface for dependency breaks, Registry for controlled well-known objects, Value Object and Money for value semantics, Special Case for repeated null or exceptional handling, Plugin when implementations must be selected or extended without changing core code, Service Stub to test or run without a real remote service, and Record Set when tabular interchange is natural.
- Do not distribute objects or services by default; when distribution is required, separate local object design from the remote contract and budget latency, serialization, versioning, and partial failure.
- Generate code in this order: choose the business logic pattern, place use-case coordination in application services, put rich domain decisions in the domain model, hide persistence behind repositories/mappers/gateways, define transactions explicitly, put DTOs or facades only at boundaries, and keep presentation/transport at the edge.
- Test each responsibility at the level where it owns behavior: domain logic apart from UI and persistence when possible, repositories/mappers/gateways as data infrastructure, services for workflow and transactions, locking where concurrency matters, and DTO/facade mapping at boundaries.

## Trigger rules

- If domain behavior appears in controllers, views, handlers, DTOs, serialization code, or vendor payload adapters, move it to the owning layer.
- If one class or layer coordinates rendering, validation, SQL, transactions, domain rules, and external calls, split by responsibility before adding another pattern.
- If a Transaction Script accumulates duplicated decisions, invariants, or lifecycle rules, revisit Domain Model and the supporting persistence pattern.
- If a model is table-shaped in a behavior-rich domain, a repository is generic CRUD, or a service only forwards to persistence, check whether the ORM or database schema has taken over the design.
- If SQL, mapping, transaction ownership, saves, or external resource access is scattered across callers, introduce the smallest repository, mapper, gateway, Unit of Work, or service boundary that centralizes access or ownership.
- If lazy loading, duplicate in-memory identities, hidden auto-persistence, N+1 behavior, or ad hoc saves can happen inside one logical work scope, define identity scope, Unit of Work, and loading behavior before continuing.
- If concurrency conflicts or user-level edits matter, choose explicit optimistic, pessimistic, coarse-grained, or implicit locking semantics; if long-running workflows matter, make transaction ownership explicit instead of treating the workflow as one immediate transaction.
- If a remote API looks like local object collaboration, leaks domain internals, or requires many calls per user action, redesign it as a coarse use-case contract with DTO translation.
- If session storage, integrity, security, scaling, cleanup, durability, server-farm sharing, or database load is unclear, choose the session-state pattern before adding features.
- If a layer exists only to forward calls, a generic repository covers everything, an ORM model doubles as aggregate/service/DTO, or a controller owns the enterprise workflow, treat it as a forbidden-pattern review blocker.

## Final checklist

- Are presentation, workflow, domain, persistence, transaction, concurrency, integration, session, and distribution responsibilities separated intentionally?
- Does the business logic pattern match actual complexity rather than habit or ORM shape?
- Are repositories, mappers, gateways, Active Record, Unit of Work, Identity Map, and Lazy Load used only where their forces fit?
- Is transaction ownership explicit and kept out of hidden helpers, are transactions short, and are remote-call spans avoided when possible?
- Are concurrency conflicts, offline locks, identity scope, and loading behavior visible?
- Are integration boundaries clear and translated without shaping internal design?
- Are remote boundaries coarse, separate from local object design, version-aware, and failure-aware?
- Is session state chosen deliberately with integrity, security, scaling, cleanup, durability, sharing, and database-load costs explicit?
- Are tests aligned to the responsibility that owns each behavior?
