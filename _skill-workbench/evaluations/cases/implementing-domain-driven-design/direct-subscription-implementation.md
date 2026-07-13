# Apply Implementing Domain-Driven Design

Use the Implementing Domain-Driven Design lens to turn this approved Subscription context into an implementation design. Cover Aggregate boundaries, identities, Repository contracts, application coordination, Domain Events, modules, and the read model.

Approved language and rules:

```text
Subscription: a customer's active commercial agreement for one plan
Renewal: the decision to extend a Subscription for another term
RenewalWindow: the dates during which automatic renewal may be evaluated

- A cancelled Subscription cannot renew.
- Renewal must use the plan terms captured for the next term.
- At most one renewal may be accepted for a Subscription and term.
- Payment authorization is owned by the Payments context.
- Customer-facing renewal history may lag by up to one minute.
```

Current proposal:

```yaml
Subscription:
  contains: [Customer, Plan, PaymentMethod, RenewalHistory]
  setters: public
  repository: GenericRepository<SubscriptionRow>
RenewalService:
  transaction: loads_and_updates_Subscription_Customer_Plan_and_Payment
events:
  RenewalRowInserted: emitted_after_HTTP_response
queries:
  renewal_history: load_complete_Subscription_graph
```

Produce an implementation-focused correction without reopening the approved context boundary.
