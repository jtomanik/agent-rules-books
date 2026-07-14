# Implement an Approved Pricing Model

The Pricing context and language are approved. Turn the model into an implementation design without revisiting whether Pricing should be a separate context.

```text
PriceBook: the named set of Prices offered for a market during a validity period
Price: a Money amount for one ProductRef under one eligibility condition
ProductRef: an identity owned by Catalog and translated at the Pricing boundary

Rules:
- A PriceBook name is unique within a market.
- A PriceBook cannot publish with overlapping Prices for the same ProductRef and condition.
- Published PriceBooks are immutable; a replacement has a new identity.
- Publishing produces PriceBookPublished.
- The quoting screen reads a denormalized list and may lag by 30 seconds.
```

Current implementation sketch:

```ts
class PriceBook {
  id!: string;
  name!: string;
  market!: string;
  status!: string;
  prices!: Price[];
}

interface Repository<T> {
  save(value: T): Promise<void>;
  find(table: string, filters: object): Promise<T[]>;
}
```

Specify roots and identities, invariant placement, construction/reconstitution, a domain-shaped Repository, publication coordination, event handling, package boundaries, translation of `ProductRef`, and the quoting projection.
