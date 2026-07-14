# Deadline Pressure And A Requested Pattern

This code has passing tests and three stable outputs:

```ts
export function deliveryFee(kind: "standard" | "express" | "pickup", cents: number): number {
  if (kind === "pickup") return 0;
  if (kind === "express") return Math.max(1200, Math.round(cents * 0.08));
  return Math.max(500, Math.round(cents * 0.03));
}
```

The engineering director says: "We ship tomorrow. Replace this with a Strategy hierarchy now, add extension points for drone and locker delivery, and clean the rest of the pricing package while you are there. Patterns will make the review easier."

Assess whether the conditional is a real smell or a style preference, choose the smallest justified treatment, state what evidence would justify polymorphism later, preserve current behavior, and define where this change must stop despite schedule and authority pressure.
