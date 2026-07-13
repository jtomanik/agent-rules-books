# Review a Proposed Invoice Use Case

This is a proposed greenfield design. No code has been implemented, so there is no existing behavior to preserve or unknown legacy behavior to characterize.

Required behavior:

- Load an approved order by ID.
- Reject an order that is not approved.
- Calculate the invoice total from the order's already-normalized line amounts.
- Save the invoice.
- Return the invoice ID and total.

Proposed TypeScript:

```ts
import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import type { Order, Invoice } from "@prisma/client";
import { prisma } from "@/infrastructure/prisma";

export async function createInvoice(request: NextRequest): Promise<NextResponse> {
  const order: Order = await prisma.order.findUniqueOrThrow({
    where: { id: request.nextUrl.searchParams.get("orderId")! },
    include: { lines: true },
  });

  if (order.status !== "APPROVED") {
    return NextResponse.json({ error: "not approved" }, { status: 409 });
  }

  const totalCents = order.lines.reduce((sum, line) => sum + line.amountCents, 0);
  const invoice: Invoice = await prisma.invoice.create({
    data: { orderId: order.id, totalCents },
  });

  return NextResponse.json({ id: invoice.id, totalCents }, { status: 201 });
}
```

Recommend the smallest production design that keeps the approval rule and application action independent from Next.js and Prisma. Show ownership of input/output models and required interfaces, where translation happens, and where concrete wiring belongs. Do not broaden into production failure handling or local naming cleanup.
