# Run a Complete Clean Architecture Assessment

Use `$clean-architecture` and apply its complete reference end to end.

Audit a subscription-renewal feature whose HTTP handler constructs an ORM client and payment SDK, calculates renewal eligibility, writes subscription state, sends email, and returns ORM rows. The same policy is duplicated in a scheduled job, tests require the real database, and dependency wiring is hidden in constructors.

Produce a prioritized complete-lens assessment covering policy ownership, dependency direction, entities/use cases, ports/adapters, boundary models, component structure, testing, incremental migration, boundary economics, tradeoffs, and a final review checklist. Do not implement changes.
