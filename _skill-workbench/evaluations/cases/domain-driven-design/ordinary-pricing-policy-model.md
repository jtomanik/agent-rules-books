# Review a Procedural Pricing Policy

Review this implementation for the smallest model improvement that makes the pricing policy explicit and testable. The task is limited to local domain modeling; do not redesign service boundaries or infrastructure.

```ts
export function calculateAdjustment(
  ruleType: string,
  customerStatus: string,
  order: { subtotal: number; createdAt: Date; metadata: Record<string, string> },
): number {
  let adjustment = 0;

  if (ruleType === "LOYALTY" && customerStatus === "GOLD") {
    adjustment += order.subtotal * 0.08;
  }

  if (ruleType === "CAMPAIGN" && order.metadata.campaign === "SUMMER") {
    adjustment += order.subtotal * 0.12;
  }

  if (order.metadata.expiresAt && new Date(order.metadata.expiresAt) < order.createdAt) {
    adjustment = 0;
  }

  if (order.metadata.stackable !== "true" && adjustment > order.subtotal * 0.12) {
    adjustment = order.subtotal * 0.12;
  }

  return adjustment;
}
```

Business facts:

- Eligibility, expiry, and stacking are pricing concepts used by pricing specialists.
- New rule kinds are added monthly.
- A pricing specialist must be able to validate examples with developers.
- The current function has no tests that name those concepts.

Recommend a bounded redesign and the feedback needed to confirm that the model matches the policy.
