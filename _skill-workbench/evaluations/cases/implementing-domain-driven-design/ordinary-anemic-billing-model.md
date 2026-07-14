# Review an Anemic Billing Implementation

Review this billing slice for a bounded implementation correction. The Billing context and its terminology are already accepted; do not redesign the organization or platform.

```ts
class Invoice {
  id!: string;
  status!: string;
  total!: number;
  currency!: string;
  dueDate!: Date;

  setStatus(value: string) { this.status = value; }
  setTotal(value: number) { this.total = value; }
  setCurrency(value: string) { this.currency = value; }
}

export async function issueInvoice(id: string): Promise<void> {
  const row = await genericRepository.find("invoices", { id });
  if (row.status !== "DRAFT") throw new Error("wrong status");
  if (row.total <= 0) throw new Error("wrong total");
  row.status = "ISSUED";
  row.issuedAt = new Date();
  await genericRepository.save("invoices", row);
  await broker.publish("invoice-row-updated", row);
}
```

Rules:

- Only a draft Invoice with at least one valid line may be issued.
- Invoice totals use currency-safe Money arithmetic.
- Issuing records the issue date and produces `InvoiceIssued`.
- The application layer owns transaction and publication coordination.

Recommend the smallest Entity/Value Object, Repository, service, and event changes that express those rules.
