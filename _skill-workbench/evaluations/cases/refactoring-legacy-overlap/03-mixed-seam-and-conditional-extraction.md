# Add a Renewal Rule and Consolidate Duplicated Eligibility Logic

The renewal worker has no focused tests. It constructs its database client internally and reads the system clock directly. A slow end-to-end test covers only the successful renewal path.

Product now requires trial accounts older than 30 days to be ineligible for automatic renewal. In the same delivery, the duplicated eligibility conditional should have one clear owner, without changing any other current outcome.

```ts
type Account = {
  id: string;
  state: "active" | "paused" | "closed";
  plan: "trial" | "paid";
  trialStartedAt: string | null;
  balanceCents: number;
};

export class RenewalWorker {
  private readonly database: RenewalDatabase;

  constructor(private readonly accountId: string) {
    this.database = new RenewalDatabase(process.env.RENEWAL_DSN!);
  }

  quote(): number | null {
    const account = this.database.accounts.load(this.accountId);
    const now = new Date();

    if (
      account.state !== "closed" &&
      account.state !== "paused" &&
      account.balanceCents >= 0
    ) {
      return this.database.prices.forPlan(account.plan, now);
    }

    return null;
  }

  renew(): "renewed" | "skipped" {
    const account = this.database.accounts.load(this.accountId);
    const now = new Date();

    if (
      account.state !== "closed" &&
      account.state !== "paused" &&
      account.balanceCents >= 0
    ) {
      this.database.transaction(() => {
        this.database.renewals.insert({ accountId: account.id, at: now.toISOString() });
        this.database.accounts.markRenewed(account.id, now.toISOString());
      });
      return "renewed";
    }

    return "skipped";
  }
}
```

Provide a safe, reviewable work order and patch boundaries for adding the trial-age rule and then eliminating the duplicated conditional. Be explicit about what must be learned or controlled before semantic edits and what must remain behavior-preserving during the structural work.
