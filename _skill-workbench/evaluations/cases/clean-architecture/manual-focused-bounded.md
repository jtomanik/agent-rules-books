# Resolve and Arbitrate a Clean Architecture Ownership Dispute

Use `$clean-architecture` as the project book lens for this task.

An application use case imports a plain `CustomerStore` interface declared beside `SqlCustomerStore` in the infrastructure package. Reviewer A says interface indirection satisfies dependency inversion; Reviewer B says infrastructure still owns the abstraction and the source dependency points outward.

Resolve the ownership interpretation and arbitrate the final choice against the book's dependency rule. Keep retrieval bounded to the ownership, layer-responsibility, reversed-ownership, and final-arbitration guidance; do not redesign the feature or perform a complete audit.
