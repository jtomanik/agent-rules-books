# Decide a Supervised Consumer Failure Boundary

Two engineers disagree about this queue consumer. One argues that the supervisor will restart the process, so every exception should escape and crash it. The other wants one broad catch that logs the error, acknowledges the message, and keeps the process alive.

Review the implementation, broker behavior, and supervisor configuration. Decide the exact boundary between quarantine, retry or pause, and process crash for malformed messages, transient dependency failure, and compromised process state. Recommend only changes needed to make this failure policy safe and testable; this is not a general service audit.

```ts
export async function consume(message: Delivery): Promise<void> {
  try {
    const event = JSON.parse(message.body.toString()) as InventoryEvent;
    const response = await inventoryClient.get(`/items/${event.sku}`);
    const item = await response.json();

    await database.transaction(async (tx) => {
      await tx.inventoryEvents.insert({
        eventId: event.id,
        sku: event.sku,
        available: item.available,
      });
      await tx.inventory.update(event.sku, item.available);
    });

    await message.ack();
  } catch (error) {
    logger.error({ error }, "inventory event failed");
    throw error;
  }
}
```

```yaml
consumer:
  prefetch: 100
  queue_capacity: 250
  max_deliveries: 0
  dead_letter_exchange: null
  dependency_timeout_ms: 0
  dependency_retries: 3

supervisor:
  restart: always
  restart_backoff_ms: 100
  restart_backoff_max_ms: 1000
  max_restarts_per_minute: 0
  replicas: 6

health:
  liveness: process_is_running
  readiness: broker_connection_is_open
```

Operational facts:

- `max_deliveries: 0` means unlimited delivery attempts.
- If the process exits, every unacknowledged delivery is immediately eligible for redelivery.
- The broker has no quarantine queue unless one is configured explicitly.
- The inventory dependency can return `503`, time out, or return status `200` with malformed JSON.
- Three malformed messages caused continuous restarts across all six replicas during a staging test.
- Operators can pause the deployment, but there is no per-partition or per-message pause control.
