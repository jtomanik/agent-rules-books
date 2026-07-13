# Review Checkout Provider Integration

The payment-provider integration below is scheduled to receive all checkout traffic tomorrow. The provider sometimes returns `429`, stalls for several seconds, and occasionally returns an HTML error page with status `200`. During the last load test, checkout latency rose until every request worker was busy.

Review the raw implementation and configuration. Recommend the smallest production-ready changes required before enabling 100% traffic. Keep the review scoped to this integration and explain what must happen when the provider is slow, overloaded, unavailable, or returns a malformed response.

```ts
const provider = new ProviderClient({
  baseUrl: env.PAYMENT_URL,
  retries: Number(env.PAYMENT_SDK_RETRIES),
  retryDelayMs: 100,
});

const paymentSlots = new Semaphore(Number(env.PAYMENT_MAX_IN_FLIGHT));
const pendingAuthorizations: AuthorizationRequest[] = [];

export async function authorizePayment(
  order: Order,
  requestSignal: AbortSignal,
): Promise<AuthorizationResult> {
  const release = await paymentSlots.acquire();
  const transaction = await database.beginTransaction();

  try {
    for (let attempt = 0; attempt < 4; attempt += 1) {
      try {
        const response = await provider.post("/authorize", {
          orderId: order.id,
          amount: order.total,
          currency: order.currency,
        });
        const body = await response.json();

        await transaction.authorizations.insert({
          orderId: order.id,
          providerId: body.authorization_id,
          state: body.state,
        });
        await transaction.commit();
        metrics.increment("payment.authorized");
        return { kind: "authorized", providerId: body.authorization_id };
      } catch (error) {
        logger.warn({ error, orderId: order.id }, "provider attempt failed");
        await sleep(100);
      }
    }

    pendingAuthorizations.push({ orderId: order.id, amount: order.total });
    await transaction.commit();
    return { kind: "pending" };
  } finally {
    release();
  }
}
```

```env
PAYMENT_SDK_RETRIES=2
PAYMENT_MAX_IN_FLIGHT=400
CHECKOUT_REQUEST_TIMEOUT_MS=2500
PAYMENT_CONNECT_TIMEOUT_MS=0
PAYMENT_RESPONSE_TIMEOUT_MS=0
PENDING_AUTHORIZATION_CAPACITY=0
```

Configuration semantics:

- A timeout value of `0` means the SDK default, which is no deadline.
- A capacity of `0` means unbounded.
- The SDK retries transport errors and `429`/`5xx` responses.
- `ProviderClient.post` does not use `requestSignal` unless it is passed explicitly.
- `Semaphore.acquire` waits indefinitely.
