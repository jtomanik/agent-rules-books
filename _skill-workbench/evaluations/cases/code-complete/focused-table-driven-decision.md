# Resolve a Table-Driven Construction Decision

Two reviewers disagree about whether this stable shipping calculation should remain a branch chain or become table-driven logic.

```ts
type Zone = "local" | "regional" | "international";
type Service = "standard" | "express";

export function shippingCents(zone: Zone, service: Service): number {
  if (zone === "local" && service === "standard") return 400;
  if (zone === "local" && service === "express") return 900;
  if (zone === "regional" && service === "standard") return 700;
  if (zone === "regional" && service === "express") return 1300;
  if (zone === "international" && service === "standard") return 1800;
  if (zone === "international" && service === "express") return 3200;
  throw new Error("unsupported shipping combination");
}
```

Resolve this specifically under Code Complete's statement/conditional, table-driven, and testing guidance. State whether a table is clearer here, show the smallest acceptable representation, and identify validation and edge-case tests. Keep the analysis limited to this decision; do not perform a general audit or edit files.
