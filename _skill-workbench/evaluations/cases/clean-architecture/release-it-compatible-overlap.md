# Design a Payment Use Case and Its Production Failure Contract

Design a new `CapturePayment` application action. The business policy is:

- An authorized order may be captured exactly once.
- A successful provider capture records the provider payment ID on the order.
- A declined payment is a business outcome and does not retry.
- The use case must not depend on the provider SDK, HTTP framework, or database types.

The production integration also has explicit operational requirements:

- The provider call must have a finite total timeout.
- Only timeout and provider-unavailable outcomes may retry.
- Retries must be bounded, backed off, and safe against duplicate capture.
- Provider saturation must not consume every request worker.
- Logs and metrics must identify latency, attempts, final outcome, and provider saturation without exposing secrets.

Propose the use-case input/output, policy-owned ports, provider and persistence adapters, and composition-root wiring. Also define the timeout, idempotency, retry, isolation, degradation, and diagnostic behavior at the provider boundary. Keep policy/detail ownership separate from production-failure mechanics; both concerns must remain explicit.
