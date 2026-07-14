# Comprehensive Legacy-Code Assessment of a Billing Entry Point

Give this subsystem a comprehensive, end-to-end Michael Feathers legacy-code assessment. No rewrite or cleanup implementation has been requested; the immediate need is a safe change strategy for a forthcoming billing-policy change.

```ts
export class BillingController {
  static currentTenant = "";

  constructor() {
    GlobalConfig.loadFromProcess();
    Database.connect(GlobalConfig.billingDsn());
    Metrics.startReporter();
  }

  handle(request: FrameworkRequest): FrameworkResponse {
    BillingController.currentTenant = request.header("x-tenant")!;
    const now = new Date();
    const account = Database.accounts.find(request.param("accountId"));

    if (account.status === "closed") {
      Logger.info("billing skipped");
      return FrameworkResponse.json(409, { code: "closed" });
    }

    const amount = account.lines.reduce(
      (sum, line) => sum + line.quantity * line.unitPriceCents,
      0,
    );

    if (FeatureFlags.enabled("regional-tax")) {
      const tax = TaxService.fetchFor(
        BillingController.currentTenant,
        account.region,
        amount,
      );
      Database.invoices.insert({ accountId: account.id, amount, tax, at: now });
      MessageBus.publish("invoice.created", { accountId: account.id, amount, tax });
      return FrameworkResponse.json(201, { amount, tax });
    }

    Database.invoices.insert({ accountId: account.id, amount, tax: 0, at: now });
    MessageBus.publish("invoice.created", { accountId: account.id, amount, tax: 0 });
    return FrameworkResponse.json(201, { amount, tax: 0 });
  }
}
```

Current evidence:

- There are no focused tests for `BillingController`.
- A nightly browser test reaches the happy path through a shared staging database.
- Equality, timezone, transaction, retry, and duplicate-message behavior are undocumented.
- The framework request, static database API, feature flags, tax service, clock, global tenant, and message bus cannot currently be substituted.
- Operations has observed occasional duplicate invoices, but the causal path is unknown.

Assess change points, observation and test points, seams, dependency barriers, suitable legacy techniques, risky boundaries, sequencing, cleanup obligations, and stop conditions. Distinguish facts that can be characterized from product or operational decisions that require clarification.
