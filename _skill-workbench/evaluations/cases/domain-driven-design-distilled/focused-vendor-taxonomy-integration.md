# Resolve a Vendor Taxonomy Boundary

The Product team disputes whether to adopt a marketplace vendor's taxonomy as its own domain language. Give a focused context-relationship and integration-style decision. Do not perform a complete product-model audit.

Local Product language:

```text
Assortment: products offered for a market and season
MerchandisingGroup: a planning grouping chosen by merchandisers
Availability: whether a sellable item may be promised to a channel
```

Vendor API language:

```text
CatalogTree / CategoryNode / ListingState / MerchantOffer
```

Facts:

- The vendor controls taxonomy IDs and may split or merge categories without notice.
- Merchandisers reject the vendor taxonomy for internal planning.
- The vendor is the only marketplace channel and cannot accept local terminology.
- Product publishes availability changes to three internal consumers.
- One consumer needs a synchronous availability answer; two can consume messages.
- The current proposal imports vendor DTOs into the Product model and publishes them as internal events.

State the relationship to the vendor, where translation belongs, and when RPC, messaging, an event payload, or query-back is appropriate for the internal consumers.
