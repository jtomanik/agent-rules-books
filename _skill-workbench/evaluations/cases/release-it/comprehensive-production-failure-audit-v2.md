# Comprehensive Production Failure Audit

Perform a comprehensive end-to-end production-readiness audit for a checkout service before peak traffic.

It calls inventory, tax, payment, fraud, shipping, and notification providers; uses unbounded queues and connection pools; retries most failures immediately; accepts malformed downstream success payloads; has shared caches, scheduled reconciliation jobs, rolling migrations, weak readiness checks, sparse metrics, and manual runtime controls with no audit trail.

Cover stability assumptions, release risk, dependency protection, overload and capacity, runtime state and restart safety, resources, data boundaries, visibility, incidents and controls, deployment and startup, routing and security, contracts, caches, background work, testing, forbidden patterns, and final review. State failure semantics, limits, degradation, and blast-radius choices explicitly.
