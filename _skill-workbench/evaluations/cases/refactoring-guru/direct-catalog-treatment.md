# Refactoring.Guru Catalog Review

Use the Refactoring.Guru lens to diagnose this code and recommend the smallest suitable treatment. The supplied tests pass and define the observable behavior; this is a structural review, not a feature request.

```ts
export function invoiceLabel(
  customerName: string,
  customerCountry: string,
  customerPostalCode: string,
  subtotalCents: number,
  taxCents: number,
): string {
  // Build the customer part.
  const customer = `${customerName} (${customerCountry}-${customerPostalCode})`;

  // Build the amount part.
  const totalCents = subtotalCents + taxCents;
  const amount = `${(totalCents / 100).toFixed(2)} EUR`;

  return `${customer}: ${amount}`;
}
```

Identify the concrete smell or smells, compare the plausible named treatments, state the verification path and stopping condition, and avoid unrelated redesign.
