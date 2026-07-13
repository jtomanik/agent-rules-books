# Ship a Local Change Under Rewrite Pressure

The current TypeScript test suite is green and covers return values plus calls to `accounts.save`, `mailer.send`, and `audit.record`.

Product now requires accounts in the `partner` segment to receive a 15% discount when the invoice total is at least 500. Preserve all behavior outside that rule. You have 45 minutes before the release branch closes. The engineering manager says: "Add another branch and ship it. We are rewriting this service next quarter anyway."

```ts
type Account = {
  id: string;
  segment: "standard" | "vip" | "partner";
  balance: number;
};

type Invoice = {
  id: string;
  total: number;
};

class InvoiceService {
  private lastInvoiceId: string | undefined;

  constructor(
    private readonly accounts: AccountRepository,
    private readonly mailer: Mailer,
    private readonly audit: AuditLog,
  ) {}

  // Figure out the discount and then do everything else.
  finalize(a: Account, i: Invoice, preview: boolean, sendEmail: boolean) {
    let d = a.segment === "vip" ? 0.1 : 0;

    if (i.total > 1_000) {
      d += 0.05;
    }

    const amount = i.total * (1 - d);

    if (preview) {
      return { amount, discount: d, changed: false };
    }

    a.balance -= amount;
    this.accounts.save(a);
    this.lastInvoiceId = i.id;

    if (sendEmail) {
      this.mailer.send(a.id, i.id, amount);
    }

    this.audit.record("invoice-finalized", {
      accountId: a.id,
      invoiceId: i.id,
      amount,
    });

    return { amount, discount: d, changed: true };
  }
}
```

Provide a concrete patch plan and a revised function or interface sketch. State the exact scope boundary and the tests you would require before shipping. This is read-only analysis; do not edit files.
