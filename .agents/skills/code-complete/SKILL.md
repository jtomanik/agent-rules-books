---
name: code-complete
description: Code Complete guidance for construction in implementation/change, review, debugging, refactoring, and tuning. Use when nontrivial work coordinates several concerns, or when solution-first coding, happy-path-only tests, mixed behavior/refactoring, guess-driven debugging drives code changes, or evidence-free tuning threatens defect control. It owns construction coordination; labels alone are insufficient, and another lens needs its own explicit objective rather than shared construction vocabulary.
---

# Code Complete

## Primary Bias

Construction quality is not accidental. Do not treat typing code, making it work once, or using a clever idiom as complete construction; choose the option that lowers defect risk and makes the code easier to reason about.

## Construction Context

- Before large construction work, verify that requirements, architecture, major risks, coding conventions, language constraints, error policy, data representation, reuse, integration, and testing approach are clear enough.
- When coding starts from a proposed solution, restate the requirement, architecture fit, risks, conventions, and success constraints before implementation.
- When upstream uncertainty remains, build a small validated slice instead of speculative code, and make expensive-to-reverse decisions deliberately.

## Readable Routines and Data

- Optimize first for human readers: clarity, locality, explicitness, visible control flow, consistent conventions, and practical correctness over cleverness, minimal keystrokes, or fashion.
- For complex routines, sketch precise pseudocode or intent comments at a consistent abstraction level, then convert them into code and keep only comments that still explain intent, constraints, contracts, or rationale.
- Keep routines cohesive, precisely named, small at the interface, and hard to misuse. Separate setup, validation, computation, and side effects when they are conceptually different.
- When a routine is hard to name, mixes phases, has flag arguments, long parameters, or hidden side effects, redesign the interface or split the routine.
- Make variable and data meaning explicit through purpose-revealing names, small scope, deliberate initialization, named constants, stronger types, and visible units or sentinel meanings.
- Choose data types that make invalid or ambiguous values harder to represent; use booleans only for true binary meanings, enumerations for closed sets, and records/maps/tables only when their shape communicates meaning.
- When readers must decode units, ranges, precision, encoding, ownership, status, magic values, or primitive flags, move that meaning into names, constants, types, or structures.

## Inspectable Control and Tables

- Keep control flow simple enough to verify: shallow nesting, named predicates for complex conditions, clear normal path, clear loop initialization/termination/update, and no side-effect-dependent expressions or clever one-liners.
- When branches, loops, exits, or exception paths become hard to verify, simplify before adding logic.
- Use table-driven or data-driven logic for stable explicit mappings only when the table is clearer, obvious, and validated; do not hide complex behavior in inscrutable encodings.
- When repeated branching maps a stable, explicit, configuration-like decision, consider a validated table.

## Boundaries, Errors, and Modules

- Validate input at trust boundaries. Use assertions, invariant checks, and simple contracts for programmer assumptions; use validation or domain errors for expected external or business failures.
- When input crosses a user, file, network, external-system, or other trust boundary, decide what is validated, rejected, recovered from, asserted, and kept diagnosable.
- Handle errors at the right abstraction, preserve diagnostic context, standardize similar failures, keep the normal path readable, and never silently continue from corrupted or impossible state.
- Keep classes and modules focused, cohesive, and bounded by clear contracts; hide representation and internal bookkeeping, and avoid mixed persistence, formatting, business, and integration concerns.
- When a class or module exposes representation, grows into a god object, or mixes unrelated responsibilities, restore the abstraction boundary.
- Treat rising complexity as defect risk: split tangled routines or modules, remove duplication that multiplies maintenance effort, and reduce what a maintainer must keep in working memory.

## Incremental Defect Finding

- Build in small, verifiable increments; integrate often enough to expose conflicts, keep partial work from rotting, and review and improve code during construction.
- Match reviews, inspections, pair work, tests, static checks, and regression tests to defect risk. Debug by reproducing, isolating, explaining, fixing, and verifying root causes rather than guessing.
- When tests cover only the happy path, add normal, boundary, invalid-input, defensive-check, routine-contract, and data-driven edge cases.
- When debugging begins from a guess, first make the failure repeatable, collect evidence, isolate the path, and explain the cause.

## Refactoring, Tuning, and Tools

- Refactor when structure hides intent, duplicates knowledge, or raises defect probability, and keep refactoring separate from behavior change when that improves reviewability.
- When refactoring would mix structural and behavior changes, separate them when that improves reviewability.
- Tune performance only when requirements and evidence justify it; measure before and after, and keep clarity unless an explicit measured tradeoff warrants the cost.
- When performance work begins, verify that requirements and evidence justify it, measure before and after, and document any clarity tradeoff.
- Use tools, scripts, debuggers, profilers, editors, and build automation to reduce error-prone manual work.

## Comments and Standards

- Use layout, comments, documentation, and coding standards to lower reader effort. Prefer self-documenting structure first; comments should explain intent, assumptions, constraints, limitations, usage, or non-obvious facts.
- When comments restate obvious mechanics or go stale, rewrite the code or delete the comment; when code cannot express intent, constraints, or usage, add a close accurate comment.
- When local style starts to diverge, follow shared formatting, naming, file-structure, and idiom conventions instead of creating a module-specific dialect.

## Reference Router

Use this file alone for ordinary matched construction work.

Do not open references merely to confirm, elaborate, or report an implementation recommendation already supported here.

For an explicit dispute about interpreting or applying Code Complete guidance, you must read [references/index.md](references/index.md), then its bounded sections in [references/full.md](references/full.md). Also use that focused route when, after applying this file, you can state one concrete bounded question that the body does not answer.

For a comprehensive construction audit, an explicit request for the complete Code Complete lens, or an unresolved system-level decision whose correctness depends on interactions across several independent concern groups, read [references/full.md](references/full.md) end to end.

## Final Checklist

- Requirements, architecture fit, risks, conventions, and construction approach are clear enough.
- Names, routines, data, classes, layout, comments, and standards reduce reader effort.
- Inputs, errors, assertions, contracts, invariants, impossible states, and trust boundaries are deliberate.
- Control flow, loops, tables, exits, and exception paths are simple enough to inspect.
- Tests, reviews, debugging, refactoring, integration, tooling, and tuning are evidence-based.
- The change is small enough to verify and would stand up to careful review.
