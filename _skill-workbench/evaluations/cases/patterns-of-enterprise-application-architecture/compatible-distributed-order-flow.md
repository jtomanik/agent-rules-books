# Durable order submission flow

Review and redesign this flow. The answer must settle both in-process responsibility/pattern placement and cross-system data correctness. Keep the design bounded to order submission and projection delivery.

```text
POST /orders
  controller validates HTTP fields
  controller writes OrderRow through GenericRepository
  controller publishes OrderCreated JSON to a broker
  controller calls Inventory.reserve(orderJson)
  controller returns OrderRow

Projection worker
  consumes OrderCreated
  upserts order_search by order_id
  advances one global offset after each message

Current facts
  - database commit and broker publish are separate writes
  - clients retry timed-out POST requests
  - the broker is at-least-once and preserves order only within a partition
  - producers may add fields before all consumers deploy
  - order_search may be dropped and rebuilt
  - Inventory owns stock and can reject a reservation after the order commit
```

Specify the application operation, business-logic shape, repository/mapping and transaction ownership, DTO or remote boundary, authoritative records, idempotency keys, ordering scope, schema evolution, projection repair/rebuild behavior, and the meaning of partial success.
