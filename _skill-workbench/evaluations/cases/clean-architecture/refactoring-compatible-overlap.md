# Move Protected Policy Inward Without Changing Behavior

The behavior below is complete, intentional, and protected by focused green controller tests. The task is a behavior-preserving structural change: move the approval policy out of the HTTP controller and into a focused application action without changing status codes, repository calls, or audit order.

```ts
export async function approveExpense(req: Request, res: Response): Promise<void> {
  const expense = await expenseRepository.find(req.params.id);

  if (expense.status !== "SUBMITTED") {
    res.status(409).json({ code: "invalid-status" });
    return;
  }

  if (expense.amountCents > req.user.approvalLimitCents) {
    res.status(422).json({ code: "limit-exceeded" });
    return;
  }

  await expenseRepository.markApproved(expense.id, req.user.id);
  await auditLog.record("expense-approved", expense.id, req.user.id);
  res.status(204).end();
}
```

Recommend a concrete, reviewable sequence that preserves observable behavior while restoring inward dependency direction and a humble controller. Show the target use-case input/output and policy-owned ports, keep HTTP translation at the edge, and state where the cleanup stops. The tests are trustworthy; no characterization or first-feedback work is needed.
