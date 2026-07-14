# Choose Boundary Granularity Under Independent Release Pressure

The Billing policy is currently a framework-free in-process module with inward-only dependencies. Billing and Fulfillment now have different teams and release schedules. One reviewer wants a remote Billing service immediately; another says package boundaries and a policy-owned port are sufficient.

Facts:

- Billing rules change weekly; the transport and database change less often.
- Fulfillment needs one synchronous price decision per order.
- A remote call would add latency, retries, deployment coordination, versioning, and partial-failure behavior.
- The two teams need independent code ownership now, but independent scaling is not required.
- Current tests can run Billing policy without a framework or database.

Resolve this bounded source-interpretation dispute. Compare an in-process module boundary, a separately deployable component, and a remote service. Identify the specific boundary, deployment, and operational costs that must justify the stronger split, and state the smallest defensible boundary now. Do not perform a complete architecture audit.
