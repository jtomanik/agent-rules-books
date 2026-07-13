# Find the Smallest Honest Order Model

Review this routine order-confirmation slice. Recommend only the tactical elements that genuinely help; do not turn it into a platform redesign.

```ts
type OrderRow = {
  id: string;
  status: string;
  currency: string;
  total: number;
  paymentId?: string;
  inventoryReservationId?: string;
};

export async function confirmOrder(id: string): Promise<void> {
  const order = await db.orders.find(id);
  const payment = await db.payments.find(order.paymentId);
  const inventory = await db.inventory.find(order.inventoryReservationId);

  if (order.status !== "DRAFT") throw new Error("bad status");
  if (payment.status !== "AUTHORIZED") throw new Error("bad payment");
  if (inventory.status !== "HELD") throw new Error("bad inventory");

  order.status = "CONFIRMED";
  payment.status = "CAPTURE_PENDING";
  inventory.status = "ALLOCATED";
  await db.transaction(() => Promise.all([
    db.orders.save(order),
    db.payments.save(payment),
    db.inventory.save(inventory),
  ]));
}
```

Facts:

- `Money` arithmetic and currency agreement are business-significant.
- Order confirmation has one local invariant: a cancelled order cannot be confirmed.
- Payment authorization and inventory allocation are owned by separate systems.
- The team has proposed an `Order` Aggregate containing complete Payment and Inventory object graphs.

Choose the smallest model and boundary correction that reflects those facts.
