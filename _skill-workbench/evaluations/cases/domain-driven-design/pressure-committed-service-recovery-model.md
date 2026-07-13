# Deliver the Committed Recovery Model

The team has already committed to replace a generic exception engine with an implementation-driving model inside the Service Recovery context. Do not revisit whether modeling is worth the investment. A Friday deadline and six months of sunk cost in the old engine are now being used to argue for one more generic branch.

```ts
export function applyException(
  type: string,
  state: Record<string, string | number | boolean>,
): Record<string, string | number | boolean> {
  if (type === "delay") return applyDelay(state);
  if (type === "reroute") return applyReroute(state);
  if (type === "credit") return applyCredit(state);
  if (type === "vip_override") return applyVipOverride(state);
  throw new Error(`unsupported exception ${type}`);
}
```

Recovery specialists use different concepts:

- A `Disruption` is an observed failure that threatens a service commitment.
- A `RecoveryOption` is a feasible operational response, not yet promised to the customer.
- A `RecoveryPromise` is the response accepted for one affected commitment.
- A `GoodwillCredit` acknowledges harm but does not recover the service.
- Rerouting may satisfy a promise; a credit alone never does.
- The next requested `vip_override` must choose among recovery options under a customer-specific commitment, not bypass the distinctions above.

Develop the deeper model that should drive the Friday slice, and name the expert scenarios that would prove or disprove it. Give a bounded incremental path that preserves current behavior and delivery while moving one vertical slice out of the generic engine. Do not propose a platform rewrite or reduce the task to another type/status branch.
