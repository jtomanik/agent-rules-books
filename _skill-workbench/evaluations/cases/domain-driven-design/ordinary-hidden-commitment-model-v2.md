# Clarify Two Kinds of Allocation Commitment

Inside the established Fulfillment context, `Allocation` currently uses one `allocated` state for two different business situations:

- Planning proposes a warehouse that appears able to supply an order line. The proposal can be replaced freely.
- Warehouse Operations accepts responsibility and reserves stock. Releasing that commitment requires an explicit decision.

The same flag now drives customer promises, warehouse work, and cancellation rules. Domain experts use the phrases `proposed source` and `committed reservation`, but those concepts do not exist in code.

Choose the smallest model change that makes the distinction explicit. Explain the language and scenarios that should drive it, show how implementation and tests should reflect the model, and keep migration incremental and behavior-preserving. Do not redesign infrastructure or perform a complete multi-context audit.
