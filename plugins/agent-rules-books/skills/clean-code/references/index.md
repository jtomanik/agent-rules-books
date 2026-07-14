# Clean Code Reference Index

Use this semantic index for a focused Clean Code ambiguity or hotspot. Read only the named sections from [full.md](full.md). For a comprehensive audit, disputed interpretation, explicit request for the complete lens, or decision spanning several concerns, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Priority and behavior](full.md#priority-and-behavior) | `5-12` | Tradeoffs need ordering, schedule pressure invites a shortcut, or touched code risks becoming harder to change. |
| [Core clean code principles](full.md#core-clean-code-principles) | `14-22` | Code is surprising, indirect, difficult to modify, or understandable only through wide cross-file reconstruction. |
| [Naming rules](full.md#naming-rules) | `24-42` | Names are vague, overloaded, abbreviated, misleading, visually confusable, or dependent on comments for meaning. |
| [Function rules](full.md#function-rules) | `44-62` | Functions mix phases or abstraction levels, hide mutation, combine commands with queries, use mode flags, take many parameters, duplicate logic, or nest deeply. |
| [Comment rules](full.md#comment-rules) | `64-79` | Comments explain confusing flow, compensate for names or structure, drift from behavior, narrate code, or need classification as rationale, warning, constraint, or contract. |
| [Formatting and structure](full.md#formatting-and-structure) | `81-91` | Layout separates related concepts, ordering hides the high-level story, or formatting obscures scope and scanning. |
| [Objects, modules, and data structures](full.md#objects-modules-and-data-structures) | `93-102` | Representation leaks outward, train-wreck navigation appears, or data carriers and behavior-rich objects are mixed without intent. |
| [Class and module design](full.md#class-and-module-design) | `104-113` | A class or module has mixed responsibilities, low cohesion, an easy-to-misuse API, unstable inheritance, or setup that overwhelms behavior. |
| [Error handling](full.md#error-handling) | `115-124` | The happy path is buried, null-like sentinel flow represents invalid states, callers lack useful error distinctions, diagnostics lack context, or cleanup is implicit. |
| [Boundaries and external dependencies](full.md#boundaries-and-external-dependencies) | `126-132` | Core logic couples to third-party, persistence, vendor, or unstable external behavior and the local boundary or its tests are unclear. |
| [System construction rules](full.md#system-construction-rules) | `134-143` | Startup wiring, dependency injection, factories, cross-cutting mechanisms, or framework bootstrapping obscures ordinary business behavior. |
| [Tests](full.md#tests) | `145-157` | Tests are brittle, noisy, skipped, order-dependent, unclear, coupled to irrelevant implementation, or missing for changed behavior. |
| [TDD and clean test rules](full.md#tdd-and-clean-test-rules) | `159-170` | Behavior can be specified before implementation, test names or data hide intent, repeated setup obscures meaning, coverage substitutes for assertions, or flaky tests remain unresolved. |
| [Concurrency and async work](full.md#concurrency-and-async-work) | `172-186` | Shared mutable state, execution policy, shutdown, cancellation, timeouts, scheduling, thread counts, or timing-sensitive behavior affects correctness. |
| [Refactoring rules](full.md#refactoring-rules) | `188-197` | Structure needs incremental cleanup while preserving behavior, names are weak, duplication appears, or an abstraction no longer earns its cost. |
| [Emergent design and successive refinement](full.md#emergent-design-and-successive-refinement) | `199-205` | A working draft needs refinement, design cleanup tempts a grand redesign, or the proportional stopping point is unclear. |
| [Smells to detect and eliminate](full.md#smells-to-detect-and-eliminate) | `207-240` | A touched area needs a concrete smell diagnosis or the next smallest high-value cleanup has not been identified. |
| [Change Process](full.md#change-process) | `242-253` | A non-trivial change needs a complete intent, localization, testing, validation, and diff-review check. |
| [Implementation preferences](full.md#implementation-preferences) | `255-264` | Choosing among dependencies, optimization, project conventions, interface size, state transitions, or explicit maintainable code shape. |
| [Review checklist](full.md#review-checklist) | `266-279` | Performing a comprehensive final scan of names, function shape, responsibilities, comments, errors, duplication, tests, and complexity. |
| [Output Expectations](full.md#output-expectations) | `281-288` | Reporting completed changes, validation, unresolved risk, assumptions, tradeoffs, or a user-requested conflict with the guidance. |
| [Hard rules](full.md#hard-rules) | `290-297` | A change risks misleading names, unjustified duplication, comments instead of clearer code, query/mutation mixing, silent scope growth, or reduced readability. |
