# Customer credit adjustment

Implement a design-level correction for this small application operation. Keep the response concrete: name the fitting structures, assign responsibilities, and outline tests. Do not broaden the change into a system rewrite.

```typescript
export async function adjustCustomerCredit(req: Request): Promise<Response> {
  const customer = await db.customer.findUnique({ where: { id: req.params.id } });
  const amount = Number(req.body.amount);
  const adjusted = customer.credit + amount;

  await db.customer.update({
    where: { id: customer.id },
    data: { credit: adjusted },
  });

  return json({ ...customer, credit: adjusted });
}
```

Current rules: the amount must be non-zero, the resulting credit cannot be negative, and one audit row must be committed with the customer update. The operation is local, has no remote calls, and is not expected to gain additional lifecycle behavior.
