# Resolve a Claim Dashboard Repository Dispute

The team disputes whether this dashboard query belongs on `ClaimRepository`. Give a focused decision about Repository semantics, query responsibilities, and the appropriate read representation. Do not broaden the answer into a complete Claims implementation audit.

```java
interface ClaimRepository {
  Claim byId(ClaimId id);
  void save(Claim claim);
  List<ClaimDashboardRow> dashboard(
      AdjusterId adjuster,
      LocalDate from,
      LocalDate to,
      Set<String> statuses,
      int page,
      int pageSize);
}
```

```java
record ClaimDashboardRow(
    String claimNumber,
    String claimantName,
    String policyNumber,
    String statusLabel,
    BigDecimal reserve,
    Instant lastActivityAt,
    int openTaskCount) {}
```

Facts:

- `Claim` is the Aggregate root used for adjudication commands.
- The dashboard joins claims, policies, parties, tasks, and a reporting projection.
- Dashboard rows are never modified and may lag commands by 20 seconds.
- The ORM currently reconstitutes full `Claim` graphs before mapping each row.
- A separate query adapter already owns SQL for two other screens.

State what `ClaimRepository` should expose, where this query belongs, and how its representation should relate to the domain model.
