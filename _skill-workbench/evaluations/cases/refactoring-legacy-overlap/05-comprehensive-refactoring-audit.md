# Comprehensive Refactoring Audit of a Proposed Cleanup

Give this proposed change a comprehensive, end-to-end Martin Fowler refactoring audit. The module has a fast public-contract suite covering current totals, discount thresholds, shipping boundaries, error values, and event order. The proposal is intended to preserve all observable behavior.

Current implementation:

```ts
export function settle(order: Order, gateway: Gateway): Receipt {
  if (order.items.length === 0) throw new EmptyOrderError();

  const subtotal = order.items.reduce(
    (sum, item) => sum + item.unitPriceCents * item.quantity,
    0,
  );
  const discount = order.customerTier === "gold" && subtotal >= 10_000
    ? Math.floor(subtotal * 0.1)
    : 0;
  const shipping = order.international ? 2_500 : subtotal - discount >= 5_000 ? 0 : 500;
  const taxable = subtotal - discount + shipping;
  const tax = Math.floor(taxable * 0.2);
  const total = taxable + tax;

  gateway.authorize(total);
  gateway.capture(total);
  return { subtotal, discount, shipping, tax, total };
}
```

Proposed replacement:

```ts
interface SettlementStrategy {
  execute(order: Order, gateway: Gateway, expedited: boolean): Receipt;
}

class DefaultSettlementStrategy implements SettlementStrategy {
  execute(order: Order, gateway: Gateway, expedited: boolean): Receipt {
    if (order.items.length === 0) throw new EmptyOrderError();

    const numbers = new SettlementNumbers();
    numbers.subtotal = order.items.reduce(
      (sum, item) => sum + item.unitPriceCents * item.quantity,
      0,
    );
    numbers.discount = order.customerTier === "gold" && numbers.subtotal >= 10_000
      ? Math.floor(numbers.subtotal * 0.1)
      : 0;
    numbers.shipping = expedited
      ? 4_000
      : order.international
        ? 2_500
        : numbers.subtotal - numbers.discount >= 5_000
          ? 0
          : 500;
    numbers.tax = Math.floor(
      (numbers.subtotal - numbers.discount + numbers.shipping) * 0.2,
    );
    numbers.total = numbers.subtotal - numbers.discount + numbers.shipping + numbers.tax;

    gateway.capture(numbers.total);
    gateway.authorize(numbers.total);
    return numbers.toReceipt();
  }
}

class SettlementNumbers {
  subtotal = 0;
  discount = 0;
  shipping = 0;
  tax = 0;
  total = 0;

  toReceipt(): Receipt {
    return {
      subtotal: this.subtotal,
      discount: this.discount,
      shipping: this.shipping,
      tax: this.tax,
      total: this.total,
    };
  }
}

export class SettlementFacade {
  constructor(private readonly strategy: SettlementStrategy) {}

  settle(order: Order, gateway: Gateway, expedited = false): Receipt {
    return this.strategy.execute(order, gateway, expedited);
  }
}
```

Identify what is and is not refactoring, which parts should be rejected or resequenced, the smallest useful transformations, the verification obligations, and a defensible stopping point.
