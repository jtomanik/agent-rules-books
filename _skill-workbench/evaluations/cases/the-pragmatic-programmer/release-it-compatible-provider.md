# Make a Provider Integration Reversible and Survivable

Review this outbound payment-provider proposal. Address both engineering
ownership and production failure behavior.

```ts
export async function capture(order: Order): Promise<void> {
  const payload = VendorPayPayload.from(order);
  const response = await fetch("https://vendor-pay.example/capture", {
    method: "POST",
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    return capture(order);
  }

  order.vendorTransaction = await response.json();
}
```

```yaml
operations:
  timeout: none
  retry_limit: none
  idempotency_contract: unknown
  concurrency_limit: none
  failover: operator_edits_source_and_redeploys
  diagnostics: response_body_discarded
  second_provider: required_this_quarter
```

Define the owner and reversible boundary for provider knowledge and remove the
manual failover ritual. Also define the timeout, retry-safety, demand-limit,
failure-isolation, recovery, and diagnostic decisions required before this path
can be called production-ready.
