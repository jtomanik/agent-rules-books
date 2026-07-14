# Relational inheritance mapping decision

Choose a relational mapping for this hierarchy and explain the tradeoff against the other two standard inheritance mappings represented by the candidate schemas. Consult the smallest applicable packaged reference section before answering and identify the section consulted.

```text
Domain types:
  PaymentMethod(id, label)
  CardPayment(id, label, network, last4)
  BankPayment(id, label, ibanCountry, mandateId)

Workload:
  - 85% load a payment method by id without knowing its subtype
  - 10% list all methods for one customer
  - 5% subtype-specific administration
  - new subtypes are rare
  - database constraints and understandable migrations matter more than write throughput

Candidate A: one PAYMENT_METHOD table with discriminator and nullable subtype columns
Candidate B: PAYMENT_METHOD plus CARD_PAYMENT and BANK_PAYMENT joined by id
Candidate C: separate concrete tables repeating id, customer_id, and label
```
