# Implement a Durable Order Search Projection

Design the implementation path from an Ordering Domain Event to an Elasticsearch order-history projection. Cover both domain-event/application boundaries and distributed-data replay correctness.

Approved domain facts:

- `Order` is an Aggregate root in Ordering.
- Confirming an Order produces `OrderPlaced` containing stable domain identities and the confirmed commercial facts.
- Search is a disposable read model, not the source of truth.
- Ordering must not import Elasticsearch types.

Runtime facts:

```yaml
source: ordering-postgres
publication: transaction_outbox
broker:
  delivery: at_least_once
  ordering: per_order_id
  retention_days: 7
consumer:
  writes: elasticsearch
  duplicate_detection: false
  checkpoint: memory
  schema_version: omitted
  unknown_fields: reject
projection:
  acceptable_lag_seconds: 60
  full_rebuild: none
  current_document_shape_owned_by: ordering
failures:
  duplicate_delivery: observed
  out_of_order_delivery_after_repartition: observed
  bad_mapping_requires_reindex: possible
```

Specify event construction and publication responsibilities, subscriber/application-service boundaries, translation into the read representation, idempotency and ordering contracts, schema evolution, lag visibility, and rebuild procedure.
