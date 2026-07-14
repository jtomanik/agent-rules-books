# A Philosophy of Software Design Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit dispute, demonstrated complexity hotspot, or one bounded question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a comprehensive module and API complexity audit or an explicit request for the complete book lens, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-19` | Decide whether complexity reduction, deep modules, information hiding, and strategic design are central rather than incidental to the task. |
| [Primary Directive](full.md#primary-directive) | `21-34` | Arbitrate a disputed design by cognitive load, hidden detail, exception elimination, module depth, and future reader burden. |
| [Core Complexity Rules](full.md#core-complexity-rules) | `36-55` | Diagnose change amplification, cognitive load, unknown unknowns, hidden dependencies, information spread, temporal coupling, or an awkward feature. |
| [Module Depth Rules](full.md#module-depth-rules) | `57-79` | Decide whether a module, wrapper, service, helper, or layer hides enough complexity to justify its interface. |
| [Information Hiding Rules](full.md#information-hiding-rules) | `81-94` | Determine where volatile decisions, representations, workflow bookkeeping, storage, protocol, framework, file-format, normalization, or edge knowledge belongs. |
| [Interface Design Rules](full.md#interface-design-rules) | `96-116` | Resolve a caller-knowledge, semantic guarantee, staged-operation, setup-sequence, flag, mode, or mechanism-leak dispute. |
| [Strategic Programming over Tactical Programming](full.md#strategic-programming-over-tactical-programming) | `118-133` | Judge a deadline patch, recurring friction, local workaround, copy/paste, flag, or exception against future change locality. |
| [General-Purpose vs Special-Purpose Modules](full.md#general-purpose-vs-special-purpose-modules) | `135-142` | Choose the right abstraction level between one-caller overfitting and a vague over-generalized module. |
| [Error Handling and Exception Elimination](full.md#error-handling-and-exception-elimination) | `144-157` | Redesign invalid states, caller defensive ceremony, scattered special cases, half-valid objects, or exceptional-path ownership. |
| [Pull Complexity Downward](full.md#pull-complexity-downward) | `159-168` | Decide whether a more complex implementation should absorb repeated reasoning, flags, setup steps, or coupled operations from callers. |
| [Comment Rules](full.md#comment-rules) | `170-187` | Settle what comments should preserve and whether a comment narrates code or compensates for naming, decomposition, flow, or abstraction defects. |
| [Function and Variable Rules](full.md#function-and-variable-rules) | `189-202` | Review function depth, tiny call chains, pass-through variables, syntax-mirroring names, local details, or exposed intermediate state. |
| [Temporal Decomposition Rules](full.md#temporal-decomposition-rules) | `204-216` | Decide whether prepare/process/finalize phases, initialization, cleanup, staged objects, or call order reflect stable concepts or secret temporal knowledge. |
| [Special-General Decomposition](full.md#special-general-decomposition) | `218-229` | Isolate a small number of unusual cases without polluting the general path with accumulating conditionals. |
| [Combine or Separate Code](full.md#combine-or-separate-code) | `231-244` | Resolve whether a boundary reduces total complexity or instead scatters one idea, invariant, state transition, or design decision across shallow fragments. |
| [Design Alternatives and Comments-First Design](full.md#design-alternatives-and-comments-first-design) | `246-259` | Determine how many plausible designs to compare, which criteria to use, when to sketch public contracts and comments first, or what a complicated explanation signals. |
| [Naming, Consistency, and Obviousness](full.md#naming-consistency-and-obviousness) | `261-269` | Resolve mechanism-revealing names, inconsistent operation conventions, non-obvious behavior, or surprising local code. |
| [Performance, Trends, and Tests](full.md#performance-trends-and-tests) | `271-279` | Decide whether measured performance evidence justifies a design tradeoff, whether a trend reduces local complexity, or whether tests are distorting an interface. |
| [Review Rules](full.md#review-rules) | `281-295` | Run a focused design review for shallow modules, leaking interfaces, flags, scattered cases, interacting modules, temporal constraints, caller burden, comments, or tactical patches. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `297-315` | Classify shallow decomposition, interface leakage, tactical complexity debt, or complexity spread in a disputed design. |
| [Code Generation Rules](full.md#code-generation-rules) | `317-334` | Translate a settled concept boundary, strong interface, hidden detail, caller-simplicity, special-case, or reader-burden decision into code-generation defaults. |
| [Testing Rules](full.md#testing-rules) | `336-343` | Design tests through public contracts and stable APIs for hidden complexity and isolated special cases without coupling callers to implementation details. |
| [Review Checklist](full.md#review-checklist) | `345-359` | Apply the canonical pre-finalization scan for cognitive load, depth, hidden complexity, call-site special cases, public details, pass-through layers, and future changeability. |
| [Final Instruction](full.md#final-instruction) | `361-370` | Arbitrate the final choice by module depth, hidden complexity, special-case reduction, caller cognitive load, and abstraction improvement. |
