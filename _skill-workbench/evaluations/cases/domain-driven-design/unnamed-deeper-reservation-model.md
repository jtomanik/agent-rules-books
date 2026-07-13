# Evolve the Reservation Model

The team has already committed to model-driven design inside the Reservation context. Do not revisit whether that investment is worthwhile, and do not redesign persistence, APIs, or service boundaries.

The current model is one record plus branching behavior:

```ts
type ReservationStatus = "PENDING" | "CONFIRMED" | "RELEASED";

type Reservation = {
  status: ReservationStatus;
  capacityHeld: boolean;
  expiresAt?: Date;
  confirmedAt?: Date;
  releaseReason?: string;
};

function confirm(reservation: Reservation, now: Date): Reservation {
  if (reservation.status !== "PENDING") throw new Error("invalid status");
  if (!reservation.capacityHeld) throw new Error("capacity unavailable");
  if (reservation.expiresAt && reservation.expiresAt <= now) {
    return { ...reservation, status: "RELEASED", releaseReason: "expired" };
  }
  return { ...reservation, status: "CONFIRMED", confirmedAt: now };
}
```

Domain experts describe the work differently:

- A request may create a temporary capacity hold, but a hold is not yet a customer commitment.
- A hold expires; an accepted commitment does not.
- Confirmation consumes a still-valid hold and creates a commitment.
- Releasing a hold and cancelling a commitment return capacity for different business reasons.
- The next feature must extend a hold without changing an existing commitment.

Review the model behind this behavior. Identify the missing concepts and language distinctions, propose a deeper implementation-driving model, and name the expert scenarios that would test whether it explains the domain better. Give an incremental refactoring direction that preserves current behavior while comparing explanatory gain with migration cost.
