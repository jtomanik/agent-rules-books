# Construct a Replay-Safe Import Slice

Design the first implementation slice for this object import. Apply both distributed data correctness and construction-discipline judgment: make the data contracts explicit, then propose readable routines, data structures, defensive boundaries, error semantics, focused tests, and an integration sequence. This is substantial new construction, not a production-readiness, architecture-layer, or refactoring audit.

```ts
type ImportMessage = {
  manifestId: string;
  objectKey: string;
  position: number;
  schemaVersion: 1 | 2;
  checksum?: string;
};

export async function importObject(message: ImportMessage): Promise<void> {
  const bytes = await objectStore.read(message.objectKey);
  const decoded = decode(bytes, message.schemaVersion);
  await database.records.insertMany(decoded.records);
  await checksumIndex.put(message.objectKey, checksum(bytes));
  await broker.ack(message);
}
```

Contracts and constraints:

- The broker is at-least-once and redelivers after consumer crash or acknowledgment timeout.
- PostgreSQL `records` is authoritative; `checksumIndex` is derived and must be rebuildable.
- Each manifest position may be applied once, skipped as an already completed duplicate, or retried after a failed attempt.
- Records for one `objectKey` must preserve source order; different objects may import concurrently.
- Schema versions 1 and 2 overlap for one release, and invalid input must not partially persist.
- Object reads can succeed while the database write, derived-index update, or acknowledgment fails.
- The first slice must be small enough to review and test without introducing a framework, service split, deployment mechanism, overload policy, or speculative generalization.

Return the proposed contracts, routine and type boundaries, error outcomes, minimal implementation slice, and focused duplicate/replay/order/schema/derived-rebuild tests.
