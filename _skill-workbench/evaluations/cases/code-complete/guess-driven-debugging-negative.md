# Diagnose Before Applying a Guessed Fix

A cache-backed lookup intermittently returns stale values in one deterministic integration test. A manager wants to add a second retry immediately because "it is probably a race." No root cause is established yet, and the requested task is only to diagnose the failure and identify the minimal evidence-supported correction.

```ts
it("returns the value written in the same session", async () => {
  await store.write("account:42", "active");
  expect(await store.read("account:42")).toBe("active");
});
```

Explain the next diagnostic steps and the evidence needed before changing code. Do not perform a broad construction, architecture, data-system, reliability, readability, or refactoring review, and do not edit files.
