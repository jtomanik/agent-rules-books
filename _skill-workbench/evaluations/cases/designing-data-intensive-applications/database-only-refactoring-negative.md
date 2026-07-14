# Refactor a Fully Specified Repository Adapter

The tests are green and fully specify this adapter. Make the smallest behavior-preserving rename and extraction that removes repeated row mapping. Keep the SQL, transaction, consistency, durability, and public result semantics unchanged. This is a local structural cleanup, not a data-system or architecture redesign.

```ts
type User = {
  id: string;
  email: string;
};

export class PgUsers {
  constructor(private readonly db: DatabaseClient) {}

  async one(id: string): Promise<User | null> {
    const result = await this.db.query(
      "select id, email from users where id = $1",
      [id],
    );
    if (result.rows.length === 0) {
      return null;
    }
    return {
      id: String(result.rows[0].id),
      email: String(result.rows[0].email),
    };
  }

  async all(): Promise<User[]> {
    const result = await this.db.query(
      "select id, email from users order by id",
    );
    return result.rows.map((row) => ({
      id: String(row.id),
      email: String(row.email),
    }));
  }
}
```

Exact behavior:

- `one()` returns `null` for no row and maps the first row otherwise.
- `all()` preserves database order.
- Both methods preserve the current SQL and convert `id` and `email` with `String()`.
- `DatabaseClient` already has a stable adapter boundary; no framework or persistence type enters domain policy.
- No retry, queue, cache, replication, schema change, event, derived data, or production-failure behavior is involved.

Return the revised adapter and concise tests. Do not edit repository files.
