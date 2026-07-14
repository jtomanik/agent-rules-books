# Complete Distilled DDD Audit

Apply the complete Domain-Driven Design Distilled lens to this order-to-cash proposal. Review strategic and tactical choices end to end, but keep recommendations proportionate to business value and complexity.

```yaml
subdomains:
  dynamic_pricing: differentiating
  order_capture: supporting
  invoicing: supporting
  email_notifications: generic

organization:
  teams: [commerce, finance, customer-platform]
  model: one_enterprise_model
  glossary: [Customer, Order, Invoice, Status]
  ownership: architecture_team

design:
  shared_package: commerce-domain
  aggregates:
    CommerceAccount:
      contains: [Customer, Orders, Invoices, Payments, Addresses]
      transaction: one_database_transaction
  services:
    OrderController: validates_prices_and_credit_then_updates_all_objects
  repositories:
    CommerceRepository: returns_complete_object_graph
  value_objects:
    Money: mutable_amount_and_currency_fields

integration:
  pricing_to_order: shared_tables
  order_to_invoicing: synchronous_rpc_with_shared_Order
  invoicing_to_notifications: synchronous_rpc
  vendor_tax: vendor_DTOs_used_in_finance_model
  events: named_after_database_rows

delivery:
  first_release: eight_weeks
  tactical_DDD_for_every_subdomain: true
  modeling_sessions: none
  feedback: design_review_after_code_complete
```

Constraints:

- Pricing strategy changes weekly and is the main commercial differentiator.
- Notifications are conventional template CRUD.
- Finance and Commerce use different meanings of `Customer` and `posted`.
- Payment and tax providers are externally controlled.
- The first release needs only quote, order confirmation, invoice issue, and email receipt.
