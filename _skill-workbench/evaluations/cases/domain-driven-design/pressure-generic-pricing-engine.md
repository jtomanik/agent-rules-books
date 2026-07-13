# Extend the Existing Generic Pricing Engine

The VP of Engineering has promised a new contractual-pricing rule by Friday. The company has already spent nine months on this generic engine, and the lead architect says creating another model now would waste that investment.

```ts
export function applyRule(rule: Rule, context: Record<string, unknown>): Money {
  if (rule.type === "percentage") return percentage(rule, context);
  if (rule.type === "fixed") return fixed(rule, context);
  if (rule.type === "segment") return segment(rule, context);
  if (rule.type === "contract") return contract(rule, context);
  if (rule.type === "contract-renewal") return contractRenewal(rule, context);
  throw new Error(`Unsupported rule ${rule.type}`);
}
```

New requirement:

- A negotiated price is valid only for the products and quantities in an accepted commercial agreement.
- Renewals may inherit selected terms but must re-evaluate eligibility on the renewal date.
- Sales calls both artifacts a `contract`; Billing uses `contract` for the legally executed agreement only.
- The existing engine represents all inputs as string-keyed metadata and all outcomes as one amount.
- The latest branch added 14 type/status checks and has no domain-expert examples.

Decide whether to add another branch or change direction. Give a bounded action that can still meet the deadline, and explain how to protect delivery while testing whether a deeper model is warranted.
