# Resolve a Hidden Fulfillment Concept

Give a focused model-discovery decision for one hotspot in the already established Fulfillment context. Do not broaden the answer into a complete domain-model audit or implementation architecture.

The model currently stores:

```ts
type FulfillmentLine = {
  status: "UNALLOCATED" | "ALLOCATED" | "SHIPPED";
  warehouseId?: string;
  quantity: number;
};
```

The same `ALLOCATED` state is used after either of these business events:

1. Planning proposes a warehouse that appears able to supply the line. The proposal may be replaced without customer impact.
2. Warehouse operations accepts responsibility and reserves stock. Releasing it requires an explicit operational decision.

Developers disagree whether this only needs clearer status names or reveals a missing domain concept. Decide what interpretation should drive the model, what explanatory gain would justify the refactoring, and which two or three domain-language scenarios would falsify the proposed deeper model. Keep the migration incremental and behavior-preserving.
