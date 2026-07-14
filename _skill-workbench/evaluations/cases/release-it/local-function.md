# Rename and Split a Pure Local Function

Review this pure local function. Propose clearer names and split its validation, normalization, and calculation phases without changing observable behavior. Show the resulting TypeScript and keep the change local.

```ts
type PriceInput = {
  quantity: number;
  unitPrice: number;
  discountPercent?: number;
};

export function doIt(x: PriceInput): number {
  if (!Number.isFinite(x.quantity) || !Number.isFinite(x.unitPrice)) {
    throw new Error("invalid price input");
  }
  if (x.quantity < 0 || x.unitPrice < 0) {
    throw new Error("invalid price input");
  }

  const p = x.discountPercent == null
    ? 0
    : Math.min(100, Math.max(0, x.discountPercent));

  return x.quantity * x.unitPrice * (1 - p / 100);
}
```

The function performs no I/O, reads no global state, and is not used in a concurrent or distributed path.
