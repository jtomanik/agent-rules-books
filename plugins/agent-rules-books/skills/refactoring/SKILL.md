---
name: refactoring
description: Refactoring guidance for behavior-preserving structural change once observable behavior is known or protected. Use when renaming, extracting, moving, splitting, or another current code smell drives a behavior-preserving change. Dependency-seam work whose purpose is to gain first feedback belongs to Legacy Code until control exists.
---

# Refactoring

## Primary Bias

Refactoring is behavior-preserving design work in small steps. Do not turn cleanup into a rewrite, a hidden feature change, or speculative architecture.

## Preserve Behavior and Control Risk

- Preserve observable behavior during refactoring. Isolate behavior changes from structural changes and never disguise a feature, migration, or redesign as cleanup.
- Work in small, reversible, buildable, testable, reviewable steps. Split a patch when it is too large to reason about locally.
- Establish or identify a safety net before risky refactoring. Use characterization tests for unclear behavior, keep test updates aligned with intended behavior, and never delete a failing test to finish cleanup.
- When fixing a bug in unclear code, characterize the current failure and refactor only enough to make the fix visible before changing behavior.
- When tests are absent or weak, make the smallest possible structural move and improve testability before attempting broader cleanup.

## Sequence and Bound the Change

- Use preparatory and follow-up refactoring around feature work: identify what makes the requested change awkward, reshape that local structure first when useful, make the behavior change, then clean debt introduced by the change.
- When adding behavior, first ask what structural friction blocks the change; refactor before the feature only when it makes the feature safer or simpler.
- Refactor the current blocking smell, not every smell in sight: duplication, long functions, long parameter lists, globals, divergent change, shotgun surgery, feature envy, primitive obsession, repeated conditionals, temporary fields, middle men, or speculative generality.
- Keep patch intent reviewable. Group related refactorings, separate structural edits from behavior where practical, and avoid giant patches that rename, move, redesign, and change logic together.
- When a patch mixes intents or code motion makes review hard, split the change unless context makes that impractical.
- Stop when the requested change is easy, the blocking smell is gone, readability and local changeability are clearly better, and the next cleanup would be speculative.
- When tempted to rewrite, choose the next small behavior-preserving transformation that recovers control.

## Choose Small, Named Moves

- Prefer the simplest named move that helps: rename, extract, inline, move, split meanings, introduce a parameter or value object, encapsulate a field or collection, decompose conditionals, use guard clauses, or substitute a clearer algorithm.
- Make names and functions reveal intent. Rename before deeper work when bad names block understanding; keep functions coherent, at one abstraction level, with tight variable scope and separated phases.
- When a function mixes responsibilities, abstraction levels, phases, or hidden side effects, rename, extract, split phases, or isolate side effects before adding more logic.
- When the same edit appears for a third time, remove duplication through clearer ownership instead of copying again.

## Put Structure Around Ownership

- Put behavior and state with the concept that owns them. Split classes or modules with multiple reasons to change; separate business policy from formatting, transport, persistence, I/O, frameworks, and integration details.
- Keep data, mutation, and call contracts explicit. Avoid behavior-switching boolean flags, confusing argument order, parameter reassignment, exposed mutable collections, unnecessary setters, public fields, and duplicated state-transition logic.
- When one change forces edits across many files, centralize the knowledge or introduce a clearer boundary.
- When UI and domain behavior mix, move rules toward domain objects and verify any required presentation synchronization.

## Simplify with Evidence

- Simplify conditionals honestly. Use guard clauses, extracted predicates, lookup tables, consolidated duplicate fragments, state, strategy, polymorphism, or null objects only when they reduce repeated branching or clarify variation.
- When repeated conditionals or type codes grow, decompose intent first; introduce polymorphism, state, strategy, or a table only when the variation is real.
- Use abstraction and generalization only when current evidence justifies them. Remove pass-through layers, vague utilities, middle men, unused hierarchy, and just-in-case interfaces that do not improve changeability.
- Preserve error semantics unless intentionally changing behavior. Refactor error handling to reveal the main path and consolidate duplicate validation, cleanup, recovery, or error structures.

## Reference Map

Use this file alone for ordinary behavior-preserving structural work; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Refactoring versus behavior change: [What Counts as Refactoring](references/full.md#what-counts-as-refactoring)
- Weak tests or mixed patch intent: [Safety Rules](references/full.md#safety-rules)
- Smell diagnosis and duplication: [Code Smell Policy](references/full.md#code-smell-policy)
- Local transformation choice: [Preferred Refactoring Moves](references/full.md#preferred-refactoring-moves)
- Named catalog technique: [Refactoring Catalog Index](references/full.md#refactoring-catalog-index)
- Conditional structure: [Rules for Working with Conditionals](references/full.md#rules-for-working-with-conditionals)
- Behavior-preserving verification: [Testing Rules](references/full.md#testing-rules)
- Scope and stopping: [Stopping Rules](references/full.md#stopping-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For an explicit comprehensive refactoring audit or complete Fowler lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Observable behavior preserved?
- Structural change, behavior change, and test updates separated where practical?
- Safety net, characterization, or verification gap recorded?
- At least one real source of friction removed?
- Names, responsibilities, control flow, data ownership, and interfaces clearer?
- Patch still reviewable and runnable?
- Cleanup stopped before speculative abstraction or rewrite pressure took over?
