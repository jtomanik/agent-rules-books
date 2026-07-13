# Evolve an Approved Claims Model

The Claims context and the decision to use model-driven design are already approved. Keep this as a bounded local-model change; do not choose infrastructure, integration contracts, or persistence mechanics.

The current implementation reduces every decision to flags:

```ts
function mayAdjudicate(claim: Claim): boolean {
  return claim.policyActive
    && claim.memberEligible
    && !claim.duplicate
    && (!claim.priorAuthorizationRequired || claim.priorAuthorizationPresent)
    && claim.submittedAt <= claim.filingDeadline;
}
```

Claims specialists use these distinctions:

- Coverage determines whether a service belongs to the policy benefit.
- Entitlement determines whether this member may use that benefit on the service date.
- Filing timeliness determines whether the claim may enter adjudication.
- Prior authorization can be satisfied, waived, or absent for a documented reason.
- Duplicate detection blocks adjudication but does not change coverage or entitlement.

Recommend a bounded evolution from the flag bundle to an implementation-driving model that makes these concepts and decisions explicit. Include domain-language examples or tests that would confirm the model with claims specialists, and identify the smallest safe sequence for moving current behavior into it.
