# Resolve One Interface Ownership Dispute

The application layer imports an interface that is declared beside its SQL implementation:

```ts
// infrastructure/sql-customer-store.ts
export interface CustomerStore {
  findName(id: string): Promise<string | null>;
}

export class SqlCustomerStore implements CustomerStore {
  // SQL implementation omitted.
}
```

```ts
// application/get-customer-name.ts
import type { CustomerStore } from "../infrastructure/sql-customer-store";

export class GetCustomerName {
  constructor(private readonly customers: CustomerStore) {}

  execute(id: string): Promise<string | null> {
    return this.customers.findName(id);
  }
}
```

Reviewer A says depending on an interface is sufficient. Reviewer B says the abstraction is still infrastructure-owned, so the source dependency points outward.

Resolve only this Clean Architecture ownership dispute. State which layer owns the interface and why, and identify the smallest detailed sections needed to settle that interpretation. Do not redesign the feature or perform a complete audit.
