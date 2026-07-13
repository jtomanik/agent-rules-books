# Apply the Evans Domain-Driven Design Lens

Use Eric Evans's Domain-Driven Design lens to review this pricing brief. Identify the model and context decisions that should be settled before implementation, then recommend the smallest useful next modeling step.

```yaml
initiative: negotiated-pricing
business_priority: differentiating
teams: [sales, pricing, billing]
terms:
  sales:
    quote: a negotiable commercial proposal
    customer: an account being pursued
  pricing:
    quote: a priced configuration with eligibility and expiry rules
    customer: the party whose segment and agreements affect price
  billing:
    quote: an immutable charging commitment
    customer: the legal entity that receives an invoice
current_plan:
  shared_types: [Customer, Quote, PriceAdjustment]
  implementation: one shared pricing library
  integration: direct database access among all three applications
open_questions:
  - whether negotiated discounts may stack
  - whether a quote remains valid after a segment change
  - when a commercial proposal becomes a billing commitment
```

Keep the review centered on the domain model, language, context boundaries, and integration relationships. Do not turn it into a general delivery or production-readiness audit.
