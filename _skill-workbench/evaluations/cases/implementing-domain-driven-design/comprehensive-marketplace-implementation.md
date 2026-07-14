# Complete Implementing DDD Audit

Apply the complete Implementing Domain-Driven Design lens to this marketplace proposal. Review the implementation end to end: model objects, Aggregates, services, events, Repositories, modules, context integration, application coordination, and read models.

```yaml
contexts:
  catalog:
    language: [Product, Assortment, Listing]
  ordering:
    language: [Order, OrderLine, OfferRef, BuyerRef]
  payments:
    language: [Payment, Authorization, MerchantAccount]

implementation:
  shared_package: marketplace-domain
  shared_types: [Product, Customer, Order, Payment, Status]
  entities:
    style: public_getters_and_setters
    constructors: empty
    validation: controllers
  aggregate:
    MarketplaceAccount:
      contains: [Customer, Products, Orders, Payments, Addresses]
      root: Customer
      transaction: one_commit
  services:
    MarketplaceService:
      responsibilities: [pricing, eligibility, payment, inventory, notifications]
  repositories:
    GenericRepository:
      returns: ORM_rows
      methods: [find, query, save, delete]
  events:
    names: [OrderRowInserted, PaymentStatusChanged]
    publication: controller_after_commit
    subscribers: mutate_shared_ORM_entities
  modules:
    packages: [controllers, services, entities, repositories]
  integration:
    contexts_share_database: true
    vendor_catalog_DTOs_in_domain: true
    enum_sharing: all_status_values
  queries:
    order_history: reconstitute_full_MarketplaceAccount
    seller_dashboard: reconstitute_full_MarketplaceAccount
```

Constraints:

- Context boundaries and language above are approved.
- An Order must enforce line and total invariants atomically.
- Payments and Catalog remain independent contexts.
- Buyer order history may lag by one minute.
- Seller dashboards combine data from all three contexts.
- Vendor catalog schemas change independently.
