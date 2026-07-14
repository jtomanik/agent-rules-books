# Resolve One Shared Customer Model

Three teams have been told to replace their separate customer representations with one enterprise `Customer` class.

| Team | `active` means | Identity | Required data |
| --- | --- | --- | --- |
| Sales | an account with an open opportunity in the last 90 days | CRM account ID | owner, pipeline stage, territory |
| Billing | a legal entity allowed to receive invoices | tax registration and billing account ID | payment terms, credit hold, invoice address |
| Support | a party entitled to receive support | entitlement ID | plan, covered products, service window |

The proposed shared class is:

```ts
class Customer {
  id: string;
  active: boolean;
  status: string;
  ownerId?: string;
  taxNumber?: string;
  supportPlan?: string;
}
```

Review the proposal. Explain what must be clarified about language and model boundaries before the teams share code, and recommend how information should cross any boundary you identify. Keep the answer specific to this model collision.
