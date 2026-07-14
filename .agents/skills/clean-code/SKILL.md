---
name: clean-code
description: Clean Code guidance for locally readable, low-surprise implementation. Use when vague names, mixed responsibilities, boolean modes, hidden mutation, flow-narrating comments, schedule/rewrite pressure, or framework/concurrency detail obstructs a scoped change. Do not add it to an explicit refactoring-only audit or legacy-control task unless a separate local-readability decision is requested.
---

# Clean Code

## Primary Bias

Working code is not automatically clean code.

## Delivery and Proportional Cleanup

- Treat cleanliness as part of delivery. Preserve behavior, leave touched code cleaner within scope, and do not add mess because the schedule is tight or a rewrite is promised.
- When touching code, remove the smell that most increases change cost, but do not silently broaden the task beyond the smallest cleanup that makes the requested change safe.
- When cleanup starts spreading into unrelated areas, cut back to the smallest refactor that keeps the requested change safe and readable.

## Local Reasoning and Names

- Write for local reasoning. A reader should understand the path without reconstructing hidden state, wide jumps, or naming trivia.
- Use precise names and one term per concept. Rename code when vocabulary hides intent, overloads meaning, or forces comments to compensate.

## Functions, State, and Comments

- Keep functions small, focused, and at one level of abstraction. Tell the story top-down so intent appears before detail.
- When a function mixes setup, validation, computation, and side effects, split the phases.
- Keep parameters few and meaningful. Avoid boolean flags, output parameters, and grab-bag argument lists; model the concept instead.
- When a function both mutates and answers, or hides a mode switch behind a flag, separate the responsibilities.
- Separate commands from queries and eliminate hidden side effects. A function that answers should not also mutate behind the reader's back.

Application note: Cache population still mutates. A strict split uses a command that does not return the answer, followed by a nonmutating query; a load-and-return method remains a strong-reason exception, not command-query separation.

- Use comments only for rationale, constraints, warnings, or external contracts. Do not narrate code instead of improving it.
- When a comment explains control flow, simplify names or structure before keeping the comment.

## Errors, Objects, and Boundaries

- Keep the happy path readable. Isolate error handling, invalid-state handling, and cleanup; prefer explicit optionality or typed results over null-like sentinel flow when the language supports it.
- Expose behavior rather than raw representation. Avoid train-wreck access, utility dumping grounds, and classes or modules with mixed responsibilities.
- Keep construction, framework, persistence, transaction, security, and vendor details outside business behavior.
- When a boundary leaks framework, vendor, or persistence quirks inward, add or strengthen a local adapter.
- Make public APIs small, explicit, and hard to misuse. Encode boundary logic, required order, and likely changes where readers can see them.
- When async or concurrency enters, isolate threading policy, minimize shared mutable state, define shutdown, and test timing-sensitive behavior.

## Tests and Emergent Design

- Treat tests as production code: readable, deterministic, aligned with the behavior or contract they protect, and backed by proportionate validation before calling the change done.
- When fixing a bug or changing behavior, add or update the test that protects the intended contract.
- Let design emerge through tests, duplication removal, expressiveness, and minimal structure; do not add needless abstractions or infrastructure.
- When duplication, repeated switches, or primitive clusters appear, name the concept with an argument object, polymorphism, special case, or other small abstraction.

## Reference Map

Use this file alone for ordinary matched work; do not open references merely to confirm its answer.

For an explicit source dispute or bounded detail absent above, open the smallest matching section:

- Vague or misleading names: [Naming rules](references/full.md#naming-rules)
- Function shape, command-query separation, or hidden mutation: [Function rules](references/full.md#function-rules)
- External APIs and framework boundaries: [Boundaries and external dependencies](references/full.md#boundaries-and-external-dependencies)
- Test readability and reliability: [Tests](references/full.md#tests)
- Async state or concurrency structure: [Concurrency and async work](references/full.md#concurrency-and-async-work)
- Non-negotiable interpretation: [Hard rules](references/full.md#hard-rules)

For any other bounded source question, use [the exhaustive index](references/index.md). For an explicit comprehensive audit or complete Clean Code lens, read [the full reference](references/full.md) end to end.

## Final Checklist

- Can a reader follow the change locally?
- Are names and APIs carrying the meaning without narration?
- Is mutation explicit and the happy path still clear?
- Did framework, persistence, vendor, and construction details stay behind boundaries?
- Did I remove at least one smell from the touched area?
- Do tests protect the changed behavior or contract?
- Did I actually run the relevant tests or checks for this change?
