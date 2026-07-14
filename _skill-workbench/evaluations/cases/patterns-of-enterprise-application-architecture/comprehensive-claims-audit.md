# Exhaustive claims application audit

Perform an exhaustive audit of the design below across presentation, application workflow, business logic placement, persistence and object-relational mapping, identity and write coordination, transactions, concurrency, integration, session state, distribution, code-generation defaults, testing, review checks, and forbidden structures. Consult the complete applicable packaged reference end to end before answering.

```text
ClaimsPortalController
  parses browser requests and stores ClaimEntity in the HTTP session
  calculates eligibility, reserves, and settlement amounts
  opens a database transaction
  loads and saves ORM entities through GenericRepository<T>
  lazily walks claimant, policy, incidents, documents, and payments
  calls FraudService, DocumentVendor, and PaymentNetwork inside the transaction
  serializes ORM entities directly to partner JSON
  retries the entire request after optimistic-lock failures

GenericRepository<T>
  find(tableName, id)
  save(tableName, row)
  query(tableName, filters)

ClaimService
  forwards each controller call to GenericRepository

Remote clients
  expose one method per internal entity getter/setter
  require 20-60 calls for one claim review
```

The team wants a staged correction, not a rewrite. Identify which current choices are acceptable, which block review, which patterns fit each force, and how the test boundaries should change.
