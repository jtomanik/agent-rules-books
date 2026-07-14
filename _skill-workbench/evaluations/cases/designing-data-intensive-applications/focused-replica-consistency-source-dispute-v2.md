# Resolve a Replica Consistency Source Dispute

A profile update commits on the primary and redirects the same user to a page read from the nearest asynchronous follower. Followers usually lag by 2.4 seconds, have reached 18 seconds, expose their applied commit position, and may be promoted during a regional failover. The product contract requires that the updating user see the committed profile immediately; other users may see stale data for up to 30 seconds.

Two reviewers disagree about the exact source guidance:

- One says the read-your-writes requirement categorically forbids any follower read after the update.
- The other says a follower is permissible only when the design explicitly provides the required read-your-writes guarantee and defines behavior for lag, catch-up, failover, and reconfiguration.

Resolve only this source-interpretation dispute. State the exact consistency and replication conditions that govern the decision, what the design must prove, and which product-contract change would permit a weaker guarantee. Do not perform a general data-platform or reliability audit.
