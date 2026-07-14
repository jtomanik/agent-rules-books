# Complete Clean Code Audit

Apply the complete Clean Code lens to this TypeScript fragment. Do not rely only on a summary: consult the full Clean Code reference end to end before answering. Produce a prioritized audit, a bounded remediation plan, and a validation checklist. Preserve current behavior unless a finding explicitly identifies a defect. This is read-only analysis; do not edit files.

```ts
export class Handler {
  private last: any;

  constructor() {
    this.db = new PrismaClient();
  }

  // This gets the order, checks it, updates it and sends everything.
  async go(req: any, res: any, quick: boolean, send: boolean) {
    const x = await this.db.order.findUnique({ where: { id: req.params.id } });

    if (x == null) {
      res.status(404).send(null);
      return null;
    }

    if (quick) {
      x.status = "approved";
    } else {
      if (x.total > 1000) {
        x.status = "review";
      } else {
        x.status = "approved";
      }
    }

    this.last = x;
    await this.db.order.update({ where: { id: x.id }, data: x });

    if (send) {
      setTimeout(async () => {
        await fetch(process.env.NOTIFY_URL + "/orders", {
          method: "POST",
          body: JSON.stringify(x),
        });
      }, 0);
    }

    // Return the order so the caller knows the update happened.
    return res.send(x);
  }
}

it("works", async () => {
  const result = await new Handler().go(request, response, true, true);
  expect(result).toBeTruthy();
});
```
