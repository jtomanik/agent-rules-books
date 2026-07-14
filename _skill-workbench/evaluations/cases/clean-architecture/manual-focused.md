# Resolve a Focused Clean Architecture Interpretation

Use `$clean-architecture` as the project book lens for this task.

Two reviewers dispute whether an application-owned use case may import an interface declared in `infrastructure/sql-customer-store.ts` merely because the concrete SQL class implements it. The interface returns plain strings and has no SQL types.

Resolve the ownership and dependency-direction interpretation. Keep retrieval focused on the smallest detailed sections needed to decide which layer owns the abstraction; do not redesign the feature or perform a complete audit.
