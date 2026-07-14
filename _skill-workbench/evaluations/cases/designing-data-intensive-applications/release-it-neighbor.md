# Stabilize a Stateless Thumbnail Gateway

Review this stateless production gateway for failure containment and overload behavior. Recommend bounded timeouts, retry ownership, isolation, degradation, and observability changes. Do not redesign data ownership or persistence; the gateway does not store, replicate, derive, replay, or evolve business data.

```ts
export async function thumbnail(url: string): Promise<Buffer> {
  const image = await imageProvider.fetch(url);
  return renderer.resize(image, 320, 180);
}
```

```yaml
replicas: 20
request_timeout_ms: 0

image_provider:
  SDK_retries: 3
  application_retries: 2
  response_timeout_ms: 0
  connection_pool: shared

renderer:
  worker_pool_size: 200
  queue_capacity: 0

traffic:
  normal_rps: 400
  observed_spike_rps: 9000

degradation:
  placeholder_response: supported
  load_shedding: false

health:
  liveness: process_running
  readiness: process_running

observability:
  dependency_latency: false
  worker_saturation: false
  queue_depth: false
  retry_count: false
```

Incident evidence:

- A provider slowdown filled every renderer worker and the unbounded queue until instances were killed for memory pressure.
- Client and server retries multiplied one request into as many as eighteen provider calls.
- Returning a placeholder thumbnail is an accepted degraded mode.
- No durable write, message replay, schema migration, replica read, ordering invariant, or derived-data repair decision exists in this task.
