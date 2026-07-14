# Complete Engineering Delivery Audit

Select the engineering guidance whose distinctive concerns are accountable
outcomes, authoritative knowledge, orthogonality, reversible choices, tracer
feedback, automation, explicit contracts, and broken-window containment. Read
its complete packaged reference end to end and audit this proposal against
every applicable section.

```yaml
product: municipal-permit-platform
requirements:
  source: copied_legacy_screens
  specification: 180_pages_and_growing
  unresolved_questions: [fee_ownership, appeal_timing, jurisdiction_changes]
architecture:
  first_running_slice: planned_after_all_layers
  shared_module: knows_ui_database_vendor_and_domain_details
  vendor_workflow_ids: stored_in_core_domain
  mutable_global_context: [tenant, user, clock, transaction]
delivery:
  prototype: promoted_without_hardening
  build: developer_laptop_only
  release: 14_manual_steps
  feedback: integration_test_at_end_of_quarter
errors:
  representation: null_or_generic_exception
  diagnostic_context: discarded
resources:
  ownership: shared_between_callers
  cleanup: success_path_only
team:
  risk_reporting: discouraged
  small_decay: accepted_until_rewrite
```

Separate source-backed findings from any general implementation suggestions.
Recommend an incremental correction order without treating every listed issue
as justification for irreversible redesign.
