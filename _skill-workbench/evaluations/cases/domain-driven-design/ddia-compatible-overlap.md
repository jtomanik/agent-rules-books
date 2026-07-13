# Review Context Meaning and Event Correctness Together

Review this order-event design. Cover both the model boundary between Ordering and Billing and the distributed-data correctness of the event path. Recommend explicit contracts and the smallest safe correction.

Ordering defines `Order.status = CONFIRMED` when customer intent and inventory reservation are accepted. Billing defines `Order.status = POSTED` only after ledger entries balance.

```yaml
producer:
  service: ordering
  database: orders-postgres
  publish: commit_then_send
  event:
    type: OrderUpdated
    key: order_id
    payload: { order_id, status, total, customer }
    schema_version: omitted

broker:
  delivery: at_least_once
  ordering: per_partition
  partitions: 48
  retention_days: 3

consumers:
  billing:
    maps_payload_to_shared_Order_class: true
    duplicate_detection: false
    accepts_out_of_order_updates: true
  order_history:
    projection_store: postgres
    checkpoint: in_memory
    rebuild: none

failures:
  producer_may_crash_after_commit: true
  consumer_may_crash_after_ledger_write: true
  partition_count_may_change: true
```

Constraints:

- Ordering remains authoritative for commercial order confirmation.
- Billing remains authoritative for ledger posting.
- A duplicate must never create a second ledger posting.
- Order history must be rebuildable after a projection defect.
- Both contexts need to evolve their status concepts independently.
