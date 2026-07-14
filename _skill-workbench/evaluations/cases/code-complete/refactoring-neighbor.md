# Perform a Behavior-Preserving Structural Change

All observable behavior is specified by green tests, including exception text and call order. Make no semantic change. The sole objective is to remove the duplicated conditional calculation through small, reversible, behavior-preserving transformations.

```java
final class PriceCalculator {
    Money price(Order order, boolean preferred) {
        if (preferred) {
            Money base = order.subtotal().minus(order.subtotal().times(0.10));
            return base.plus(order.expedited() ? Money.cents(700) : Money.cents(500));
        }

        Money base = order.subtotal();
        return base.plus(order.expedited() ? Money.cents(700) : Money.cents(500));
    }
}
```

Give the exact sequence of named refactorings, the safety checks after each step, and the stop condition. Do not redesign the pricing policy, add new behavior, conduct a general construction audit, or edit files.
