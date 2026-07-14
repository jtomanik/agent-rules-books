# Resolve a Focused Replica Consistency Dispute

Use `$designing-data-intensive-applications` as the project book lens for this task.

After updating a profile on the primary, the same user is redirected to a randomly selected asynchronous replica. Reviewers disagree whether a five-second lag target is enough or whether the product needs an explicit read-your-writes contract across catch-up and failover.

Resolve the dispute using only the smallest detailed consistency and replication sections. State the session/position contract and fallback behavior; do not perform a complete audit.
