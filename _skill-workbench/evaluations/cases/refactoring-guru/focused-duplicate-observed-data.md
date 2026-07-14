# Focused Technique Decision: Duplicate Observed Data

An invoice editor currently keeps the same domain amount in the UI control and in the invoice object:

```ts
class InvoiceEditor {
  private subtotalText = "0.00";
  private invoice = new Invoice(0);

  onSubtotalInput(text: string): void {
    this.subtotalText = text;
    this.invoice.subtotalCents = parseMoney(text);
    this.refreshTaxPreview();
  }

  load(invoice: Invoice): void {
    this.invoice = invoice;
    this.subtotalText = formatMoney(invoice.subtotalCents);
    this.refreshTaxPreview();
  }
}
```

The team proposes the named `Duplicate Observed Data` technique but disagrees about when it applies and how to perform it safely. Decide whether the symptom and use condition fit, identify the avoid condition, give the source-defined safe steps, and state the required verification. Consult only the smallest detailed packaged guidance needed when compact guidance does not settle those specifics. Do not broaden this into a complete UI architecture audit.
