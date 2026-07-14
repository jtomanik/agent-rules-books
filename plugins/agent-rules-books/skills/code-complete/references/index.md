# Code Complete Reference Index

Use `SKILL.md` alone when it resolves ordinary construction work. For an explicit construction dispute or one bounded choice left unresolved after applying the skill, use this index and read only the named sections from [full.md](full.md). For a comprehensive audit, explicit request for the complete lens, or unresolved system-level decision whose correctness depends on interactions across several independent concern groups, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-18` | Confirming whether a broad request is construction work and which quality outcomes the Code Complete policy optimizes. |
| [Primary Directive](full.md#primary-directive) | `20-33` | Several construction options remain and defect probability, inspectability, control-flow cost, data clarity, or invalid-state protection must arbitrate. |
| [Foundational Construction Rules](full.md#foundational-construction-rules) | `35-43` | A disputed local choice needs the baseline priorities for human readability, explicitness, visible flow, correctness, and conventions. |
| [Construction Prerequisites and Decisions](full.md#construction-prerequisites-and-decisions) | `45-53` | A solution is proposed before requirements, architecture fit, risks, language constraints, error policy, data, integration, or testing decisions are settled. |
| [Pseudocode Programming Process](full.md#pseudocode-programming-process) | `55-62` | A complex routine's steps or abstraction levels are unclear and precise pseudocode may expose the design before coding. |
| [Routine Design Rules](full.md#routine-design-rules) | `64-80` | A routine is hard to name or misuse-resistant design is disputed because phases, parameters, return values, nesting, or side effects are mixed. |
| [Variable and Data Rules](full.md#variable-and-data-rules) | `82-96` | Variable purpose, scope, initialization, mutability, constants, units, or sentinel meanings are difficult to inspect. |
| [Data Type Rules](full.md#data-type-rules) | `98-108` | Primitives, flags, closed states, unusual structures, units, ranges, precision, encoding, or ownership obscure data meaning. |
| [Control Flow Rules](full.md#control-flow-rules) | `110-125` | Nesting, predicates, exits, dead paths, side effects, or compact expressions make the logic hard to verify. |
| [Statement, Conditional, and Loop Rules](full.md#statement-conditional-and-loop-rules) | `127-137` | Statement order, normal-path placement, loop mechanics, extraction, or a possible table-driven replacement is disputed. |
| [Defensive Programming Rules](full.md#defensive-programming-rules) | `139-152` | A trust boundary, programmer assumption, recoverability decision, corrupted state, or swallowed failure needs an explicit defense policy. |
| [Error Handling Rules](full.md#error-handling-rules) | `154-162` | Failure abstraction, diagnostic context, normal-path readability, standardization, or explicit failure semantics are unresolved. |
| [Table-Driven and Data-Driven Rules](full.md#table-driven-and-data-driven-rules) | `164-171` | Stable repeated branching may become a table or map, but clarity, validation, and encoding transparency need judgment. |
| [Class and Module Design Rules](full.md#class-and-module-design-rules) | `173-186` | Representation leaks, cohesion is weak, contracts expose internals, or persistence, formatting, business, and integration concerns are mixed. |
| [Complexity Management Rules](full.md#complexity-management-rules) | `188-196` | Tangled code, duplication, or working-memory load is increasing defect risk and the right simplification boundary is unclear. |
| [Construction with Preconditions and Postconditions](full.md#construction-with-preconditions-and-postconditions) | `198-205` | Routine assumptions or invariants need a simple contract, or assertion, validation, and domain-error responsibilities are disputed. |
| [Comment Rules](full.md#comment-rules) | `207-214` | Comments may narrate mechanics, drift from code, or need classification as intent, rationale, contract, or non-obvious fact. |
| [Coding Standards Rules](full.md#coding-standards-rules) | `216-223` | A module diverges in formatting, naming, file structure, or idiom and local taste conflicts with shared convention. |
| [Incremental Construction Rules](full.md#incremental-construction-rules) | `225-232` | Work is becoming a long-lived, unverifiable batch and the appropriate construction or integration slice is unclear. |
| [Quality, Collaboration, Debugging, and Refactoring](full.md#quality-collaboration-debugging-and-refactoring) | `234-243` | Defect risk must determine reviews or tests, a diagnosis is guess-driven, or refactoring and behavior change need separation. |
| [Performance, Integration, Tools, and Craftsmanship](full.md#performance-integration-tools-and-craftsmanship) | `245-255` | Performance evidence, integration cadence, automation, documentation, style, or a clarity tradeoff is an explicit construction decision. |
| [Review Rules](full.md#review-rules) | `257-271` | A construction-focused review needs a bounded scan for names, routines, parameters, nesting, effects, boundaries, duplication, modules, and comments. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `273-296` | Clever compression, routine bloat, defensive vacuum, comment-as-crutch, or consistency neglect is defended under pressure. |
| [Code Generation Rules](full.md#code-generation-rules) | `298-316` | Generated code needs explicit default choices for names, routines, data, flow, boundaries, modules, style, and hidden assumptions. |
| [Testing Rules](full.md#testing-rules) | `318-325` | Normal, boundary, invalid-input, defensive-check, contract, or table-driven tests are missing or disputed. |
| [Review Checklist](full.md#review-checklist) | `327-343` | Finalizing a construction change requires a complete inspection of names, routines, flow, boundaries, contracts, complexity, modules, comments, and consistency. |
| [Final Instruction](full.md#final-instruction) | `345-354` | The final choice still needs the book's ordered defect-risk, readability, flow, defensive-correctness, and maintainability test. |
