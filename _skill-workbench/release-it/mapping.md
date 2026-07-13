# Release It! Skill Mapping

## Scope

- Distinctive lens: Production survivability under slow, partial, prolonged, overload-amplified, bad-data, and operator-induced failure. The skill asks how a system fails, contains demand, preserves core service, recovers, and exposes enough state to operate.
- Intended invocation: Model-invoked only when production failure behavior is an explicit objective or demonstrated operational problem, including failure semantics, demand or capacity limits, blast-radius isolation, degraded service, recovery, operability, deployment or startup controls, incident chains, or bounded resilience tests.
- Positive boundary: Do not infer the lens from testability, safe-change work, routine rollout verification, local API design, ordinary errors, in-process concurrency, service or database calls, or money and transaction vocabulary.
- Leading vocabulary: production survivability, partial failure, blast radius, demand control, load shedding, degraded mode, restartability, operability, and recovery.
- Closest neighboring skills: `clean-code` for local readability and code shape; `designing-data-intensive-applications` for data semantics under distributed failure; `clean-architecture` for policy/detail boundaries; `refactoring` and `working-effectively-with-legacy-code` for safe change; `code-complete` for construction quality.
- Compatibility evidence: Every current pairwise Release It! compatibility document classifies the pair as complementary. The recurring constraint is to add reliability mechanisms only when a real production failure surface triggers them; do not turn local design work into speculative resilience infrastructure.
- Live final catalog boundary: `clean-code` owns requested local-readability decisions; `refactoring` owns explicit behavior-preserving structural change after behavior is known or protected; `working-effectively-with-legacy-code` requires a semantic change blocked on first feedback. Release It! joins a neighbor only when production failure behavior is independently explicit or operationally demonstrated.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Activation threshold | `production failure behavior is an explicit objective or demonstrated operational problem` | Requires task evidence rather than incidental production vocabulary. |
| Failure decisions | `failure semantics` or `degraded service` | Selects explicit production behavior rather than an ordinary error-handling change. |
| Demand and isolation | `demand/capacity limits` or `blast-radius isolation` | Selects overload, saturation, containment, and core-service preservation rather than generic code structure. |
| Runtime and release control | `recovery`, `operability`, or `deployment/startup controls` | Selects partial operational state, diagnosis, restartability, and production control paths. |
| Diagnosis and resilience practice | `incident chains` or `bounded resilience tests` | Selects production-causal analysis and controlled failure exercises rather than generic debugging or unit testing. |
| Negative scope gate | `Do not infer this lens from testability, safe-change work, routine rollout verification, local API design, ordinary errors, in-process concurrency, service/database calls, or money/transactions.` | Prevents local construction, testing, rollout, and incidental infrastructure vocabulary from activating Release It! without a distinct production-failure decision. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Apply the complete Release It! lens to this service before launch." | `release-it` | Direct book request; comprehensive reference route. |
| "Add an HTTP payment call that times out, retries safely, and degrades without exhausting workers." | `release-it` | Remote dependency failure, retry discipline, degraded behavior, and isolation are central. |
| "Our queue age grows without bound during bursts; preserve checkout while shedding analytics work." | `release-it` | Capacity bounds, demand control, saturation, and core-service preservation are central. |
| "Make this migration resumable after a partial deploy and expose durable progress." | `release-it` | Restartable automation, partial operational state, and recovery are central. |
| "Rename this handler and split its mixed validation and mutation phases." | `clean-code`; `refactoring` allowed | Local readability is requested, and explicit behavior-preserving rename/split work may also invoke Refactoring; no production failure surface is central. |
| "Rename this money-transfer DTO field and split its local mapper." | `clean-code`; `refactoring` allowed | Money and transaction vocabulary alone does not create a production-survivability decision. |
| "Move the database adapter behind a use-case-owned port." | `clean-architecture` | Policy/detail dependency direction dominates; no operational failure mechanism is requested. |
| "Move the remote adapter behind a port and add timeout, breaker, and degraded-mode behavior." | `clean-architecture`, `release-it` | Policy independence and production dependency protection are both central and complementary. |
| "Fix duplicate and reordered events during replay while preserving source-of-truth semantics." | `designing-data-intensive-applications` | Ordering, idempotency, replay, and data correctness dominate; Release It! joins only if overload or runtime containment is also central. |
| "Refactor this retry loop in behavior-preserving steps." | `refactoring`, `release-it` | Safe structural change and production retry semantics are both central. |
| "Add a timeout to this untested legacy worker whose behavior is unclear." | `working-effectively-with-legacy-code`, `release-it` | Characterization/seams govern change safety; Release It! governs timeout and caller-survival behavior. |
| "Review this pull request for general quality." | none of the book skills by default | The prompt has no distinctive book lens or production symptom; automatic multi-book activation would add noise. |
| "Design a chaos experiment with a bounded blast radius, stop condition, and recovery proof." | `release-it` | Controlled resilience practice is a distinctive Release It! branch. |

## Shared-Term Review

| Shared term | Neighbor | Why the overlap is necessary |
| --- | --- | --- |
| boundaries / external data | `clean-code`, `code-complete`, `designing-data-intensive-applications` | Release It! uses the term only for production poisoning, trust, and failure containment; neighbors own readability, defensive construction, or data semantics. |
| APIs / integrations | `clean-architecture`, DDD skills, PoEAA | Release It! owns timeout, retryability, failure, capacity, and recovery behavior; neighbors own dependency direction, model translation, or enterprise pattern fit. |
| retries / queues / caches | `designing-data-intensive-applications` | Release It! owns operational bounds and collapse prevention; DDIA owns idempotency, ordering, replay, consistency, and source-of-truth semantics. |
| testing | `clean-code`, `code-complete`, legacy/refactoring skills | Release It! invokes only for production failure, overload, startup, health, automation, chaos, and disaster behavior. |
| observability / diagnosis | general debugging guidance | Release It! requires production boundary and saturation signals that expose live failure chains, not generic defect localization. |
| recovery / reversible change | `the-pragmatic-programmer`, refactoring skills | Release It! owns restartability and rollback/roll-forward after partial operational changes; neighbors own general design reversibility or behavior-preserving change. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance | Description failure-semantics branch; `Failure Semantics and Dependency Protection` first rule | Preserves slow, partial, prolonged dependency/queue/cache/caller/degraded-state failure assumptions without treating a dependency call alone as sufficient invocation. |
| `N2` | description, primary-bias, early-guidance, final-check | Description capability, blast-radius-isolation, degraded-service, and operability branches; `Primary Bias`; failure-semantics second rule; final checklist isolation/overload item | Keeps production survivability, visible failure, blast-radius control, load shedding, core-service preservation, and diagnosis salient. |
| `N3` | description, early-guidance, final-check | Description demand/capacity branch; timeout rule; `Demand, Capacity, and Workflows`; first three checklist items | Promotes explicit bounds without splitting the complete `M4`, `M7`, `M10`, or `M17` concerns. |
| `N4` | early-guidance, final-check | Retry rule and retry checklist item | Retry is no longer an invocation keyword by itself; safety, total bounds, backoff/jitter, permanent failures, and stacked retry storms remain complete normal-use guidance. |
| `N5` | description, early-guidance, final-check | Description blast-radius-isolation and degraded-service branches; failure-isolation rule; deterministic release rule; isolation/overload checklist item | Circuit breakers, bulkheads, fast failure, separate pools, degraded modes, and cleanup retain their complete mini homes. |
| `N6` | description, early-guidance, final-check | Description recovery, operability, and deployment/startup-control branches; `Release and Runtime Safety`; diagnostics and operational-control checklist items | Treats deployment, startup, automation, health, observability, configuration, rollback, security, and runtime state as production design. |
| `N7` | early-guidance, final-check | `Boundaries, Contracts, and Diagnosis` first rule; validation checklist item | Bad boundary data no longer invokes the skill by itself; input/response validation and downstream-poisoning prevention remain complete normal-use guidance after a production-failure match. |
| `N8` | description, early-guidance, final-check | Description recovery, operability, and deployment/startup-control branches; production-aware workflows rule; `Security, Controls, and Resilience Exercises`; last checklist item | Keeps failure, capacity, recovery, authorization, and stop behavior explicit across APIs, interconnects, caches, jobs, and controls. |
| `N9` | early-guidance, reference-router, final-check | `M16` and `M17` trigger rules; index dependency/load/resource/visibility sections; first six checklist items | Remote calls, waits, queues, pools, caches, retries, jobs, and large-result paths do not invoke the skill alone; once production failure behavior is central, they route bounds, failure behavior, validation, and saturation detail. |
| `N10` | description, early-guidance, reference-router, final-check | Description recovery, operability, and deployment/startup-control branches; `M18` trigger; index runtime-state, incidents/control, and deployment/startup sections; operational-control checklist item | Preserves recovery, auditability, observability, restartability, and partial-change handling. |
| `N11` | description, early-guidance, reference-router, final-check | Description demand/capacity and incident-chain branches; overload and production-aware-workflow rules; index load/capacity, routing, cache, and background-work sections; isolation/overload checklist item | Keeps traffic concentration tied to back pressure, shedding, pacing, or isolation before expensive work. |
| `N12` | description, early-guidance, reference-router, final-check | Description bounded-resilience-test branch; `Security, Controls, and Resilience Exercises`; index routing/security/chaos and testing sections; final checklist item | Preserves hypothesis through the full reference, plus blast radius, observability, stop condition, and recovery in normal guidance. |

The nano checklist is intentionally represented only as the final scan. It does not create a second authoritative definition of `N3-N12`.

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | Failure Semantics and Dependency Protection | Moved verbatim and promoted | Keeps slow, partial, prolonged production failure assumptions. |
| `M2` | Failure Semantics and Dependency Protection | Moved verbatim and promoted | Retains visible failure, blast-radius limits, shedding, core service, and diagnosability. |
| `M3` | Release and Runtime Safety | Moved verbatim as the section's governing rule | Keeps deployment, operations, security, observability, rollback, and visible state inside system design. |
| `M4` | Failure Semantics and Dependency Protection | Moved verbatim | Keeps explicit intentional time limits, rejects defaults and infinite waits. |
| `M5` | Failure Semantics and Dependency Protection | Moved verbatim | Keeps caller/provider safety, count and total-time bounds, backoff/jitter, and permanent-failure exclusions. |
| `M6` | Failure Semantics and Dependency Protection | Moved verbatim | Co-locates breakers, fast failure, bulkheads, separate pools, and slow-work isolation. |
| `M7` | Demand, Capacity, and Workflows | Moved verbatim | Keeps back pressure, finite queues, demand limits, reserved critical capacity, and value-aware shedding. |
| `M8` | Demand, Capacity, and Workflows | Moved verbatim | Retains the conditions for steady state, fail fast, let-it-crash, handshaking, decoupling middleware, and governors. |
| `M9` | Release and Runtime Safety | Moved verbatim | Keeps visible/validated operational state and rollback or roll-forward for partial changes. |
| `M10` | Demand, Capacity, and Workflows | Moved verbatim | Keeps explicit budgets, deterministic release, no scarce resources across slow calls, streaming, and pagination. |
| `M11` | Boundaries, Contracts, and Diagnosis | Moved verbatim | Keeps layered validation and prevents bad data from poisoning state or downstream systems. |
| `M12` | Boundaries, Contracts, and Diagnosis | Moved verbatim | Retains the complete diagnostic signal inventory plus secret and retry-storm logging limits. |
| `M13` | Release and Runtime Safety | Moved verbatim | Keeps startup, health, migrations, jobs, controls, process code, and delivery tooling safe and recoverable. |
| `M14` | Demand, Capacity, and Workflows | Moved verbatim | Keeps production-aware topology, contracts, caches, scheduled/background work, and concentration/fan-out/dogpile risks together. |
| `M15` | Security, Controls, and Resilience Exercises | Moved verbatim | Keeps hostile traffic and security in readiness and bounds production tests, game days, chaos, and disaster work. |
| `M16` | Failure Semantics and Dependency Protection | Moved verbatim beside `M4-M6` | Keeps timeout, retry eligibility/bounds, fallback, validation, and caller survival as one trigger. |
| `M17` | Demand, Capacity, and Workflows | Moved verbatim beside `M7`, `M10`, and `M14` | Keeps capacity/full/cleanup/cache/pacing/pagination/saturation decisions together. |
| `M18` | Release and Runtime Safety | Moved verbatim beside `M3`, `M9`, and `M13` | Keeps idempotency/restartability, durable state, audit, verification, and recovery paths together. |
| `M19` | Release and Runtime Safety | Moved verbatim beside readiness and health guidance | Keeps traffic limited to ready components and health tied to real service ability. |
| `M20` | Boundaries, Contracts, and Diagnosis | Moved verbatim | Keeps material failures, retryability, resilient granularity, versioning, compatibility, timeout, and retry expectations. |
| `M21` | Boundaries, Contracts, and Diagnosis | Moved verbatim | Keeps failure-chain, defense, detection, demand, saturation, latency, queue, dependency, concentration, and design-change analysis. |
| `M22` | Security, Controls, and Resilience Exercises | Moved verbatim beside `M15` | Keeps authorization, auditability, safe defaults, stop mechanisms, blast-radius bounds, and recovery paths. |

The final checklist intentionally restates `M4-M7`, `M9-M22` as questions. The concern sections above remain their single authoritative definitions.

## Wording Fidelity

No authoritative `M1-M22` decision or trigger rule was reworded. Every complete rule is moved verbatim from `release-it.mini.md`; the primary bias and all final-checklist items are also verbatim.

The standalone mini invocation sentence is metadata input rather than an authoritative `M*` rule, but its transformation is recorded for completeness:

| Original wording | Final wording | Reason | Affected traceability IDs |
| --- | --- | --- | --- |
| `Use for services, APIs, jobs, queues, deployment paths, control tooling, and critical flows that must survive production failures, overload, latency, bad data, hostile traffic, and operational mistakes.` | `Use only when production failure behavior is an explicit objective or demonstrated operational problem, such as deciding failure semantics, demand/capacity limits, blast-radius isolation, degraded service, recovery, operability, deployment/startup controls, incident chains, or bounded resilience tests. Do not infer this lens from testability, safe-change work, routine rollout verification, local API design, ordinary errors, in-process concurrency, service/database calls, or money/transactions.` | Skill invocation metadata exposes the distinctive production-failure decisions, requires explicit or demonstrated operational evidence, and rejects testability, routine rollout, local design, incidental infrastructure, and money/transaction context without a separate production-failure decision. Detailed retry, boundary-validation, and resource triggers remain in normal-use guidance rather than becoming independent invocation shortcuts. | `N1-N12` |

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 848 words.
- `SKILL.md`: 1020 words.
- Packaging overhead: 172 words.
- Decision: retain the source-driven exception. The canonical mini already exceeds the 500-word target, every mini rule remains required for complete ordinary use, and the documented soft-target overage preserves explicit ordinary stopping, mandatory disputed/hotspot retrieval, and one bounded post-body unresolved route. It remains below the 200-word hard maximum. Do not paraphrase rules or compress routing merely to reduce this count.

## Evaluation Environment

- Runner: `_skill-workbench/scripts/run_skill_eval.py` with explicit `--model gpt-5.4`; every run is ephemeral, read-only, ignores user configuration, forbids canonical-rule discovery, and records only the answer, selected project skills, consulted runtime files, and reference mode against `_skill-workbench/evaluations/result.schema.json`. The blind solver is not asked to identify recommendations or sources.
- RED control: retroactive baseline in an isolated temporary directory with no repository skills available.
- GREEN workspace: `/Users/jakubtomanik/github/agent-rules-books`. The final money/transaction boundary was held fixed for the E2-only rerun. E1b, E3, and E4 retain the preceding final-boundary evidence by protocol; E1 retains its earlier routing-fix evidence under the frozen contract.
- Codex version recorded by all RED and final GREEN runs: `codex-cli 0.144.1`.
- Live descriptions:
  - `clean-code`: `Clean Code guidance for locally readable, low-surprise implementation. Use when vague names, mixed responsibilities, boolean modes, hidden mutation, flow-narrating comments, schedule/rewrite pressure, or framework/concurrency detail obstructs a scoped change. Do not add it to an explicit refactoring-only audit or legacy-control task unless a separate local-readability decision is requested.`
  - `refactoring`: `Refactoring guidance for behavior-preserving structural change once observable behavior is known or protected. Use when renaming, extracting, moving, splitting, or another current code smell drives a behavior-preserving change. Dependency-seam work whose purpose is to gain first feedback belongs to Legacy Code until control exists.`
  - `release-it`: `Use only when production failure behavior is an explicit objective or demonstrated operational problem, such as deciding failure semantics, demand/capacity limits, blast-radius isolation, degraded service, recovery, operability, deployment/startup controls, incident chains, or bounded resilience tests. Do not infer this lens from testability, safe-change work, routine rollout verification, local API design, ordinary errors, in-process concurrency, service/database calls, or money/transactions.`
  - `working-effectively-with-legacy-code`: `Use only when a semantic change is blocked because current behavior is materially unknown, no trustworthy focused tests exist, or a dependency cannot be observed or substituted. The task must require gaining first feedback before changing behavior. Do not use when observable behavior and operational facts are already supplied, or when first feedback is not blocked.`
- E2 run-time catalog hashes: Clean Code `ffb0bb9542a8ea1253521b8bd8c680c0049cf6343ddde34736f4ad9e480b57fe`; Refactoring `1d267c2fe8249f4f461ffd45d73625103cea2bb581dd4a759f88b0eadaf0b9c6`; Release It! `54df54afb643a63b102d71cd3e18695fa5d44fe89224b6bdaba8442ed51d552f`; Legacy Code `a339aa74e1767a4c96e2882117807dba7e5cb957004a246c265d86b64cd5c3c4`. The same hashes were observed immediately after all three result files were written.
- Post-run catalog note: the Clean Code runtime body changed after the E2 result timestamps to hash `619715f020a45c106acd21d919deb3962b33bd6000b4213b74af92603045d741`; its description did not change, and no E2 run selected or consulted Clean Code. Release It! remained byte-stable, so the later unrelated body edit does not invalidate this routing matrix.

## Evaluation Cases

### E1: Outbound Provider Partial Failure and Overload

- Class: distinctive symptom recognition, application, and pressure.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/outbound-provider.md` (verbatim TypeScript, environment configuration, provider behavior, and deadline pressure).
- Required skills: `{release-it}`.
- Allowed skills: `{designing-data-intensive-applications, code-complete}` when ambiguous payment state or coordinated construction concerns become independently central.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture}`.
- Required order: `release-it` only.
- Reference mode: `ordinary`.
- Expected sections: none; `SKILL.md` must supply the normal-use guidance without opening either reference.
- Forbidden sections: every section of `references/full.md`; `references/index.md` and `references/full.md` must not appear in `consulted_files`.
- Baseline runs: retroactive baseline `019f5334-8508-7873-bc3b-9c4698e4ad9d`, `019f5335-e2e8-7fb3-8d7a-ea2e01b87ffd`, and `019f5335-e30d-7322-a844-9f042f5c744e`. All three found infinite waits, stacked retries, a database transaction held across remote work, unbounded in-memory fallback, and unvalidated responses. Only one run made retry safety/idempotency explicit; none established a complete breaker or fast-failure state, degraded-mode contract, and latency/retry/saturation diagnostic surface.
- Before-routing-fix GREEN: `019f5346-3797-7361-bcfa-b98b90750999`, `019f5347-79d0-7b90-9244-35f71fcd1e31`, and `019f5347-79e4-7c80-8189-b37f9e79d7a3`, preserved byte-for-byte as `green-before-routing-fix-1.json` through `green-before-routing-fix-3.json`.
- Post-skill runs after the routing fix: `019f5354-5e18-7ab1-8dc2-ec6bcb89981d`, `019f5354-5dbf-7f70-b744-e36783e6da5a`, and `019f5354-5dde-7281-a89b-275898f1909e`. All three selected only `release-it`, retained bounded waits, one retry owner, resource release, response validation, bounded fallback, overload isolation, and explicit degraded behavior, and avoided unrelated code-style or architecture work. All three consulted `.agents/skills/release-it/SKILL.md`, `references/index.md`, and `references/full.md` and self-reported `focused` rather than the frozen predeclared `ordinary` mode.
- Final-boundary treatment: E1 was not rerun by protocol. Its routing-fix results remain the current `green-1.json` through `green-3.json` evidence for the frozen expectation; no claim is made that they exercise the final catalog descriptions.
- Behavioral delta: preserve the baseline's strong local findings while making caller/provider retry safety, total bounds, isolation or fast failure, bounded degradation, boundary validation, and production diagnostics a consistent integrated contract. The skill must not broaden this into an unrelated architecture or code-style review.
- Independent source trace:

| Material recommendation | G1 | G2 | G3 | Reviewer trace |
| --- | :---: | :---: | :---: | --- |
| Bound semaphore acquisition and provider calls; propagate cancellation and preserve caller survival. | yes | yes | yes | `M4`, `M16`, `N3`, `N9`; full `Dependency Protection Rules`. |
| Keep one retry owner with safe eligibility, count and total-time bounds, and backoff or jitter. | yes | yes | yes | `M5`, `N4`; full `Dependency Protection Rules` and `Forbidden Patterns`. A payment idempotency key is a justified engineering inference from retry safety, not a standalone source rule. |
| Do not retain the database transaction across slow remote work. | yes | yes | yes | `M10`, `N3`, `N5`; full `Resource Management Rules`. |
| Validate status, content type, parseability, shape, and semantics before persistence. | yes | yes | yes | `M11`, `N7`; full `Runtime State and Restart Safety Rules` and `Data Boundary Rules`. |
| Make fallback capacity finite and define behavior when full; do not rely on unbounded process memory. | yes | yes | yes | `M7`, `M17`, `N3`, `N9`; full `Load and Capacity Rules` and `Forbidden Patterns`. Durability is general judgment needed to make the promised pending state survive restart. |
| Treat concurrency as a deliberate bulkhead and fail fast rather than queueing checkout workers indefinitely. | yes | yes | yes | `M6`, `M7`, `M10`, `M16`, `N5`, `N9`; full `Dependency Protection Rules` and `Load and Capacity Rules`. |
| Add dependency latency, timeout, retry, malformed-response, semaphore-saturation, and pending-queue signals. | yes | partial | yes | `M12`, `N6`, `N9`; full `Operational Visibility Rules`. G2 names dedicated malformed-response metrics/logs but does not enumerate the full saturation surface. |

- Result: **frozen fail** under the original predeclared contract. Discovery, application, and fidelity pass, but disclosure fails `3/3` both before and after the catalog routing fix: the case expected `ordinary` and every valid GREEN run chose `focused`. The artifact describes a reproduced worker-exhaustion load-test incident, which satisfies the runtime router's existing `production hotspot` condition. Its expectation is intentionally not rewritten post hoc; E1b supplies the separate routine ordinary-mode proof.

### E1b: Routine Outbound Carrier Quote

- Class: ordinary distinctive-symptom recognition and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/routine-outbound.md` (verbatim TypeScript, environment configuration, and provider contract for a first-release pre-merge review with no incident, dispute, failed load test, or known hotspot).
- Required skills: `{release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: `release-it` only.
- Reference mode: `ordinary`.
- Expected sections: none; the complete normal-use answer must come from `.agents/skills/release-it/SKILL.md` alone.
- Forbidden sections: every full-reference section; neither `references/index.md` nor `references/full.md` may appear in `consulted_files`.
- Baseline runs: retroactive skill-disabled runs `019f5350-d415-7ac3-b387-b76b660fc883`, `019f5350-d437-7c80-b4f7-8a3dae19bf0d`, and `019f5350-d42a-79e1-9d2f-c2a5d093498f`. All three bound the semaphore/connect/response path to caller cancellation, preserved the explicit no-retry policy, distinguished provider `4xx` contract failures from `429`/`5xx`/timeout/transport unavailability, and validated the successful response contract. None treated `CARRIER_MAX_IN_FLIGHT=32` as an intentional bulkhead with explicit saturation/full behavior, and none required carrier latency, timeout, unavailable-outcome, or slot-saturation signals.
- Before-final-boundary GREEN: `019f5357-aed8-7d53-befb-a2945ec0f3e0`, `019f5357-aedd-7eb2-8688-4818024fa61b`, and `019f5357-aef1-71e1-be2f-2bf0c74b9d0a`, preserved byte-for-byte as `green-before-final-boundary-fix-1.json` through `green-before-final-boundary-fix-3.json`. All three selected only `release-it`, self-reported `ordinary`, and consulted only the runtime Release It! `SKILL.md`.
- Final-boundary GREEN: `019f5361-8af0-79e2-a957-dc9ccaf576e6`, `019f5361-8b32-7ad0-b8b8-129f2ca9f884`, and `019f5361-8b3f-77a0-9762-5433af7508fd`. All three selected only `release-it`. G1 and G3 self-reported `focused` and consulted the runtime `SKILL.md`, `references/index.md`, and `references/full.md`; G2 self-reported `ordinary` and consulted only the runtime `SKILL.md`. Every consulted path is inside the repository's `.agents/skills` tree.
- Behavioral delta: preserve the baseline's correct timeout/cancellation, no-retry, failure-classification, degraded-outcome, and response-validation guidance while consistently adding deliberate bulkhead capacity/full behavior and a minimal dependency/saturation diagnostic surface. Do not broaden into an incident investigation, comprehensive audit, or unrelated code-shape review.
- Independent source trace:

| Material recommendation | G1 | G2 | G3 | Reviewer trace |
| --- | :---: | :---: | :---: | --- |
| Bound semaphore acquisition, connect, and response time to the checkout budget and propagate cancellation. | yes | yes | yes | `M4`, `M16`, `N3`, `N9`; `Failure Semantics and Dependency Protection` in runtime `SKILL.md`. |
| Preserve the explicit no-retry request-path policy. | yes | yes | yes | `M5`, `N4`; the existing no-retry choice is consistent with safe retry eligibility and total-time bounds. |
| Return the declared unavailable outcome on saturation, timeout, `429`, `5xx`, and transport failure. | yes | yes | yes | `M2`, `M6`, `M16`, `N2`, `N5`; visible degradation, caller survival, and fast failure in runtime `SKILL.md`. |
| Treat the semaphore as a finite bulkhead and define full behavior with a bounded acquire. | yes | yes | yes | `M6`, `M7`, `M10`, `M16`, `M17`, `N3`, `N5`, `N9`; `Failure Semantics and Dependency Protection` plus `Demand, Capacity, and Workflows`. |
| Validate HTTP status, content type, parseability, amount, currency, and expiry before returning an available quote. | yes | yes | yes | `M11`, `M20`, `N7`, `N8`; `Boundaries, Contracts, and Diagnosis`. |
| Distinguish provider `4xx` and invalid-success contract failures from routine dependency unavailability. | yes | yes | yes | `M11`, `M20`, `N7`, `N8`; explicit material failure modes and retryability. Exact logging severity is general judgment. |
| Make persistent contract failures visible through distinct logs or metrics. | yes | yes | yes | `M12`, `N6`, `N9`; `Boundaries, Contracts, and Diagnosis`. The answers do not consistently enumerate latency, timeout, unavailable-result, and slot-saturation metrics. |

- Result: **fail current ordinary disclosure**, with discovery, application, scope, and fidelity passing `3/3`. Only G2 satisfies the predeclared `ordinary` contract; G1 and G3 unnecessarily escalate a case that explicitly excludes an incident, failed load test, disputed policy, and known production hotspot to focused reference loading. The before-final-boundary matrix passed ordinary disclosure `3/3`, so the final catalog boundary exposes a routing-stability regression rather than an application or source-fidelity failure. Every final answer still adds deliberate bulkhead/full behavior and distinct contract-failure visibility while preserving RED's correct timeout, no-retry, classification, degradation, and validation guidance. The complete saturation metric inventory remains too unstable to claim as an observed E1b delta.

### E2: Supervised Consumer Poison and Dependency Failures

- Class: ambiguous neighbor, application, pressure, and focused retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/supervised-consumer.md` (verbatim TypeScript, queue and supervisor configuration, broker semantics, and staging incident evidence).
- Required skills: `{release-it}`.
- Allowed skills: `{designing-data-intensive-applications}` only when explicitly invoked for the independently central replay/idempotency contract.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture, code-complete}`.
- Required order: `release-it` only.
- Reference mode: `focused`.
- Expected sections: bounded allowed set of `Dependency Protection Rules`, `Load and Capacity Rules`, `Data Boundary Rules`, `Operational Visibility Rules`, `Forbidden Patterns`, `Testing Rules`, and `Final Instruction`; `Load and Capacity Rules` is required because it contains the controlling let-it-crash condition and poison-message handling.
- Forbidden sections: every other full-reference section, including `Production Readiness and Release Risk Rules`, `Runtime State and Restart Safety Rules`, `Deployment and Startup Rules`, `Interconnect, Routing, Security, and Chaos Rules`, `API and Contract Rules`, `Cache Rules`, and `Code Generation Rules`.
- Baseline runs: retroactive baseline `019f5335-e2e8-7aa2-ab76-a39a1d4065eb`, `019f5335-e2e8-7c03-b589-4a91ddbf4846`, and `019f5337-3596-7822-8543-759eca0c5279`. All three rejected both blanket crash and blanket catch-and-ack, quarantined deterministic poison data, used bounded retry or pause for dependency failure, and reserved process crash for compromised integrity. Across all three, finite `prefetch` or queue capacity, supervisor restart-rate bounds, queue-age/saturation/restart telemetry, and an explicit full-queue policy were absent; readiness/idempotency appeared inconsistently.
- Before-routing-fix GREEN: `019f5347-79ed-7843-a936-6c25b8047289`, `019f5347-7999-78c2-ada3-d351dc2484a5`, and `019f5348-9efd-7c51-9392-73922cfbd857`, preserved byte-for-byte as `green-before-routing-fix-1.json` through `green-before-routing-fix-3.json`; all three selected only `release-it`.
- Before-final-boundary GREEN: `019f5354-5ea7-70d1-8b8e-a715b6213843`, `019f5355-d69f-7882-ab0c-a6f13f7e46c7`, and `019f5355-d5ae-75b0-9947-b56e7dbd25a3`, preserved byte-for-byte as `green-before-final-boundary-fix-1.json` through `green-before-final-boundary-fix-3.json`. G1 and G3 selected only `release-it`; G2 selected both `release-it` and forbidden `working-effectively-with-legacy-code` and loaded both runtime packages despite having no behavior-uncertainty, characterization, seam, or blocked-observation reason for the extra lens.
- Before-money-boundary GREEN: `019f5361-8ae1-73b2-af1a-308f5d795a97`, `019f5362-e915-7d82-a5aa-25b683c2d80c`, and `019f5362-e906-7681-b63e-162cc1ff3a1b`, preserved byte-for-byte as `green-before-money-boundary-fix-1.json` through `green-before-money-boundary-fix-3.json`. All three selected only `release-it`, self-reported `focused`, consulted only the runtime Release It! `SKILL.md`, `references/index.md`, and `references/full.md`, and preserved the nuanced operational boundary.
- Final money-boundary GREEN: `019f536c-9125-7422-89a2-c50de8cab5d3`, `019f536c-90e4-7b71-9f79-6e24d6a6a04d`, and `019f536c-912e-70a1-8155-5ce17c7eb4c9`. All three selected required `release-it` and self-reported `focused`. G1 also selected forbidden `working-effectively-with-legacy-code` and consulted that runtime package's `SKILL.md`, index, and full reference; its answer contains no characterization, seam, first-feedback, or behavior-uncertainty recommendation that needs the Legacy Code lens. G2 and G3 selected and consulted only Release It!. Every consulted path is inside the repository's `.agents/skills` tree. G3 weakens the required failure boundary by treating malformed `200` JSON from the inventory dependency as a reason to quarantine the original queue message rather than as a dependency contract failure eligible for bounded retry and pause.
- Behavioral delta: retain the correct three-way boundary but consistently connect it to supervised and isolated crash safety, finite queue and redelivery bounds, dependency timeout/backoff/pause behavior, durable quarantine, readiness or pause visibility, restart-storm containment, and tests of broker disposition. The focused read must remain below one-third of the 22 full sections.
- Independent source trace:

| Material recommendation | G1 | G2 | G3 | Reviewer trace |
| --- | :---: | :---: | :---: | --- |
| Separate malformed-message, dependency-failure, and compromised-process outcomes. | yes | yes | partial | `M8`, `M11`, `M16`, `N5`, `N7`; full `Load and Capacity Rules`, `Dependency Protection Rules`, and `Data Boundary Rules`. G3 separates the broad classes but assigns one dependency-response defect to message quarantine. |
| Quarantine deterministic poison data durably, then ack; never crash-loop or silently drop it. | yes | yes | yes | `M7`, `M11`, `M17`, `N7`, `N9`; full `Load and Capacity Rules`, `Data Boundary Rules`, and `Forbidden Patterns`. Durable publish-before-ack is general judgment that preserves the source's anti-poisoning requirement. |
| Use a finite dependency timeout, one bounded retry layer with backoff or jitter, then pause or requeue without ack. | yes | yes | yes | `M4-M6`, `M16`, `N3-N5`, `N9`; full `Dependency Protection Rules` and `Final Instruction`. |
| Let the process crash only when continuing or deciding disposition is unsafe, under supervision and isolation. | yes | yes | yes | `M8`, `N5`; full `Load and Capacity Rules`. |
| Replace unlimited delivery attempts with finite redelivery and explicit exhausted-message behavior. | yes | yes | yes | `M7`, `M17`, `N3`, `N9`; full `Load and Capacity Rules` and `Forbidden Patterns`. |
| Make pause or breaker state visible through readiness while avoiding restart churn. | yes | yes | yes | `M12`, `M19`, `N6`, `N9`; full `Operational Visibility Rules`. G3's liveness-during-pause detail is general judgment that preserves the selected pause state. |
| Treat malformed success data from the inventory dependency as a dependency contract failure, not poison in the original broker message. | yes | yes | no | `M11`, `M16`, `M20`, `N7`, `N8`; full `Dependency Protection Rules`, `Data Boundary Rules`, and `API and Contract Rules`. The exact disposition is case-specific engineering judgment; quarantining the unrelated original message loses a potentially recoverable delivery. |
| Test broker disposition for poison, dependency, fatal, and sustained-outage cases. | no | yes | yes | Full `Testing Rules`; `M15` supplies the bounded production-failure-test constraint. G1 asks for a safe, testable policy but does not specify disposition tests. |
| Make redelivery after commit but before ack duplicate-safe. | yes | yes | no | `M5` retry-safety pressure plus general judgment; event-ID uniqueness is not presented as a standalone Release It! rule. |
| Lower prefetch to reduce unacked crash blast radius. | no | no | no | `M6`, `M8`, `M10`, `M17`, `N5`, `N9`; all three discuss the current prefetch blast radius, but none recommends a lower value. Exact prefetch is general judgment. |
| Cap supervisor restart churn. | yes | yes | no | `M6`, `M8`, `N5`; exact restart-rate and backoff values are general judgment. |

- Result: **fail under the final money boundary**. Required Release It! selection and focused disclosure pass `3/3`, but catalog discovery passes only `2/3` because G1 selects forbidden Legacy Code without a qualifying safe-change-control decision. Case-specific application passes only `2/3` because G3 quarantines the original message for malformed dependency success data. The money/transaction-only negative does not address either failure surface in this non-money E2 case. The preserved pre-money matrix passed `3/3`, so the current failure is recorded rather than hidden by the prior result. Exact prefetch and supervisor restart-rate tuning remain unstable implementation details and must not become skill guidance.

### E3: Pure Local Function Rename and Split

- Class: pair-specific negative and near-neighbor discovery.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/local-function.md` (verbatim pure TypeScript function and explicit absence of I/O, global state, concurrency, or distribution).
- Catalog contract revision: the final catalog assigns the requested local-readability decision to `clean-code` and explicitly permits `refactoring` when renaming or splitting drives a behavior-preserving change. Missing test details alone do not invoke Legacy Code. This E3 contract follows that current catalog; only E1 remains intentionally frozen.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}`.
- Forbidden skills: `{release-it, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: none.
- Reference mode: `ordinary`.
- Expected sections: none; the selected Clean Code and Refactoring runtime bodies are sufficient.
- Forbidden sections: every full-reference section; no index or full reference may appear in `consulted_files`.
- Baseline runs: retroactive baseline `019f5337-3589-7cd3-a125-9263d49d30ee`. It renamed the function, split validation/normalization/calculation, and preserved errors and clamping behavior without adding production mechanisms.
- Before-routing-fix GREEN: `019f5348-9f9c-7793-8596-245e86005e23`, preserved byte-for-byte as `green-before-routing-fix-1.json`; it selected `{clean-code, refactoring}` and used ordinary skill bodies.
- Before-final-boundary GREEN: `019f5355-d69b-7b31-a523-5ff81781911d`, preserved byte-for-byte as `green-before-final-boundary-fix-1.json`. It selected only required `clean-code`, consulted its runtime `SKILL.md`, index, and full reference, self-reported `focused`, and preserved the behavior while introducing no Release It! or Legacy Code mechanisms.
- Final-boundary GREEN: `019f5362-edce-7ef2-aec4-d05bee43f715`. It selected required `clean-code` and allowed `refactoring`, consulted only the two runtime `SKILL.md` files, self-reported `ordinary`, preserved error text, defaulting, clamping, arithmetic, and public-API compatibility, and introduced no Release It! or Legacy Code mechanisms.
- Behavioral delta: discovery and catalog discrimination only. GREEN should retain the same local result, select `clean-code` with `refactoring` neutral if justified, and never introduce Release It! failure/capacity/deployment machinery or Legacy Code safe-change control without uncertainty evidence.
- Independent source trace:
  - Rename `doIt`, `x`, and `p` to expose intent and split validation, normalization, and calculation -> `.agents/skills/clean-code/SKILL.md` local-reasoning, naming, and single-responsibility guidance plus `.agents/skills/refactoring/SKILL.md` behavior-preserving rename and split guidance.
  - Preserve error text, defaulting, clamping, arithmetic, and exported behavior while making the structural change -> the Clean Code cleanup-scope rule and Refactoring's requirement that observable behavior be known or protected.
  - No Release It! recommendation appears; non-selection matches the Release It! description's requirement that production survivability be central.
- Result: **pass under the final catalog contract**. The required and allowed skill sets, ordinary disclosure, local scope, and Release It!/Legacy non-selection match. Refactoring's return is permitted because the prompt explicitly requests a behavior-preserving rename and split; it is not evidence for Legacy Code. Both historical matrices remain preserved to show the catalog-boundary changes.

### E4: Complete Pre-Launch Release It! Audit

- Class: direct invocation and comprehensive retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/comprehensive-audit.md` (verbatim service topology and operational configuration spanning dependencies, demand, queues, cache, startup, deployment, health, jobs, controls, observability, and resilience validation).
- Required skills: `{release-it}`.
- Allowed skills: `{designing-data-intensive-applications}` only when explicitly invoked for the independently central data-system audit.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture, code-complete}`.
- Required order: `release-it` only.
- Reference mode: `comprehensive`.
- Expected sections: all 22 level-two sections of `references/full.md`, read end to end; `consulted_files` must include `SKILL.md` and `references/full.md` and recommendation support must span early, middle, and final headings.
- Forbidden sections: none inside the Release It! reference; bounded focused routing is insufficient for this explicit complete-lens request.
- Baseline runs: retroactive baseline `019f5337-3589-7b91-a39b-bd19a0746372`. It produced a strong launch-blocker audit covering payment safety, overload, isolation, migrations, readiness, controls, queues, observability, cache, and resilience tests, but had no exhaustive canonical retrieval and omitted the three synchronized hourly jobs despite the artifact making that concentrated-demand risk explicit.
- Before-routing-fix GREEN: `019f5348-a252-74c1-8f88-96cdd74db8f5`, preserved byte-for-byte as `green-before-routing-fix-1.json`.
- Before-final-boundary GREEN: `019f5355-d6a2-7983-9529-b436a2ed5274`, preserved byte-for-byte as `green-before-final-boundary-fix-1.json`. It selected only `release-it`, consulted the runtime `SKILL.md` and full reference, self-reported `comprehensive`, retained risk prioritization, and caught the synchronized top-of-hour job concentration omitted by RED.
- Final-boundary GREEN: `019f5362-e902-7dc3-8628-c47db924e13c`. It again selected only `release-it`, consulted only the runtime `SKILL.md` and full reference, self-reported `comprehensive`, retained risk prioritization, and caught the synchronized top-of-hour job concentration omitted by RED.
- Behavioral delta: add demonstrable end-to-end retrieval and source-grounded completeness, including scheduled-work pacing and every applicable final-check category, without displacing the baseline's risk prioritization with a flat checklist.
- Independent source trace:

| Material recommendation | Reviewer trace |
| --- | --- |
| Bound payment deadlines, remove stacked retries, and make ambiguous money outcomes explicit. | `M4`, `M5`, `M16`, `M20`, `N3`, `N4`, `N9`; full `Dependency Protection Rules` and `API and Contract Rules`. Payment-intent deduplication is general judgment required to satisfy retry safety. |
| Add admission control, finite queues, reserved checkout capacity, and value-aware shedding. | `M7`, `M17`, `N3`, `N9`, `N11`; full `Load and Capacity Rules`. |
| Bound payment fallback delivery attempts, add dead-letter handling, and expose replay controls. | `M7`, `M13`, `M17`, `M22`, `N8-N10`; full `Load and Capacity Rules` and `Incidents, Capacity, and Runtime Control`. |
| Make migration and rollout restartable, compatible, staged, visible, and recoverable. | `M3`, `M9`, `M13`, `M18`, `M19`, `N6`, `N10`; full `Production Readiness and Release Risk Rules`, `Runtime State and Restart Safety Rules`, and `Deployment and Startup Rules`. |
| Isolate analytics, payment workers, and synchronous checkout resources. | `M6`, `M10`, `M14`, `N5`, `N11`; full `Dependency Protection Rules`, `Resource Management Rules`, and `Interconnect, Routing, Security, and Chaos Rules`. |
| Authorize, audit, isolate, and test administrative controls and emergency stop. | `M13`, `M15`, `M22`, `N8`, `N10`, `N12`; full `Incidents, Capacity, and Runtime Control` and `Interconnect, Routing, Security, and Chaos Rules`. |
| Make readiness meaningful and add dependency, queue, retry, breaker, saturation, version, and correlation signals. | `M12`, `M19`, `N6`, `N9`; full `Operational Visibility Rules` and `Deployment and Startup Rules`. |
| Define cache authority/outage behavior and prevent miss storms during rebuild. | `M14`, `M17`, `N7-N9`; full `Cache Rules`. |
| Stagger or pace the three top-of-hour jobs and expose overlap/backlog. | `M14`, `M17`, `N8`, `N11`; full `Scheduled and Background Work Rules`. This is the explicit GREEN improvement over RED. |
| Verify dependency failure, overload, queue saturation, migration restart, controls, and bounded chaos before launch. | `M15`, `M21`, `M22`, `N10`, `N12`; full `Testing Rules`, `Review Checklist`, and `Final Instruction`. |

- Result: **pass under the final catalog boundary**. Direct invocation, comprehensive disclosure, source-grounded breadth, risk prioritization, and the required RED-to-GREEN completeness delta all match.

## Evaluation Protocol Status

- RED baseline: complete as a labeled retroactive skill-disabled control using the same five durable raw-artifact cases, `gpt-5.4`, and read-only configuration as GREEN. E1b has three complete baselines; no baseline was rerun or replaced after the description change.
- GREEN evidence: eight valid pre-routing-fix results are preserved under `green-before-routing-fix-*.json`, eight under `green-before-final-boundary-fix-*.json`, and the three immediately preceding E2 results under `green-before-money-boundary-fix-*.json`. Eleven files remain current under `green-*.json`: three retained E1 runs, three retained E1b runs, three final-money-boundary E2 runs, and one retained run each for E3 and E4. Every result uses `gpt-5.4`, exits successfully, matches its case hash, and consults only runtime paths under the repository's `.agents/skills` tree.
- Stability: E1 remains focused `3/3` against its frozen ordinary contract. E1b selects only Release It! but satisfies ordinary disclosure only `1/3`. Final-money-boundary E2 selects required Release It! and focused mode `3/3`, but selects forbidden Legacy Code in G1 and misclassifies malformed dependency success data in G3. E3 passes with required Clean Code and allowed Refactoring in ordinary mode. E4 remains Release It!-only and comprehensive.
- Fidelity trace: completed independently by the reviewer after each result. Solver output contains no source-trace request. Material recommendations are mapped above to `M*`, `N*`, full headings, or explicitly labeled general judgment.
- Acceptance under current process: **closed as failed under the current catalog**. Frozen E1 remains a documented case-contract failure and E1b remains its replacement ordinary-mode case, but E1b passes disclosure only `1/3`. E2 passes required Release It! selection and focused disclosure `3/3` but passes catalog discovery and case-specific application only `2/3`. E3 and E4 pass. No expectation was weakened post hoc and no runtime skill was edited during the retrofit.

### E1c: One Optional Outbound Deadline

- Class: ordinary disclosure replacement; calibration control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/ordinary-outbound-deadline.md`.
- Required skills: `{release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: `release-it` only.
- Reference mode: `ordinary`.
- Expected sections: none; the Release It! body is sufficient for one optional outbound deadline.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: three retained baselines already found the missing deadline; this is disclosure calibration rather than behavioral RED.
- Post-skill runs: retained four-skill GREEN passed `3/3`; rerun against the seven-skill catalog.
- Behavioral delta: preserve the smallest finite deadline and unavailable fallback without widening into data, architecture, or broad construction guidance.
- Source trace: Release It! ordinary dependency-deadline and degradation guidance.
- Result: current-catalog rerun pending.

## Independent Review

- Reviewer: parent conversion reviewer, separate from the conversion worker.
- Catalog snapshot: `clean-code`, `release-it`, `refactoring`, and `working-effectively-with-legacy-code`.
- Semantic verdict: Release It! operational scope and source-preserving guidance remain coherent; no canonical rule was reworded, strengthened, or imported from another skill. The final money/transaction-only negative accurately narrows invocation but is orthogonal to E2. Current evidence still exposes an unstable ordinary/focused boundary in E1b, stochastic Legacy Code over-selection in E2, and one E2 dependency-response classification error.
- Unsupported or altered guidance: none at book-rule level. Idempotency keys, event-ID uniqueness, exact prefetch, restart caps, and durable publish-before-ack are recorded as engineering inferences from retry safety, isolation, and blast-radius rules rather than attributed as verbatim Release It! rules. G3's decision to quarantine the original message for malformed dependency success data is recorded as an unsupported case-specific application, not as skill guidance.
- Closure findings: the runtime Release It! router's `focused ambiguity` condition needs a more explicit evidence threshold if ordinary E1b disclosure must be stable. The Legacy Code catalog boundary must distinguish uncertainty about the desired failure policy from materially uncertain current behavior; E2 G1 needs no safe-change-control lens. Stabilizing the malformed-response disposition may require a source-supported clarification that malformed broker messages and malformed dependency responses are different failure owners. No further run is queued in this closure, and E2's required/forbidden sets remain unchanged.

## Validation Evidence

- Structural validation: Fresh `validate_conversion.py release-it` passed on 2026-07-12: 69-line, 1003-word `SKILL.md` with 155 words of packaging overhead; valid folder/name/frontmatter shape; direct one-level links to both references; no runtime-package placeholders or auxiliary docs; explicit ordinary/focused/comprehensive routes; complete `N1-N12` and `M1-M22` mappings; and all 22 full-reference sections indexed. Official `skill-creator/scripts/quick_validate.py` also passes through `uv run --with pyyaml`.
- YAML and metadata validation: Ruby/Psych parsed both YAML documents. Frontmatter keys were exactly `name` and `description`; `short_description` was within 25-64 characters; `default_prompt` contained `$release-it`; and `policy.allow_implicit_invocation` was boolean `true`.
- Wording fidelity: `python3 _skill-workbench/scripts/check_rule_wording.py --mini release-it/release-it.mini.md --skill .agents/skills/release-it/SKILL.md` passed with 22 mini rules, 22 skill guidance rules, 22 exact matches, zero missing/reworded rules, zero added/reworded rules, and `wording fidelity: exact`. A separate multiset comparison also confirmed all 30 mini bullets, including the eight final checks, match exactly; the primary bias matches verbatim.
- Full-reference equality: `cmp -s` passed. Both files have SHA-256 `ac72b846e9584f376090c8508b2bc66f557ea8d14195ea3b20e15a66b27c4aec`.
- Index validation: Passed deterministic comparison of all 22 level-two full headings against index names, GitHub-style anchors, and ranges beginning at each heading and ending at the last non-empty line before the next level-two heading or EOF; every `Read when` cell is nonempty. The index is the single source of truth for section routing.
- Harness validation: The final runner schema has no recommendation or source fields. All 11 repository script tests pass. All 30 preserved and current GREEN results consult only runtime `.agents/skills` packages; no canonical rule, workbench, compatibility, or evaluation path appears. Absolute runtime paths, where present, resolve under the same repository `.agents/skills` root.
- Invocation evaluation: Retained E1 and E1b select only `release-it` in all six current runs; E4 selects only `release-it`; E3 selects required `clean-code` plus allowed `refactoring`; final-money-boundary E2 selects required `release-it` in all three runs and adds forbidden Legacy Code in G1.
- Application evaluation: E1b consistently adds deliberate bulkhead/full behavior and distinct contract-failure visibility while preserving strong RED guidance, but its disclosure mode is unstable. E1 preserves its source-supported operational decisions. E2 G1 and G2 preserve the required failure boundary; G3 incorrectly quarantines an original message for malformed dependency success data. E3 remains local and behavior-preserving. E4 again finds the scheduled-demand concentration omitted by RED.
- Reference-routing evaluation: E1b ordinary routing passes `1/3`; E1 remains focused `3/3` against its frozen ordinary expectation; final E2 focused routing passes `3/3`; E3 uses ordinary Clean Code and Refactoring bodies; E4 comprehensive routing passes `1/1`.
- Catalog review: The final descriptions are recorded exactly. E2 was the only case rerun for the money/transaction narrowing; E1b, E3, and E4 evidence was preserved as instructed. Money-only over-selection is narrowed in metadata, but the non-money E2 matrix still exposes forbidden Legacy Code co-selection.
- Remaining risks: The live catalog does not yet contain DDIA, Clean Architecture, Code Complete, or the other planned book skills, so their retry/queue/cache/API collisions remain unevaluated. `consulted_files` records file paths and the solver reports the tier, but not exact full-reference line ranges; focused section precision is reviewer-inferred from the answer rather than tool-instrumented. E1b remains a multi-concern disclosure-boundary warning, and exact prefetch or supervisor restart-rate advice remains implementation judgment.

## 2026-07-12 Final Retrofit Reconciliation

This section supersedes every earlier use of `current` above while retaining all intermediate files as evidence of the fixes.

- Hotspot E1 selected only `release-it` and used focused disclosure in `3/3` final runs: `019f55bf-699c-7ab2-87fb-0132f7a9e30b`, `019f55bf-695e-7c03-9b9b-99c4e7de27a5`, and `019f55bf-697e-76a3-9b10-3d9cbe54c301`.
- Supervised-consumer E2 selected only `release-it`, used focused disclosure, and classified malformed downstream `200` JSON as dependency failure rather than poison input in `3/3`: `019f55c5-9695-7fa1-9ade-4537fcaecf09`, `019f55c5-9694-7d22-90c6-c0253e2c1f7f`, and `019f55c5-96ec-76c0-9d12-e15498b30ea1`.
- E3 excluded Release It! for local behavior-preserving work; E4 selected only Release It! and read the full reference comprehensively.
- E1b's multi-concern carrier fixture selected Release It! `3/3` but used ordinary disclosure `2/3` and focused disclosure `1/3`. Its frozen ordinary-only contract is retained as a case-shape warning, not treated as a reason to weaken the router or compress guidance.
- E1c, `_skill-workbench/evaluations/cases/release-it/ordinary-outbound-deadline.md`, is the replacement ordinary-disclosure control. All three baselines already found the missing timeout, so it is explicitly disclosure calibration rather than a behavioral RED. All three GREEN runs selected only Release It! and used `SKILL.md` alone: `019f55d5-f5ad-7842-a61f-17c398300700`, `019f55d5-f56e-7a10-afe5-93e84eb6a264`, and `019f55d5-f5de-7f13-981f-f01b678903f0`.
- The 155-word packaging overhead is accepted under the documented 150-word soft target and 200-word hard maximum. The clearer wording is preferable to an arbitrary four-word compression.
- Final acceptance: **pass** using E1c for ordinary disclosure and E1b as preserved ambiguity evidence. No Release It! pilot rewrite is required before the next conversion batch.
