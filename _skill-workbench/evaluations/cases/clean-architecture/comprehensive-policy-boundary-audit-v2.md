# Comprehensive Policy and Boundary Audit

Perform a comprehensive end-to-end architecture audit of this order platform. Do not limit the review to the first visible defect.

The codebase has HTTP controllers calling ORM repositories directly, domain objects carrying ORM decorators, use cases returning framework responses, background jobs duplicating pricing rules, and presenters querying reporting tables. A shared `core` package contains business rules, SQL helpers, vendor DTOs, environment reads, and service clients. Three deployable services import that package and call each other's databases. Most business tests require the web framework and a real database.

Cover policy independence, dependency direction, layer responsibilities, use-case and adapter ownership, boundary economics, service and process boundaries, component stability, testing, forbidden structures, and an incremental migration strategy. State tradeoffs where a full boundary is not yet worth its cost.
