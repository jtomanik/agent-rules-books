---
name: refactoring-guru
description: Refactoring.Guru guidance for code-smell classification, catalog treatment selection, and incomplete-library-class decisions. Use when explicit smell classification, choosing among named techniques and their preconditions or tradeoffs, or deciding how to add missing operations to an external class you cannot modify is central after behavior is known or protected. Refactoring owns ordinary behavior-preserving structural change; Clean Code local readability; Legacy Code first feedback.
---

# Refactoring.Guru

## Primary Bias

Refactoring is not general cleanup or pattern application. It is a small, smell-driven, behavior-preserving treatment with verification and a stop condition.

## Refactoring Scope, Control, and Stopping

- Separate refactoring from feature work and bug fixes; if behavior changes, name it as behavior change and isolate it from structural edits. You should refactor before feature work when existing code is too dirty to understand the change safely or makes the feature awkward, and reshape the local structure so the feature becomes straightforward. You should refactor after feature work when the feature leaves new duplication, awkward names, or unnecessary structure. For bugs, you should clean the structure that allowed the bug to hide when cleanup is small and local. In review, you should fix simple smells immediately when context and ownership allow, estimate and isolate larger smells instead of smuggling them into the reviewed change, and collaborate with the author when a smell needs judgment about intent.
- Diagnose the smell before choosing a technique: symptom, maintenance cost, scope, expected cleaner end state, verification path, and stop condition; check whether the smell is real or only a style preference.
- Prefer the smallest treatment that directly reduces the diagnosed smell; escalate only when the smaller technique is blocked, and reject a treatment if its own tradeoff is worse than the smell.
- Keep the code runnable and understandable through small named transformations rather than broad redesign.
- Before risky refactoring, identify the relevant tests or checks. Run all relevant existing tests after refactoring, and run relevant checks after each risky move, public interface change, state-flow change, or algorithm substitution; diagnose failures as behavior changes, refactoring mistakes, or tests coupled to implementation details, and fix refactoring mistakes before continuing. You should replace or lift brittle low-level tests when they block behavior-preserving structure changes; never delete failing tests to make a refactoring appear successful.
- Refactoring succeeds only if the touched code becomes cleaner; you should pause and re-diagnose when small edits are not improving clarity. Stop when the named smell is gone or materially reduced, before crossing ownership, public API, or feature scope without explicit approval, and when the next improvement needs a different smell diagnosis; record new smells separately unless they block the current change.
- When cleanup keeps expanding, stop at the diagnosed smell and report the next smell separately.
- Use the Rule of Three: tolerate uncertain duplication early and consider refactoring on the third similar occurrence, but do not abstract coincidental similarity before the repeated responsibility is clear.
- Treat technical debt as compounding cost; pay down the debt that slows current change speed, correctness, or team understanding.

## Smell Families and Treatment Choice

- Scan smells by category: bloaters, object-orientation abusers, change preventers, dispensables, couplers, and incomplete library gaps.
- For bloaters, prefer extraction, parameter/data modeling, and responsibility splits before creating method objects, subclasses, or interfaces.
- For switch/type-code smells, isolate the decision first; use polymorphism, subclasses, or state/strategy only when variation is stable and repeated.
- For change preventers, move behavior and data toward the owner of the changing concept so one conceptual change has one main edit site.
- For dispensables, delete or inline unused structure, but check public, generated, reflected, serialized, plugin-facing, and framework extension uses first.
- For couplers, reduce navigation and private knowledge; keep delegating layers only when they hide volatile structure, policy, or a real boundary.
- Use comments for rationale, constraints, contracts, or hard algorithms; use names, variables, methods, or assertions when comments explain unclear code.
- Keep behavior with the data it changes unless separation deliberately supports interchangeable behavior.
- Encapsulation is not finished by adding getters and setters; move behavior inward when callers are still manipulating exposed data.
- Avoid speculative abstractions: do not create parameter objects, interfaces, superclasses, or hierarchy variants without a real concept, shared behavior, or client.

## Transformation Safety and Exceptions

- Preserve public compatibility or provide a transition path when changing signatures, constructors, visibility, type hierarchy, or externally reachable APIs.
- Before extraction or movement, identify inputs, outputs, mutated variables, callers, visibility, construction paths, and invariants.
- Before condition consolidation or algorithm substitution, verify side effects, ordering, truth tables, edge cases, and performance-sensitive behavior.
- Before data reorganization, decide identity, value/reference semantics, mutability, equality, lifecycle ownership, association direction, and synchronization.
- Before generalization changes, prove shared behavior is real; preserve substitutability and avoid inheriting unused behavior.
- Choose exceptions deliberately: a simple conditional, useful comment, intentional strategy separation, small extension point, or clear duplication may be better than a mechanical treatment.

## Catalog Triggers

- When a method needs comments, scrolling, or local-state reconstruction, try `Extract Method`; use `Replace Temp with Query`, `Introduce Parameter Object`, or `Preserve Whole Object` when locals block extraction.
- When a class has multiple reasons to change, use `Extract Class`; use subclass/interface extraction only for stable variants or real client-facing subsets.
- When primitives, arrays, magic numbers, or type codes carry meaning, model the concept only if the model adds naming, validation, behavior, or safer variation handling.
- When a parameter list grows beyond local reasoning, replace derived parameters, preserve a whole object, or introduce a parameter object only for a real recurring concept.
- When the same change requires edits across many files, move methods/fields or extract ownership so the knowledge is centralized.
- When client code navigates object chains, hide the delegate or move behavior closer to the data; do not add pure forwarding.
- When a class mostly forwards, remove the middle man unless it protects boundary policy or volatile structure.
- When a method both queries and mutates, separate query from modifier unless atomic read-modify behavior is the public contract.
- When branches repeat behavior, decompose, consolidate, or move duplicate fragments only after checking side effects and execution order.
- When null checks dominate, introduce a null object only if absence can obey the same interface; keep absence explicit when it is an error.
- When inheritance creates refused bequest or intimacy, push members down or replace inheritance with delegation.
- When deleting dead or speculative code, verify external reachability and test-only access before removal.
- When a library class is incomplete, use a foreign method for one narrow gap and a local extension only for substantial repeated gaps.

## Reference Router

Use this file alone when it resolves smell classification, treatment comparison, risk ordering, verification, and stopping; do not open references merely to confirm or elaborate that answer.

Only when the task explicitly requires source detail absent above - an exact preferred/fallback/risky triad for one smell; a named technique's applicability, tradeoff, safe steps, or verification; incomplete-library-class migration or vendor-update compatibility; or another bounded canonical question - read [references/index.md](references/index.md), then the smallest relevant sections of [references/full.md](references/full.md).

For an explicit complete Refactoring.Guru lens or exhaustive catalog audit, read [references/full.md](references/full.md) end to end.

## Final Checklist

- Is this change clearly refactoring, feature work, or bug fixing?
- Which smell was diagnosed, and what cost did it create?
- Was the smallest suitable treatment used before riskier structure?
- Did behavior stay preserved under relevant checks?
- Did the named smell become materially better?
- Did the change avoid speculative abstraction and mechanical pattern use?
- Were public compatibility, state flow, and ownership checked?
- Is any intentionally untreated smell documented rather than hidden?
