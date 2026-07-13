# Add a Rule to Uncontrolled Existing Code

The production behavior of this Java class is not fully understood. It has no automated tests, its constructor opens the real database, and several callers are outside the team's repository. The requested change is to add a seven-day grace period before overdue accounts are suspended.

```java
public final class BillingService {
    private final Connection connection;

    public BillingService() throws SQLException {
        this.connection = DriverManager.getConnection(System.getenv("BILLING_DSN"));
    }

    public boolean process(String accountId) throws SQLException {
        ResultSet row = connection
            .createStatement()
            .executeQuery("select due_at, suspended from accounts where id = '" + accountId + "'");

        if (!row.next()) {
            return false;
        }

        boolean overdue = row.getTimestamp("due_at").toInstant().isBefore(Instant.now());

        if (overdue && !row.getBoolean("suspended")) {
            connection
                .createStatement()
                .executeUpdate("update accounts set suspended = true where id = '" + accountId + "'");
            return true;
        }

        return false;
    }
}
```

Recommend the safest order of work before and during this behavior change. State what must be learned or controlled first, the smallest dependency intervention you would make, and how you would separate structural work from the new rule. Do not propose broad naming, formatting, or architecture cleanup, and do not edit files.
