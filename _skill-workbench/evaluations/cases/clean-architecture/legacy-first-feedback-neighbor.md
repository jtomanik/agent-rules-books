# Gain First Feedback Around Database and Time

The team must change the suspension threshold from an unknown current rule to a proposed seven-day rule, but nobody knows all current outcomes. There are no trustworthy focused tests. The class constructs a database client and reads ambient time, so it cannot be instantiated cheaply or driven deterministically.

```ts
export class AccountSuspender {
  private readonly database = new ProductionDatabase(process.env.DSN!);

  suspend(accountId: string): void {
    const account = this.database.accounts.find(accountId);
    const now = new Date();
    if (now.getTime() - account.lastPaymentAt.getTime() > unknownThreshold()) {
      this.database.accounts.markSuspended(accountId, now);
    }
  }
}
```

Do not choose a target architecture or implement the seven-day rule yet. Identify the smallest observation path and dependency seams needed to characterize current behavior and gain first deterministic feedback. Keep the public API stable and separate the later semantic change from any structural preparation.
