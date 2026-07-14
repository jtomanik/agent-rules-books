# Choose the Smallest Effective DDD Investment

Use the Domain-Driven Design Distilled lens to decide where this program warrants strategic or tactical DDD and where simpler delivery is enough. Recommend the smallest effective modeling investment.

```yaml
program: retail-returns
capabilities:
  adaptive_returns_policy:
    business_value: differentiating
    change_rate: weekly
    rules: depend_on_customer_history_product_condition_and_channel
  carrier_label_purchase:
    business_value: commodity
    change_rate: vendor_driven
    behavior: validate_address_call_carrier_store_label
  notification_preferences:
    business_value: supporting
    change_rate: quarterly
    behavior: CRUD
teams: [returns, fulfillment, customer-care]
proposal:
  - create Aggregates, Repositories, Domain Services, and Domain Events for every capability
  - share Customer, Return, Label, and Status classes across all teams
  - place all operations in one transaction
```

Explain which subdomain deserves the deepest modeling, where tactical machinery must earn its cost, and what context/language decisions are needed first.
