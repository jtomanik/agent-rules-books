# Choose the Safest Order for a Legacy Rule and Shared Eligibility Owner

The subscription promotion worker has no focused tests. It constructs its database internally and reads the system clock directly. A slow end-to-end test covers only one successful paid-subscription path.

Product now requires introductory subscriptions older than 60 days to be ineligible for automatic credit. The duplicated eligibility condition in `previewCredit()` and `applyCredit()` should also have one clear owner without changing any other current outcome.

```ts
type Subscription = {
  id: string;
  state: "active" | "paused" | "cancelled";
  kind: "introductory" | "paid";
  startedAt: string | null;
  balanceCents: number;
  manualHold: boolean;
};

export class PromotionWorker {
  private readonly database: SubscriptionDatabase;

  constructor(private readonly subscriptionId: string) {
    this.database = new SubscriptionDatabase(process.env.SUBSCRIPTION_DSN!);
  }

  previewCredit(): number | null {
    const subscription = this.database.subscriptions.load(this.subscriptionId);
    const now = new Date();

    if (
      subscription.state === "active" &&
      subscription.balanceCents >= 0 &&
      !subscription.manualHold
    ) {
      return this.database.credits.preview(subscription.kind, now);
    }

    return null;
  }

  applyCredit(): "applied" | "skipped" {
    const subscription = this.database.subscriptions.load(this.subscriptionId);
    const now = new Date();

    if (
      subscription.state === "active" &&
      subscription.balanceCents >= 0 &&
      !subscription.manualHold
    ) {
      this.database.transaction(() => {
        this.database.credits.insert({
          subscriptionId: subscription.id,
          at: now.toISOString(),
        });
        this.database.subscriptions.markCredited(
          subscription.id,
          now.toISOString(),
        );
      });
      return "applied";
    }

    return "skipped";
  }
}
```

Choose the safest order for gaining deterministic test control, adding the 60-day rule, and consolidating the duplicated eligibility condition. Explain why that order is safer than the alternatives, identify decisions that must be clarified first, and define reviewable patch boundaries. Do not assume that either the semantic change or the extraction must come first; decide from the evidence.
