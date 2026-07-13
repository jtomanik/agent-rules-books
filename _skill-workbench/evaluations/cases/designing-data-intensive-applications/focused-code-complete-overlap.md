# Construct One Replay-Safe Projection Slice

Design one bounded implementation slice for applying manifest entries. Apply both distributed-data correctness and construction-discipline judgment.

```ts
type ManifestEntry = {
  manifestId: string;
  position: number;
  objectKey: string;
};

export async function applyEntry(entry: ManifestEntry): Promise<ApplyResult> {
  throw new Error("not implemented");
}
```

Contracts:

- The broker is at-least-once and can redeliver after a crash or acknowledgment timeout.
- PostgreSQL records are authoritative; the checksum index is derived and rebuildable.
- One manifest position may be applied once or reported as an already-applied duplicate.
- Entries for one manifest must apply in position order; different manifests may proceed concurrently.
- The schema is fixed for this slice, and no external notification or production-capacity policy is involved.

Resolve the replay/order/derived-state boundary and then propose the routine and type boundaries, defensive validation, error outcomes, smallest implementation increment, and focused tests. Keep retrieval bounded to the sections needed for this slice; do not perform either complete book audit or edit files.
