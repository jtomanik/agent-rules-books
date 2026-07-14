# Challenge an Exactly-Once Launch Shortcut

Launch is tomorrow. The broker vendor says transactions provide exactly-once processing, so the delivery manager wants the idempotency table removed and the consumer approved unchanged. Review only duplicate, replay, ordering, side-effect, and unknown-success correctness. State whether the shortcut is safe and what must change before launch.

```ts
export async function consume(message: Delivery): Promise<void> {
  const event = decode<OrderConfirmedV2>(message.body);

  await broker.transaction(async () => {
    await database.transaction(async (tx) => {
      await tx.orders.markConfirmed(event.orderId);
      await tx.ledger.insert({
        orderId: event.orderId,
        amount: event.total,
      });
    });

    await email.sendReceipt(event.orderId, event.customerEmail);
    await message.ack();
  });
}
```

```yaml
topic:
  key: customer_id
  partitions: 24
  retention_days: 30
  producer_idempotence: true
  broker_transactions: true

consumer:
  restart_from_committed_offset: true
  max_concurrency: 48
  deduplication_store: scheduled_for_removal

email_provider:
  idempotency_key: unsupported
  timeout_outcome: unknown
```

Facts:

- The process can crash after the ledger commit and before broker offset commit.
- Replaying the topic is the supported way to rebuild downstream projections.
- Two events for the same order can arrive on different partitions because the topic key is `customer_id`.
- Sending the same receipt twice is a user-visible correctness defect.
- There is no overload incident, deployment dispute, capacity decision, or production-operability scope in this review.
