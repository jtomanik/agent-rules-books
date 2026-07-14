# Comprehensive Distributed Data Platform Audit

Perform a comprehensive end-to-end data-system audit of a marketplace platform with multi-region writes, asynchronous replicas, event-driven projections, evolving schemas, retryable consumers, partitioned order streams, local and cross-service transactions, batch rebuilds, caches, search indexes, and an analytics lake.

The platform has duplicate side effects after retries, stale post-write reads, ordering assumptions across partitions, incompatible event changes, projections with no rebuild path, unclear authority between services and caches, and failover procedures that can lose acknowledged writes.

Cover reliability, scalability, maintainability, data and query models, storage and indexes, consistency, replay, ordering, logs and streams, schema and encoding, partitioning, replication, transactions, derived data, distributed faults and coordination, batch and stream processing, APIs, testing, and final review. Distinguish explicit guarantees from assumptions.
