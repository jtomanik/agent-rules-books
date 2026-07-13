# Separate Structural Preparation from a Substantial Import Change

The current CSV-import module is fully characterized by focused green tests. It currently returns only accepted rows and silently drops rejected rows. Product now requires a typed result for every source line, including the rejection reason and original line number.

```ts
export function importRows(lines: string[]): AcceptedRow[] {
  const accepted: AcceptedRow[] = [];

  for (let line = 0; line < lines.length; line++) {
    const fields = lines[line].split(",");
    if (fields.length === 4) {
      if (fields[0] !== "") {
        if (fields[1] === "person" || fields[1] === "company") {
          if (/^\d+$/.test(fields[2])) {
            if (fields[3] === "active" || fields[3] === "inactive") {
              accepted.push({
                id: fields[0],
                kind: fields[1],
                score: Number(fields[2]),
                status: fields[3],
              });
            }
          }
        }
      }
    }
  }

  return accepted;
}
```

New output:

```ts
type ImportResult =
  | { accepted: true; line: number; row: AcceptedRow }
  | {
      accepted: false;
      line: number;
      reason: "field-count" | "missing-id" | "kind" | "score" | "status";
    };
```

First make only the behavior-preserving structural moves needed to expose parsing and validation. Then design the new result types, validation boundary, explicit error outcomes, routine shape, and tests for every rejection reason and mixed accepted/rejected input. Keep the two intents reviewable and separate; do not edit files.
