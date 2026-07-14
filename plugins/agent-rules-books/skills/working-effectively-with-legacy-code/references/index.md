# Working Effectively with Legacy Code Reference Index

Use this index to select bounded sections from [full.md](full.md). Each range starts at its level-two heading and ends at the last non-empty line before the next level-two heading or end of file.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-18` | Deciding whether poor understanding, weak tests, dependency knots, or change fear make the area legacy code for this task. |
| [Primary Directive](full.md#primary-directive) | `20-37` | A risky existing-code change needs an order of control, observation, dependency breaking, behavior change, and local improvement. |
| [Non-Negotiable Rules](full.md#non-negotiable-rules) | `39-59` | Rewrite pressure, uncertain behavior, missing seams, hard dependencies, or a failure to improve changeability threatens the task. |
| [Default Workflow for Legacy Changes](full.md#default-workflow-for-legacy-changes) | `61-76` | Planning a specific risky change from affected area and trusted tests through seam, dependency break, behavior change, and local refactor. |
| [Testing Strategy Rules](full.md#testing-strategy-rules) | `78-100` | Choosing characterization versus new-behavior tests, preserving ugly relied-on behavior, or improving testability without distorting production design. |
| [Seam Rules](full.md#seam-rules) | `102-126` | Selecting a substitution, observation, or interception seam and deciding whether it is explicit, durable, correctly placed, and for sensing or separation. |
| [Dependency Breaking Rules](full.md#dependency-breaking-rules) | `128-162` | Hidden inputs, hard outputs, object construction, globals, statics, runtime context, or direct side effects block focused tests. |
| [Test Selection and Understanding Rules](full.md#test-selection-and-understanding-rules) | `164-176` | The change impact is unclear, effects need tracing, or interception points, pinch points, scratch refactoring, or responsibility sketches may help. |
| [Preferred Legacy Techniques](full.md#preferred-legacy-techniques) | `178-206` | Choosing among sprout method/class, wrap method/class, or extract-and-override for a fragile insertion or observation point. |
| [Dependency-Breaking Technique Index](full.md#dependency-breaking-technique-index) | `208-226` | An ordinary seam is unavailable and a language-, object-, build-, hierarchy-, parameter-, global-, or factory-specific dependency break is needed. |
| [Legacy Refactoring Heuristics](full.md#legacy-refactoring-heuristics) | `228-238` | Excessive setup, impossible observation or invocation, mechanism-policy coupling, or unsafe direct edits indicate a smaller local move. |
| [Handling Risky Areas](full.md#handling-risky-areas) | `240-269` | Large methods, globals/statics, database-heavy code, UI/framework handlers, or side-effecting constructors need targeted treatment. |
| [Review Rules](full.md#review-rules) | `271-284` | Reviewing a legacy-oriented patch for missing tests, mixed intent, broad edits, hard collaborators, side-effecting construction, or trapped business logic. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `286-306` | A rewrite-first, edit-and-pray, hidden-dependency expansion, or cosmetic-only cleanup proposal needs rejection or reduction. |
| [Code Generation Rules](full.md#code-generation-rules) | `308-333` | Choosing safe implementation outputs and first moves for a concrete legacy change while avoiding architecture-before-control. |
| [Testing Rules](full.md#testing-rules) | `335-343` | Deciding test speed, level, seam usage, or the balance between focused and real-boundary integration tests. |
| [Review Checklist](full.md#review-checklist) | `345-360` | Running a complete final scan over legacy risk, behavior capture, seams, dependencies, locality, separation, and improved changeability. |
| [Final Instruction](full.md#final-instruction) | `362-371` | Several risky options remain and the deciding criterion should increase understanding, testability, and control with the smallest change. |
