# Designing Data-Intensive Applications Skill Mapping

## Scope

- Distinctive lens: make distributed data contracts explicit and correct across ownership, consistency, durability, visibility, replay, ordering, evolution, derived representations, replication, partitioning, transactions, and coordination.
- Intended invocation: select only when one or more of those data semantics, including cross-system writes or side effects, are central to the task or block a correct decision. A queue, cache, retry, database, or production failure is not sufficient by itself.
- Closest neighboring skills: `release-it` owns production survivability, overload, isolation, degradation, recovery, operability, and deployment/runtime controls; `clean-architecture` owns policy independence, inward dependencies, ports, adapters, and replaceable details. They co-invoke only when the task independently contains their concern and a DDIA data-contract decision. `code-complete` may accompany substantial multi-concern construction, but ordinary data work or DDIA review does not qualify for it automatically.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`. Manual-only metadata and description gating were not enforced by the repo-local runtime. The positive central-data-semantics threshold is therefore the enforceable boundary; source-grounded focused/comprehensive retrieval is the retained package value despite strong unnamed baselines.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Ownership and consistency | `source-of-truth ownership, consistency/durability` | Ordinary database use or local persistence mechanics with no open authority, durability, visibility, staleness, or conflict decision. |
| Replay, ordering, evolution, and derived data | `replay/order, schema evolution, derived repair` | Mere use of a queue, retry, cache, event, or API when duplicate, replay, order, compatibility, authority, and rebuild semantics are already fixed or irrelevant. |
| Cross-system effects, topology, and coordination | `replication/partitioning, or cross-system write/side-effect, transaction, or coordination semantics` | In-process concurrency, routine service calls, and production-failure hardening without a distributed data invariant. |
| Positive threshold and neighbor boundary | `are central` plus the explicit queue/cache/retry/database/failure insufficiency clause | `release-it` when operational survival is central and `clean-architecture` when policy/dependency direction is central, while preserving compatible co-invocation when data semantics are independently central. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "A Kafka consumer can commit the database and crash before offset acknowledgment; prove replay and duplicate safety." | `designing-data-intensive-applications` | Retry, replay, durable-success, idempotency, and exactly-once semantics are the central correctness decision. |
| "After a write, the same user is redirected to a follower read; define read-your-writes across lag and failover." | `designing-data-intensive-applications` | Replica staleness and consistency semantics are central. |
| "Bound this stateless gateway's dependency timeout, retry amplification, worker queue, and degraded response after an outage." | `release-it`, not DDIA | Production survival and overload containment are central; no ownership, replay, schema, replica, or derived-data correctness decision exists. |
| "Move pricing policy out of Express and Prisma without changing the supplied local transaction semantics." | `clean-architecture`, optionally `refactoring`, not DDIA | Policy independence and dependency direction are central; persistence is present but its data contract is closed. |
| "Make this payment consumer duplicate-safe and recoverable while containing an observed outage cascade." | `designing-data-intensive-applications` plus `release-it` | Idempotency/durability and runtime failure containment are independent central concerns. |
| "Keep order policy independent of Prisma and Kafka while making database-plus-event publication replay-safe and versioned." | `clean-architecture` plus `designing-data-intensive-applications` | Dependency direction and distributed write/event semantics are independently central. |
| "Implement a new replicated write subsystem while coordinating requirements, data/control shape, defensive boundaries, verification, and integration." | `designing-data-intensive-applications` plus `code-complete` | Distributed data semantics and substantial construction-discipline decisions are independently central. |
| "Rename and extract repeated row mapping in a fully specified PostgreSQL adapter without changing SQL or semantics." | `refactoring`, with `clean-code` allowed; not DDIA | A database appears, but the task is behavior-preserving local structure with no open data-system contract. |
| "Explain what this pure array program prints." | No book skill | The shared catalog-null control has no design, change, data, operational, or architecture decision. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance, final-check | Description ownership/consistency branch; `Data Contracts and Ownership`; final checklist | Promotes complete `M1`, `M7`, and `M19` rules rather than a shortened duplicate. |
| `N2` | description, early-guidance, reference-router | Description positive threshold; `Workload, Storage, Replication, and Partitioning`; focused router | Workload and tool choice stay connected to complete `M3-M5`, `M12`, and `M13` guidance. |
| `N3` | description, early-guidance, final-check | Description derived-data branch; `Data Contracts and Ownership`; final checklist | Promotes complete `M6` and `M20` with authority, lag, observability, repair, and rebuild intact. |
| `N4` | description, early-guidance, final-check | Description replay branch; `Retry, Replay, Ordering, and Data Flow`; final checklist | Promotes complete `M8` and `M22`; exactly-once skepticism remains part of the full rule. |
| `N5` | description, early-guidance, final-check | Description schema branch; `Data Contracts and Ownership`; final checklist | Promotes complete `M11` and `M21` for old/new readers, writers, data, messages, rollout, and migration. |
| `N6` | early-guidance, reference-router, final-check | `Retry, Replay, Ordering, and Data Flow`; focused router; final checklist | Distributed uncertainty remains complete in `M2` and `M15` rather than becoming a detached warning list. |
| `N7` | description, early-guidance, final-check | Description topology/coordination branch; storage/topology and coordination concerns; final checklist | Replication, partitioning, transactions, and coordination remain tied to invariants in complete `M12-M16` rules. |
| `N8` | description, early-guidance, reference-router | Description replay/order branch; `Retry, Replay, Ordering, and Data Flow`; focused router | The complete `M22` trigger carries duplicate, replay, ordering, side-effect, and recovery scope. |
| `N9` | description, early-guidance, reference-router, final-check | Description schema branch; `Data Contracts and Ownership`; focused router; final checklist | The complete `M21` trigger preserves compatibility and migration across every mixed-version participant. |
| `N10` | description, early-guidance, reference-router | Description replication/partitioning branch; `Workload, Storage, Replication, and Partitioning`; focused router | Complete `M23` and `M24` distinguish replica-read semantics from partition locality and skew decisions. |
| `N11` | description, early-guidance, reference-router, final-check | Description coordination branch; `Transactions and Distributed Coordination`; focused router; final checklist | The complete `M26` trigger retains clock, fault-model, quorum, membership, and coordination-dependency requirements. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Data Contracts and Ownership` | Moved verbatim | Leads with the complete source-of-truth, consistency, retry, failure, evolution, and state-classification tradeoff. |
| `M2` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Keeps uncertainty and accepted/persisted/applied/durable distinctions together. |
| `M3` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Keeps workload evidence before architectural change. |
| `M4` | `Data Contracts and Ownership` | Moved verbatim | Co-locates data/query model and ownership choice with authority and service-boundary guidance. |
| `M5` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Preserves storage, index, analytics, amplification, and durability fit as one rule. |
| `M6` | `Data Contracts and Ownership` | Moved verbatim | Stays beside its complete derived-representation trigger `M20`. |
| `M7` | `Data Contracts and Ownership` | Moved verbatim | Stays beside the write-path trigger `M19`. |
| `M8` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Stays beside the retry/job/consumer trigger `M22`. |
| `M9` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Preserves ordering scope and locality without splitting its examples. |
| `M10` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Keeps command/event/log/stream/projection distinctions and consumer requirements whole. |
| `M11` | `Data Contracts and Ownership` | Moved verbatim | Stays beside the compatibility and migration trigger `M21`. |
| `M12` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Stays beside the replica-read trigger `M23`. |
| `M13` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Stays beside the partition trigger `M24`. |
| `M14` | `Transactions and Distributed Coordination` | Moved verbatim | Stays beside the anomaly-to-invariant trigger `M25`. |
| `M15` | `Transactions and Distributed Coordination` | Moved verbatim | Keeps the complete distributed fault and authority assumption set together. |
| `M16` | `Transactions and Distributed Coordination` | Moved verbatim | Keeps agreement mechanisms and their availability/latency cost as one rule. |
| `M17` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Keeps recomputation, time semantics, checkpoints, side effects, and source-to-sink guarantees together. |
| `M18` | `Data Contracts and Ownership` | Moved verbatim | Co-locates service boundaries with ownership and update semantics. |
| `M19` | `Data Contracts and Ownership` | Moved verbatim | Placed directly after `M7` to bind the write-path trigger to write semantics. |
| `M20` | `Data Contracts and Ownership` | Moved verbatim | Placed directly after `M6` to bind the derived-data trigger to authority and rebuild semantics. |
| `M21` | `Data Contracts and Ownership` | Moved verbatim | Placed directly after `M11` to bind contract evolution to its mixed-version trigger. |
| `M22` | `Retry, Replay, Ordering, and Data Flow` | Moved verbatim | Placed directly after `M8` so queue/retry vocabulary cannot lose the duplicate/replay/order/side-effect threshold. |
| `M23` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Placed directly after `M12` for replica-read consistency decisions. |
| `M24` | `Workload, Storage, Replication, and Partitioning` | Moved verbatim | Placed directly after `M13` for partition-locality decisions. |
| `M25` | `Transactions and Distributed Coordination` | Moved verbatim | Placed directly after `M14` to bind isolation choice to named invariants and compensation. |
| `M26` | `Transactions and Distributed Coordination` | Moved verbatim | Placed beside `M15-M16` to preserve the full clock, fault-model, quorum, membership, and coordination-dependency decision. |
| `M27` | `Review and Testing` | Moved verbatim | Remains one complete review scan rather than being fragmented across concern groups. |

## Wording Fidelity

- Verbatim primary bias: exact.
- Verbatim mini rules: all 27 decision and trigger rules are moved whole and exact; no rule is added, omitted, merged, or reworded.
- Verbatim final checklist and order: all ten items are exact and remain in canonical order.
- Documented exceptions: none. Concern headings, description, and reference-router prose are packaging and routing additions, not transformed source rules.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Inline reference map: eight source-backed labels link common focused questions directly to canonical full headings; every other bounded question still uses the exhaustive index. This changes loading only.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 890 words.
- `SKILL.md`: 1,067 words across 82 lines.
- Packaging overhead: 177 words, within the documented 151-200 allowance.
- Description: 497 characters.
- Decision: retain the source-driven exception because the canonical mini already exceeds the 500-word target and every mini rule is required for complete ordinary use. The 27-word soft-target overage keeps the ordinary stop visible and adds eight direct correctness-detail routes without duplicating the exhaustive index. Do not paraphrase canonical guidance to reduce the count.

## Evaluation Cases

The contracts and raw artifacts below preserve the pre-execution record. Their original `not run` fields are historical; the final batch reconciliation at the end of this file supersedes those fields without rewriting frozen contracts.

### E1: Complete distributed data design audit

- Class: direct invocation and comprehensive retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/comprehensive-audit.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `comprehensive`.
- Expected sections: all 26 DDIA level-two sections, read end to end.
- Forbidden sections: every other book skill's reference sections.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: add exhaustive, prioritized treatment of authority, workload, storage, consistency, replay/order, evolution, topology, transactions, derived data, clocks/coordination, processing, boundaries, tests, and repair over any baseline omissions.
- Source trace: `M1-M27`, `N1-N11`, and all 26 full-reference headings.
- Result: predeclared; not executed.

### E2: Ordinary derived search projection

- Class: ordinary application from `SKILL.md` alone.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/ordinary-derived-projection.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `ordinary`.
- Expected sections: none; the DDIA skill body is sufficient.
- Forbidden sections: every full-reference section from every skill.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: make PostgreSQL authority, asynchronous propagation, accepted staleness, lag visibility, durable checkpointing, rebuild, and repair explicit instead of accepting an unrecoverable direct dual-write.
- Source trace: `M6`, `M20`, `N3`; full `Derived Data Rules` only as reviewer support, not expected disclosure.
- Result: predeclared; not executed.

### E3: Focused replica read-after-write dispute

- Class: focused retrieval and distinctive consistency recognition.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/focused-replica-read.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `focused`.
- Expected sections: DDIA `Consistency Rules` and `Replication Rules`.
- Forbidden sections: the other 24 DDIA full sections and every other skill's references.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: turn nearest-replica routing into an explicit read-your-writes contract with commit/applied positions, primary fallback or session routing, and defined failover behavior while retaining bounded staleness for other users.
- Source trace: `M7`, `M12`, `M23`, `N1`, `N7`, `N10`; full `Consistency Rules` and `Replication Rules`.
- Result: predeclared; not executed.

### E4: Exactly-once launch pressure

- Class: distinctive symptom recognition, pressure, and ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/pressure-exactly-once-consumer.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `ordinary`.
- Expected sections: none; the DDIA skill body is sufficient under launch pressure.
- Forbidden sections: every full-reference section from every skill.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: reject broker-level exactly-once as proof across database and email boundaries; require stable identity, idempotent state transitions, replay-safe side effects, ordering scope, and unknown-success recovery despite schedule pressure.
- Source trace: `M2`, `M8-M10`, `M22`, `N4`, `N6`, `N8`; full `Idempotency and Replay Rules`, `Ordering Rules`, and `Event, Log, and Stream Rules` as reviewer support only.
- Result: predeclared; not executed.

### E5: Release It! near-neighbor exclusion

- Class: near-neighbor discovery and pair-specific DDIA negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/release-it-neighbor.md`.
- Required skills: `{release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{designing-data-intensive-applications, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `release-it` only.
- Reference mode: `ordinary`.
- Expected sections: none; the Release It! skill body is sufficient.
- Forbidden sections: all DDIA references and every other non-required skill reference.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: preserve Release It! ownership of timeout/retry amplification, finite queue and worker capacity, isolation, load shedding, degraded response, health, and saturation telemetry without importing source-of-truth or replay machinery.
- Source trace: Release It! `M4-M10`, `M12`, `M16-M17`, `M19`, `N3-N6`, `N9`; DDIA non-selection follows the positive central-data-semantics threshold.
- Result: predeclared; not executed.

### E6: Clean Architecture near-neighbor exclusion

- Class: near-neighbor discovery and pair-specific DDIA negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/clean-architecture-neighbor.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{refactoring}`.
- Forbidden skills: `{designing-data-intensive-applications, release-it, code-complete, clean-code, working-effectively-with-legacy-code}`.
- Required order: `clean-architecture` before allowed structural refactoring.
- Reference mode: `ordinary`.
- Expected sections: none; the Clean Architecture runtime body and optional Refactoring body are sufficient.
- Forbidden sections: all DDIA references and every other non-required skill reference.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: move pricing policy behind inward-owned ports and humble adapters while preserving the supplied local transaction; do not invent consistency, replay, replication, schema, or derived-data work merely because Prisma is present.
- Source trace: Clean Architecture `M2-M7`, `M12-M14`, `N1-N4`; DDIA non-selection follows the positive central-data-semantics threshold.
- Result: predeclared; not executed.

### E7: DDIA and Release It! compatible overlap

- Class: compatible co-invocation, focused retrieval, and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/release-it-compatible-overlap.md`.
- Required skills: `{designing-data-intensive-applications, release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: none; data correctness and production survival govern separate required decisions.
- Reference mode: `focused`.
- Expected sections: DDIA `Reliability Rules`, `Idempotency and Replay Rules`, and `Transaction Rules`; Release It! `Dependency Protection Rules`, `Load and Capacity Rules`, `Operational Visibility Rules`, and `Incidents, Capacity, and Runtime Control`.
- Forbidden sections: every other DDIA and Release It! full section and all other skills' references.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: combine a stable invoice/payment idempotency and durable recovery contract with finite timeout/retry/capacity, isolation, pause/degradation, readiness, and diagnostic behavior; neither lens substitutes for the other.
- Source trace: DDIA `M2`, `M7-M8`, `M14`, `M19`, `M22`, `N1`, `N4`, `N6`, `N8`; Release It! `M4-M8`, `M10`, `M12`, `M16-M17`, `M19`, `N3-N6`, `N9` and the seven named full sections.
- Result: predeclared; not executed.

### E8: DDIA and Clean Architecture compatible overlap

- Class: compatible co-invocation and ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/clean-architecture-compatible-overlap.md`.
- Required skills: `{designing-data-intensive-applications, clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: none; policy independence and distributed write correctness govern separate required decisions.
- Reference mode: `ordinary`.
- Expected sections: none; both runtime bodies are sufficient.
- Forbidden sections: every full-reference section from every skill.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: introduce policy-owned persistence/event ports and outer adapters while preserving one authoritative write, invariant-safe concurrency, atomic publication or repair, stable event identity, replay, and mixed-version compatibility.
- Source trace: DDIA `M1`, `M6-M11`, `M14`, `M18-M22`, `N1`, `N3-N5`, `N8-N9`; Clean Architecture `M2-M7`, `M12-M14`, `N1-N4`.
- Result: predeclared; not executed.

### E9: Database-only structural negative

- Class: pair-specific negative and near-neighbor ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/database-only-refactoring-negative.md`.
- Required skills: `{refactoring}`.
- Allowed skills: `{clean-code}`.
- Forbidden skills: `{designing-data-intensive-applications, release-it, clean-architecture, code-complete, working-effectively-with-legacy-code}`.
- Required order: `refactoring` first if `clean-code` is also selected.
- Reference mode: `ordinary`.
- Expected sections: none; the selected runtime bodies are sufficient.
- Forbidden sections: every full-reference section from every skill.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: preserve local rename/extract scope and exact adapter behavior; database vocabulary alone must not trigger DDIA, Release It!, Clean Architecture, or Legacy Code.
- Source trace: Refactoring `M1-M2`, `M6-M7`, `M11`, `M14`, `N1-N2`, `N5-N6`, `N8`; optional Clean Code local naming and duplication guidance.
- Result: predeclared; not executed.

### E10: DDIA and Code Complete comprehensive overlap

- Class: compatible co-invocation, comprehensive retrieval, and application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/code-complete-compatible-overlap.md`.
- Required skills: `{designing-data-intensive-applications, code-complete}`.
- Allowed skills: `{}`.
- Forbidden skills: `{release-it, clean-architecture, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` establishes data contracts before `code-complete` shapes the implementation slice.
- Reference mode: `comprehensive`.
- Expected sections: all 26 DDIA and all 27 Code Complete full-reference sections, read end to end.
- Forbidden sections: every other book skill's reference sections.
- Baseline runs: not run; parent contract review is required before behavioral execution.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: combine authority, idempotency, replay/order, schema compatibility, partial-write, and derived-rebuild semantics with explicit routine/type boundaries, defensive input handling, error outcomes, focused tests, and a small reviewable integration slice; the several independent concern families require both full references rather than pretending this is ordinary disclosure.
- Source trace: DDIA `M1-M2`, `M6-M11`, `M14`, `M19-M22`, `M27`, `N1`, `N3-N6`, `N8-N9` and all 26 full headings; Code Complete construction context, readable routines/data, defensive boundaries, error semantics, incremental construction, verification guidance, and all 27 full headings.
- Result: predeclared; not executed.

### E11: Shared catalog-null control

- Class: catalog-null negative.
- Prompt or artifact: `_skill-workbench/evaluations/cases/catalog-null.md`; no DDIA-specific duplicate is created.
- Required skills: `{}`.
- Allowed skills: `{}`.
- Forbidden skills: every book skill in the reviewed live catalog, currently `{clean-architecture, clean-code, code-complete, designing-data-intensive-applications, refactoring, release-it, working-effectively-with-legacy-code}`.
- Required order: none.
- Reference mode: `none`.
- Expected sections: none.
- Forbidden sections: every book skill body, index, and full reference.
- Baseline runs: use the existing shared catalog-null baseline only after parent contract review; no new run was made.
- Post-skill runs: not run; GREEN is explicitly prohibited for this conversion handoff.
- Behavioral delta: none; explain the existing output without activating a design or engineering guidance lens.
- Source trace: no book guidance should be used.
- Result: shared predeclared control; not executed for this conversion.

### E5b: Ordinary Release It! Neighbor Replacement

- Class: near-neighbor discovery; ordinary disclosure replacement for E5's incident-hotspot fixture.
- Prompt or artifact: `_skill-workbench/evaluations/cases/release-it/ordinary-outbound-deadline.md`.
- Required skills: `{release-it}`.
- Allowed skills: `{}`.
- Forbidden skills: `{designing-data-intensive-applications, clean-architecture, code-complete, clean-code, refactoring, working-effectively-with-legacy-code}`.
- Required order: `release-it` only.
- Reference mode: `ordinary`.
- Expected sections: none; the Release It! body is sufficient for one routine outbound deadline.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: existing skill-disabled baseline may be reused when its case hash and model match; otherwise rerun before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: require the smallest finite deadline and optional fallback without importing DDIA merely because an outbound call exists.
- Source trace: Release It! ordinary outbound-deadline guidance; DDIA's positive central-data-semantics threshold.
- Result: replacement predeclared; not executed.

### E10b: Focused DDIA and Code Complete Replacement

- Class: compatible co-invocation; focused retrieval; replacement for E10's over-broad comprehensive fixture and forbidden-Clean-Code contract.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/focused-code-complete-overlap.md`.
- Required skills: `{designing-data-intensive-applications, code-complete}`.
- Allowed skills: `{clean-code}` when local routine shape becomes independently central.
- Forbidden skills: `{release-it, clean-architecture, refactoring, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` before `code-complete`.
- Reference mode: `focused`.
- Expected sections: DDIA requires `Reliability Rules`, `Idempotency and Replay Rules`, `Ordering Rules`, and `Derived Data Rules`, with `Testing Rules` allowed; Code Complete requires `Routine Design Rules`, `Defensive Programming Rules`, `Error Handling Rules`, and `Testing Rules`, with `Data Type Rules` and `Incremental Construction Rules` allowed.
- Forbidden sections: every other DDIA and Code Complete section and every forbidden-skill reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: establish authority, replay, ordering, and rebuild semantics before shaping a small typed, defensive, testable implementation slice; avoid unrelated architecture or production-resilience work.
- Source trace: DDIA `M2`, `M6`, `M8-M9`, `M20`, `M22`, `N3-N4`, `N6`, `N8`; Code Complete routine, type, boundary, error, incremental, and testing guidance plus the named full headings.
- Result: replacement predeclared; not executed.

### X1: Explicit Ordinary Acceptance

- Class: explicit invocation; ordinary disclosure.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/manual-ordinary.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, code-complete, clean-code, refactoring, release-it, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `ordinary`.
- Expected sections: none.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: define one derived projection contract from the mini-derived body without extra retrieval.
- Source trace: `M6`, `M20`, `N3`.
- Result: pending.

### X2: Explicit Focused Acceptance

- Class: explicit invocation; focused disputed interpretation.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/manual-focused.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, code-complete, clean-code, refactoring, release-it, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `focused`.
- Expected sections: exactly `Consistency Rules` and `Replication Rules`.
- Forbidden sections: every other DDIA section and every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle read-your-writes, catch-up, and failover from the two bounded source sections.
- Source trace: `M7`, `M12`, `M23`, `N1`, `N7`, `N10` and the named headings.
- Result: pending.

### X2b: Explicit Focused Bounded Replacement

- Class: explicit invocation; focused replacement for X2's narrow subsection contract.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/manual-focused-bounded.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, code-complete, clean-code, refactoring, release-it, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `focused`.
- Expected sections: exactly `Consistency Rules`, `Replication Rules`, and `Distributed Fault, Clock, and Consensus Rules`.
- Forbidden sections: every other DDIA section and every other book reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle read-your-writes and failover under explicit distributed uncertainty from three coherent headings.
- Source trace: `M7`, `M12`, `M15`, `M23`, `N1`, `N6-N7`, `N10` and the named headings.
- Result: pending.

### X3: Explicit Comprehensive Acceptance

- Class: explicit invocation; comprehensive retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/manual-comprehensive.md`.
- Required skills: `{designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, code-complete, clean-code, refactoring, release-it, working-effectively-with-legacy-code}`.
- Required order: `designing-data-intensive-applications` only.
- Reference mode: `comprehensive`.
- Expected sections: all 26 DDIA headings, recorded as `*`.
- Forbidden sections: every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: provide source-grounded end-to-end data-system coverage unavailable to the package-free baseline.
- Source trace: every `M*`, `N*`, checklist item, and full heading.
- Result: pending.

### P1: Manual-Policy Implicit Exclusion

- Class: invocation-policy counterexample; repeated catalog control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/pressure-exactly-once-consumer.md`.
- Required skills: `{}` under the explicit-only policy.
- Allowed skills: `{clean-architecture, code-complete, clean-code, refactoring, release-it, working-effectively-with-legacy-code}` are neutral for this DDIA policy check.
- Forbidden skills: `{designing-data-intensive-applications}`.
- Required order: none.
- Reference mode: `none` for DDIA; other allowed skills follow their own contracts.
- Expected sections: none from DDIA.
- Forbidden sections: every DDIA packaged file.
- Baseline runs: retained unnamed baselines already rejected the shortcut reliably.
- Post-skill runs: not run under the explicit-only policy.
- Behavioral delta: the package must not add automatic context when the user did not invoke it.
- Source trace: invocation policy only.
- Result: pending `3/3` policy probe.

## Independent Review

- Reviewers: independent reverse-trace reviews `019f58a9-d0d9-7153-b03e-e89cd1eedc09`, `019f58ba-0c72-7460-af90-48434c787ef8`, `019f58ca-56d5-7a83-ade1-2a7d4aac7dfc`, and the final acceptance review recorded in `_skill-workbench/BATCH_2_RESULTS.md`.
- Catalog snapshot: all seven live project book skills.
- Semantic verdict: PASS after rule-layer repair. Every active mini/nano/package requirement now reverse-traces to the cited canonical full sections; the semantic index no longer advertises unsupported convergence or fencing guidance.
- Unsupported or altered active guidance: none. Removed details remain documented in `_rule-workbench/designing-data-intensive-applications/traceability.md`.

## Source Repair

- Independent review found plausible DDIA mechanisms in mini/nano that were absent from the canonical full rule. Per the authoritative process, conversion stopped and repaired `_rule-workbench` before regenerating the package.
- Removed or narrowed details include request-rate/data-volume examples, convergence, rollback, warehouse, routing metadata, rebalancing, retention, bootstrap, session semantics, stale-authority behavior, fencing, stale-leader wording, broad anomaly remedies, and a replica/partition trigger that incorrectly applied both branches' requirements together.
- Traceability now cites the actual supporting storage/indexing, transaction, replication, partitioning, and distributed-coordination sections for every retained detail.
- Workbench and released mini/nano copies match exactly; the canonical full rule was not edited.

## Final Batch Reconciliation

- Invocation policy: manual-only metadata and description gating were not enforced by the repo-local runtime. The package therefore uses implicit invocation with the central-data-semantics threshold.
- Current explicit disclosure: `manual-ordinary/green-final-source-1.json` used the body only; `manual-focused-bounded/green-final-source-1.json` read exactly `Consistency Rules`, `Replication Rules`, and `Distributed Fault, Clock, and Consensus Rules`; `manual-comprehensive/green-final-source-1.json` recorded `*` after an end-to-end read.
- Current selection: all six final-source runs selected DDIA exactly as required. The database-only negative selected Refactoring alone in its post-repair control.
- Pressure fixture: `pressure-exactly-once-consumer/green-final-source-{1,2,3}.json` selected required DDIA in `3/3` and correctly rejected cross-boundary exactly-once claims, but read 8, 8, and 14 sections instead of the frozen ordinary contract. No run reported an end-to-end `*` read. The expansion remains a manual tier-collapse diagnostic, especially the 14-section run, rather than an exact-section acceptance failure.
- Solver diagnostics: the explicit runs reintroduced retention/bootstrap, session-token, or fencing mechanisms even though the repaired package does not contain them. Those general solver additions remain preserved and do not justify restoring non-source guidance.
- Baseline timing: package-free baselines ran after draft authoring. They remain optional diagnostic evidence under the current protocol.
- Current-policy status: **accepted conversion**. Source and package semantics pass, every positive current run includes required DDIA, and explicit ordinary/focused/comprehensive mechanics pass. Pressure over-reading and general solver additions remain non-blocking diagnostics.

## Validation Evidence

- Structural validation: 75 lines, 1,049 words, 159 packaging words, all 27 mini and 11 nano IDs mapped, direct one-level reference links, valid metadata, and all 26 full sections indexed.
- Full-reference equality: canonical and runtime copies have matching SHA-256 `8c1bfe1529076fda8f828ed6939b63bc3016830ad3c705071699a250e98b8f25`; byte comparison returned success.
- Index validation: repository validation passes all 26 headings, GitHub anchors, order, and heading-to-last-nonempty ranges, including canonical `---` separators before subsequent level-two headings.
- Wording fidelity: 27/27 exact rules, exact primary bias, and exact final-checklist wording and order.
- Official validator: `/Users/jakubtomanik/.codex/skills/.system/skill-creator/scripts/quick_validate.py` reports `Skill is valid!` through `uv run --with pyyaml`.
- Evaluation contracts: the required-skill contract validator passes; historical allowed/forbidden partitions remain preserved diagnostics.
- Remaining risk: pretrained DDIA knowledge can cause solvers to import mechanisms absent from this repository's canonical rule even when package fidelity is exact.

## Inline Reference Map Evaluation

### RM1: Ordinary derived-projection control

- Contract version: 2
- Class: application and disclosure
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/ordinary-derived-projection.md`
- Fixture SHA-256: `1366abebcdc6d3ef6654c31038a42011a91b4fe79c835bdb99ac97582ccdfc48`
- Required skills: `{designing-data-intensive-applications}`
- Distinctive judgment: Preserve authoritative source data and make the derived projection rebuildable using the compact body alone.
- Neighbor ownership: Clean Architecture may place adapters and Release It! may discuss runtime failure, but data authority and derivation correctness are central.
- Ownership review: PASS - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; fixture blindness, central ownership, and the ordinary tier premise were accepted.
- Reference expectation: ordinary
- Runs: `green-inline-map-1`; selected `designing-data-intensive-applications`; reported `focused` access to `Reliability Rules`, `Derived Data Rules`, and `Batch and Stream Processing Rules`
- Package fidelity trace: exact mini-derived ownership and derived-data guidance; router-only change
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass with disclosure diagnostic
- Diagnostics: expected ordinary but read three relevant sections; bounded nonmaterial over-read, not end-to-end tier collapse

### RM2: Focused replica-consistency control

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/focused-replica-read.md`
- Fixture SHA-256: `d9915d792c20f5c99a85e6af71602659658e196a7a16c2d14e75dddd040d169d`
- Required skills: `{designing-data-intensive-applications}`
- Distinctive judgment: Resolve one read-after-write guarantee against replica lag and topology without broad system redesign.
- Neighbor ownership: This is distributed-data consistency and replication semantics, not general reliability or architecture placement.
- Ownership review: REJECTED - post-run contract audit on 2026-07-14 found ordinary team disagreement rather than an explicit source-interpretation dispute; the earlier independent review had recorded `PASS` under the mistaken broader interpretation.
- Reference expectation: focused
- Compact-body gap: invalid as recorded; the fixture disputes the design decision but does not state competing source propositions.
- Intended index destinations: `Consistency Rules` and `Replication Rules`
- Runs: `green-inline-map-1`; selected `designing-data-intensive-applications`; `focused`; read intended `Consistency Rules` and `Replication Rules` plus three related sections
- Package fidelity trace: the two named canonical full headings
- Attribution review: not counted because the focused contract was invalid, although the answer contained no unsupported book attribution
- Behavioral result: not counted
- Diagnostics: preserve the bounded five-section run as invalid-contract evidence; separately named source-dispute replacement RM2b supersedes it

### RM2b: Focused replica-consistency source-dispute replacement

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/focused-replica-consistency-source-dispute-v2.md`
- Fixture SHA-256: `de4b1d04e3e2fc782f67b48e2e37fbd7079f058dbe4d779da30bfe8571217b1a`
- Required skills: `{designing-data-intensive-applications}`
- Distinctive judgment: Resolve the exact read-your-writes source proposition under asynchronous lag, catch-up, failover, and reconfiguration without widening to general reliability.
- Neighbor ownership: Release It! owns operational survival, but the disputed consistency contract and replication semantics are central here.
- Ownership review: PASS - independent pre-dispatch review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14 accepted blindness, DDIA ownership, the explicit source dispute, focused tier, and exact two-section destination.
- Reference expectation: focused
- Compact-body gap: none; the fixture explicitly disputes whether source guidance categorically forbids follower reads or permits them only when the design proves the required read-your-writes guarantee under lag and topology changes.
- Intended index destinations: `Consistency Rules` and `Replication Rules`
- Runs: `green-inline-map-contract-fix-1`; selected only `designing-data-intensive-applications`; reported `focused`; read exactly `Consistency Rules` and `Replication Rules`
- Package fidelity trace: canonical full headings `Consistency Rules` and `Replication Rules` plus unchanged mini-derived consistency and topology guidance
- Attribution review: PASS - independent final result review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` found no unsupported book attribution; application-level implementation deductions remained distinct from source claims
- Behavioral result: pass
- Diagnostics: exact two-section focused route passed; separately named source-dispute replacement supersedes post-run-rejected RM2

### RM3: Comprehensive DDIA control

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/comprehensive-audit.md`
- Fixture SHA-256: `5f1473ea6f13c6431188e079ae4f7ba077f2f7d30eb26c7e3242518a984ee28e`
- Required skills: `{designing-data-intensive-applications}`
- Distinctive judgment: Apply the complete distributed-data correctness lens end to end.
- Neighbor ownership: Compatible operational or architectural guidance may co-apply, but the explicit complete DDIA audit owns this control.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture exposes the required source lens and cannot be reused unchanged.
- Reference expectation: comprehensive
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: all canonical full headings
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM3b; the frozen fixture, hash, and required set remain unchanged

### RM3b: Comprehensive data-platform replacement

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/designing-data-intensive-applications/comprehensive-data-platform-audit-v2.md`
- Fixture SHA-256: `0bf8952b5401d2954f3b7c8c59d73a174ec55b382272fd06e2d113b0d15ec285`
- Required skills: `{designing-data-intensive-applications}`
- Distinctive judgment: Apply the complete distributed-data correctness lens across authority, models, storage, consistency, replay, ordering, evolution, partitioning, replication, transactions, derivation, faults, and processing.
- Neighbor ownership: Architecture and production-resilience skills may contribute compatible findings, but the fixture's explicit exhaustive data-system objective makes this skill central.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, and end-to-end comprehensive loading were accepted.
- Reference expectation: comprehensive
- Runs: `green-inline-map-1`; selected `designing-data-intensive-applications` and compatible `release-it`; both reported `sections=["*"]`, including the required target
- Package fidelity trace: all canonical full headings
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: permitted production-resilience overlap; required target inclusion and end-to-end access passed
