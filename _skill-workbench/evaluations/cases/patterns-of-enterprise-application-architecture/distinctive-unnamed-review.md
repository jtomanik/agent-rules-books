# Responsibility and pattern review

Review the design below and propose a bounded correction. Decide which business-logic and data-access structures fit the actual forces, where the transaction belongs, and what the remote contract should look like.

```java
final class CheckoutController {
  CheckoutResponse checkout(HttpRequest request) {
    var rows = jdbc.query("select * from cart_line where cart_id = ?", request.cartId());
    var total = rows.stream().mapToLong(r -> r.price() * r.quantity()).sum();
    if (request.coupon() != null) total -= jdbc.lookupDiscount(request.coupon(), total);

    jdbc.execute("update cart set total = ? where id = ?", total, request.cartId());
    jdbc.execute("insert into purchase(cart_id, total) values (?, ?)", request.cartId(), total);
    shippingVendor.createShipment(request.body());

    return new CheckoutResponse(request.body(), rows, total);
  }
}
```

The shipping vendor needs six calls to create one shipment. Tests currently require a database and the vendor sandbox. Coupon rules are expected to gain lifecycle and eligibility constraints, but there is no committed rich domain model.
