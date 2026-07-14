# Resolve a Replica Read Contract Through Failover

Use `$designing-data-intensive-applications` as the project book lens for this task.

After updating a profile on the primary, the same user is redirected to an asynchronous replica. Replicas can lag, a failover can promote a node that has not applied the session's commit position, and network delay can make catch-up status uncertain. Reviewers disagree whether a five-second lag target is enough.

Resolve the read-your-writes contract through catch-up and failover using only the bounded consistency, replication, and distributed-fault guidance. Do not perform a complete audit.
