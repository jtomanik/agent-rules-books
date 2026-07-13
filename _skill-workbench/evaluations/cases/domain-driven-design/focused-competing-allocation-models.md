# Choose Between Competing Allocation Models

Give a focused decision about two competing implementation-driving models inside the established Allocation context. The commitment to model-driven design is settled. Do not broaden the answer into an architecture, persistence, or integration review.

The current model treats allocation as a status:

```ts
type Allocation = {
  status: "REQUESTED" | "ALLOCATED" | "RELEASED";
  orderId: string;
  warehouseId?: string;
  quantity: number;
};
```

Domain experts have proposed two replacements:

- **Candidate A:** keep `Allocation` as a lifecycle object, but split `Proposed`, `Committed`, and `Released` transitions.
- **Candidate B:** model a customer `SupplyPromise` separately from a warehouse `CapacityReservation`; allocation is the policy that tries to reconcile them.

Both candidates explain today's happy path. A newly observed scenario does not: one order line may retain its customer promise while operations releases one warehouse reservation and seeks another, without treating the order as unallocated.

Decide which candidate offers the stronger explanatory model for that scenario, what implicit concept it makes explicit, and what one or two domain-language experiments could falsify it before migration. Address explanatory gain versus migration cost and preserve current behavior through incremental steps.
