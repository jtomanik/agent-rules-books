# Apply Clean Architecture to One Ordinary Boundary

Use `$clean-architecture` as the project book lens for this task.

The proposed `ApproveOrder` application action imports a Prisma row type, constructs `PrismaClient`, and publishes Kafka messages directly. PostgreSQL remains authoritative, and the business rule is simply that only pending orders may become approved. The HTTP and persistence contracts are fixed.

Recommend the smallest ordinary design with a focused use case, plain input/output data, application-owned ports, outer Prisma/Kafka adapters, and composition-root wiring. Do not perform a comprehensive audit or broaden into runtime resilience.
