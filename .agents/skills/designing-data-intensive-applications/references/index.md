# Designing Data-Intensive Applications Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit dispute, demonstrated correctness hotspot, or one bounded question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a complete DDIA audit or a decision spanning several independent concern families, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-18` | Decide whether explicit data ownership, consistency, replay safety, durable boundaries, evolution, and realistic distributed assumptions are central to the task. |
| [Primary Directive](full.md#primary-directive) | `20-34` | Resolve a disputed source-of-truth, consistency, retry, ordering, evolution, or durability tradeoff that local-looking abstractions obscure. |
| [Reliability Rules](full.md#reliability-rules) | `36-48` | Define acknowledgment and durable-success semantics or recovery from crashes, partial writes, duplicate work, timeouts, stale reads, and unknown downstream success. |
| [Scalability and Maintainability Rules](full.md#scalability-and-maintainability-rules) | `50-59` | Evaluate a demonstrated workload or performance hotspot using concrete load, bottleneck, contention, percentile, operability, simplicity, and evolution facts. |
| [Data Model and Storage Rules](full.md#data-model-and-storage-rules) | `61-81` | Choose ownership and primary-versus-derived storage shape from access, update, consistency, replication, and repair needs. |
| [Query Model and Data Shape Rules](full.md#query-model-and-data-shape-rules) | `83-92` | Decide among relational, document, graph, key-value, analytical, declarative, or application-side query forms from relationships and access patterns. |
| [Storage Engine and Indexing Rules](full.md#storage-engine-and-indexing-rules) | `94-104` | Compare LSM, B-tree, secondary-index, OLTP, analytical, columnar, materialized, compressed, or memory-resident layouts for a concrete workload. |
| [Consistency Rules](full.md#consistency-rules) | `106-126` | Specify read-after-write, staleness, durability, visibility, or conflict semantics when eventual versus stronger consistency is disputed. |
| [Idempotency and Replay Rules](full.md#idempotency-and-replay-rules) | `128-140` | Prove retry, duplicate-delivery, deduplication, replay, acknowledgment, or exactly-once safety for commands, jobs, handlers, or events. |
| [Ordering Rules](full.md#ordering-rules) | `142-158` | Determine whether correctness needs per-key, stream, partition, entity-history, or stronger ordering and how out-of-order work is detected. |
| [Event, Log, and Stream Rules](full.md#event-log-and-stream-rules) | `160-179` | Distinguish commands, events, durable histories, streams, and projections or design consumer lag, restart, replay, identity, metadata, and payload semantics. |
| [Schema Evolution Rules](full.md#schema-evolution-rules) | `181-194` | Plan a contract change across old and new readers, writers, stored data, in-flight messages, enum meanings, and rollout migration. |
| [Encoding and Data Flow Rules](full.md#encoding-and-data-flow-rules) | `196-205` | Select an encoding or RPC/data-flow contract under compatibility, schema, language, size, latency, version-skew, and partial-failure constraints. |
| [Partitioning and Locality Rules](full.md#partitioning-and-locality-rules) | `207-219` | Choose or challenge a partition key using locality, consistency, skew, hot keys, ordinary query paths, and cross-partition costs. |
| [Replication Rules](full.md#replication-rules) | `221-230` | Select topology or define lag, failover, catch-up, read guarantees, quorum behavior, and concurrent-write conflict handling. |
| [Transaction Rules](full.md#transaction-rules) | `232-249` | Map atomicity, isolation anomalies, commit, reconciliation, and external side effects to named invariants and repair paths. |
| [Derived Data Rules](full.md#derived-data-rules) | `251-263` | Establish authority, propagation, staleness, lag visibility, resynchronization, rebuild, or repair for indexes, caches, search copies, and read models. |
| [Distributed Fault, Clock, and Consensus Rules](full.md#distributed-fault-clock-and-consensus-rules) | `265-276` | Review timeout inference, clock assumptions, leases, locks, leadership, membership, linearizability, or consensus under a stated fault model. |
| [Batch and Stream Processing Rules](full.md#batch-and-stream-processing-rules) | `278-288` | Define recomputation, checkpoints, side effects, event/processing/ingestion time, windows, late data, joins, CDC, or source-to-sink guarantees. |
| [API and Service Boundary Rules](full.md#api-and-service-boundary-rules) | `290-297` | Decide whether a service split, API, identifier, or remote join matches data ownership, update semantics, consistency, and failure contracts. |
| [Review Rules](full.md#review-rules) | `299-313` | Perform a focused code or design review for hidden order, exactly-once, ownership, versioning, repair, multi-write, rebuild, locality, and hotspot assumptions. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `315-334` | Classify exactly-once wishful thinking, hidden consistency, uncoordinated multi-writes, or accidental schema drift and explain the violated contract. |
| [Code Generation Rules](full.md#code-generation-rules) | `336-353` | Translate a resolved ownership, idempotency, ordering, derived-data, compatibility, or observability decision into generated implementation defaults. |
| [Testing Rules](full.md#testing-rules) | `355-364` | Design focused tests for duplicate delivery, out-of-order handling, replay, conflict resolution, schema compatibility, or derived-view rebuild. |
| [Review Checklist](full.md#review-checklist) | `366-382` | Run the canonical pre-finalization scan over ownership, consistency, retry, order, rebuild, evolution, atomicity, service boundaries, and observability. |
| [Final Instruction](full.md#final-instruction) | `384-393` | Arbitrate a final design choice using explicit ownership, consistency, retry/replay survival, evolution, and honest distributed tradeoffs. |
