# Review a Routine Carrier Quote Integration

This outbound carrier-quote call is in ordinary pre-merge review before its first release. There has been no incident, failed load test, disputed policy, or known production hotspot. Review only this integration's production failure behavior and recommend the smallest changes needed before merge; do not perform a comprehensive checkout audit.

Product and provider contracts:

- A carrier quote is optional. Checkout must continue with `{ kind: "unavailable" }` when the carrier cannot answer within the request budget.
- The request path must not retry carrier calls.
- A valid response is HTTP `200`, JSON content, and `{ amount: non-negative finite number, currency: three-letter string, expires_at: ISO-8601 timestamp }`.
- Provider `4xx` responses indicate a request or contract problem. `429`, `5xx`, timeout, and transport failure mean the quote is unavailable for this checkout.

```ts
const carrierSlots = new Semaphore(Number(env.CARRIER_MAX_IN_FLIGHT));

export async function fetchCarrierQuote(
  cart: Cart,
  requestSignal: AbortSignal,
): Promise<CarrierQuoteResult> {
  const release = await carrierSlots.acquire();

  try {
    const response = await carrierClient.post("/quotes", {
      cartId: cart.id,
      destination: cart.shippingAddress,
      items: cart.items.map((item) => ({
        sku: item.sku,
        quantity: item.quantity,
      })),
      timeoutMs: Number(env.CARRIER_RESPONSE_TIMEOUT_MS),
    });
    const body = await response.json();

    return {
      kind: "available",
      amount: body.amount,
      currency: body.currency,
      expiresAt: body.expires_at,
    };
  } catch (error) {
    logger.warn({ error, cartId: cart.id }, "carrier quote unavailable");
    return { kind: "unavailable" };
  } finally {
    release();
  }
}
```

```env
CHECKOUT_REQUEST_TIMEOUT_MS=2500
CARRIER_RESPONSE_TIMEOUT_MS=2000
CARRIER_MAX_IN_FLIGHT=32
CARRIER_RETRIES=0
```

Implementation facts:

- `Semaphore.acquire()` waits indefinitely unless given a deadline or signal.
- `carrierClient.post()` does not observe `requestSignal` unless it is passed explicitly.
- `timeoutMs` covers response waiting but not connection establishment.
- The client performs no implicit retries.
