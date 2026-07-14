# Review Meaning Boundaries and Replayable Data Flow

Review this invoice-posting design. Address both the meaning boundary between Billing and Ledger and the correctness of the asynchronous data path.

```yaml
billing:
  posted: invoice has been issued to the customer
  source_of_truth: billing-postgres
  publish_path: transaction_outbox
  event: InvoicePosted
  payload: { invoice_id, customer_id, status, amount, currency }

ledger:
  posted: balanced debit and credit entries are durable
  source_of_truth: ledger-postgres
  consumes_billing_status_directly: true
  idempotency: none

broker:
  delivery: at_least_once
  order: per_invoice_id
  retention_days: 7

projections:
  finance_dashboard:
    input: InvoicePosted
    schema_version: omitted
    checkpoint: in_memory
    rebuild: none
```

Constraints:

- Billing and Ledger must evolve their `posted` concepts independently.
- The broker may redeliver and reorder messages after partition changes.
- A projection defect may require replay after the seven-day retention window.
- A duplicate event must not create duplicate ledger entries.

Recommend the minimum context, translation, schema, idempotency, and rebuild contracts needed.
