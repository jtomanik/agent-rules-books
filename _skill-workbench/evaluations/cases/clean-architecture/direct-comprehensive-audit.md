# Complete Clean Architecture Audit of Subscription Renewal

Apply the complete Clean Architecture lens to this proposed module. Read the exhaustive Clean Architecture reference end to end before answering. This is an architecture review, not an implementation request.

```text
src/
  domain/
    subscription.ts
  application/
    renew-subscription.ts
  web/
    renewal-route.ts
  persistence/
    prisma-subscription.ts
  shared/
    service.ts
```

```ts
// domain/subscription.ts
import type { SubscriptionRow } from "../persistence/prisma-subscription";

export function renewalPrice(row: SubscriptionRow, today: Date): number {
  const years = today.getUTCFullYear() - row.startedAt.getUTCFullYear();
  return years >= 3 ? row.planPriceCents * 0.9 : row.planPriceCents;
}
```

```ts
// application/renew-subscription.ts
import type { Request, Response } from "express";
import { prisma } from "../persistence/prisma-subscription";
import { stripe } from "../shared/service";
import { renewalPrice } from "../domain/subscription";

export async function renewSubscription(req: Request, res: Response): Promise<void> {
  const subscription = await prisma.subscription.findUniqueOrThrow({
    where: { id: req.params.id },
  });
  const priceCents = renewalPrice(subscription, new Date());
  const charge = await stripe.charges.create({
    amount: priceCents,
    customer: subscription.customerId,
  });
  await prisma.subscription.update({
    where: { id: subscription.id },
    data: { lastChargeId: charge.id },
  });
  res.status(204).end();
}
```

```ts
// web/renewal-route.ts
router.post("/subscriptions/:id/renew", renewSubscription);

// persistence/prisma-subscription.ts
export { prisma } from "../bootstrap/prisma";
export type SubscriptionRow = Awaited<
  ReturnType<typeof prisma.subscription.findUniqueOrThrow>
>;

// shared/service.ts
export { stripe } from "../bootstrap/stripe";
```

Current tests invoke the Express route with a real test database and a fake Stripe server. There are no direct domain or use-case tests. The team expects to add a CLI renewal path and may replace Prisma next year.

Identify the material dependency-direction, policy/detail, responsibility, structure, boundary-enforcement, and testing issues. Propose a target component shape and identify the boundary changes that are prerequisites. Do not provide a behavior-preserving refactoring sequence, and do not add production resilience mechanisms or local style cleanup unless they are necessary to explain the architecture.
