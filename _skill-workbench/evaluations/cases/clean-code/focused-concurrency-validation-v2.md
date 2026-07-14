# Settle a Concurrency Validation Dispute

Two reviewers disagree about the validation required for this bounded worker-pool change. One accepts a deterministic unit test plus one integration test. The other says the source guidance requires broader schedule-sensitive validation and explicit shutdown behavior.

```ts
class ThumbnailPool {
  private readonly active = new Map<string, Promise<void>>();
  private stopping = false;

  submit(id: string): Promise<void> {
    if (this.stopping) throw new Error("stopping");
    const task = this.generate(id).finally(() => this.active.delete(id));
    this.active.set(id, task);
    return task;
  }

  async stop(): Promise<void> {
    this.stopping = true;
    await Promise.all(this.active.values());
  }
}
```

Resolve only the disputed source interpretation. State the exact concurrency-specific validation dimensions, how to treat intermittent failures, and which shutdown, cancellation, ownership, or tunability properties must be explicit. Do not perform a general code audit.
