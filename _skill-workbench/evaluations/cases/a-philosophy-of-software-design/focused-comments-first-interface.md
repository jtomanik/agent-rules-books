Two teams disagree about how to settle an unclear public interface before
implementation.

```text
Option A: reserve(userId, sku, quantity, retryMode, publishEvent)
Option B: reserve(request) -> ReservationResult
```

The implementation will coordinate stock checks, idempotency records, and an
event publisher, but callers should not depend on those mechanics. Neither team
can yet state the guarantees for duplicate requests, unavailable stock, or
publication failure without a long explanation.

Give the specific design technique for using candidate public contracts and
explanatory comments before implementation. State how many plausible designs
must be compared, which criteria should compare them, what the comments should
describe, and what a complicated explanatory comment signals. This is a
bounded interface-design question, not a complete system audit.
