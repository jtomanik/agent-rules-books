# Decide Whether Opportunistic Shared Coordination Fits

Give a focused decision for this analysis pipeline. Consult detailed packaged
guidance if the compact guidance does not settle the coordination mechanism.

```yaml
inputs:
  - static_analyzer_findings
  - test_failures
  - dependency_advisories
  - operator_annotations
arrival_order: unknown
handlers:
  - correlate_findings_when_supporting_evidence_exists
  - request_more_evidence_when_confidence_is_low
  - publish_a_case_when_independent_signals_converge
coordination_proposal:
  shared_space: mutable_case_board
  fixed_pipeline_order: none
  handlers_may_run_opportunistically: true
```

The team is choosing between a fixed orchestrated pipeline and a shared
blackboard-style coordination space. State the source conditions that justify
the shared-space style and whether this case meets them. Keep the reference read
to the smallest coherent section set; do not perform a general architecture
audit.
