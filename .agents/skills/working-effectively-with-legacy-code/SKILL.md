---
name: working-effectively-with-legacy-code
description: Use only when a semantic change is blocked because current behavior is materially unknown, no trustworthy focused tests exist, or a dependency cannot be observed or substituted. The task must require gaining first feedback before changing behavior. Do not use when observable behavior and operational facts are already supplied, or when first feedback is not blocked.
---

# Working Effectively with Legacy Code

## Primary Bias

Gain control before improving design. Understand current behavior, protect what must stay, create the smallest useful seam, break the dependency that blocks feedback, make the requested change, then leave the area more testable.

## Establish Control Before Design

- Treat any area without trustworthy tests as legacy code; do not start with rewrite or module-wide cleanup unless that is explicitly required or clearly safer.
- Before editing, state the requested behavior change and the current behavior that must remain; characterize uncertain or suspicious behavior instead of silently fixing it.
- When behavior is uncertain, consumers may rely on ugly behavior, or a branch/path is hard to prove, add characterization or another explicit observation path before changing semantics.
- Follow the legacy loop: identify the change point, check existing protection, add characterization where possible, find or create a seam, break the blocking dependency, change behavior, then refactor locally.

## Build Fast, Trustworthy Feedback

- Prefer fast, focused tests around the slice being changed; use broader interception or integration tests only when they are the safest first observation point.
- Choose test points by tracing effects outward from the change point through values, calls, fields, outputs, collaborators, interception points, and pinch points.
- When a large method or class defeats local reasoning, sketch effects, find interception or pinch points, extract pure computation first, and avoid editing many branches at once.

## Create Narrow Seams at Real Barriers

- Use the smallest seam that allows substitution, observation, or interception; make clear whether the seam is for sensing, separation, or both.
- Break dependencies deliberately: expose hidden inputs, hard outputs, hard construction, globals, statics, ambient context, and framework callbacks only where they block testing or safe change.
- When tests require too much setup or a class cannot be instantiated cheaply, break the first real barrier: constructor work, hidden allocation, factory call, global state, static construction, framework object, or hard parameter.
- When time, randomness, environment, thread-local state, current user/request, files, network, process exits, database writes, messages, or control-flow logging block repeatable tests, wrap or inject that boundary.
- When a seam is magical, temporary, public-for-test, subclass-only, link/preprocessor-based, or probe/sensing-variable-based, add a cleanup obligation and remove it once safer structure exists.

## Use the Smallest Safe Technique

- When direct edits are risky, add behavior with sprout method, sprout class, wrap method, wrap class, or extract-and-override style moves, then fold the temporary structure into better design when tests support it.
- Use dependency-breaking techniques according to the actual barrier: adapt narrow parameters, extract interfaces or implementers, parameterize constructors or methods, encapsulate globals, introduce instance delegators, override factories/calls, or use link/preprocessing seams only when ordinary object seams are impractical.
- For hard-to-test methods, split construction from use, extract side effects behind collaborators, carve pure computation first, and isolate policy from runtime, persistence, UI, or framework mechanisms.
- When changing database-heavy, UI, framework, or API-boundary code, separate policy from query/mapping/persistence, handlers/callbacks, adapters, and runtime setup; keep real-boundary integration tests where they matter.

## Keep Change Local and Honest

- Keep behavior changes, structural refactorings, and cleanup separate; verify small steps and avoid checking in exploratory restructuring used only for understanding.
- In large code, sketch effects and group responsibilities before moving behavior; let excessive setup, impossible observation, and repeated changes point to smaller extracted responsibilities.
- When repeated edits cluster across several places, remove duplication incrementally under tests instead of launching a broad redesign.
- When rewrite or heroic cleanup feels tempting, choose the smallest sprout, wrap, seam, characterization, or refactoring step that makes today's requested change safer.

## Leave Lasting Changeability

- During review, treat no tests around modified logic, mixed structural and behavioral edits, broad edits in poorly understood modules, hard-coded collaborators, global/static reach-through, constructor side effects, and business logic trapped in framework entry points as legacy-change risks.
- Reject changes that expand hidden dependencies, mock around untestable structure without improving it, rename or format while leaving the real dependency knots intact, or introduce large architecture before basic seams exist.
- Leave the touched area easier to understand, test, or change; do not mistake test-only seams, wrappers, subclass tricks, or build tricks for design improvement by themselves.

## Reference Router

Use this file alone for ordinary safe changes in poorly understood or weakly tested code.

For a focused ambiguity about characterization, test points, seam purpose, dependency-breaking technique, or a risky runtime boundary, read [references/index.md](references/index.md), then read the sections it identifies in [references/full.md](references/full.md).

For a comprehensive legacy-change audit, an explicit request for the complete Feathers lens, or a decision involving several interacting change points, seams, dependencies, and test strategies, read [references/full.md](references/full.md) end to end.

## Final Checklist

- Untested or weakly tested area treated as legacy risk?
- Behavior delta and behavior-to-preserve stated?
- Uncertain current behavior characterized or explicitly observed?
- Tests close enough and fast enough to diagnose the change?
- Smallest useful seam chosen, with sensing vs separation clear?
- Blocking dependency reduced without expanding hidden dependencies?
- Behavior change, refactoring, and cleanup kept separate?
- Temporary seam or dependency-breaking trick has a cleanup path?
- Touched area is more understandable, testable, or changeable?
