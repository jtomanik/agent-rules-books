# Resolve a Repository Query Source Dispute

`Claim` is the Aggregate root used for adjudication commands. A read-only dashboard joins claims, policies, parties, tasks, and a reporting projection; its rows may lag commands by 20 seconds and are never modified. A separate query adapter already owns SQL for other screens.

Two reviewers disagree about the exact source guidance:

- One says `ClaimRepository` may expose the dashboard because Repository interfaces should reflect domain or application needs.
- The other says Aggregate Repositories should expose Aggregate access needs, while a multi-context screen belongs in a DTO, projection, use-case query, rendition adapter, or mediator outside the Aggregate Repository.

Resolve only this source-interpretation dispute. State the exact Repository boundary, where the dashboard query belongs, and how its client representation should relate to the domain model. Do not perform a complete Claims implementation audit.
