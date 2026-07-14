# Separate Preparatory Refactoring from New Construction

The current behavior is fully characterized by green tests. Product now requires rejected rows to report a typed reason instead of returning `false`. First make only the behavior-preserving structural changes needed to expose validation, then implement the new result behavior. Keep the two intents reviewable and separate.

```ts
export function acceptRow(row: string[]): boolean {
  if (row.length === 4) {
    if (row[0] !== "") {
      if (row[1] === "person" || row[1] === "company") {
        if (/^\d+$/.test(row[2])) {
          if (row[3] === "active" || row[3] === "inactive") {
            acceptedRows.push({
              id: row[0],
              kind: row[1],
              score: Number(row[2]),
              status: row[3],
            });
            return true;
          }
        }
      }
    }
  }

  return false;
}
```

New contract:

```ts
type AcceptanceResult =
  | { accepted: true }
  | { accepted: false; reason: "field-count" | "missing-id" | "kind" | "score" | "status" };
```

Provide a two-phase patch plan and code sketch. Phase one must preserve current observable behavior while making the validation structure easier to change. Phase two must introduce the typed result, explicit data meaning, deliberate boundary checks, and tests for every rejection reason. Do not broaden scope beyond this function and its tests; do not edit files.
