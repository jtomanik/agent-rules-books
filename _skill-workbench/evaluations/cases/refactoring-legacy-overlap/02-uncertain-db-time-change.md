# Add a Billing Grace Period Without Guessing Existing Behavior

Product wants a 48-hour grace period before an overdue account is charged. This class has no automated tests. The team does not know whether charging exactly at `nextChargeAt` is intentional, how local time has affected stored timestamps, or whether callers rely on the current exception and transaction behavior.

```ts
type AccountRow = {
  id: string;
  nextChargeAt: string;
  balanceCents: number;
};

export class BillingScheduler {
  private readonly database: BillingDatabase;

  constructor(private readonly accountId: string) {
    this.database = new BillingDatabase(process.env.BILLING_DSN!);
    this.database.connect();
  }

  chargeIfDue(): "charged" | "not-due" {
    const account: AccountRow = this.database.accounts.find(this.accountId);
    const now = new Date();

    if (new Date(account.nextChargeAt) <= now) {
      this.database.transaction(() => {
        this.database.charges.insert({
          accountId: account.id,
          amountCents: account.balanceCents,
          chargedAt: now.toISOString(),
        });
        this.database.accounts.markCharged(account.id, now.toISOString());
      });
      return "charged";
    }

    return "not-due";
  }
}
```

There is a staging database, but it is slow and its fixtures are shared. No general cleanup has been requested. Give the safest bounded implementation and verification plan for the grace-period change. Call out any product decision that must be resolved instead of inferred from the code.
