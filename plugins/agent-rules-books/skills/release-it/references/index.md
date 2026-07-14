# Release It! Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit dispute, demonstrated production hotspot, or one bounded question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a comprehensive production-readiness audit or a decision spanning several failure modes, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-19` | Establish the policy scope or decide whether production readiness, survivability, graceful degradation, and observability are central. |
| [Primary Directive](full.md#primary-directive) | `21-34` | Resolve a tradeoff between happy-path elegance and visible failure, blast-radius limits, load shedding, core-service preservation, or diagnosis. |
| [Stability Mindset Rules](full.md#stability-mindset-rules) | `36-47` | Enumerate realistic slow, partial, prolonged, retry-amplified, queue, cache, or degraded-state failure assumptions. |
| [Production Readiness and Release Risk Rules](full.md#production-readiness-and-release-risk-rules) | `49-57` | Assess release exposure, compatibility, reversibility, configuration validation, or visibility of build, dependency, and runtime state. |
| [Dependency Protection Rules](full.md#dependency-protection-rules) | `59-89` | Design or review remote calls, timeout budgets, retry eligibility, backoff, circuit breakers, fast failure, bulkheads, or resource-pool isolation. |
| [Load and Capacity Rules](full.md#load-and-capacity-rules) | `91-127` | Define overload behavior, queue limits, back pressure, demand control, reserved capacity, load shedding, readiness handshakes, or governors. |
| [Runtime State and Restart Safety Rules](full.md#runtime-state-and-restart-safety-rules) | `129-149` | Make partial deployment, migration, or automation progress visible and safely resumable, or validate external responses and operational assumptions. |
| [Resource Management Rules](full.md#resource-management-rules) | `151-170` | Budget threads, connections, sockets, descriptors, memory, workers, locks, large payloads, deterministic cleanup, streaming, or pagination. |
| [Data Boundary Rules](full.md#data-boundary-rules) | `172-180` | Handle malformed or implausible external data, distinguish parsing from domain rejection, or prevent cache, queue, state, and downstream poisoning. |
| [Operational Visibility Rules](full.md#operational-visibility-rules) | `182-212` | Choose structured logs, correlation context, metrics, meaningful health signals, dependency diagnostics, saturation indicators, or secret-safe logging. |
| [Incidents, Capacity, and Runtime Control](full.md#incidents-capacity-and-runtime-control) | `214-222` | Analyze a failure chain or capacity incident, or design authorized, auditable, safe operational controls and production-affecting tooling. |
| [Deployment and Startup Rules](full.md#deployment-and-startup-rules) | `224-232` | Change startup configuration, readiness/health checks, migrations, destructive startup work, or one-time jobs. |
| [Interconnect, Routing, Security, and Chaos Rules](full.md#interconnect-routing-security-and-chaos-rules) | `234-244` | Address DNS, discovery, routing, load balancing, fan-out, hostile traffic, permissions, launch checks, game days, chaos, or disaster simulations. |
| [API and Contract Rules](full.md#api-and-contract-rules) | `246-254` | Specify retryable versus permanent failures, resilient interaction granularity, contract versioning, compatibility, timeout, or retry expectations. |
| [Cache Rules](full.md#cache-rules) | `256-268` | Decide cache authority, outage behavior, miss storms, stale data, dogpile prevention, or correctness assumptions hidden in cache behavior. |
| [Scheduled and Background Work Rules](full.md#scheduled-and-background-work-rules) | `270-278` | Pace scheduled demand, avoid synchronized jobs or retries, or define progress, timeout, cancellation, and failure behavior for long-running work. |
| [Review Rules](full.md#review-rules) | `280-294` | Perform a focused production-readiness review for missing timeouts, retry discipline, bounds, isolation, overload strategy, visibility, meaningful health, or workload pacing. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `296-321` | Classify or explain happy-path design, retry storms, queue collapse, silent failure, or blast-radius amplification. |
| [Code Generation Rules](full.md#code-generation-rules) | `323-342` | Translate the Release It! lens into concrete defaults while generating dependency, queue, deployment, startup, or failure-handling code. |
| [Testing Rules](full.md#testing-rules) | `344-353` | Design tests for timeout, retry, degradation, overload, queue saturation, restartable automation, startup, or health-check failure modes. |
| [Review Checklist](full.md#review-checklist) | `355-371` | Run the canonical final production-readiness scan before shipping a change. |
| [Final Instruction](full.md#final-instruction) | `373-382` | Arbitrate a difficult final choice using survivability, blast radius, graceful degradation, operability, and overload-collapse prevention. |
