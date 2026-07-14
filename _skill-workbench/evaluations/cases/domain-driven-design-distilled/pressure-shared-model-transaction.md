# Respond to a Mandated Shared Model

The CTO has mandated one shared model and one transaction for the first release because separate contexts are considered too slow. The launch date is in ten days, and the team has already generated entities and migrations from this design.

```yaml
capabilities:
  core_pricing:
    change_rate: weekly
    language: offer_eligibility_agreement_adjustment
  supporting_fulfillment:
    change_rate: monthly
    language: shipment_allocation_delivery_promise
  generic_notifications:
    change_rate: rare
    language: template_recipient_delivery_status

shared_model:
  Aggregate: CommerceAccount
  contains: [PriceBook, Offer, Order, Shipment, Notification]
  transaction: single_commit
  shared_status: [DRAFT, ACTIVE, COMPLETE, FAILED]
  repository: CommerceAccountRepository
```

New requirement: pricing must support negotiated eligibility rules without waiting for Fulfillment or Notifications releases.

Give a decision that protects the deadline while addressing the model and transaction risks. State what should be separated now, what may remain simple, and which tactical patterns must justify their cost.
