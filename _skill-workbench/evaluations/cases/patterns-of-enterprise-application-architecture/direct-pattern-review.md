# Direct pattern review

Use the Patterns of Enterprise Application Architecture skill to review this proposed invoice-adjustment endpoint. Choose the smallest fitting business-logic, persistence, transaction, and boundary patterns, and explain where each responsibility belongs.

```text
POST /invoices/{id}/adjust
  controller loads InvoiceRow through the ORM
  controller applies tax and discount rules
  controller mutates InvoiceRow
  controller calls accountingClient.postAdjustment(...)
  ORM flushes sometime before the response
  controller returns InvoiceRow as JSON
```

The adjustment rules are currently three independent calculations. Product expects jurisdiction-specific exemptions and adjustment approval rules next quarter. The accounting call is remote and cannot participate in the database transaction.
