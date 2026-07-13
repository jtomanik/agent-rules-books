# Resolve a Port Ownership Dispute

Two reviewers agree that the application should depend on an interface rather than a SQL implementation, but they disagree about who owns that interface and its data types.

Current proposal:

```ts
// infrastructure/sql-order-repository.ts
export type OrderRow = {
  id: string;
  status_code: string;
  total_cents: number;
};

export interface OrderRepository {
  findById(id: string): Promise<OrderRow | null>;
}

export class SqlOrderRepository implements OrderRepository {
  // SQL implementation omitted
}
```

```ts
// application/get-order-summary.ts
import type {
  OrderRepository,
  OrderRow,
} from "../infrastructure/sql-order-repository";

export class GetOrderSummary {
  constructor(private readonly orders: OrderRepository) {}

  async execute(id: string): Promise<OrderRow | null> {
    return this.orders.findById(id);
  }
}
```

Reviewer A says dependency inversion is satisfied because the use case imports only the interface, not `SqlOrderRepository`. Reviewer B says the interface and `OrderRow` are still infrastructure-owned details, so source dependencies point outward and persistence shapes leak inward.

Resolve this disputed Clean Architecture interpretation. Give the corrected ownership and type flow, explain which layer defines the port, and identify the smallest set of detailed Clean Architecture sections needed to settle the dispute. Do not perform a complete architecture audit.
