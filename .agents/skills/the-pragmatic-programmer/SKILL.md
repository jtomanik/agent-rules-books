---
name: the-pragmatic-programmer
description: The Pragmatic Programmer guidance for accountable, adaptable delivery. Use when outcome ownership, duplicated knowledge, change fan-out, irreversible commitment, prototype fossilization, manual delivery/feedback loops, or blackboard-style coordination are central across a change. Clean Code owns local readability; Code Complete construction; Refactoring behavior-preserving change; Legacy Code blocked first feedback; Release It! production failure; A Philosophy of Software Design module depth.
---

# The Pragmatic Programmer

## Primary Bias

Do not optimize only for the local edit, requested feature, or familiar ritual. Own the outcome by reducing duplicated knowledge, keeping concerns independent, proving assumptions early, automating repeated work, and making intent clear.

## Accountability and Adaptability

- Be pragmatic, not dogmatic: choose the practice, formality, quality level, and stopping point that improves real outcomes for the users, risks, and codebase.
- Own the result. Surface tradeoffs, risks, uncertainty, and avoidable design costs instead of blaming tools, framework defaults, or existing style.
- Think beyond the local edit: quick fixes that multiply future maintenance cost are usually a bad bargain; leave touched areas better where the cost is low.
- Keep volatile decisions reversible where practical. Avoid irreversible commitments to requirements, vendors, platforms, databases, or deployment environments until evidence makes them worth the cost.
- Dig for real requirements. Separate durable needs and constraints from current implementation details, proposed solutions, growing prose specs, and unresolved team hesitation.
- Break work into small deliverable increments with honest uncertainty, visible risk, and estimates that can be corrected by feedback.
- Communicate through code, names, docs, comments, commit messages, scripts, tests, and artifacts. Use comments for rationale, contracts, or non-obvious behavior, not as substitutes for encoded rules.
- Build pragmatic teams around shared responsibility, explicit expectations, automation, fast feedback, visible quality, and artifacts you are willing to stand behind.
- Apply the broken windows rule: fix or visibly contain small quality decay before it becomes normal.
- When a volatile requirement, vendor, platform, database, or deployment environment is becoming an irreversible commitment, preserve reversibility or delay commitment until evidence justifies it.
- When uncertainty is high or a decision is hard to reverse, reduce risk with tracer feedback, a prototype, a smaller reversible step, or a delayed commitment.
- When prose specifications keep growing without reducing uncertainty, start building a working slice.
- When local decay appears in touched code, fix it if cheap or leave an explicit containment or cleanup path.

## Knowledge Ownership and Orthogonality

- Keep one authoritative representation for each piece of system knowledge. Business rules, validation, status semantics, mappings, calculations, schemas, configuration meaning, and generated output should derive from or trace to one owner; duplicated manual process steps should be automated.
- Preserve orthogonality: keep components independent, responsibilities non-overlapping, interfaces narrow, collaborator knowledge small, and policy, mechanism, data, presentation, orchestration, and computation separated.
- Use domain vocabulary and small domain languages only when they make rules clearer to the people who must validate or change them.
- Prefer inspectable plain text, open formats, scripts, explicit serialization, and version-aware configuration when longevity, diffability, automation, migration, or interoperability matter.
- When the same fact appears in multiple artifacts, choose one owner and derive, generate, or trace the rest.
- When one change requires edits in many unrelated places, repair the missing boundary or hidden coupling before it spreads.

## Feedback and Tool Leverage

- Prefer thin end-to-end tracer bullets over piles of isolated pieces. Keep the first slice simple but real enough to validate architecture, integration, and assumptions.
- Use prototypes to learn, not to pretend the work is done. State what the prototype proves, what it does not prove, and which shortcuts must be discarded or hardened.
- Automate repetitive, error-prone, easy-to-forget, or ritualized work. Builds, tests, linting, formatting, packaging, deployment, setup, validation, and release should be reproducible and aligned with shared automation.
- Shorten feedback loops with relevant tests, automated checks, visible failures, and cheap early signals before late expensive surprises.
- Use tooling as leverage for correctness and speed, but understand generated code, formal methods, specifications, and tool output before relying on them.
- Debug from reproduced facts: reproduce, observe, isolate, explain, fix, and verify instead of guessing.
- When prototype code is becoming production, harden or replace it deliberately; do not rely on generated code, tools, specifications, or formal methods you do not understand.
- When repeated manual steps, human checks, environment rituals, or release procedures appear, automate and version them.
- When tests are slow, flaky, environment-dependent, or require excessive unrelated setup, improve the feedback path rather than normalizing skipped checks.
- When repeated toolchain friction appears, improve the toolchain.
- When code works for reasons nobody can explain, reproduce and observe the behavior before depending on it.

## Contracts, Failure, and State

- Make contracts, assumptions, invariants, responsibilities, and caller/callee obligations explicit and close to the abstraction they protect.
- Distinguish programmer errors, contract violations, impossible states, expected domain failures, retryable failures, recoverable failures, and permanent failures; preserve diagnostic context and fail inside boundaries that prevent wider collapse.
- Treat resource ownership as a contract. Release every acquired allocation, handle, lock, or resource on success and failure paths, preferably opposite acquisition order.
- Treat shared mutable state, ambient context, globals, temporal coupling, and asynchronous complexity as costs that must earn themselves and be made visible.
- When hidden assumptions live only in comments, caller folklore, or tribal setup steps, move them into code, contracts, tests, scripts, or explicit configuration.
- When an error or resource crosses a boundary, decide who can recover, what context survives, and who owns cleanup.
- When shared state, async behavior, locks, ordering, or temporal coupling appears, make ownership, synchronization, cleanup, and ordering requirements explicit.

## Reference Router

Use this file alone for ordinary matched work, and stop when it resolves the task.

For an explicit dispute about pragmatic stopping, named habits, tool use, resource or coupling mechanisms, project testing scope, or one bounded source question left unresolved after applying this file, read [references/index.md](references/index.md), then the smallest relevant sections of [references/full.md](references/full.md).

For a comprehensive audit or an explicit request for the complete book lens, read [references/full.md](references/full.md) end to end.

## Final Checklist

- One authoritative owner for each system fact?
- Unrelated concerns independent and volatile choices reversible?
- Working feedback exists for risky assumptions?
- Prototype, generated, and tool-derived behavior deliberately accepted?
- Contracts, failures, diagnostics, resources, and cleanup explicit?
- State, concurrency, ordering, and coupling visible?
- Repeatable work automated, versioned, and aligned with shared checks?
- Tests automatic, relevant, and run before calling the change done?
- Names, comments, docs, scripts, tests, and commits communicate intent?
- Touched area better or explicitly contained?
