# Diagnose And Bound An Invoice Refactor

All current tests pass. Review this function without changing invoice behavior or public output.

```ts
export function renderInvoice(
  customerName: string,
  customerStreet: string,
  customerCity: string,
  customerPostalCode: string,
  itemNames: string[],
  itemPricesCents: number[],
  taxRate: number,
): string {
  // Calculate subtotal.
  let subtotal = 0;
  for (const price of itemPricesCents) {
    subtotal += price;
  }

  // Calculate tax.
  const tax = Math.round(subtotal * taxRate);

  // Render address.
  const address = `${customerName}\n${customerStreet}\n${customerPostalCode} ${customerCity}`;

  // Render lines.
  const lines: string[] = [];
  for (let i = 0; i < itemNames.length; i += 1) {
    lines.push(`${itemNames[i]}: ${(itemPricesCents[i] / 100).toFixed(2)}`);
  }

  return `${address}\n\n${lines.join("\n")}\n\nTax: ${(tax / 100).toFixed(2)}`;
}
```

Classify the code smells using a recognized smell catalog, choose the smallest treatment for each smell that actually obstructs local reasoning, order the treatments by risk, and define verification and a stop condition. Do not turn this into a larger architecture review.
