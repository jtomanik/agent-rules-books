# Complete Pre-Launch Production Audit

Apply the complete Release It! lens to the following launch artifact. Produce a prioritized audit with launch blockers, accepted risks, required verification, and the production signals or controls needed for each material failure mode.

```yaml
service: checkout-api
replicas: 12

traffic:
  ingress_timeout_ms: 3000
  max_requests_per_replica: 0
  admin_routes_share_public_listener: true
  rate_limits:
    checkout: null
    admin: null

dependencies:
  payment:
    connect_timeout_ms: 0
    response_timeout_ms: 0
    sdk_retries: 2
    application_retries: 3
    pool: shared-outbound
    fallback: enqueue-payment
  inventory:
    response_timeout_ms: 1000
    retries: 1
    pool: shared-outbound
  database:
    pool_size: 40
  cache:
    authoritative_for_price: true
    on_outage: reject_checkout
    ttl_seconds: 300
    miss_coalescing: false

queues:
  payment:
    capacity: 0
    max_deliveries: 0
    dead_letter: null
  analytics:
    capacity: 0
    workers_share_pool_with_payment: true

startup:
  run_schema_migration: true
  migration_checkpointing: false
  validate_required_configuration: false

health:
  liveness: process_is_running
  readiness: process_is_running

scheduled_work:
  reconcile_payments: "0 * * * *"
  rebuild_price_cache: "0 * * * *"
  retry_failed_analytics: "0 * * * *"

delivery:
  strategy: all-at-once
  rollback: redeploy_previous_image
  configuration_version_visible: false
  migration_version_visible: false

observability:
  structured_logs: true
  correlation_id: request-only
  metrics:
    - request_count
    - error_count
  queue_age: false
  saturation: false
  retry_count: false
  breaker_state: false

controls:
  pause_payment_consumer: true
  authorization: shared-operator-token
  audit_log: false
  emergency_stop_tested: false

resilience_validation:
  dependency_failure_tests: false
  overload_tests: false
  restartable_migration_test: false
  chaos_experiment:
    planned: true
    hypothesis: null
    blast_radius_limit: null
    stop_condition: null
    recovery_proof: null
```

Additional constraints:

- A payment authorization may charge money and is not guaranteed idempotent.
- The provider SDK interprets timeout `0` as no deadline.
- Queue capacity `0` means unbounded.
- Old and new application versions may overlap for fifteen minutes during deployment.
- Checkout must remain available when analytics is unhealthy.
- The launch owner will accept a deferred improvement only when the immediate failure behavior and operational workaround are explicit.
