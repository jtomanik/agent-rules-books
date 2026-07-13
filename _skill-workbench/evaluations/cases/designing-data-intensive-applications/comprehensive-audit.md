# Complete Distributed Data Design Audit

Apply the complete Designing Data-Intensive Applications lens to this proposed order platform. Produce a prioritized audit of correctness risks, explicit contracts that are missing, and verification required before implementation. Cover the artifact end to end rather than limiting the review to one subsystem.

```yaml
service: order-platform

traffic:
  writes_per_second: 1800
  reads_per_second: 22000
  order_history_p99_ms: 180
  largest_tenant_share: 0.31

primary_data:
  orders:
    store: postgres
    isolation: read_committed
    shard_key: customer_id
    writable_regions: [eu-west, us-east]
    conflict_policy: last_writer_wins
    acknowledged_after: local_commit
  inventory:
    store: postgres
    owner: inventory-service
    reservation_rpc: synchronous

replication:
  order_replicas: asynchronous
  read_route_after_write: nearest_replica
  failover: promote_most_recent_replica
  maximum_accepted_lag_ms: null
  read_your_writes: unspecified

derived_data:
  order_cache:
    store: redis
    populated_by: API dual-write
    ttl_seconds: 900
    rebuild: none
  order_search:
    store: opensearch
    populated_by: CDC
    checkpoint: in_memory
    rebuild: none
  revenue_cube:
    store: warehouse
    populated_by: nightly-export
    correction_policy: append-adjustment

events:
  broker: kafka
  topics:
    order-events:
      partitions: 96
      key: customer_id
      retention_days: 7
      delivery_claim: exactly_once
  publish_path: commit-order-then-publish
  payload_version: omitted
  event_time: producer_wall_clock
  late_data_policy: drop

schemas:
  database_migration: rename_status_column_in_place
  API_change: replace_status_string_with_integer
  event_change: reuse_status_field_with_new_meaning
  old_and_new_versions_overlap_minutes: 30
  backfill: online-unversioned-script

coordination:
  inventory_lease:
    store: redis
    expiry_ms: 5000
    fencing_token: none
    elapsed_time_clock: wall_clock
  global_order_number:
    mechanism: application_timestamp_plus_region

batch_and_stream:
  revenue_job:
    retry: rerun_entire_day
    external_side_effect: email_finance_summary
    idempotency_key: none
  fraud_stream:
    checkpoint: every_10000_records
    state_store: local_disk
    window: processing_time_5m
    late_events: ignored

service_boundaries:
  order_service_writes: [orders, order_cache, order_search]
  reporting_service_reads_primary_orders: true
  checkout_joins_over_rpc: [orders, inventory, pricing, customer]

observability:
  replica_lag: false
  CDC_lag: false
  consumer_retries: false
  projection_rebuild_progress: false
  conflict_count: false

tests:
  duplicate_delivery: false
  out_of_order_delivery: false
  replay: false
  schema_mixed_versions: false
  replica_failover: false
  write_skew: false
  projection_rebuild: false
```

Constraints:

- A confirmed order must never disappear after the client receives success.
- Inventory must not be oversold.
- Customers must see their new order immediately after confirmation.
- Search may lag by up to ten minutes, but finance totals must be correct after corrections.
- Regions may lose connectivity for up to twenty minutes while both continue accepting orders.
