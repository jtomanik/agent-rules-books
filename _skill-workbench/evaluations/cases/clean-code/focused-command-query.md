# Resolve a Command-Query Ambiguity

Two reviewers disagree about this TypeScript method. One says any method that returns a value while changing state violates command-query separation. The other says an internal lazy cache is a harmless exception.

```ts
type User = {
  id: string;
  displayName: string;
};

class UserDirectory {
  private readonly usersById = new Map<string, User | undefined>();

  constructor(private readonly repository: UserRepository) {}

  findUser(id: string): User | undefined {
    if (!this.usersById.has(id)) {
      this.usersById.set(id, this.repository.findById(id));
    }

    return this.usersById.get(id);
  }
}
```

Resolve this specifically under the Clean Code command-query and hidden-side-effect guidance. Give a ruling for this method, explain whether a strong-reason exception exists, and show the smallest acceptable alternatives. Keep the analysis limited to this ambiguity; do not perform a general audit or edit files.
