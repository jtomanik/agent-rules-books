# Apply DDIA to One Derived Projection

Use `$designing-data-intensive-applications` as the project book lens for this task.

PostgreSQL is authoritative for products. A search projection is updated asynchronously from a durable change log; search may lag by up to 30 seconds, and the projection must be rebuildable after loss. The schema and production-capacity policy are fixed.

Define the ordinary ownership, propagation, checkpoint, lag-observability, rebuild, and repair contract. Keep the decision bounded to this projection and do not perform a complete data-system audit.
