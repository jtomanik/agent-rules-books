# Place a Refund Rule Under Schedule Pressure

The current refund behavior is fully specified and covered by fast tests. A new rule must ship today:

- VIP customers may receive a full refund up to 30 days after purchase.
- Other customers retain the existing 14-day rule.
- The HTTP response contract and repository schema do not change.

The existing controller delegates to a `RefundPurchase` use case:

```ts
export async function postRefund(req: Request, res: Response): Promise<void> {
  const result = await refundPurchase.execute({
    purchaseId: req.params.purchaseId,
    requestedAt: new Date(),
  });
  res.status(result.accepted ? 204 : 422).end();
}
```

The delivery manager proposes this shortcut because changing and redeploying the application package requires another approval:

```ts
export async function postRefund(req: Request, res: Response): Promise<void> {
  const purchase = await purchaseRepository.find(req.params.purchaseId);
  if (purchase.customerTier === "VIP" && daysSince(purchase.createdAt) <= 30) {
    await purchaseRepository.refund(purchase.id);
    res.status(204).end();
    return;
  }

  const result = await refundPurchase.execute({
    purchaseId: req.params.purchaseId,
    requestedAt: new Date(),
  });
  res.status(result.accepted ? 204 : 422).end();
}
```

Decide whether to accept the shortcut and propose the smallest shippable placement for the VIP rule. The task is about policy placement and dependency direction, not production resilience or unknown behavior.
