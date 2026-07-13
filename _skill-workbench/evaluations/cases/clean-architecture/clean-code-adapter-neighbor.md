# Improve a Local Mapper Inside a Database Adapter

The architecture boundary is already fixed: this private mapper lives entirely inside a PostgreSQL adapter, has no business rules, and cannot move into the application or domain. The adapter's contract and tests are complete and green.

```ts
type UserRow = {
  user_id: string;
  display_name: string | null;
  deleted_at: Date | null;
};

type UserRecord = {
  id: string;
  label: string;
  active: boolean;
};

function m(x: UserRow, b: boolean): UserRecord {
  // Work out which label to expose and whether the row is active.
  let y = x.display_name === null ? "" : x.display_name.trim();
  if (b && y === "") {
    y = x.user_id;
  }
  return { id: x.user_id, label: y, active: x.deleted_at === null };
}
```

Review this helper for local readability, naming, boolean-mode clarity, and comment usefulness. Keep the mapper in the adapter, preserve its signature and exact behavior, and do not introduce ports, use cases, entities, or new architectural layers.
