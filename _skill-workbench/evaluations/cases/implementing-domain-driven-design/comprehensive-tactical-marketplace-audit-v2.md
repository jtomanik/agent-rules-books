# Comprehensive Tactical Marketplace Audit

Perform a comprehensive end-to-end implementation audit for a marketplace whose contexts are already approved: Seller, Catalog, Offer, Ordering, Payment, and Fulfillment.

The implementation has large cross-context Aggregates, mutable value-like objects, Repositories for arbitrary reporting queries, vague events emitted before commit, business decisions in Application Services, technical package names, vendor DTOs inside domain objects, and client screens traversing object graphs across contexts.

Cover strategic implementation boundaries, local language, Aggregate rules, entities and Value Objects, domain and transformation services, Repositories, events and sourcing, Application Services, modules and packages, context integration, client representations, practical simplicity, testing, forbidden patterns, and final review. Keep the already chosen context boundaries fixed unless an implementation contradiction proves one invalid.
