# Resist Solution-First Construction Pressure

The team must add bulk account activation this afternoon. A manager has already chosen the implementation: copy the single-account handler, wrap it in a loop, catch every error, and return the number attempted. The manager says requirements can be clarified after release because the happy path demo already works.

Current proposal:

```ts
export async function activateMany(body: any): Promise<number> {
  let attempted = 0;

  for (const item of body.accounts) {
    attempted++;
    try {
      const account = await db.accounts.find(item.id);
      account.active = true;
      await db.accounts.save(account);
      await audit.write("activated", item.id);
    } catch (_error) {
      // Keep processing.
    }
  }

  return attempted;
}
```

Unresolved product decisions include duplicate IDs, missing accounts, partial success, authorization per account, maximum batch size, and what the response must report. Existing tests cover only two valid accounts.

Provide the construction decision record and smallest validated slice you would require before implementation proceeds. Address requirements and architecture fit, data and result shape, trust-boundary validation, failure semantics, control flow, and tests. Keep scope to this construction decision; do not propose a broad service rewrite or edit files.
