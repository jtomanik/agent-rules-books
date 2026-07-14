---
name: designing-data-intensive-applications
description: Designing Data-Intensive Applications guidance for distributed data correctness. Use when source-of-truth ownership, consistency/durability, replay/order, schema evolution, derived-data repair, replication/partitioning, or cross-system write/side-effect, transaction, or coordination semantics are central. A queue, cache, retry, database, or production failure alone is insufficient; Release It! owns operational survival and Clean Architecture policy direction unless data semantics are central.
---

# Designing Data-Intensive Applications

## Primary Bias

Do not design distributed data behavior as if every write, read, queue, cache, replica, clock, and downstream side effect were local, ordered, fresh, and exactly once.

## Data Contracts and Ownership

- Make core trade-offs explicit: source of truth, consistency expectation, retry behavior, duplicate and reordered work, partial failure, data evolution, and whether state is durable, cached, derived, or ephemeral.
- Choose data models, query models, and ownership boundaries from relationships, access patterns, consistency needs, update locality, evolution pressure, and whether data is primary or derived.
- Treat indexes, caches, search copies, read models, materialized views, and denormalized copies as derived data with explicit propagation, lag, observability, repair, and rebuild paths.
- When adding or changing a cache, index, projection, search copy, read model, or denormalized field, define ownership, propagation, staleness, write cost, lag visibility, rebuild, and repair.
- Define write semantics: when a write is durable, when it is visible, whether stale reads are allowed, which conflicts can happen, and how conflicts are detected or resolved.
- When changing a write path, state the source of truth, consistency boundary, durability point, visibility point, downstream effects, recovery or repair path, and behavior after timeout or unknown success.
- Design schemas, encodings, APIs, messages, events, and database changes as evolving contracts across old readers, old writers, old data, in-flight messages, rolling upgrades, and cross-service formats.
- When changing a schema, API, message, event, enum, status, or payload meaning, plan compatibility for old readers, old writers, old stored data, old messages, new writers, rollout, and migration.
- Align service boundaries with data ownership and update semantics. Do not casually split one tightly consistent business concept across services or put chatty cross-service joins on hot paths.

## Retry, Replay, Ordering, and Data Flow

- Treat crashes, partial writes, duplicate work, timeouts, stale reads, and unknown downstream success as normal inputs. Distinguish accepted, persisted, applied, and durable success.
- Make commands, jobs, events, batch jobs, and stream processors safe under retry and replay with deduplication keys, naturally idempotent transitions, or an explicit transactional recovery contract.
- When adding retries, jobs, consumers, queues, CDC, event sourcing, stream processors, or replayable batch work, prove duplicate, replay, ordering, side-effect, and recovery safety.
- Preserve only the ordering the business logic actually needs. Scope it per key, stream, partition, record, entity history, or stronger contract, and keep ordering-sensitive logic close to that scope.
- Separate commands, events, durable logs, streams, and materialized views. Events describe facts; consumers must tolerate lag, duplicates, restart, replay, stable identifiers, correlation metadata, and versioned payloads.
- Make batch and stream processing recomputable and recoverable: define inputs, outputs, intermediate state, checkpoints, external side effects, event time, processing time, ingestion time, windows, late data, joins, and source-to-sink guarantees.

## Workload, Storage, Replication, and Partitioning

- Describe load and performance with concrete parameters, access patterns, latency, throughput, percentiles, bottlenecks, contention, and tail behavior before changing architecture.
- Match storage engines, indexes, and analytical layouts to write patterns, read patterns, range scans, recovery needs, write amplification, OLTP-vs-analytics separation, and memory-vs-durability assumptions.
- Choose replication topology from write topology, latency, failure tolerance, lag, failover, reconfiguration, conflict handling, read-your-writes, monotonic-read, consistent-prefix, and quorum needs.
- When routing reads to replicas or using asynchronous replication, identify read-your-writes, monotonic-read, consistent-prefix, staleness, catch-up, failover, and conflict expectations before allowing the read.
- Partition by workload-relevant locality and consistency keys, with hot-key, skew, secondary-index, and cross-partition-operation costs explicit.
- When partitioning data or work, test the ordinary query path for locality, skew, hot keys, secondary-index costs, and cross-partition coordination.

## Transactions and Distributed Coordination

- Match transactions and isolation to invariants. Make atomicity scope, commit behavior, recovery, reconciliation, lost-update, write-skew, phantom, and side-effect repair semantics explicit.
- When choosing transaction isolation or weakening consistency, map each anomaly to the invariant it can break and require stronger isolation or another deliberate design that preserves the invariant.
- Treat network delay, packet loss, partitions, duplicate messages, pauses, timeouts, wall-clock uncertainty, leases, locks, majorities, and leadership as assumptions needing a fault model.
- Use linearizability, total order broadcast, atomic commit, or consensus only where the coordination problem truly requires agreement and the availability or latency cost is acceptable.
- When using timestamps, leases, locks, leadership, majority decisions, coordination services, or consensus-like mechanisms, define the clock assumption, fault model, quorum behavior, and membership or coordination-service dependencies.

## Review and Testing

- When reviewing or testing data-intensive code, look specifically for hidden source-of-truth ownership, missing idempotency, accidental exactly-once assumptions, unscoped ordering, schema drift, unrebuildable projections, unclear multi-writes, and unobservable lag or failure.

## Reference Map

Use this file alone when it resolves ordinary matched work; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Durability and failure semantics: [Reliability Rules](references/full.md#reliability-rules)
- Read guarantees and stale data: [Consistency Rules](references/full.md#consistency-rules)
- Retries, duplicates, and replay: [Idempotency and Replay Rules](references/full.md#idempotency-and-replay-rules)
- Compatibility and migration: [Schema Evolution Rules](references/full.md#schema-evolution-rules)
- Replica topology and lag: [Replication Rules](references/full.md#replication-rules)
- Atomicity and isolation: [Transaction Rules](references/full.md#transaction-rules)
- Projection authority, rebuild, and repair: [Derived Data Rules](references/full.md#derived-data-rules)
- Clocks, faults, and coordination: [Distributed Fault, Clock, and Consensus Rules](references/full.md#distributed-fault-clock-and-consensus-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For an explicit comprehensive data-system audit or complete DDIA lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Source of truth and derived representations are explicit.
- Consistency expectations, durability points, visibility points, staleness, and conflict rules are concrete.
- Retries, duplicate delivery, replay, reordering, timeouts, crashes, and unknown success are handled.
- Schemas, encodings, APIs, messages, events, enums, and statuses evolve safely across mixed versions.
- Storage, indexing, replication, partitioning, and analytical layouts match the actual workload.
- Transaction isolation and coordination choices protect the named invariants.
- Events, logs, streams, batch jobs, and projections are replayable or have explicit repair paths.
- Service boundaries follow data ownership and update semantics.
- Lag, retries, failures, rebuilds, and repair paths are observable.
- The design avoids exactly-once wishful thinking and hidden distributed-system contracts.
