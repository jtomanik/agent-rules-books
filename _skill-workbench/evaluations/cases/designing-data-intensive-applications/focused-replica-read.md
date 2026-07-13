# Resolve a Replica Read-After-Write Dispute

The team explicitly disputes whether this post-update redirect may read from an asynchronous replica. Give a focused decision about the required consistency contract and the smallest implementation strategy that satisfies it. Do not broaden the answer into a general service audit.

```ts
export async function updateProfile(
  userId: string,
  patch: ProfilePatch,
): Promise<Response> {
  const committed = await primary.profiles.update(userId, patch);
  return redirect(`/profiles/${committed.id}`);
}

export async function showProfile(userId: string): Promise<Profile> {
  return nearestReplica.profiles.get(userId);
}
```

```yaml
replication:
  mode: leader_follower
  follower_updates: asynchronous
  p99_lag_ms: 2400
  observed_max_lag_ms: 18000
  failover: promote_available_follower

routing:
  reads: nearest_replica
  writes: primary
  session_affinity: false
  commit_position_exposed: true
  replica_applied_position_exposed: true
```

Product contract:

- After a successful profile update, the same user must see the committed profile on the redirected page.
- Other users may see the old profile for up to thirty seconds.
- A region failover may occur between the write response and the redirected read.
- The task does not change capacity, deployment, health checks, retry budgets, or dependency-isolation policy.
