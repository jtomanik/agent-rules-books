# Clean Architecture Skill Mapping

## Scope

- Distinctive lens: preserve business-policy independence by making source dependencies point inward and keeping frameworks, persistence, delivery, vendors, services, devices, and other volatile mechanisms as replaceable outer details.
- Intended invocation: select `clean-architecture` only when policy/detail ownership or inward dependency direction is central, including core imports of details, business rules in adapters, direct construction of infrastructure by policy, layer bypass, or fake boundaries that do not preserve independent change.
- Positive boundary: layers, adapters, tests, services, devices, vendors, and databases are not sufficient by themselves. The task must require a policy-dependency, policy-placement, interface-ownership, or replaceability decision.
- Closest neighboring skills: `clean-code` for local readability and low-surprise code shape; `refactoring` for protected behavior-preserving structural change; `working-effectively-with-legacy-code` for gaining first feedback before semantic change; `release-it` for explicit production failure behavior and operational resilience.
- Compatible overlap: co-invoke a neighbor only when its concern and policy dependence are independently central. Clean Architecture supplies target dependency direction and ownership; it does not replace local readability criteria, safe-change sequencing, first-feedback control, or production failure semantics.
- Leading vocabulary: inward dependencies, policy versus detail, policy-owned ports, humble adapters, use cases, replaceable details, composition root, feature-first structure, and enforceable boundaries.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`. Manual-only metadata and description gating both failed live `3/3`; repo-local packages remained discoverable. The narrow positive threshold is therefore the enforceable boundary, and comprehensive source retrieval supplies the recorded package value despite strong unnamed baselines.
- Canonical inputs: `clean-architecture/clean-architecture.md`, `clean-architecture/clean-architecture.mini.md`, `clean-architecture/clean-architecture.nano.md`, and `_rule-workbench/clean-architecture/traceability.md`.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Capability | `inward dependencies and policy/detail separation` | Generic layers, modularity, testing, adapters, database work, and broad architecture vocabulary without a policy-ownership decision. |
| Positive threshold | `policy independence is central` | Incidental detail boundaries in otherwise local, structural, legacy-control, or operational work. |
| Core detail import | `policy imports details` | Clean Code's local adapter/readability pressure; this branch requires source direction from policy toward a volatile mechanism. |
| Misplaced policy | `adapters own business rules` | Ordinary mapping and translation at an edge; this branch requires business decisions or invariants to be owned outside policy. |
| Concrete infrastructure | `core code constructs infrastructure` | Mere dependency use or test setup; construction by policy reverses ownership and prevents edge composition. |
| False positives | `Layers, adapters, tests, and databases alone are insufficient` | Prevents architecture nouns from satisfying the central-policy threshold by themselves. |
| Explicit neighbors | `Clean Code covers readability; Refactoring, protected structural change; Legacy Code, blocked first feedback; Release It, production failure` | Assigns each neighbor its distinctive first-order concern without denying compatible overlap. |
| Co-invocation threshold | `Co-invoke only when policy dependence is also central` | Prevents a neighbor's concern from dragging in Clean Architecture merely because details, tests, or a database are present. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Apply the complete Clean Architecture lens to this subscription module." | `clean-architecture` | Direct book invocation; comprehensive routing reads `full.md` end to end. |
| "The use case imports Next.js request/response types and Prisma rows; keep policy independent." | `clean-architecture` | Policy imports volatile delivery and persistence details, satisfying the positive threshold. |
| "The controller contains VIP refund eligibility because the deadline is today." | `clean-architecture` | Business policy is misplaced at the edge under schedule pressure. |
| "This PostgreSQL adapter mapper has vague names, a boolean mode, and a narrating comment; keep it in the adapter." | `clean-code`, optionally `refactoring`; not `clean-architecture` | The database and adapter are incidental. Local readability is central and policy ownership is already settled. |
| "Execute these two named behavior-preserving moves; tests are green and architecture is settled." | `refactoring`; not `clean-architecture` | Protected structural sequence is central without a policy-dependency decision. |
| "We cannot observe current behavior because the class constructs a database and reads time; gain first feedback only." | `working-effectively-with-legacy-code`; not `clean-architecture` | Database/time are barriers to feedback, not evidence that target dependency architecture should be chosen now. |
| "Move tested approval policy from the controller into a use case without changing behavior." | `refactoring`, `clean-architecture` | Refactoring controls protected structural change; Clean Architecture supplies inward policy ownership and humble-adapter target shape. |
| "Design a payment use case with provider-independent policy plus explicit timeout, retry, isolation, and diagnostics." | `clean-architecture`, `release-it` | Policy/detail separation and production failure behavior are independently central. |
| "Add a timeout to an ordinary provider call." | No `clean-architecture`; `release-it` only if production failure behavior is an explicit objective or demonstrated problem | A service call alone does not create a policy-dependency decision. |
| "Implement the ticket and add tests." | None of the book skills from wording alone | Generic implementation and test language does not identify a distinctive lens. |
| Shared `_skill-workbench/evaluations/cases/catalog-null.md` | None of the book skills | Catalog-wide null control is reused rather than duplicated under this book. |

## Catalog Term Overlap

| Shared term | Clean Architecture meaning | Neighbor boundary |
| --- | --- | --- |
| Boundaries | Source direction and ownership keep policy independent from volatile details; a boundary must preserve independent change. | Clean Code uses local adapters for readability; Legacy Code creates observation/substitution seams; Release It isolates production failures. |
| Tests | Core policy is testable without real details, and boundary contracts plus adapter tests enforce ownership. | Clean Code focuses readable contract protection; Refactoring uses tests as a safety net; Legacy Code gains first feedback; Release It tests failure modes. |
| Refactoring | Existing code moves policy inward and details outward while preserving behavior incrementally. | Refactoring governs small behavior-preserving sequence and stopping; Legacy Code governs control before the target reshape is safe. |
| Database | Persistence is replaceable and must not shape or be imported by core policy. | A database mention alone may instead be ordinary adapter work, a Legacy feedback barrier, a data-system concern, or no book trigger. |
| Services and remote calls | A service is not automatically a boundary; source dependencies, data ownership, I/O translation, and policy independence still govern. | Release It owns timeouts, retries, overload, isolation, degraded service, observability, and recovery when production failure behavior is central. |
| Readability | Structure should reveal use cases and business capabilities so policy ownership is visible. | Clean Code owns names, function shape, mutation, comments, happy-path clarity, and proportional local cleanup. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description; early-guidance; final-check | Description's inward-dependency capability; `Policy and Dependency Direction`; dependency checklist item | Promotes complete `M2`; no shortened authoritative duplicate is added. |
| `N2` | early-guidance; final-check | `Use Cases and Humble Adapters`; entity/use-case checklist item | Complete `M3` and `M4` keep invariants, application orchestration, and plain boundary models together. |
| `N3` | description; early-guidance; final-check | Description's concrete-infrastructure branch; `Policy and Dependency Direction`; detail-replaceability checklist items | Complete `M5`, `M6`, and `M18` preserve policy-owned ports, outer adapters, and edge wiring. |
| `N4` | description; early-guidance; final-check | Description's misplaced-policy branch; `Use Cases and Humble Adapters`; humble-adapter checklist item | Complete `M7` and `M17` keep translation roles beside the trigger that moves business rules inward. |
| `N5` | early-guidance; reference-router; final-check | `Structure and Boundary Economics`; focused structure/ownership routes; structure checklist item | Complete `M8`, `M10`, and `M19` preserve use-case-first organization and anti-escape-hatch pressure. |
| `N6` | description; early-guidance; reference-router; final-check | Description's false-positive boundary; `Structure and Boundary Economics`; focused boundary-cost routes; enforced-boundary checklist item | Complete `M9` and `M12` keep lightest-boundary economics beside enforceability; service/package/diagram nouns do not trigger alone. |
| `N7` | early-guidance; reference-router; final-check | `Tests and Incremental Change`; focused testing route; detail-free test checklist item | Complete `M13` and `M22` preserve core-versus-adapter testing and the volatile-detail test trigger. |
| `N8` | description; early-guidance | Description's policy-import branch; `Policy and Dependency Direction` | Complete `M16` is colocated after outer-detail guidance rather than copied from nano. |
| `N9` | description; early-guidance | Description's misplaced-policy branch; `Use Cases and Humble Adapters` | Complete `M17` and `M19` cover edge-owned business rules and generic service/utility escape hatches. |
| `N10` | description; early-guidance | Description's concrete-infrastructure branch; `Policy and Dependency Direction` | Complete `M18` preserves inward-owned ports and edge wiring. |
| `N11` | description; early-guidance; reference-router | Description's policy/detail and false-positive branches; `Use Cases and Humble Adapters`; `Structure and Boundary Economics`; focused direction/ownership routes | Complete `M12` and `M20` cover fake boundaries, layer bypass, cycles, and restored ownership without installing nano as a second rule set. |
| `N12` | early-guidance; reference-router | `Structure and Boundary Economics`; focused boundary-cost/tradeoff routes | Complete `M23` keeps unavoidable compromises outermost and reversible; `M9` and `M14` preserve proportionality and incremental change. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Policy and Dependency Direction` | Moved verbatim and promoted first. | Establishes the architecture-economics pressure before local shortcuts. |
| `M2` | `Policy and Dependency Direction` | Moved verbatim. | Defines the inward source-dependency rule and prohibited core imports. |
| `M3` | `Use Cases and Humble Adapters` | Moved verbatim. | Keeps enterprise invariants and application orchestration distinct. |
| `M4` | `Use Cases and Humble Adapters` | Moved verbatim. | Keeps plain boundary models beside use-case and adapter responsibilities. |
| `M5` | `Policy and Dependency Direction` | Moved verbatim. | Colocated with detail-type leakage trigger `M16`. |
| `M6` | `Policy and Dependency Direction` | Moved verbatim. | Colocated with direct infrastructure trigger `M18`. |
| `M7` | `Use Cases and Humble Adapters` | Moved verbatim. | Colocated with business-rule-in-adapter trigger `M17`. |
| `M8` | `Structure and Boundary Economics` | Moved verbatim. | Colocated with generic escape-hatch trigger `M19`. |
| `M9` | `Structure and Boundary Economics` | Moved verbatim. | Kept beside compromise rule `M23` and enforcement rule `M12`. |
| `M10` | `Structure and Boundary Economics` | Moved verbatim. | Preserves actor, change-reason, ownership, deployment, and release-pressure qualifiers. |
| `M11` | `Structure and Boundary Economics` | Moved verbatim. | Retains component and dependency principles as policy-protection mechanisms. |
| `M12` | `Structure and Boundary Economics` | Moved verbatim. | Keeps concrete enforcement beside fake-boundary and service-boundary concerns. |
| `M13` | `Tests and Incremental Change` | Moved verbatim. | Colocated with detail-bound test trigger `M22`. |
| `M14` | `Tests and Incremental Change` | Moved verbatim. | Preserves behavior, incremental extraction, and explicit debt. |
| `M15` | `Policy and Dependency Direction` | Moved verbatim and promoted after `M1`. | Keeps schedule pressure beside the rule whose cost it tries to override. |
| `M16` | `Policy and Dependency Direction` | Moved verbatim. | Colocated after complete outer-detail rule `M5`. |
| `M17` | `Use Cases and Humble Adapters` | Moved verbatim. | Colocated after complete humble-adapter rule `M7`. |
| `M18` | `Policy and Dependency Direction` | Moved verbatim. | Colocated after complete interface ownership and wiring rule `M6`. |
| `M19` | `Structure and Boundary Economics` | Moved verbatim. | Colocated after use-case-first organization rule `M8`. |
| `M20` | `Use Cases and Humble Adapters` | Moved verbatim. | Keeps adapter bypass, presenter persistence access, and import cycles together. |
| `M21` | `Structure and Boundary Economics` | Moved verbatim. | Keeps services, process/deployment boundaries, remote I/O, and hardware under the same ownership test. |
| `M22` | `Tests and Incremental Change` | Moved verbatim. | Colocated after core-versus-adapter testing rule `M13`. |
| `M23` | `Structure and Boundary Economics` | Moved verbatim. | Colocated after boundary economics rule `M9` and before coupling tradeoffs. |

## Wording Fidelity

- Verbatim primary bias: exact text from `clean-architecture/clean-architecture.mini.md` appears under `Primary Bias`.
- Verbatim mini rules: every authoritative `M1`-`M23` sentence appears exactly once in `SKILL.md`; only whole rules were reordered.
- Verbatim final checklist and order: all eight items appear exactly and in canonical order.
- Reworded mini rules: none.
- Faithful mini-rule merges: none.
- Nano handling: no `N*` item is installed as a second authoritative rule. Nano affects description routing, concern order, focused-reference triggers, and the existing final checklist as recorded above.
- Authored runtime text: frontmatter, concern headings, and reference-router prose provide selection and progressive disclosure. They do not replace or strengthen canonical mini guidance.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Inline reference map: six source-backed labels link common focused questions directly to canonical full headings; every other bounded question still uses the exhaustive index. This changes loading only.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 758 words.
- `SKILL.md`: 915 words across 71 lines.
- Packaging overhead: 157 words.
- Frontmatter description: 478 characters, excluding the terminating newline.
- Decision: retain the source-driven exception. The canonical mini already exceeds the 500-word target, all 23 mini rules and eight checklist items remain required for complete ordinary use, and the seven-word soft-target overage provides direct focused routes while preserving the ordinary stop. Do not paraphrase canonical rules to reduce this count.

## Evaluation Cases

These contracts and their blind raw-artifact files preserve the pre-execution record. Their original withheld or pending fields are historical; the final batch reconciliation at the end of this file supersedes them without rewriting frozen contracts. The shared catalog-null file is referenced as E10 rather than duplicated.

### E1: Direct Complete Architecture Audit

- Class: direct invocation; comprehensive retrieval; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/direct-comprehensive-audit.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture`.
- Reference mode: `comprehensive`.
- Expected sections: all 18 Clean Architecture full-reference sections, read end to end.
- Forbidden sections: every reference section belonging to a forbidden skill.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: compared with a skill-disabled answer, GREEN must demonstrate exhaustive dependency-direction, policy/detail, layer-responsibility, structure, boundary-economics, enforcement, test-shape, and tradeoff coverage without importing neighbor concerns.
- Source trace: all `M1-M23`, nano salience `N1-N12`, and all 18 full-reference headings.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E2: Ordinary Policy/Detail Design

- Class: distinctive symptom recognition; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/ordinary-policy-detail-design.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture`.
- Reference mode: `ordinary`.
- Expected sections: none; `SKILL.md` is sufficient.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must replace Next.js/Prisma-owned policy with a focused application action, plain input/output models, application-owned ports, outer translation/adapters, and composition-root wiring while preserving the stated business behavior.
- Source trace: `M2-M7`, `M13`, `M16-M18`, `N1-N4`, `N8-N10`, and the final checklist.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E3: Focused Port Ownership Dispute

- Class: focused retrieval; disputed interpretation; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/focused-port-ownership-dispute.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture`.
- Reference mode: `focused`.
- Expected sections: exactly `Non-Negotiable Rules` and `Required Layer Responsibilities`.
- Forbidden sections: every other Clean Architecture full-reference section and every forbidden-skill reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must reject infrastructure-owned ports and row types despite interface indirection, place the required abstraction and plain models inward, and keep SQL translation plus implementation outward without widening into a full audit.
- Source trace: `M2`, `M4-M6`, `M12`, `M16`, `M18`, `N1`, `N3`, `N8`, `N10`, plus the two expected full headings.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E4: Policy Placement Under Schedule Pressure

- Class: distinctive symptom recognition; pressure; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/schedule-pressure-controller-policy.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture`.
- Reference mode: `ordinary`.
- Expected sections: none; `SKILL.md` is sufficient.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must resist putting VIP eligibility in the controller, state the future ownership/test/replacement cost without being prompted to do so, keep the controller translating, place policy in the use case or domain, and keep any unavoidable compromise outermost and explicit.
- Source trace: `M1`, `M3`, `M7`, `M15`, `M17`, `M23`, `N2`, `N4`, `N9`, `N12`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E5: Clean Code Adapter Neighbor

- Class: near-neighbor counterexample; pair-specific negative; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/clean-code-adapter-neighbor.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}` only if behavior-preserving structural change is treated as central.
- Forbidden skills: `{clean-architecture, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: none; Clean Code must remain the source of the local-shape decision if Refactoring is also selected.
- Reference mode: `ordinary`.
- Expected sections: none; selected skill bodies are sufficient.
- Forbidden sections: every book-skill index and full-reference section, especially every Clean Architecture section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must assign ownership to Clean Code despite database, adapter, test, and layer vocabulary, improve local names/mode/comment shape within the fixed boundary, and avoid inventing ports, use cases, entities, or architecture work.
- Source trace: Clean Code `M3`, `M5`, `M11`, `M16`, `M17`; Clean Architecture description false-positive boundary and `docs/compatibility/clean-architecture/clean-code.md`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E6: Refactoring-Only Structural Neighbor

- Class: near-neighbor counterexample; pair-specific negative; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/refactoring-structural-neighbor.md`.
- Required skills: `{refactoring}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, clean-code, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `refactoring`.
- Reference mode: `ordinary`.
- Expected sections: none; the Refactoring body is sufficient.
- Forbidden sections: every book-skill index and full-reference section, especially every Clean Architecture section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must govern the requested named, behavior-preserving sequence and stopping condition through Refactoring without inferring policy/detail work from general structure vocabulary.
- Source trace: Refactoring `M1`, `M2`, `M6`, `M13`, `M14`; Clean Architecture description neighbor boundary and `docs/compatibility/clean-architecture/refactoring.md`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E7: Legacy Code First-Feedback Neighbor

- Class: near-neighbor counterexample; pair-specific negative; focused application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/legacy-first-feedback-neighbor.md`.
- Required skills: `{working-effectively-with-legacy-code}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, clean-code, refactoring, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `working-effectively-with-legacy-code`.
- Reference mode: `focused`.
- Expected sections: exactly Legacy Code `Testing Strategy Rules`, `Seam Rules`, and `Dependency Breaking Rules`.
- Forbidden sections: every Clean Architecture section and every Legacy Code section outside the expected set.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must treat database construction and ambient time as first-feedback barriers, characterize before semantics, and avoid choosing a Clean Architecture target before control exists.
- Source trace: Legacy Code `M2-M7`, `M17`, `M18`, `N2-N5`, `N9`, `N10`; Clean Architecture description neighbor boundary and `docs/compatibility/clean-architecture/working-effectively-with-legacy-code.md`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E8: Protected Architectural Refactoring Overlap

- Class: compatible co-invocation; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/refactoring-compatible-overlap.md`.
- Required skills: `{refactoring, clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: none; Refactoring must control behavior-preserving sequence and stopping, while Clean Architecture must control target dependency direction and policy ownership.
- Reference mode: `ordinary`.
- Expected sections: none; both selected skill bodies are sufficient.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must preserve status codes, repository/audit effects, and order through small reviewable steps while moving approval policy into a focused use case with plain models, inward-owned ports, edge translation, and a humble controller.
- Source trace: Refactoring `M1-M4`, `M13`, `M14`; Clean Architecture `M2-M7`, `M12-M14`, `M17`, `M20`, `N1-N4`, `N11`; `docs/compatibility/clean-architecture/refactoring.md`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E9: Architecture and Production-Failure Overlap

- Class: compatible co-invocation; ordinary application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/release-it-compatible-overlap.md`.
- Required skills: `{clean-architecture, release-it, designing-data-intensive-applications}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, code-complete}`.
- Required order: none; Clean Architecture owns policy/detail shape, Release It owns production failure semantics, and DDIA owns exactly-once, idempotency, retry, and unknown-success data semantics.
- Reference mode: `ordinary`.
- Expected sections: none; all three selected skill bodies are sufficient for one explicit provider boundary.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; parent contract review precedes behavioral execution.
- Post-skill runs: not run by converter.
- Behavioral delta: GREEN must define provider-independent policy, plain models, inward-owned ports, outward adapters, and edge wiring while separately defining finite timeout, retry eligibility/bounds, idempotency, unknown-success recovery, isolation, degraded behavior, and diagnostics.
- Source trace: Clean Architecture `M2-M7`, `M13`, `M18`, `M21`, `N1-N4`, `N7`, `N10`; Release It `M1-M6`, `M12`, `M18`, `M20`; DDIA `M2`, `M8`, `M14`, `M19`, `M22`, `N1`, `N4`, `N6`, `N8`; `docs/compatibility/clean-architecture/release-it.md`.
- Result: contract predeclared; execution intentionally withheld pending parent review.

### E10: Shared Catalog Null

- Class: catalog-null counterexample; stability control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/catalog-null.md`.
- Required skills: `{}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-architecture, clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: none.
- Reference mode: `none`.
- Expected sections: none.
- Forbidden sections: every book-skill body, index, and full-reference section.
- Baseline runs: existing shared controls remain authoritative; no new run was made for this conversion.
- Post-skill runs: not run by converter; rerun after parent approves the new catalog contract.
- Behavioral delta: adding Clean Architecture must not make a generic non-book task select any book guidance skill.
- Source trace: catalog routing contract only; no book recommendation should appear.
- Result: existing shared fixture reused; post-description regression intentionally withheld pending parent review.

### E3b: Focused Interface Ownership Replacement

- Class: focused retrieval; disputed interpretation; replacement for E3's over-prescribed exact section set.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/focused-interface-ownership-dispute.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture`.
- Reference mode: `focused`.
- Expected sections: `Non-Negotiable Rules` and `Required Layer Responsibilities` are required; `Forbidden Patterns` is an allowed bounded addition.
- Forbidden sections: every other Clean Architecture section and every other book reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: reject infrastructure-owned abstraction despite interface indirection, move interface ownership inward, and avoid expanding the answer into feature generation or a complete audit.
- Source trace: `M2`, `M4-M6`, `M12`, `M16`, `N1`, `N3`, `N8`; the required two headings and optional `Forbidden Patterns`.
- Result: replacement predeclared; not executed.

### X1: Explicit Ordinary Acceptance

- Class: explicit invocation; ordinary disclosure.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/manual-ordinary.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture` only.
- Reference mode: `ordinary`.
- Expected sections: none.
- Forbidden sections: every book-skill index and full-reference section.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: apply inward ownership and plain boundaries without loading exhaustive guidance.
- Source trace: `M2-M7`, `M12-M14`, `N1-N4`.
- Result: pending.

### X2: Explicit Focused Acceptance

- Class: explicit invocation; focused disputed interpretation.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/manual-focused.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture` only.
- Reference mode: `focused`.
- Expected sections: `Non-Negotiable Rules` and `Required Layer Responsibilities` are required; `Forbidden Patterns` is allowed.
- Forbidden sections: every other Clean Architecture section and every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle interface ownership from source-supported dependency direction without a complete audit.
- Source trace: `M2`, `M4-M6`, `M12`, `M16`, `N1`, `N3`, `N8` and the named headings.
- Result: pending.

### X2b: Explicit Focused Bounded Replacement

- Class: explicit invocation; focused replacement for X2's narrow subsection contract.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/manual-focused-bounded.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture` only.
- Reference mode: `focused`.
- Expected sections: `Non-Negotiable Rules` and `Required Layer Responsibilities` are required; `Forbidden Patterns` and `Final Instruction` are allowed.
- Forbidden sections: every other Clean Architecture section and every other book reference.
- Baseline runs: not run; predeclared before replacement GREEN.
- Post-skill runs: not run.
- Behavioral delta: settle and arbitrate interface ownership from no more than four coherent headings.
- Source trace: `M2`, `M4-M6`, `M12`, `M16`, `N1`, `N3`, `N8` and the named headings.
- Result: pending.

### X3: Explicit Comprehensive Acceptance

- Class: explicit invocation; comprehensive retrieval.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/manual-comprehensive.md`.
- Required skills: `{clean-architecture}`.
- Allowed skills: `{}`.
- Forbidden skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}`.
- Required order: `clean-architecture` only.
- Reference mode: `comprehensive`.
- Expected sections: all 18 Clean Architecture headings, recorded as `*`.
- Forbidden sections: every other book reference.
- Baseline runs: not run; predeclared before explicit-policy GREEN.
- Post-skill runs: not run.
- Behavioral delta: provide source-grounded end-to-end coverage that the skill-disabled baseline cannot retrieve.
- Source trace: every `M*`, `N*`, checklist item, and full heading.
- Result: pending.

### P1: Manual-Policy Implicit Exclusion

- Class: invocation-policy counterexample; repeated catalog control.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/ordinary-policy-detail-design.md`.
- Required skills: `{}` under the explicit-only policy.
- Allowed skills: `{clean-code, refactoring, working-effectively-with-legacy-code, release-it, designing-data-intensive-applications, code-complete}` are neutral for this Clean Architecture policy check.
- Forbidden skills: `{clean-architecture}`.
- Required order: none.
- Reference mode: `none` for Clean Architecture; other allowed skills follow their own contracts.
- Expected sections: none from Clean Architecture.
- Forbidden sections: every Clean Architecture packaged file.
- Baseline runs: retained unnamed baselines were already strong.
- Post-skill runs: not run under the explicit-only policy.
- Behavioral delta: the package must not add automatic context when the user did not invoke it.
- Source trace: invocation policy only.
- Result: pending `3/3` policy probe.

## Independent Review

- Reviewers: independent batch source/package reviews `019f58a9-d0d9-7153-b03e-e89cd1eedc09`, `019f58ba-0c72-7460-af90-48434c787ef8`, and the final acceptance review recorded in `_skill-workbench/BATCH_2_RESULTS.md`.
- Catalog snapshot: all seven live project book skills.
- Semantic verdict: PASS. The source compression, exact package guidance, description, router, index, full reference, checklist, and catalog boundary have no independent-review finding.
- Unsupported or altered active guidance: none.

## Final Batch Reconciliation

- Invocation policy: repo-local manual-only controls were not enforced, so the package uses implicit invocation with its narrow positive policy/dependency threshold.
- Explicit progressive disclosure: `manual-ordinary/green-1.json` used the body only; `manual-focused-bounded/green-1.json` read exactly `Non-Negotiable Rules`, `Required Layer Responsibilities`, `Forbidden Patterns`, and `Final Instruction`; `manual-comprehensive/green-1.json` recorded `*` after the end-to-end full read.
- Current catalog boundary: `ordinary-policy-detail-design/green-final-cc-scope-{1,2,3}.json` selected Clean Architecture alone in `3/3` and excluded Code Complete in `3/3`. Only one run remained ordinary; two over-read focused references.
- Application diagnostics: the same current runs invented order statuses, not-found behavior, or HTTP semantics absent from the fixture. These are general solver additions, not packaged or book-attributed guidance.
- Baseline timing: case fixtures were frozen before package authoring, but the isolated skill-disabled runs happened after draft authoring. They remain optional diagnostic evidence under the current protocol.
- Current-policy status: **accepted conversion**. Source and package semantics pass, required Clean Architecture discovery passes, and explicit ordinary/focused/comprehensive probes pass. The two focused reads in the ordinary application case did not become end-to-end `*` reads and remain disclosure diagnostics rather than material tier collapse.

## Validation Evidence

- Wording validation: 23/23 exact mini rules, exact primary bias, and exact final-checklist wording and order.
- Structural validation: 66 lines, 908 words, 150 packaging words, 23 mini IDs, 12 nano IDs, and 18 indexed full-reference sections.
- Full-reference equality: `cmp clean-architecture/clean-architecture.md .agents/skills/clean-architecture/references/full.md` exited `0`; both files have SHA-256 `1f0366be1720989c63df6da8f15f12e78f8786f6e712eeb16cf3690b4dab6cc4`.
- Index validation: the repository validator accepted all 18 headings, GitHub anchors, order, and heading-to-last-nonempty line ranges; every row has manually authored `Read when` guidance.
- Official validator: `/Users/jakubtomanik/.codex/skills/.system/skill-creator/scripts/quick_validate.py` reports `Skill is valid!` through `uv run --with pyyaml`.
- Evaluation contracts: the required-skill contract validator passes; historical allowed/forbidden partitions remain preserved diagnostics.
- Remaining risk: model answers can still over-read source detail or invent fixture state despite a source-faithful package.

## Inline Reference Map Evaluation

### RM1: Ordinary policy-detail control

- Contract version: 2
- Class: application and disclosure
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/ordinary-policy-detail-design.md`
- Fixture SHA-256: `be0ba2e68a8e7f76e31839b2fc76a26b62ef0fb4be8826ddc4ec9d65d0ed7ca8`
- Required skills: `{clean-architecture}`
- Distinctive judgment: Keep application policy inward and make the outer adapter own framework and persistence translation without opening source detail already present in the compact body.
- Neighbor ownership: Clean Code may comment on local readability, but policy/detail dependency ownership is the Clean Architecture decision.
- Ownership review: PASS - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; fixture blindness, central ownership, and the ordinary tier premise were accepted.
- Reference expectation: ordinary
- Runs: `green-inline-map-1`; selected `clean-architecture`; `ordinary`; no reference sections
- Package fidelity trace: exact mini-derived policy, boundary, adapter, and dependency guidance; router-only change
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: none

### RM2: Focused interface-ownership control

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/focused-interface-ownership-dispute.md`
- Fixture SHA-256: `6ca5339381c6e02940bb15280a89c210fe289e163dda0a61affc1dce1f4c5dea`
- Required skills: `{clean-architecture}`
- Distinctive judgment: Resolve source dependency and abstraction ownership across an application port and SQL adapter without broad redesign.
- Neighbor ownership: The dispute is architectural ownership, not a local naming, refactoring, or production-failure decision.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture reveals the required source lens and cannot be reused unchanged.
- Reference expectation: focused
- Compact-body gap: The fixture asks for the source's detailed justification of abstraction ownership and source dependency, beyond the compact rule statement.
- Intended index destinations: `Non-Negotiable Rules` and `Required Layer Responsibilities`
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: the two named canonical full headings and the unchanged mini-derived dependency rule
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM2b; the frozen fixture, hash, and required set remain unchanged

### RM2b: Focused boundary-cost replacement

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/focused-boundary-cost-choice-v2.md`
- Fixture SHA-256: `b73482b868096a813845851f01db1f2a884c456c356165af408d1d2a9231fced`
- Required skills: `{clean-architecture}`
- Distinctive judgment: Compare in-process, deployable-component, and remote-service boundaries using source-specific boundary, deployment, and operational costs, then choose the smallest justified split.
- Neighbor ownership: Release It! may contribute remote-failure tactics, but the central decision is whether policy ownership and deployment economics justify a stronger architecture boundary.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, explicit source dispute, and the two-section destination were accepted.
- Reference expectation: focused
- Compact-body gap: none; the fixture explicitly disputes which source boundary costs justify a stronger deployment boundary and requires canonical checking.
- Intended index destinations: `Boundary Cost, Deployment, and Operations` and `Services, Distribution, and Embedded Boundaries`
- Runs: `green-inline-map-1`; selected `clean-architecture`; `focused`; target sections `Architecture Economics and Priority`, `Boundary Cost, Deployment, and Operations`, and `Services, Distribution, and Embedded Boundaries`
- Package fidelity trace: the two named canonical full headings and unchanged mini-derived dependency guidance
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: one additional relevant architecture-economics section beyond the two-section minimum; index plus full access remained bounded

### RM3: Comprehensive architecture control

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/direct-comprehensive-audit.md`
- Fixture SHA-256: `c64d18ab132bc478a08abed288b891d07884f28ef502471f0cb10a639921280b`
- Required skills: `{clean-architecture}`
- Distinctive judgment: Apply the complete Clean Architecture lens across all canonical concern families.
- Neighbor ownership: Other books may contribute compatible observations, but the requested end-to-end architecture audit is owned by this lens.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture exposes the required source lens and cannot be reused unchanged.
- Reference expectation: comprehensive
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: all canonical full headings
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM3b; the frozen fixture, hash, and required set remain unchanged

### RM3b: Comprehensive policy-boundary replacement

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-architecture/comprehensive-policy-boundary-audit-v2.md`
- Fixture SHA-256: `9071a499d3bb7b298ed7e81e73081708d619bacca3f7ad6129609023e6d1d6a2`
- Required skills: `{clean-architecture}`
- Distinctive judgment: Apply the complete policy-independence, dependency-direction, layer, boundary-economics, component, testing, and migration lens end to end.
- Neighbor ownership: Other skills may contribute compatible local or operational findings, but the explicit exhaustive policy-and-boundary objective makes this skill central.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, and end-to-end comprehensive loading were accepted.
- Reference expectation: comprehensive
- Runs: `green-inline-map-1`; selected `clean-architecture` and compatible `patterns-of-enterprise-application-architecture`; both reported `comprehensive` target access with `sections=["*"]`
- Package fidelity trace: all canonical full headings
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: permitted neighboring comprehensive selection; required target inclusion and end-to-end access passed
