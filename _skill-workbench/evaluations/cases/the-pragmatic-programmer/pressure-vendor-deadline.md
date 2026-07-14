# Respond to Deadline and Sunk-Cost Pressure

The sponsor requires a production pilot in seven days. Two weeks have already
been spent generating domain classes from Vendor A's schema, so the technical
lead says changing direction would waste sunk cost.

```yaml
current_plan:
  domain_model: vendor_a_generated_types
  business_rules: copied_into_api_worker_and_admin_ui
  release: manual_commands_on_one_laptop
  tests: postponed_until_after_pilot
  failure_context: discarded_to_keep_logs_quiet
new_fact:
  vendor_b_trial_required_next_month: true
  vendor_a_schema_changes_weekly: true
```

Give a decision that protects the seven-day pilot while keeping ownership,
adaptability, reversibility, and fast feedback visible. State what must change
now, what can be a thin real slice, and what shortcut cannot silently become the
production default.
