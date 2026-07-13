# Refactoring Reference Index

Use this index to select bounded sections from [full.md](full.md). Each range starts at its level-two heading and ends at the last non-empty line before the next level-two heading or end of file.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-18` | Confirming whether a proposed edit is behavior-preserving refactoring or a behavior change, migration, modernization, or rewrite. |
| [Primary Directive](full.md#primary-directive) | `20-33` | Sequencing structural work around a requested feature or resisting a large rewrite or mixed-intent patch. |
| [What Counts as Refactoring](full.md#what-counts-as-refactoring) | `35-51` | Classifying disputed cleanup, modernization, architecture migration, or broad renaming as refactoring or non-refactoring. |
| [Non-Negotiable Rules](full.md#non-negotiable-rules) | `53-77` | A change may break behavior, leave the system unrunnable, skip preparatory cleanup, or introduce abstraction too early. |
| [Safety Rules](full.md#safety-rules) | `79-102` | Tests are weak, patch intent is mixed, or a feature is awkward enough to need preparatory refactoring. |
| [Code Smell Policy](full.md#code-smell-policy) | `104-156` | Diagnosing which current smell raises change cost and whether similar code is real duplication or coincidental similarity. |
| [Preferred Refactoring Moves](full.md#preferred-refactoring-moves) | `158-189` | Choosing among naming, extraction, movement, simplification, or data refactorings for a known local problem. |
| [Refactoring Catalog Index](full.md#refactoring-catalog-index) | `191-256` | A specific composing-method, feature-movement, data, conditional, call, or generalization technique needs selection guidance. |
| [Function-Level Rules](full.md#function-level-rules) | `258-268` | A function mixes tasks, abstraction levels, hidden effects, phases, broad variable scope, nesting, or dead code. |
| [Class and Module Rules](full.md#class-and-module-rules) | `270-279` | A module has several reasons to change, mixes policy with mechanisms, or is accumulating god-object or utility-module behavior. |
| [Rules for Working with Conditionals](full.md#rules-for-working-with-conditionals) | `281-289` | Repeated type/status branching, nested conditionals, or pressure to introduce tables, predicates, strategies, or polymorphism appears. |
| [Data and Mutation Rules](full.md#data-and-mutation-rules) | `291-299` | Mutation is broad or ad hoc, state transitions are duplicated, or write access and intermediate values obscure reasoning. |
| [Error Handling Rules](full.md#error-handling-rules) | `301-308` | Cleanup, validation, recovery, or duplicated error paths bury the main path, while existing error semantics must remain stable. |
| [Review Rules](full.md#review-rules) | `310-327` | Performing a smell-oriented review of an existing structural change or deciding which friction matters now. |
| [Forbidden Patterns](full.md#forbidden-patterns) | `329-358` | Rewrite, mixed-intent patch, premature abstraction, refactoring theater, or untested structural surgery pressure is present. |
| [Code Generation Rules](full.md#code-generation-rules) | `360-386` | Choosing safe first moves around a requested code change or checking whether a proposed edit sequence is proportionate. |
| [Testing Rules](full.md#testing-rules) | `388-397` | Characterization, externally visible assertions, test updates, implementation coupling, or test refactoring decisions are disputed. |
| [Stopping Rules](full.md#stopping-rules) | `399-408` | Cleanup is expanding and the agent must decide whether the requested change is easy enough and further structure is speculative. |
| [Review Checklist](full.md#review-checklist) | `410-427` | Running a comprehensive final scan over behavior, friction, readability, testability, duplication, patch size, and responsibility. |
| [Final Instruction](full.md#final-instruction) | `429-433` | Several options remain and the deciding criterion should be the next small behavior-preserving transformation. |
