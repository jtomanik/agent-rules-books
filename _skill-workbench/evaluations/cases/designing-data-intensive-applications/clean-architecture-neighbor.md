# Move Pricing Policy Out of Framework Code

Restructure this code so the pricing rule can survive replacement of Express and Prisma. Preserve the supplied transaction and consistency behavior exactly. Focus on policy placement, dependency direction, ports, adapters, and tests; no distributed data semantics are open for redesign.

```ts
import type { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function quoteOrder(req: Request, res: Response): Promise<void> {
  const customer = await prisma.customer.findUniqueOrThrow({
    where: { id: req.params.customerId },
  });
  const lines = req.body.lines as Array<{ price: number; quantity: number }>;

  const subtotal = lines.reduce(
    (sum, line) => sum + line.price * line.quantity,
    0,
  );
  const discount = customer.tier === "gold" && subtotal >= 10000
    ? Math.round(subtotal * 0.1)
    : 0;

  await prisma.quote.create({
    data: {
      customerId: customer.id,
      subtotal,
      discount,
    },
  });

  res.status(201).json({ subtotal, discount });
}
```

Fixed facts:

- `quote.create()` is one local durable transaction and remains the authoritative write.
- There are no replicas, caches, queues, events, retries, projections, or cross-service writes.
- The pricing formula and HTTP response are fully covered by green integration tests.
- The requested change is architectural separation, not a consistency, durability, replay, schema, or production-failure decision.
