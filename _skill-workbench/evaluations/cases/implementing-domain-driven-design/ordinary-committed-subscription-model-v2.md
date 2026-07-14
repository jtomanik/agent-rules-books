# Implement a Committed Subscription Context

The Subscription context and its language are already approved. Implement the smallest coherent tactical model for these settled rules:

- A Subscription has stable identity and owns its current Plan and renewal date.
- Money and BillingPeriod have value semantics.
- Changing Plan must preserve the invariant that the next renewal charge is nonnegative and denominated in the account currency.
- Customer and Product belong to other contexts and are referenced by identity.
- The application use case loads one Subscription, asks it to change plan, saves it, and publishes a meaningful past-tense fact after commit.
- A read-only account page needs a projection that combines Subscription data with translated Customer display data.

Define Aggregate, Entity or Value Object, Repository, Domain Event, Application Service, module, translation, and read-representation responsibilities. Keep one local transaction and do not revisit whether the context should exist.
