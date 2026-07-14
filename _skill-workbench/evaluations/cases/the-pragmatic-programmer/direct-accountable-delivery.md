# Apply The Pragmatic Programmer Lens

Use The Pragmatic Programmer lens to review this delivery proposal. Focus on
outcome ownership, knowledge ownership, reversibility, orthogonality, and fast
feedback rather than applying a generic code-style checklist.

```yaml
feature: regional-tax-export
deadline: 12_days
proposal:
  validation:
    ui: copied_tax_rules
    api: copied_tax_rules
    batch: copied_tax_rules
  vendor:
    format: hard_coded_into_domain_objects
    contract_change_notice: 14_days
  verification:
    local: manual_spreadsheet_check
    ci: none
  rollout:
    steps: tribal_knowledge
    owner: unclear
```

Recommend the smallest delivery correction that can meet the deadline without
making copied knowledge, vendor commitment, or manual verification permanent.
