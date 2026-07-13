# Review One Optional Outbound Deadline

This is a routine pre-merge review of one outbound call. There has been no incident, failed load test, policy dispute, or known production hotspot. Review only whether the call has the required production failure behavior; do not perform a broader integration or service audit.

Contract:

- The recommendation is optional. Checkout must continue with `{ kind: "unavailable" }` if the provider does not answer within 150 ms.
- The request path must not retry this call.

```ts
export async function fetchRecommendation(
  cartId: string,
): Promise<RecommendationResult> {
  try {
    const response = await recommendationClient.get(`/carts/${cartId}`);
    return { kind: "available", recommendation: await response.json() };
  } catch {
    return { kind: "unavailable" };
  }
}
```

Client facts:

- `recommendationClient.get()` has no default deadline.
- The client performs no implicit retries.

State whether this meets the contract and recommend the smallest correction needed before merge.
