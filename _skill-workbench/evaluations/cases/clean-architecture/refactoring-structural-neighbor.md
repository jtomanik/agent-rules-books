# Sequence a Protected Structural Refactoring

The public behavior is complete, intentional, and protected by focused green tests. Architecture ownership and policy/detail boundaries are already accepted. Do not change behavior or redesign the API.

```ts
export class RangeFormatter {
  format(start: number, end: number, compact: boolean): string {
    let result = "";
    if (compact) {
      if (start === end) {
        result = `${start}`;
      } else {
        result = `${start}-${end}`;
      }
    } else {
      if (start === end) {
        result = `from ${start}`;
      } else {
        result = `from ${start} through ${end}`;
      }
    }
    return result;
  }
}
```

The team has already chosen two behavior-preserving moves: extract the compact and expanded formatting branches, then replace the temporary result with direct returns. Recommend a small, reversible, reviewable sequence and a stopping condition. This is an explicit refactoring-only task; do not turn it into general local-hygiene, architecture, legacy-control, or production review.
