# Clean Architecture Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit dispute, demonstrated dependency-rule hotspot, or one bounded question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a comprehensive architecture audit or a decision spanning several concern families, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-17` | Establish the binding scope or decide whether independent business rules, inward dependencies, replaceable details, and testability are the governing concerns. |
| [Non-Negotiable Rules](full.md#non-negotiable-rules) | `19-72` | Resolve a dependency-rule, business-rule purity, framework/database/web detail, explicit-boundary, use-case, entity, or inward-ownership dispute. |
| [Required Layer Responsibilities](full.md#required-layer-responsibilities) | `74-154` | Decide whether code or a type belongs in domain, application, interface adapters, or infrastructure, including what each layer may import and own. |
| [Code Generation Rules](full.md#code-generation-rules) | `156-210` | Design a non-trivial feature's use case, plain boundary models, volatile-dependency ports, composition root, stable dependencies, or visible boundaries. |
| [Architecture Heuristics](full.md#architecture-heuristics) | `212-255` | Diagnose an import direction, policy-versus-detail placement, replaceable-edge goal, or feature-first structure when the correct location remains unclear. |
| [Architecture Economics and Priority](full.md#architecture-economics-and-priority) | `257-266` | Arbitrate urgent feature pressure, future change cost, option preservation, boundary value, or evidence that architecture should be revisited. |
| [Paradigm and Component Rules](full.md#paradigm-and-component-rules) | `268-282` | Resolve dependency inversion, actor/reason separation, substitution, interface sizing, component cohesion, cycles, or stability-versus-abstraction tradeoffs. |
| [Boundary Cost, Deployment, and Operations](full.md#boundary-cost-deployment-and-operations) | `284-294` | Choose among source, deployment, process, service, or partial boundaries, or decide whether duplication and enforcement better preserve independent change. |
| [Services, Distribution, and Embedded Boundaries](full.md#services-distribution-and-embedded-boundaries) | `296-304` | Decide whether a service is a real architecture boundary, place remote I/O and listeners, or isolate firmware and hardware details from policy. |
| [Naming Rules](full.md#naming-rules) | `306-315` | Name modules, use cases, ports, adapters, and business capabilities, or challenge an ambiguous `Service` role after ownership is established. |
| [Testing Rules](full.md#testing-rules) | `317-346` | Separate fast entity/use-case/boundary-contract tests from adapter and integration tests, or choose the supported boundary through which to test. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `348-387` | Classify a concrete framework/database leak, controller-centric rule, god service, layer bypass, reversed interface ownership, or utility dumping ground. |
| [Refactoring Rules](full.md#refactoring-rules) | `389-417` | Plan an incremental existing-code move of policy inward, volatile details behind ports, translation outward, god services apart, or framework-free tests. |
| [Output Expectations](full.md#output-expectations) | `419-442` | Determine the expected Clean Architecture shape for a feature, existing-code change, or architecture-focused code review. |
| [Review Checklist](full.md#review-checklist) | `444-464` | Run the canonical final architecture scan before accepting a design or change. |
| [Preferred Default Shapes](full.md#preferred-default-shapes) | `466-492` | Choose a feature/use-case directory shape or inward-owned interface pattern after policy and adapter ownership are known. |
| [When Tradeoffs Are Necessary](full.md#when-tradeoffs-are-necessary) | `494-504` | Place and document an unavoidable boundary compromise while preventing it from becoming normalized core architecture. |
| [Final Instruction](full.md#final-instruction) | `506-515` | Arbitrate a final uncertain choice using policy independence, inward dependencies, isolated details, testability, and replaceability. |
