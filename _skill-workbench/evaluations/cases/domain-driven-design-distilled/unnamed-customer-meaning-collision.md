# Separate Conflicting Customer Meanings

An enterprise data initiative requires Billing, Identity, and Fulfillment to use one canonical `Customer` model.

```yaml
billing:
  customer: legal party responsible for payment
  active: may receive a new invoice
  identity: billing_account_id
identity:
  customer: authenticated person or organization
  active: login is enabled
  identity: subject_id
fulfillment:
  customer: delivery recipient for an order
  active: delivery instructions are currently usable
  identity: recipient_id

canonical_model:
  id: uuid
  active: boolean
  status: string
  billing_account_id: optional
  subject_id: optional
  recipient_id: optional
```

Review the proposed shared model. Identify the smallest set of language and boundary decisions needed to prevent one team's meaning from leaking into the others, and state how information should cross those boundaries.
