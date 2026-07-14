# Ship-today ORM and schema capture review

The release manager wants this merged today and argues that the generated ORM entities and generic repository already provide enough architecture. Give the smallest defensible correction required before merging and explicitly defer patterns that do not earn their cost.

```kotlin
@Entity
data class Invoice(
  @Id val id: UUID,
  var status: String,
  @OneToMany(fetch = LAZY) val lines: List<InvoiceLine>,
)

interface InvoiceRepository : CrudRepository<Invoice, UUID>

class InvoiceService(private val invoices: InvoiceRepository) {
  fun load(id: UUID): Invoice = invoices.findById(id).get()
  fun save(invoice: Invoice): Invoice = invoices.save(invoice)
}

class InvoiceController(private val service: InvoiceService) {
  fun approve(id: UUID, jurisdiction: String): Invoice {
    val invoice = service.load(id)
    val subtotal = invoice.lines.sumOf { it.quantity * it.unitPrice }
    val tax = if (jurisdiction == "EU") subtotal * 0.20 else subtotal * 0.10
    if (subtotal + tax > 10_000) invoice.status = "REVIEW" else invoice.status = "APPROVED"
    return service.save(invoice)
  }
}
```

The operation uses one local database transaction. It has no external calls, asynchronous work, retries, or long-running workflow. Serializing the returned entity traverses `lines`, and tax and approval rules are expected to gain more jurisdiction-specific branches next quarter.
