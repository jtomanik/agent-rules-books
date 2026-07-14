# Meet a Deadline Without One Object Graph

The release manager requires this checkout change today. Six months of code already assumes that `Order`, `Customer`, and `InventoryItem` can be loaded and committed as one graph, and the principal engineer says splitting it now is too risky.

```ts
export async function confirmOrder(orderId: string): Promise<void> {
  const order = await commerceRepository.loadGraph(orderId);
  order.customer.status = "ACTIVE";
  for (const line of order.lines) {
    line.inventoryItem.available -= line.quantity;
    line.status = "ALLOCATED";
  }
  order.status = "CONFIRMED";
  await commerceRepository.saveGraph(order);
}
```

Approved ownership:

- `Order` is an Ordering Aggregate root.
- `Customer` is a Customer context Aggregate root.
- `InventoryItem` is an Inventory Aggregate root.
- Ordering may store only translated references and snapshots from the other contexts.
- Confirmation must not partially violate the local Order invariant.
- Cross-context completion may be asynchronous and compensating action is allowed.

Recommend the smallest implementation change that honors those boundaries today. Address transaction scope, references, application coordination, integration messages, and the foreign `status` value without proposing a full rewrite.
