# Ship-today ORM capture review

The release manager wants this merged today and argues that the ORM already provides architecture. Give the smallest defensible correction that must happen before shipping and explicitly defer changes that do not earn their cost.

```kotlin
@Entity data class Order(
  @Id val id: UUID,
  val status: String,
  @OneToMany(fetch = LAZY) val lines: List<OrderLine>,
)

class OrderController(
  private val repo: CrudRepository<Order, UUID>,
  private val carrier: CarrierClient,
) {
  fun ship(id: UUID): Order {
    val order = repo.findById(id).get()
    order.lines.forEach { carrier.reserve(order.id, it.id) }
    order.status = "SHIPPED"
    return repo.save(order)
  }
}
```

Observed behavior: serializing the returned entity triggers additional queries; each line causes a remote reservation call; a failed fifth reservation leaves four remote reservations but no saved status; callers retry the whole endpoint.
