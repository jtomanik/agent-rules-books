# Complete Domain-Driven Design Audit

Apply the complete Eric Evans Domain-Driven Design lens to this proposed insurance claims platform. Review the artifact end to end. Identify modeling risks, missing strategic decisions, unsuitable tactical choices, and the feedback needed before implementation.

```yaml
business:
  differentiator: rapid commercial-claim adjudication
  commodity_capabilities: [identity, email, document_storage]

teams:
  policy: owns policy wording and coverage
  claims: owns intake, assessment, and settlement
  fraud: owns fraud investigation
  finance: owns reserves and payment accounting

shared_model:
  package: insurance-common
  classes: [Customer, Policy, Claim, Payment, Address, Status]
  database: insurance
  status_enum: [NEW, ACTIVE, APPROVED, REJECTED, PAID, CLOSED]

claims_flow:
  controller:
    - loads Customer, Policy, Claim, FraudCase, and Payment
    - checks coverage and fraud flags
    - computes settlement and reserve
    - mutates all objects
    - commits one transaction
  claim_entity: getters_and_setters_only
  rules: switch_statements_in_application_service

integrations:
  policy_to_claims: shared_database_tables
  claims_to_fraud: synchronous_rpc_with_shared_dtos
  claims_to_finance: nightly_csv
  identity_vendor: vendor_schema_imported_into_common_package

language:
  customer: one enterprise definition
  claim_status: one enum across all teams
  glossary_owner: architecture_board
  domain_expert_sessions: none_planned

delivery:
  design_target: complete_model_before_first_release
  code_generation: generate_entities_then_validate_with_experts
  refactoring_budget: none_after_schema_freeze

tests:
  examples_from_domain_experts: false
  context_contracts: false
  aggregate_invariants: false
  repository_reconstitution: false
```

Constraints:

- Policy wording changes monthly.
- Claims settlement rules differ by jurisdiction and product.
- Finance requires an immutable accounting trail.
- Fraud may delay a claim without changing its coverage status.
- The first usable claims slice is due in six weeks.
