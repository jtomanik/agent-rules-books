# Diagnose an Observable Pure-Function Failure

The failure is deterministic, current behavior is fully observable, focused tests exist, and the pure function has no collaborators, I/O, hidden state, clock, randomness, concurrency, or substitution barrier. A manager says to call the parser twice because the failure is "probably intermittent."

```ts
export function parseDecimal(value: string): number {
  return Number(value.replace(",", ""));
}

it("parses a comma decimal", () => {
  expect(parseDecimal("1,25")).toBe(1.25);
});
```

The test consistently reports `expected 1.25, received 125`. Diagnose the exact cause and minimal evidence-supported correction. Do not add a retry, redesign the API, perform a construction or readability audit, or edit files.
