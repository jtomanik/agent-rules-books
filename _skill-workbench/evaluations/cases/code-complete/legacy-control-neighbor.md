# Gain First Feedback Before a Behavior Change

Production behavior is materially unknown. There are no automated tests, construction opens the real database, current time is ambient, and callers outside the repository may depend on undocumented behavior. The requested semantic change is to add a three-day grace period before suspension.

```java
public final class SuspensionJob {
    private final Connection connection;

    public SuspensionJob() throws SQLException {
        connection = DriverManager.getConnection(System.getenv("ACCOUNT_DSN"));
    }

    public boolean run(String accountId) throws SQLException {
        ResultSet row = connection.createStatement().executeQuery(
            "select due_at, suspended from accounts where id = '" + accountId + "'"
        );

        if (!row.next()) return false;
        if (row.getTimestamp("due_at").toInstant().isBefore(Instant.now())
                && !row.getBoolean("suspended")) {
            connection.createStatement().executeUpdate(
                "update accounts set suspended = true where id = '" + accountId + "'"
            );
            return true;
        }
        return false;
    }
}
```

Recommend the order of work needed to gain trustworthy first feedback. State what behavior must be characterized and the smallest seam or dependency substitution required before changing the rule. Do not perform broad construction, naming, formatting, or architecture cleanup, and do not edit files.
