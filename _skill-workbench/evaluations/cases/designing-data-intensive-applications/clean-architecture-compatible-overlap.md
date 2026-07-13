# Separate Policy While Preserving Event Correctness

Redesign this use case so business policy is independent of Prisma and Kafka while also making the order write and emitted event correct under retry, crash, replay, and mixed event versions. Both concerns are required; do not turn the answer into a general production-readiness review.

```ts
import { PrismaClient } from "@prisma/client";
import { Kafka } from "kafkajs";

const prisma = new PrismaClient();
const producer = new Kafka({ brokers: [process.env.BROKER!] }).producer();

export async function approveOrder(orderId: string): Promise<void> {
  const order = await prisma.order.findUniqueOrThrow({
    where: { id: orderId },
  });

  if (order.status !== "pending") {
    throw new Error("order is not pending");
  }

  await prisma.order.update({
    where: { id: orderId },
    data: { status: "approved" },
  });

  await producer.send({
    topic: "orders",
    messages: [{
      key: order.customerId,
      value: JSON.stringify({
        type: "OrderApproved",
        orderId,
        status: "approved",
      }),
    }],
  });
}
```

Contracts:

- PostgreSQL is authoritative for order state.
- Approval is idempotent by `orderId`; concurrent approvals must preserve the pending-to-approved invariant.
- The broker is at-least-once and may be unavailable after the database commit.
- Consumers rebuild projections by replaying `orders`.
- Event version 1 consumers remain deployed while version 2 producers roll out.
- The domain and use-case code must not import Prisma, Kafka, transport payloads, or environment configuration.
- Capacity, deployment mechanics, overload, health checks, and incident response are outside scope.

Provide the policy boundary, owned ports, transaction/outbox or equivalent write contract, event identity/version contract, and focused tests.
