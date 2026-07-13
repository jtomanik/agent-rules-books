# Split a Well-Protected Pricing Calculation

The team wants a structural cleanup before adding any new pricing behavior. The public API and every observable result must remain unchanged. The focused tests below are trustworthy, fast, and currently green.

```ts
type Order = {
  items: Array<{ unitPriceCents: number; quantity: number }>;
  customerTier: "standard" | "gold";
  destination: "domestic" | "international";
};

type Price = {
  subtotalCents: number;
  discountCents: number;
  shippingCents: number;
  taxCents: number;
  totalCents: number;
};

export class OrderPricer {
  price(order: Order): Price {
    let subtotalCents = 0;
    for (const item of order.items) {
      subtotalCents += item.unitPriceCents * item.quantity;
    }

    let discountCents = 0;
    if (order.customerTier === "gold" && subtotalCents >= 10_000) {
      discountCents = Math.floor(subtotalCents * 0.1);
    }

    let shippingCents = 500;
    if (order.destination === "international") {
      shippingCents = 2_500;
    } else if (subtotalCents - discountCents >= 5_000) {
      shippingCents = 0;
    }

    const taxableCents = subtotalCents - discountCents + shippingCents;
    const taxCents = Math.floor(taxableCents * 0.2);

    return {
      subtotalCents,
      discountCents,
      shippingCents,
      taxCents,
      totalCents: taxableCents + taxCents,
    };
  }
}
```

```ts
describe("OrderPricer", () => {
  it("prices a standard domestic order", () => {
    expect(pricer.price(order(4_000, "standard", "domestic"))).toEqual({
      subtotalCents: 4_000,
      discountCents: 0,
      shippingCents: 500,
      taxCents: 900,
      totalCents: 5_400,
    });
  });

  it("applies the gold threshold before free shipping", () => {
    expect(pricer.price(order(10_000, "gold", "domestic"))).toEqual({
      subtotalCents: 10_000,
      discountCents: 1_000,
      shippingCents: 0,
      taxCents: 1_800,
      totalCents: 10_800,
    });
  });

  it("charges international shipping", () => {
    expect(pricer.price(order(10_000, "gold", "international"))).toEqual({
      subtotalCents: 10_000,
      discountCents: 1_000,
      shippingCents: 2_500,
      taxCents: 2_300,
      totalCents: 13_800,
    });
  });
});
```

Recommend a concrete, reviewable restructuring sequence. Explain the boundaries of the cleanup and where it should stop. Do not add behavior, redesign the public API, or replace the module wholesale.
