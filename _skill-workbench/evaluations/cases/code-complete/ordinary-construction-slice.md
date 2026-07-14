# Design One Verifiable Construction Slice

Implement the first production slice of an order-quote function. The input comes from an HTTP JSON body and is therefore untrusted. Keep the solution local to this module; persistence, networking, retries, deployment, and distributed-system behavior are out of scope.

```ts
type QuoteRequest = {
  customerKind: "retail" | "trade";
  subtotalCents: number;
  destination: "domestic" | "international";
  expedited?: boolean;
};

type Quote = {
  subtotalCents: number;
  discountCents: number;
  shippingCents: number;
  totalCents: number;
};

export function quoteOrder(input: unknown): Quote {
  throw new Error("not implemented");
}
```

Required behavior:

- Reject malformed input with a `QuoteInputError` that names the invalid field.
- Require nonnegative integer cents.
- Trade customers receive a 10% subtotal discount, rounded down to whole cents.
- Domestic shipping is 500 cents; international shipping is 1500 cents.
- Expedited shipping adds 700 cents.
- The total is subtotal minus discount plus shipping.

Provide a concrete implementation sketch and tests. Explain the construction decisions for input validation, data meaning, arithmetic, control shape, error semantics, and the smallest verifiable increment. Do not perform a comprehensive audit or edit files.
