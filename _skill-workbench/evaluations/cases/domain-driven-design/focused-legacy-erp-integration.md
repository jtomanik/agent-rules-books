# Decide a Legacy ERP Context Relationship

The team disputes how the Ordering model should integrate with a vendor-controlled ERP. Give a focused decision about the context relationship and translation boundary. Do not broaden the answer into a complete domain audit.

Ordering uses:

```text
Order: confirmed customer intent to buy
OrderLine: requested product and quantity
FulfillmentPriority: standard | expedited | contractual
```

The ERP exposes:

```json
{
  "DOC_TYPE": "SO",
  "PARTY_CLASS": "A17",
  "LINES": [{ "MATNR": "008821", "MENGE": "3.000", "PRIO": "02" }],
  "STATUS": "REL"
}
```

Constraints:

- The vendor controls the ERP schema and quarterly protocol changes.
- Ordering cannot influence the ERP roadmap.
- Reusing ERP field names inside Ordering has already made policy discussions harder.
- Two other internal systems also consume the ERP protocol.
- The integration team proposes publishing a documented internal protocol derived from the ERP payload.

State which relationship patterns fit these facts, where translation should live, and what must be tested before the integration code is treated as stable.
