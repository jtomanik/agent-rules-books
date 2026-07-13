# Repair a Payment Consumer After a Failure Cascade

Review both the distributed data correctness and production failure behavior of this payment consumer. Decide how to make invoice creation, payment submission, redelivery, and recovery correct while bounding the outage blast radius. Keep the answer focused on the shown write path and runtime failure evidence.

```ts
export async function consume(message: Delivery): Promise<void> {
  const command = decode<CapturePayment>(message.body);

  const invoice = await database.invoices.insert({
    orderId: command.orderId,
    amount: command.amount,
  });

  await paymentProvider.capture({
    invoiceId: invoice.id,
    amount: invoice.amount,
  });

  await message.ack();
}
```

```yaml
broker:
  delivery: at_least_once
  queue_capacity: 0
  max_deliveries: 0
  dead_letter: null

consumer:
  replicas: 12
  prefetch: 500
  idempotency_key: none

database:
  invoice_order_id_unique: false
  outbox: none

payment_provider:
  timeout_ms: 0
  SDK_retries: 2
  idempotency_key: supported_but_unused

health:
  readiness: broker_connected

observability:
  queue_age: false
  redeliveries: false
  duplicate_invoice_count: false
  provider_latency: false
```

Failure evidence:

- A provider timeout can mean the charge succeeded or failed.
- Restart after invoice insert redelivers the command and inserts another invoice.
- A six-minute provider slowdown accumulated 1.8 million deliveries and exhausted database connections.
- Operators cannot pause one consumer partition or inspect retry age.
- The payment provider accepts a stable idempotency key for the lifetime of an invoice.

Recommend the exact durability/idempotency/recovery contract and the finite timeout, retry, capacity, isolation, degradation, and diagnostic behavior needed.
