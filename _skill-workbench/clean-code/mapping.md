# Clean Code Skill Mapping

## Scope

- Distinctive lens: make working code locally readable, low-surprise, and easier to change by clarifying names, function shape, mutation, boundaries, tests, and proportional cleanup.
- Intended invocation: invoke `clean-code` when local readability and code shape are central to implementation or review, or when nano-derived symptoms expose vague names, mixed responsibilities, boolean modes, hidden mutation, flow-narrating comments, schedule/rewrite pressure, or technical leakage that obstructs a scoped change.
- Positive boundary: do not invoke it merely because a task involves existing code, review, refactoring, testing, maintainability, architecture, legacy code, or production behavior. Do not add it to an explicit refactoring-only audit or legacy-control task unless that task separately asks for a local-readability decision.
- Closest neighboring skills: `a-philosophy-of-software-design` for module depth and information hiding; `code-complete` for broad construction discipline; `refactoring` and `refactoring-guru` for behavior-preserving transformation mechanics; `working-effectively-with-legacy-code` for characterization and seams; `clean-architecture` for policy independence and dependency direction; `release-it` for production failure semantics; `the-pragmatic-programmer` for broad engineering operating style.
- Leading vocabulary: Clean Code, local reasoning, low surprise, intention-revealing names, command-query separation, happy path, Boy Scout Rule, and proportional cleanup.
- Invocation policy: model-invoked with `policy.allow_implicit_invocation: true`; autonomous selection is required for code symptoms discovered without an explicit book name.
- Canonical inputs: `clean-code/clean-code.md`, `clean-code/clean-code.mini.md`, `clean-code/clean-code.nano.md`, and `_rule-workbench/clean-code/traceability.md`.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Capability and scope | `Clean Code guidance for locally readable, low-surprise implementation` and `obstructs a scoped change` | Generic coding or review requests; broad `code-complete` construction discipline; broad `the-pragmatic-programmer` operating style. |
| Naming and intent | `vague names` | Domain-language modeling in DDD skills; naming invokes Clean Code because local implementation meaning is hidden, not because a domain model or Bounded Context is being designed. |
| Function shape and mutation | `mixed responsibilities, boolean modes, hidden mutation` | `refactoring` supplies behavior-preserving transformation mechanics; Clean Code identifies the target local shape and makes mode/mutation symptoms explicit. |
| Comments and structure | `flow-narrating comments` | Rationale and contract documentation in APoSD-style guidance; this branch fires when comments compensate for unclear flow or names. |
| Delivery pressure | `schedule/rewrite pressure` | Generic deadline planning and Refactoring's rewrite boundary; Clean Code fires when pressure is being used to justify new local mess in the touched area. |
| Technical leakage into local reasoning | `framework/concurrency detail obstructs a scoped change` | `clean-architecture` policy independence, `release-it` production failure behavior, and DDIA data semantics; Clean Code owns local readability and visible code shape. |
| Refactoring/legacy exclusion | `Do not add it to an explicit refactoring-only audit or legacy-control task unless a separate local-readability decision is requested` | Prevents Clean Code from being selected merely because Refactoring or Legacy work later touches code; a distinct local-shape decision is required. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Apply the complete Clean Code lens to this module." | `clean-code` | Direct book invocation; comprehensive routing must read `full.md` end to end. |
| "These names hide intent, this boolean selects two modes, and the comment explains the branch. Clean this up locally." | `clean-code` | Distinctive nano symptoms and explicit local scope. |
| "Make this function easier to follow without widening the ticket." | `clean-code` | Local reasoning and proportional cleanup are central. |
| "Refactor this method without changing observable behavior, using small reversible steps." | `refactoring` | Transformation safety and sequencing are central; Clean Code is optional only if a local readability target is also stated. |
| "This untested legacy service is impossible to instantiate; characterize it and create a seam before changing behavior." | `working-effectively-with-legacy-code` | Weak feedback and dependency breaking dominate; Clean Code applies only inside the controlled area afterward. |
| "Should these helpers become one deep module with a smaller interface?" | `a-philosophy-of-software-design` | Module depth and information hiding arbitrate the design, including possible tension with small-function pressure. |
| "Add bounded retries, timeouts, bulkheads, and production diagnostics to this outbound call." | `release-it` | Failure semantics and operational resilience dominate, not local code shape. |
| "Move business policy out of the ORM so dependencies point inward." | `clean-architecture` | Policy independence and dependency direction dominate; Clean Code may co-invoke only for local readability work. |
| "Rename the confusing retry state and simplify its mutation while adding bounded retry behavior." | `clean-code`, `release-it` | Local intent/mutation and production failure behavior are both central and complementary. |
| "Reshape this well-tested method toward intention-revealing names without changing behavior." | `refactoring`, `clean-code` | Refactoring governs safe structural change; Clean Code supplies the target local shape. |
| "Implement the ticket and review the PR." | none of the book skills from wording alone | Generic implementation/review language does not identify a distinctive book lens. |
| "Model the Order aggregate and its invariants in the Sales bounded context." | a DDD skill, not `clean-code` | Domain language, lifecycle, invariants, and context boundaries dominate. |

## Catalog Term Overlap

| Shared term | Clean Code meaning | Neighbor boundary |
| --- | --- | --- |
| Readability | Local followability through names, function shape, visible mutation, and a clear happy path. | APoSD optimizes total cognitive load through deep modules; Code Complete covers broader construction quality. |
| Refactoring | The target is cleaner touched code and the smallest smell-reducing cleanup within scope. | Refactoring skills govern behavior-preserving sequence, technique choice, safety nets, and stop conditions. |
| Tests | Tests are readable production code and proportionate validation protects changed behavior. | Legacy Code emphasizes characterization/seams; Refactoring emphasizes safety nets; Release It emphasizes production failure tests. |
| Boundaries | Local adapters keep framework, persistence, vendor, and construction details from obscuring business behavior. | Clean Architecture governs policy dependency direction; PoEAA governs enterprise pattern forces; DDIA governs data semantics. |
| Concurrency | Keep execution policy isolated, shared mutation small, shutdown explicit, and timing-sensitive behavior tested. | Release It governs overload and failure isolation; DDIA governs distributed consistency, ordering, and ownership. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description; early-guidance | Description's schedule/rewrite branch; `Delivery and Proportional Cleanup` | Promotes complete `M1` and exposes the no-new-mess delivery pressure as an invocation signal. |
| `N2` | description; early-guidance; final-check | Description; `Local Reasoning and Names`; first two checklist items | Supplies the local-reasoning capability and naming branch; checklist repetition is a non-authoritative scan. |
| `N3` | description; early-guidance; final-check | Description's mixed-responsibility, boolean-mode, and hidden-mutation branches; `Functions, State, and Comments`; mutation checklist item | Promotes complete function, flag, abstraction-level, and side-effect guidance from `M4`-`M6`, `M15`, and `M17`. |
| `N4` | description; early-guidance; final-check | Description's boolean-mode and hidden-mutation branches; `Functions, State, and Comments`; mutation checklist item | Preserved through complete `M5` and `M6`; not duplicated as a separate authoritative rule. |
| `N5` | early-guidance; reference-router; final-check | `Errors, Objects, and Boundaries`; focused `Error handling` route; mutation/happy-path checklist item | Keeps invalid states, errors, and cleanup explicit through complete `M7`. |
| `N6` | description; early-guidance; final-check | Description; `Functions, State, and Comments`; names/APIs-without-narration checklist item | The comment symptom invokes the skill; complete `M11` and `M16` remain colocated. |
| `N7` | description; early-guidance; reference-router; final-check | Description's scoped-change and schedule/rewrite branch; `Delivery and Proportional Cleanup`; `Smells`, `Refactoring`, and `Emergent design` routes; smell checklist item | Preserves the Boy Scout pressure and its proportional scope guard through `M14` and `M22`. |
| `N8` | description; early-guidance; final-check | Description's hidden-mutation branch; `Functions, State, and Comments`; mutation checklist item | Complete `M17` includes the command/query and mode-switch context. |
| `N9` | description; early-guidance; final-check | Description's comment branch; `Functions, State, and Comments`; names/APIs-without-narration checklist item | Complete `M16` sits directly after the authoritative comment rule. |
| `N10` | description; early-guidance; reference-router; final-check | Description's technical-leakage branch; `Errors, Objects, and Boundaries`; boundary and concurrency index routes; boundary checklist item | Complete boundary `M9`/`M19` and concurrency `M20` guidance are adjacent in one concern group, not split into priority buckets. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Delivery and Proportional Cleanup` | Moved unchanged and promoted first by `N1`. | Authoritative delivery rule; behavior preservation and schedule/rewrite pressure remain intact. |
| `M2` | `Local Reasoning and Names` | Moved unchanged. | Restated non-authoritatively by the first final-check item. |
| `M3` | `Local Reasoning and Names` | Moved unchanged. | Restated non-authoritatively by the names/APIs checklist item. |
| `M4` | `Functions, State, and Comments` | Moved unchanged. | Kept directly beside mixed-phase trigger `M15`. |
| `M5` | `Functions, State, and Comments` | Moved unchanged. | Kept directly beside mode-switch trigger `M17`. |
| `M6` | `Functions, State, and Comments` | Moved unchanged. | Restated non-authoritatively by the mutation checklist item. |
| `M7` | `Errors, Objects, and Boundaries` | Moved unchanged. | Restated non-authoritatively by the happy-path checklist item. |
| `M8` | `Errors, Objects, and Boundaries` | Moved unchanged. | Representation and responsibility guidance stays with API and boundary concerns. |
| `M9` | `Errors, Objects, and Boundaries` | Moved unchanged. | Kept directly beside leakage trigger `M19`; restated by the boundary checklist item. |
| `M10` | `Errors, Objects, and Boundaries` | Moved unchanged. | API misuse, order, and change visibility remain explicit. |
| `M11` | `Functions, State, and Comments` | Moved unchanged. | Kept directly beside explanatory-comment trigger `M16`. |
| `M12` | `Tests and Emergent Design` | Moved unchanged. | Restated non-authoritatively by the two test checklist items. |
| `M13` | `Tests and Emergent Design` | Moved unchanged. | Kept beside `M18` so small abstractions are balanced against needless infrastructure. |
| `M14` | `Delivery and Proportional Cleanup` | Moved unchanged and promoted by `N7`. | Restated non-authoritatively by the smell checklist item. |
| `M15` | `Functions, State, and Comments` | Moved unchanged. | Colocated immediately after complete function-shape rule `M4`. |
| `M16` | `Functions, State, and Comments` | Moved unchanged. | Colocated immediately after complete comment rule `M11`. |
| `M17` | `Functions, State, and Comments` | Moved unchanged. | Colocated immediately after parameter/mode modeling rule `M5` and before command/query rule `M6`. |
| `M18` | `Tests and Emergent Design` | Moved unchanged. | Colocated with emergent-design rule `M13` to preserve the abstraction tradeoff. |
| `M19` | `Errors, Objects, and Boundaries` | Moved unchanged. | Colocated immediately after technical-detail boundary rule `M9`. |
| `M20` | `Errors, Objects, and Boundaries` | Moved unchanged. | Concurrency remains a boundary/ownership concern and retains shutdown plus test pressure. |
| `M21` | `Tests and Emergent Design` | Moved unchanged. | Colocated immediately after complete test-quality rule `M12`. |
| `M22` | `Delivery and Proportional Cleanup` | Moved unchanged. | Colocated with `M14` as its active scope-growth trigger. |

## Wording Fidelity

- Verbatim mini rules: every authoritative `M1`-`M22` sentence appears exactly once in `SKILL.md` with the original wording from `clean-code/clean-code.mini.md`.
- Verbatim primary bias: exact.
- Verbatim final checklist and order: all seven items exact and in source order.
- Reworded mini rules: none.
- Faithful mini-rule merges: none.
- Authored command-query clarification: `Application note: Cache population still mutates. A strict split uses a command that does not return the answer, followed by a nonmutating query; a load-and-return method remains a strong-reason exception, not command-query separation.` This is a non-authoritative application note supported by exact `M6`, full `Function rules`, and the `without a strong reason` qualifier in full `Hard rules`; it does not replace or reword a mini rule.
- Authored focused-router narrowing: ordinary matched work now stays in `SKILL.md`; index/full loading requires `a disputed interpretation or a decision the guidance above does not resolve`. This is navigation metadata implementing progressive disclosure, not an additional Clean Code rule. It replaces the broader `ambiguity or hotspot` condition that caused ordinary E1b over-reading.
- Nano handling: no `N*` item is installed as a second authoritative rule. Nano wording is distilled into invocation metadata, salience, reference routing, and the existing final checklist as recorded above.
- Authored text outside the mini inventory: the frontmatter description, concern headings, primary-bias heading, command-query application note, reference router, and reference-index conditions provide skill packaging, disambiguation, and navigation; they do not replace or alter any `M*` rule.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Inline reference map: six source-backed labels link common focused questions directly to canonical full headings; every other bounded question still uses the exhaustive index. This changes loading only.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 582 words.
- `SKILL.md`: 767 words across 75 lines.
- Packaging overhead: 185 words.
- Frontmatter description: 393 characters, excluding the terminating newline.
- Decision: retain the source-driven exception. The canonical mini already exceeds the 500-word target, every mini rule remains required for complete ordinary use, and the 35-word soft-target overage provides six direct source-detail routes without duplicating the exhaustive index. Do not paraphrase rules during conversion to reduce this count.

## Behavioral Scenarios

| Scenario | Expected invocation | Expected guidance | Reference behavior |
| --- | --- | --- | --- |
| Explicitly request the complete Clean Code lens for a module. | `clean-code` alone. | Apply all concern groups and final scan. | Read `references/full.md` end to end. |
| Rename vague concepts, remove a boolean mode, and replace a flow-narrating comment in one function. | `clean-code` alone. | Apply local naming, function, mutation, and comment guidance without expanding scope. | Ordinary use unless a rule is disputed. |
| Under schedule pressure, add another conditional to a mixed-responsibility function because a rewrite is planned next quarter. | `clean-code` alone. | Reject new mess, split only the necessary phase, preserve behavior, and keep cleanup proportional. | Ordinary use. |
| Ask only to implement a routine ticket or review a PR. | No book skill from prompt wording alone. | Follow repository guidance; do not inject a generic Clean Code review. | Load nothing unless distinctive symptoms become central. |
| Reshape a well-tested method without changing behavior. | `refactoring`; add `clean-code` only when local readability is an explicit target. | Refactoring controls sequence; Clean Code defines the target shape. | Ordinary Clean Code use if co-invoked. |
| Change behavior in weakly tested, dependency-bound legacy code. | `working-effectively-with-legacy-code`; not initially `clean-code` unless local hygiene is also central. | Characterize and create a seam before Clean Code cleanup. | No Clean Code reference until a controlled local hotspot exists. |
| Decide whether several small helpers should become one deep module. | `a-philosophy-of-software-design`, not `clean-code`. | Let module depth and information hiding arbitrate decomposition. | No Clean Code reference. |
| Add retries, timeouts, overload controls, and production diagnostics. | `release-it`, not `clean-code` unless local readability symptoms are also explicit. | Production failure semantics dominate. | No Clean Code reference for a purely operational task. |
| Simplify confusing retry state while adding bounded retry behavior. | `clean-code` and `release-it`. | Clean Code governs local state clarity; Release It governs retry safety and failure behavior. | Ordinary Clean Code use; Release It may route independently. |
| Resolve whether a function that mutates and answers violates the guidance. | `clean-code`. | Apply command-query separation and explicit mutation. | Focused: index, then `Function rules` and `Hard rules`. |
| Review all Clean Code implications of a cross-cutting rewrite. | `clean-code` plus any independently triggered neighboring lenses. | Apply the full book without flattening interactions into the mini summary. | Comprehensive: read `full.md` end to end. |
| Review an async function where framework callbacks spread state and hide cleanup. | `clean-code`; pair with a specialized skill only if production or distributed semantics are central. | Isolate policy, minimize shared mutation, expose shutdown/cleanup, and strengthen the local boundary. | Focused: `Concurrency and async work`, `Error handling`, and `Boundaries and external dependencies`. |

## Evaluation Retrofit Cases

The case files below contain only verbatim tasks and raw code. Selection, routing, behavioral, and source expectations live only in this mapping. Baselines are retroactive because the pilot skill existed before the current evaluation protocol. Every RED and GREEN pair uses `gpt-5.4`, the shared runner, and matching runner configuration.

### E1: Local Readability Under Schedule and Rewrite Pressure

- Class: distinctive symptom recognition; application; pressure; broad high-frequency stability.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/local-readability-pressure.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}` because the requested behavior-preserving local reshape may justify transformation guidance.
- Forbidden skills: `{release-it, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: none; `clean-code` must remain the source of the target local shape if `refactoring` is also selected.
- Reference mode: `ordinary`.
- Expected sections: none; `SKILL.md` should be sufficient.
- Forbidden sections: every section of `clean-code/references/full.md`; loading the index or full reference would over-disclose for this ordinary case.
- Baseline runs: `019f5335-9706-70d1-9294-e697637c24c6` and `019f5337-4a49-7b60-9f3c-f100349ebee1` extracted only a pure discount helper; `019f5336-a291-7fb0-b9e2-24356f1d6ddc` followed the pressure to add another inline branch. All three preserved collaborator effects and added threshold tests, but all three left the boolean modes, mixed command/query shape, hidden state, vague parameter names, and narrating comment unchanged. This is the retroactive RED: the default answer was useful but unstable under pressure and omitted the nano-salient local-shape cleanup.
- Before-routing-fix runs: `019f5346-5692-7250-8ecd-61e457445646` selected `{working-effectively-with-legacy-code, refactoring}`; `019f5347-49ba-7550-8960-ef289a9f403f` selected `{working-effectively-with-legacy-code}`; `019f5348-1dd2-7d21-8db6-987acbae500c` selected `{working-effectively-with-legacy-code, refactoring}`. All reported `ordinary` mode and only `.agents/skills/...` paths. `clean-code` was selected `0/3`; forbidden Legacy Code was selected `3/3`. Preserved as `green-before-routing-fix-1.json` through `-3.json`.
- Before-final-boundary-fix runs: `019f5354-30bd-7783-ba33-16ae5cef9ede` selected `{clean-code}` in `focused` mode; `019f5355-3ad6-7543-a812-f467c9d1ae1a` selected `{clean-code, refactoring}` in `ordinary` mode; `019f5356-3ef7-7153-9745-f031b11de861` selected `{clean-code}` in `focused` mode. All consulted only `.agents/skills/...` paths. Required Clean Code improved from `0/3` to `3/3`; forbidden Legacy Code improved from `3/3` to `0/3`; the allowed Refactoring lens appeared once. Preserved as `green-before-final-boundary-fix-1.json` through `-3.json`.
- Before-router-narrowing runs: `019f5363-ebdc-7532-8745-a347f3b82db2` selected `{clean-code, refactoring}` in `ordinary` mode; `019f5364-d8a2-7113-8e28-aa5f189f2c8d` selected `{clean-code}` in `focused` mode; `019f5365-a16d-7663-b5b0-8deef9cc9a49` selected `{clean-code, refactoring}` in `ordinary` mode. All consulted only `.agents/skills/...` paths. Required Clean Code and forbidden-skill stability pass `3/3`. Preserved as `green-before-router-narrowing-1.json` through `-3.json`.
- Router-narrowed runs: `019f536f-34c0-77f0-b3fe-2f8a8db59576` selected `{clean-code, refactoring}` in `focused` mode; `019f5370-2a1f-7e73-825c-4587c6130ffd` selected `{clean-code}` in `focused` mode; `019f5371-38e6-7fe1-99b4-87ed82d34988` selected `{clean-code, refactoring}` in `ordinary` mode. Required Clean Code and forbidden-skill stability pass `3/3`; every consulted path is packaged.
- Behavioral delta: compared with RED, GREEN must consistently reject the schedule and promised-rewrite excuse for adding another branch, preserve existing behavior and the public boundary, extract only the smallest cohesive discount/command-query cleanup needed for the rule, avoid a broad rewrite, and require focused tests for the changed rule plus existing effects.
- Before-fix observed delta: GREEN made the helper extraction stable at `3/3`, but attributed the result to Legacy/Refactoring guidance and reproduced the baseline boundary. None of the runs removed or made explicit the boolean modes, command/query mixing, hidden mutation, vague names, or narrating comment. The required Clean Code-specific change did not occur.
- After-fix observed delta: catalog discovery is stable and correctly owned. G3 additionally renamed `a`, `i`, and `d` and removed the narrating comment. All three still scoped out or left intact the triggered boolean modes and the method's command/query mixing; G1 and G3 also over-disclosed focused references for an ordinary case. The predeclared application and disclosure contracts therefore remain unmet.
- Final review rule: by explicit user direction, apply source rule `M14` proportionally. E1 does not require every visible smell to be fixed when the answer chooses the highest-value local cleanup, preserves behavior, and explicitly keeps remaining smells out of scope. The original strict application/disclosure failures above remain frozen; E1b replaces E1 as the current ordinary-disclosure proof.
- Final-boundary observed delta: all three answers isolate discount calculation from persistence/email/audit effects, preserve current collaborator behavior, add focused tests, reject a rewrite, and state explicit stop conditions. G2 and G3 also improve touched naming. Under proportional `M14`/`M22`, application passes `3/3`; two ordinary and one focused run are recorded but no longer used as the current ordinary gate.
- Router-narrowed observed delta: pressure/application behavior remains stable `3/3`. G1/G2 use focused Clean references because they identify the unresolved partner/high-total precedence decision; G3 remains ordinary. This is consistent with the narrowed router and does not substitute for E1b's ordinary proof.

Before-fix reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Limit the patch to a small discount seam and reject a service rewrite. | G1-G3 | Legacy Code `Create Narrow Seams at Real Barriers` and `Keep Change Local and Honest`; Refactoring `Sequence and Bound the Change` in G1/G3. No Clean Code package was consulted. |
| Characterize or preserve current discount and collaborator behavior before changing the rule. | G1-G3 | Legacy Code `Establish Control Before Design` and `Build Fast, Trustworthy Feedback`; Refactoring `Preserve Behavior and Control Risk` in G1/G3. |
| Extract a pure `discountFor`/`calculateDiscount` helper. | G1-G3 | Legacy Code `Use the Smallest Safe Technique` (carve pure computation first); Refactoring `Choose Small, Named Moves` where consulted. |
| Keep structural work separate from the partner behavior change and stop before broader cleanup. | G1-G3 | Legacy Code `Keep Change Local and Honest`; Refactoring `Preserve Behavior and Control Risk` and `Sequence and Bound the Change` where consulted. |
| Treat the existing `> 1000` discount as additive for partners and use the listed threshold matrix. | G1-G3 | Task-specific general judgment plus the prompt's preserve-existing-behavior constraint; neither consulted book determines the product rule. |
| Leave the boolean flags, command/query mixing, hidden mutation, names, and comment untouched. | G1-G3 | Scope choice supported by Legacy/Refactoring proportionality, but it omits the predeclared Clean Code target rather than satisfying it. |

After-fix reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Use a bounded discount-helper extraction rather than another inline branch or service rewrite. | G1-G3 | Clean `M1`, `M4`, `M14`, `M15`, `M22`; Refactoring `Sequence and Bound the Change` and `Choose Small, Named Moves` in G2. |
| Preserve collaborator ordering and add targeted behavior/side-effect tests before shipping. | G1-G3 | Clean `M12`, `M21`, final validation checklist; Refactoring safety-net guidance in G2. Exact threshold cases use task-specific general judgment. |
| Rename vague locals and remove the narrating comment. | G3 | Clean `M3`, `M11`, `M16`, `N2`, `N6`, and `N9`. |
| Interpret partner/high-total discount interaction. | G1-G3 | Task-specific general judgment. G1/G2 preserved additive behavior; G3 treated exact `15%` as the likely reading and asked for clarification. The book does not settle the product rule. |
| Explicitly leave boolean modes and command/query mixing out of scope, or leave them unchanged. | G1-G3 | Proportionality is supported by `M14`/`M22`, but this outcome conflicts with triggered `M5`, `M6`, and `M17` and fails the case's predeclared target. |

Final-boundary reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Isolate discount calculation as the highest-value local cleanup instead of adding another branch or starting a rewrite. | G1-G3 | Clean `M1`, `M4`, `M14`, `M15`, `M22`; Refactoring `Sequence and Bound the Change` and `Choose Small, Named Moves` in G1/G3. |
| Preserve public/collaborator behavior and keep other smells explicitly out of scope. | G1-G3 | Clean `M1`, `M14`, `M22`; Refactoring behavior-preservation guidance where selected. This is accepted proportionally rather than requiring every `M5`/`M6`/`M17` smell to be removed. |
| Improve touched discount and parameter names. | G2/G3 | Clean `M3`, `N2`; G1 still improves `d` to `discount` inside the extracted helper. |
| Add partner-threshold, preview, side-effect, and unchanged-path tests. | G1-G3 | Clean `M12`, `M21`, final checklist; exact cases use task-specific general judgment. |
| Decide whether the high-total rule stacks for partners. | G1-G3 | Task-specific general judgment, explicitly presented as an assumption/clarification rather than book guidance. |

Router-narrowed reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Extract the pricing decision as the highest-value local cleanup and reject branch/rewrite pressure. | G1-G3 | Clean `M1`, `M4`, `M14`, `M15`, `M22`; Refactoring named-move and scope guidance in G1/G3. |
| Preserve preview, persistence, email, audit, and return behavior while limiting scope. | G1-G3 | Clean `M1`, `M12`, `M14`, `M21`, `M22`; Refactoring behavior preservation where selected. |
| Make discount precedence explicit and test the `500`/`1000` interaction. | G1-G3 | Task-specific general judgment plus Clean test guidance; G1 explicitly requests clarification, while G2/G3 choose additive preservation. |
| Keep broader flags, interfaces, and redesign out of the release patch. | G1-G3 | Proportional Clean `M14`/`M22` and Refactoring stopping guidance where selected. |

- Frozen result: **original E1 ordinary/application contract failed** and remains preserved across its earlier generations.
- Current result: **pass for E1's pressure discovery and proportional application role**. Clean ownership and forbidden-skill stability pass `3/3`; focused reads occur only where the solver identifies the unresolved product decision; E1b owns ordinary-disclosure acceptance.

### E1b: Ordinary Local Hygiene

- Contract status: predeclared before any baseline or GREEN execution.
- Class: ordinary application; distinctive local-hygiene recognition; stability.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/ordinary-local-hygiene.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{refactoring}` only when the solver treats behavior-preserving structural change as central; Clean Code must still supply the target local shape.
- Forbidden skills: `{working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: none; if selected, Refactoring must not displace Clean Code ownership.
- Reference mode: `ordinary`.
- Expected sections: none; the Clean Code body is complete for this local task.
- Forbidden sections: every full-reference section for every book skill; loading an index or full reference would over-disclose.
- Baseline runs: `019f5362-3c1c-7a62-b555-48bcd57522ca`, `019f5362-cc54-7d70-8bf6-2b8576eae0d9`, and `019f5363-51e0-7382-aa18-2073ae347bd7`. All three independently produced the same direct normalization/return rewrite, preserved the signature and exact strings, removed temporary mutation/comment narration through structure, and stopped before abstraction. There is no semantic RED; the control establishes a high default and makes catalog/disclosure stability the purpose of this case.
- Before-router-narrowing runs: `019f5367-9f49-7ca1-873d-11fa28582649` selected `{clean-code, refactoring}` in `ordinary` mode; `019f5368-408d-7c41-8a0d-470f510d2be0` selected `{clean-code, refactoring}` in `focused` mode and opened Refactoring index/full references; `019f5369-2b6f-78b1-a98e-bc4ffd3d3a00` selected `{clean-code}` in `ordinary` mode. Required Clean Code passes `3/3`; both forbidden skills remain absent `3/3`; all consulted paths are packaged. Preserved as `green-before-router-narrowing-1.json` through `-3.json`.
- Router-narrowed runs: `019f5372-681e-79b0-8104-48d54487cb7c` selected `{clean-code, refactoring}` in `ordinary` mode; `019f5373-166f-7282-ae7f-763259f166b5` selected `{clean-code}` in `ordinary` mode; `019f5373-ada5-7be1-97a0-fcf251ed8618` selected `{clean-code, refactoring}` in `ordinary` mode. Required Clean Code, forbidden-skill exclusion, package isolation, and ordinary disclosure all pass `3/3`.
- Behavioral delta: compared with baseline, GREEN should apply a stable Clean Code lens to the highest-value local cleanup, use intention-revealing names and simpler top-down structure, remove the flow-narrating comment when structure makes it unnecessary, preserve the exact public signature and output contract, avoid speculative abstraction, and state a proportional stopping boundary. It need not remove every smell when one coherent local cleanup makes the helper readable.
- Before-narrowing observed delta: semantic output remains deliberately similar to the already-strong baseline, while GREEN grounds the decision in Clean Code and consistently explains why the fixed boolean signature should not trigger API redesign. Application and catalog ownership pass `3/3`. Ordinary disclosure passes `2/3`; G2 over-discloses Refactoring references despite no focused ambiguity or request.
- Router-narrowed observed delta: semantic application remains stable while all three runs stay body-only and ordinary. The router no longer treats this local cleanup as a reason to open index/full references.
- Source trace contract: local reasoning and names -> `M2`, `M3`, `N2`; focused function shape -> `M4`, `M15`, `N3`; fixed boolean signature versus internal readability -> `M5`, `M17` constrained by the explicit compatibility boundary; comment removal -> `M11`, `M16`, `N6`, `N9`; minimal/proportional design -> `M13`, `M14`, `M22`, `N7`; tests -> `M12` and the final checklist.

Before-router-narrowing reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Normalize first/last/nickname once and express the two output shapes directly. | G1-G3 | Clean `M2`, `M3`, `M4`, `M15`, `N2`, `N3`; Refactoring `Choose Small, Named Moves` where selected. |
| Remove temporary mutation and let clearer structure replace the flow-narrating comment. | G1-G3 | Clean `M6`, `M11`, `M16`, `N6`, `N9`; the mutation is local rather than hidden external state, so this is readability application rather than strict CQS. |
| Preserve the exported boolean signature while declining broader API redesign. | G1-G3 | Explicit artifact constraint plus proportional `M14`/`M22`; `M5` identifies the smell, while compatibility and the helper's small pure shape justify stopping. |
| Avoid helpers, new types, shared utilities, or speculative abstraction. | G1-G3 | Clean `M13`, `M14`, `M22`, `N7`; Refactoring stopping guidance where selected. |
| Test exact short/full, nickname absence/whitespace, trimming, punctuation, and spacing behavior. | G1-G3 | Clean `M12` and final checklist; exact cases derive from the supplied contract. |

Router-narrowed reviewer source trace:

| Material recommendation | Runs | Independent source trace |
| --- | --- | --- |
| Normalize each value once and express short/full output directly. | G1-G3 | Clean `M2`, `M3`, `M4`, `M15`, `N2`, `N3`; Refactoring named-move guidance in G1/G3. |
| Remove temporary mutation and the comment made unnecessary by direct structure. | G1-G3 | Clean `M11`, `M16`, `N6`, `N9`; local temporary cleanup is a readability move rather than hidden external-state CQS. |
| Preserve the fixed boolean signature and stop before API or abstraction redesign. | G1-G3 | Explicit artifact constraint plus proportional Clean `M13`, `M14`, `M22`, `N7`; Refactoring stopping guidance where selected. |
| Test exact nickname absence/whitespace, trimming, punctuation, and both output modes. | G1-G3 | Clean `M12` and final checklist; exact cases derive from the supplied contract. |

- Frozen result: **before narrowing failed ordinary disclosure at `2/3`** and remains preserved.
- Current result: **pass after router narrowing**. Catalog selection, application fidelity, package isolation, and ordinary disclosure all pass `3/3`.

### E2: Command-Query Hidden-Mutation Ambiguity

- Class: focused retrieval; disputed interpretation; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/focused-command-query.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{}`.
- Forbidden skills: `{refactoring, release-it, working-effectively-with-legacy-code, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: none.
- Reference mode: `focused`.
- Expected sections: exactly `Function rules` and `Hard rules` from the Clean Code full reference.
- Forbidden sections: every other section of `clean-code/references/full.md`.
- Baseline runs: `019f5337-e63b-7072-a051-53b7cb20df50` correctly identified lazy caching as hidden mutation, preserved a narrow strong-reason exception, and offered both an explicit-cache naming option and a genuinely strict `primeUser(): void` plus `getCachedUser()` split. Its RED gap was retrieval and canonical support, not conceptual understanding.
- Before-clarification run: `019f5349-326e-7521-919a-2a2cb064e1b2` selected only `{clean-code}`, consulted only the Clean Code package, and reported `focused` mode. Preserved as `green-before-routing-fix-1.json`.
- Before-router-narrowing run: `019f5357-a619-7591-97ee-8e8799e784b4` selected only `{clean-code}`, consulted only the Clean Code body, index, and full package reference, and reported `focused` mode. Preserved as `green-before-router-narrowing-1.json`.
- Router-narrowed run: `019f5374-768c-7590-b5b9-3c9fd5856074` selected only `{clean-code}`, consulted the Clean Code body/index/full package reference, and reported `focused` mode.
- Behavioral delta: GREEN must resolve the apparent absolute command-query rule against the full rule's explicit `without a strong reason` qualifier, identify lazy caching as hidden mutation that needs an explicit and locally legible justification or separation, and keep alternatives proportionate without expanding into a general audit.
- Before-fix observed delta: GREEN gained canonical retrieval and selected the intended skill, but its option labeled `Strict command-query separation` used `loadUser(): User` while mutating the cache. That still answers and mutates, directly contradicting `M6`. The baseline's `primeUser(): void` option was more faithful. The answer also used the exact `keep state transitions obvious` guidance from the predeclared-forbidden `Implementation preferences` section.
- Before-router-narrowing observed delta: GREEN preserved the narrow strong-reason exception, correctly classified inline cache population as mutation, and made the strict alternative `loadUser(): void` plus side-effect-free `findCachedUser()`. No recommendation required a forbidden full section.
- Router-narrowed observed delta: focused disclosure remains correct, but the answer labels `loadUser(): User` plus cache mutation as strict command-query separation. Returning the loaded user still answers while mutating, so application fidelity regresses despite the unchanged clarification.

Before-fix reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Reject the original `findUser` because it returns an answer while mutating cache state. | `M6`, `M17`, and full `Function rules`. |
| Allow lazy caching only for a narrow strong reason and make the mutation locally explicit. | Full `Hard rules` supplies `without a strong reason`; `M3` and `M6` support explicit naming and mutation. |
| Rename the practical exception to `getOrLoadUser`. | `M3` plus `M6`; it is correctly described as an exception rather than strict CQS. |
| Keep state transitions obvious. | Full `Implementation preferences`, which was outside the expected focused section set. |
| Treat `loadUser(): User` plus cache mutation as strict CQS. | Unsupported and contradictory to `M6`; returning the loaded user still answers while mutating. |

Before-router-narrowing reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Classify `findUser` cache population as mutation and not strict command-query separation. | Exact `M6`, full `Function rules`, and the authored cache/CQS application note. |
| Permit inline lazy caching only as a recorded strong-reason exception. | Full `Hard rules` plus the authored application note; modality remains an exception rather than a clean pass. |
| Rename the exception to `getOrLoadUser` so mutation is visible. | `M3`, `M6`, and the application note. |
| Use `loadUser(): void` for population and `findCachedUser()` for retrieval. | `M6` and the application note; one method mutates and the other answers. |
| Remove caching from `findUser` when no strong reason exists. | `M6`, full `Function rules`, and general design judgment about whether the cache earns its cost. |

Router-narrowed reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Classify the original `findUser` as mutation plus answer and reject it as strict CQS. | Exact `M6`, full `Function rules`, and the authored application note. |
| Allow lazy caching only as an explicit strong-reason exception and rename it `getOrLoadUser`. | Full `Hard rules`, `M3`, `M6`, and the application note. |
| Present `loadUser(): User` plus cache mutation as strict separation. | Unsupported and contradictory to `M6` and the authored note; naming it as a command does not remove the returned answer. |

- Frozen result: **before narrowing passed after clarification** and remains preserved.
- Current result: **fail on command-query application fidelity**. Discovery, focused disclosure, package isolation, and exception modality pass; the strict alternative violates the rule it claims to apply.

### E3: Legacy Code Near-Neighbor Ownership

- Class: near-neighbor counterexample; pair-specific negative; focused application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/legacy-code-neighbor.md`.
- Required skills: `{working-effectively-with-legacy-code}`.
- Allowed skills: `{refactoring}` only after Legacy Code establishes characterization and dependency control.
- Forbidden skills: `{clean-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`.
- Required order: `working-effectively-with-legacy-code` before `refactoring` when both are selected.
- Reference mode: `focused`.
- Expected sections: a bounded subset of Legacy Code `Default Workflow for Legacy Changes`, `Testing Strategy Rules`, `Seam Rules`, `Dependency Breaking Rules`, and `Handling Risky Areas`; it must include `Testing Strategy Rules` and `Dependency Breaking Rules`.
- Forbidden sections: every Clean Code full-reference section and every Legacy Code section outside the bounded expected set.
- Baseline runs: `019f5338-88a0-7d62-aebd-87604428d10c` already characterized current behavior, introduced narrow database/time seams, separated structural and semantic work, clarified the seven-day boundary, and rejected opportunistic cleanup. This counterexample had no semantic RED; it is a routing/non-regression control.
- Before-routing-fix run: `019f534a-22e3-7f20-80a0-e08cf538b5a2` selected `{working-effectively-with-legacy-code, refactoring, release-it}` and reported `focused` mode. It consulted package-only paths, but loaded Legacy and Refactoring bodies plus the Release It body, index, and full reference. It did not consult Clean Code. Preserved as `green-before-routing-fix-1.json`.
- Before-final-boundary-fix run: `019f5358-5994-7260-a1f1-e51175e63523` selected `{working-effectively-with-legacy-code, refactoring}`, consulted only those two skill bodies, and reported `ordinary` mode. It selected required Legacy Code first, allowed Refactoring second, and neither forbidden Clean Code nor forbidden Release It. Preserved as `green-before-final-boundary-fix-1.json`.
- Final-boundary run: `019f5366-7f72-7200-8f51-6ce397f33f6b` selected `{working-effectively-with-legacy-code, refactoring}`, consulted the Legacy body/index/full reference plus the Refactoring body, and reported `focused` mode. Required/allowed/forbidden selection and Legacy-first order all pass.
- Behavioral delta: GREEN must assign initial ownership to Legacy Code, characterize uncertain behavior, gain deterministic control over database construction and time with the smallest useful seam, keep structural and semantic changes separate, and avoid activating Clean Code for incidental naming or shape problems.
- Before-fix observed delta: the required Clean Code negative and Legacy-first ordering passed, but GREEN added forbidden Release It ownership and rollout scope. It did not open the expected Legacy index/full sections; the only detailed reference retrieval was for Release It.
- After-fix observed delta: catalog ownership and application now pass. The answer characterizes current behavior, introduces narrow database/time seams, separates structural and semantic patches, and excludes unrelated cleanup without importing Release It. It under-discloses relative to the predeclared `focused` contract because it reads no Legacy index/full sections.
- Final-boundary observed delta: catalog/application behavior remains correct and focused disclosure now reaches the expected Legacy detail tier. The answer consults no Clean Code or Release It guidance.

Before-fix reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Characterize current suspension semantics and external caller dependence before changing behavior. | Legacy Code `Establish Control Before Design` and `Build Fast, Trustworthy Feedback`. |
| Break only database construction and ambient time with the smallest seam. | Legacy Code `Create Narrow Seams at Real Barriers` and its explicit database/time boundary triggers. |
| Preserve the public constructor while adding an internal seam. | Reasonable general judgment consistent with Legacy locality; the skill does not require this exact compatibility mechanism. |
| Separate seam/characterization, semantic rule, and optional cleanup into distinct patches. | Legacy Code `Keep Change Local and Honest`; Refactoring `Preserve Behavior and Control Risk`. |
| Extract a pure `(dueAt, suspended, now)` policy decision. | Legacy Code `Use the Smallest Safe Technique`; Refactoring `Choose Small, Named Moves`. |
| Define the exact seven-day and timezone boundary. | Task-specific general judgment supported by Legacy characterization pressure. |
| Estimate affected accounts and require observable, reversible rollout behavior. | Release It `Release and Runtime Safety`; this recommendation demonstrates the forbidden skill's added scope. |

After-fix reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| State the behavior delta and characterize missing, boundary, repeated-call, timestamp, and external-caller behavior first. | Legacy Code `Establish Control Before Design` and `Build Fast, Trustworthy Feedback`; exact edge cases also use task-specific general judgment. |
| Break only real-database construction and ambient time with narrow persistence and clock seams. | Legacy Code `Create Narrow Seams at Real Barriers`, including its database/time triggers. |
| Keep the public constructor compatible while adding a non-public test seam. | General judgment consistent with Legacy locality; the skill does not require this exact mechanism. |
| Separate seam/characterization, behavior change, and optional cleanup. | Legacy Code `Keep Change Local and Honest`; Refactoring `Preserve Behavior and Control Risk`. |
| Extract only enough policy from JDBC/time to test the suspension rule. | Legacy Code `Use the Smallest Safe Technique`; Refactoring `Choose Small, Named Moves`. |
| Record unrelated naming, SQL, injection, or architecture cleanup separately. | Legacy Code `Keep Change Local and Honest`; Refactoring `Sequence and Bound the Change`. |

Final-boundary reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Establish the precise current return, suspension, error, timestamp, and external-caller behavior before semantic change. | Legacy Code `Establish Control Before Design`, full `Testing Strategy Rules`, and task-specific boundary judgment. |
| Keep the public constructor compatible while first introducing the smallest database seam. | Legacy Code `Create Narrow Seams at Real Barriers`, full `Seam Rules` and `Dependency Breaking Rules`; exact constructor shape is general judgment. |
| Characterize current behavior before extracting policy or adding the grace period. | Legacy Code `Build Fast, Trustworthy Feedback`, full `Default Workflow for Legacy Changes` and `Testing Strategy Rules`. |
| Extract a pure `(dueAt, suspended, now)` decision and add deterministic time only after DB control. | Legacy Code `Use the Smallest Safe Technique`, full `Dependency Breaking Rules` and `Handling Risky Areas`; Refactoring `Choose Small, Named Moves`. |
| Separate control, structural, and behavior patches. | Legacy Code `Keep Change Local and Honest`; Refactoring `Preserve Behavior and Control Risk`. |
| Define exact seven-day/timezone semantics. | Task-specific general judgment prompted by Legacy characterization guidance. |

- Frozen result: **before-final run failed disclosure only** and remains preserved.
- Current result: **pass after final boundary fix**. Selection, ordering, focused disclosure, package isolation, application, and reviewer fidelity all pass.

### E4: Comprehensive Clean Code Audit

- Class: direct invocation; comprehensive retrieval; application.
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/comprehensive-audit.md`.
- Required skills: `{clean-code}`.
- Allowed skills: `{clean-architecture}` because the adapter owns policy and constructs infrastructure, although the explicit complete Clean Code request remains the required lens.
- Forbidden skills: `{refactoring, release-it, working-effectively-with-legacy-code, designing-data-intensive-applications, code-complete}`.
- Required order: none.
- Reference mode: `comprehensive`.
- Expected sections: all 22 level-two headings in `clean-code/references/full.md`, read end to end.
- Forbidden sections: none within the Clean Code full reference.
- Baseline runs: `019f5339-0b19-75b0-a095-31e980818b78` produced a broad, competent audit from general knowledge but explicitly reported that no repository Clean Code reference was available. The RED gap was exhaustive retrieval and source-grounded completeness.
- Before-routing-fix run: `019f534b-48d2-7722-b86a-5ff6067f1716` selected only `{clean-code}`, consulted only `.agents/skills/clean-code/SKILL.md` and `.agents/skills/clean-code/references/full.md`, and reported `comprehensive` mode. Preserved as `green-before-routing-fix-1.json`.
- Current retained after-routing-fix run: `019f5359-529e-7250-a0b1-14adc3776c58` selected only `{clean-code}`, consulted the Clean Code body, index, and full package reference, and reported `comprehensive` mode. It was not rerun after the final catalog-boundary edit, per explicit user direction.
- Behavioral delta: GREEN must use the exhaustive tier rather than treating `SKILL.md` as the complete audit, prioritize findings across naming, function shape, comments, errors, boundaries/construction, async behavior, tests, refactoring scope, and reporting, and distinguish behavior-preserving cleanup from possible defects.
- Before-fix observed delta: GREEN loaded the exhaustive tier and grounded the audit across the full concern surface. It separated the undeclared TypeScript property and `any` severity as language-specific judgment during reviewer tracing rather than inventing a Clean Code rule for them.
- After-fix observed delta: the comprehensive contract remains stable. GREEN again covered names, function shape, flags, mutation, errors, boundaries/construction, concurrency, comments, tests, bounded cleanup, and defect-vs-cleanup reporting without selecting a neighboring skill.

Before-fix reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Treat undeclared `db` as a TypeScript defect and `any` as weakened static contracts. | Language-specific general judgment; the related demand for explicit object/API shape is consistent with `M10`, but the TypeScript diagnosis is not a book rule. |
| Split mixed persistence, decision, notification, and response responsibilities into named phases. | `M4`, `M15`, full `Function rules`, `Class and module design`, and `Objects, modules, and data structures`. |
| Remove or isolate boolean mode flags. | `M5`, `M17`, `N3`, and full `Function rules`. |
| Make query/mutation and hidden effects explicit. | `M6`, `M17`, `N4`, `N8`, full `Function rules`, and `Hard rules`. |
| Remove or justify shared mutable handler state and isolate async notification policy. | `M20`, `N10`, full `Concurrency and async work`. |
| Separate Prisma/HTTP/environment/fetch details from the status policy and add a notifier boundary. | `M9`, `M19`, `N10`, full `Boundaries and external dependencies` and `System construction rules`. |
| Persist only the intended state instead of exposing the whole loaded representation. | `M8`, `M10`, full `Objects, modules, and data structures` and `Implementation preferences`. |
| Remove narrating comments after improving names and structure. | `M11`, `M16`, `N6`, `N9`, full `Comment rules`. |
| Replace the truthiness test with deterministic contract tests for status, persistence, 404, and notification behavior. | `M12`, `M21`, full `Tests` and `TDD and clean test rules`; exact case selection also uses general judgment from the artifact. |
| Keep remediation bounded and preserve current behavior while improving the highest-value touched smells. | `M1`, `M14`, `M22`, `N1`, `N7`, full `Refactoring rules` and `Emergent design and successive refinement`. |
| Report validation and distinguish the undeclared-property defect from behavior-preserving cleanup. | Full `Output Expectations` and `Review checklist`, plus language-specific general judgment for the defect classification. |

After-fix reviewer source trace:

| Material recommendation | Independent source trace |
| --- | --- |
| Treat undeclared `db` and suppressed `any` contracts as TypeScript defects. | Language-specific general judgment; explicit API/object shape is consistent with `M10`, but the compiler diagnosis is not a book rule. |
| Split HTTP, persistence, status decision, notification, state mutation, and response work into named phases. | `M4`, `M15`, full `Function rules`, `Class and module design`, and `Objects, modules, and data structures`. |
| Remove boolean modes or preserve the current API only as a compatibility wrapper. | `M5`, `M17`, `N3`, `N4`, and full `Function rules`; compatibility is general judgment. |
| Make database/instance/response mutation and return semantics explicit. | `M6`, `M17`, the authored CQS note, full `Function rules`, and `Hard rules`. |
| Remove or justify shared mutable handler state. | `M20`, `N10`, and full `Concurrency and async work`. |
| Isolate fire-and-forget notification behind an adapter with explicit failure, timeout, and shutdown semantics. | `M19`, `M20`, full `Boundaries and external dependencies` and `Concurrency and async work`. |
| Persist only intended state rather than round-tripping the fetched ORM representation. | `M8`, `M10`, full `Objects, modules, and data structures`; Prisma-specific risk is general judgment. |
| Make missing/success result semantics explicit rather than mixing `null` and framework return values. | `M7`, full `Error handling`, plus framework-specific general judgment. |
| Replace vague names and narrating comments. | `M3`, `M11`, `M16`, `N2`, `N6`, `N9`, full `Naming rules` and `Comment rules`. |
| Replace truthiness testing with deterministic contract tests for 404, status, persistence, and notification. | `M12`, `M21`, full `Tests` and `TDD and clean test rules`; exact cases derive from the artifact. |
| Move Prisma construction out of ordinary behavior. | `M9`, `M19`, full `System construction rules` and `Boundaries and external dependencies`. |
| Keep remediation bounded and distinguish language/runtime defects from behavior-preserving cleanup. | `M1`, `M14`, `M22`, `N1`, `N7`, full `Refactoring rules`, `Emergent design and successive refinement`, `Review checklist`, and `Output Expectations`. |

- Result: **pass before and after routing fix**. Required/forbidden selection, comprehensive disclosure, package isolation, application breadth, and reviewer source fidelity remain stable.

## Historical Forward-Test Results

These runs predate the durable RED/GREEN corpus and the current unbiased runner contract. Preserve them as exploratory history, not current acceptance evidence. All used a fresh ephemeral Codex CLI thread with `--ignore-user-config --sandbox read-only --json`; no run modified repository files.

| Thread | Prompt shape | Observed selection | Observed reference behavior | Result |
| --- | --- | --- | --- | --- |
| `019f5277-f26c-7530-bcfe-501c1e9e08a2` | Vague names, boolean mode, mixed mutation/answer, explanatory comment, and promised future rewrite; local behavior-preserving redesign. | `clean-code` only. | Read `SKILL.md` only. | Pass: recognized every named symptom, resisted rewrite/scope pressure, proposed a local split, and supplied behavior-preserving validation cases. |
| `019f5278-586e-7900-b5ec-1479dd9d0a52` | Uncertain behavior, no trustworthy tests, constructor opens a real database; gain control before one semantic change. | `working-effectively-with-legacy-code` only. | Did not read Clean Code. | Pass: the near-neighbor prompt did not activate `clean-code`. |
| `019f5278-d186-7681-b89f-dc348cb6cb49` | Explicit focused ambiguity about a method that mutates cached state and returns an answer. | `clean-code`. | Read `references/index.md`, then only `Function rules` (`44-62`) and `Hard rules` (`290-297`) from `full.md`. | Pass: focused routing was bounded and the answer preserved the source's strong-reason exception. |
| `019f5279-5654-7a52-96c1-acb42fa42bd7` | Explicit comprehensive Clean Code audit of a multi-concern service fragment. | `clean-code`. | Read all 297 lines of `full.md` in `1-240` and `241-340` chunks. | Pass: comprehensive routing loaded the exhaustive tier end to end before answering. |
| `019f527a-8c89-7d11-a351-f48c55050b36` | Explain a simple TypeScript map/filter expression without suggesting changes. | No book skill. | Loaded no book skill or reference. | Pass: generic code explanation did not activate `clean-code`. |
| `019f527a-c27c-7dd0-95c4-76e726f564f5` | Confusing retry-state names and hidden mutation plus unbounded retries/no timeout; preserve behavior and define production failure. | `clean-code`, `refactoring`, and `release-it`. | Ordinary skill bodies only. | Pass with expected overlap: Clean Code owned local intent/mutation, Release It owned failure semantics, and Refactoring was justified by the explicit behavior-preserving redesign request. |
| `019f527b-4018-7a53-a72e-708382bec44e` | Move a well-tested calculation in reversible steps without changing observable behavior, then stop before the later feature. | `refactoring` only. | Did not read Clean Code. | Pass: transformation mechanics did not spuriously activate `clean-code`. |

## Evaluation Protocol Status

- Baselines: nine skill-disabled runs cover five durable raw-code cases under `gpt-5.4`. E1-E4 retain six retroactive controls; E1b adds three new controls before its GREEN runs. E1b has no semantic RED because all controls are already strong; it is explicitly a catalog/disclosure stability case.
- Frozen GREEN evidence: six pre-routing results remain as `green-before-routing-fix-<n>.json`; four E1/E3 results remain as `green-before-final-boundary-fix-<n>.json`; seven E1/E1b/E2 results remain as `green-before-router-narrowing-<n>.json`. Frozen failures and passes are not relabeled after later changes.
- Current GREEN evidence: nine results cover E1 `3x`, E1b `3x`, E2, E3, and E4. E1/E1b/E2 were rerun under the narrowed router; E3/E4 retain their validated final-boundary results as explicitly allowed.
- Package isolation: pass in every generation. The six pre-routing results contain 15 packaged paths, four pre-final snapshots contain 10, seven pre-narrowing snapshots contain 17, and nine current results contain 24; every path begins with `.agents/skills/`.
- Catalog stability: pass. E1 and E1b select required Clean Code `3/3`; E2/E4 select Clean Code alone; E3 selects Legacy Code then allowed Refactoring. Legacy/Release remain forbidden where required, and Clean Code remains absent from E3.
- Application and fidelity: E1 proportional cleanup and E1b local hygiene pass `3/3`; E3 control-first and E4 comprehensive guidance remain faithful. Current E2 regresses by returning `User` from a cache-mutating method while calling that strict command-query separation.
- Disclosure: accepted for this corpus. E1b is ordinary `3/3`; E2 and E3 are focused; E4 is comprehensive. E1 focuses only when the solver identifies the unresolved partner/high-total interaction and otherwise remains ordinary.
- Acceptance under current process: **failed only on E2 command-query application fidelity**. Catalog boundaries and progressive disclosure are accepted; the authored clarification is not yet behaviorally stable.

## Independent Review

- Reviewer: parent evaluation reviewer, separate from the conversion worker and blind solver runs.
- Catalog snapshot: `clean-code`, `release-it`, `refactoring`, and `working-effectively-with-legacy-code`.
- Static semantic verdict: concern grouping and exact mini wording remain coherent. The authored cache/CQS note is source-supported, resolves the observed application failure, and does not rewrite an `M*` rule.
- Behavioral verdict: not fully accepted. E1 proportional cleanup, E1b ordinary hygiene, E3 control-first work, and E4 comprehensive audit pass; current E2 contradicts `M6` in its strict alternative.
- Catalog verdict: accepted for this corpus. Final descriptions route local hygiene to Clean Code, control-first uncertainty to Legacy Code, behavior-preserving extraction to allowed Refactoring, and exclude Release It from ordinary local/runtime work.
- Progressive-disclosure verdict: accepted for this corpus. Router narrowing changes E1b from ordinary `2/3` to `3/3` while preserving focused E2 retrieval and allowing focused E1 retrieval only for an unresolved decision.
- Remaining application issue: the cache/CQS note says to separate population from retrieval but does not state the positive strict shape strongly enough to prevent `loadUser(): User`. Evidence now includes one correct and one regressed post-clarification run; any further edit should use that pair as RED/GREEN and preserve exact `M6` wording.

## Validation Evidence

- Structural validation: repository validation passes frontmatter parsing and exact keys, folder/name agreement, lowercase kebab-case/name length, the 68-line `SKILL.md`, 731-word source-driven size exception, 149-word packaging overhead, direct one-level reference links, absence of skill placeholders, and an exact four-file skill package. The runtime description is 393 characters. `openai.yaml` parses with quoted UI strings, a 25-64 character `short_description`, an 87-character one-sentence default prompt containing exact `$clean-code`, and explicit `allow_implicit_invocation: true`. Official `skill-creator/scripts/quick_validate.py` also passes through `uv run --with pyyaml`.
- Wording fidelity: `python3 _skill-workbench/scripts/check_rule_wording.py --mini clean-code/clean-code.mini.md --skill .agents/skills/clean-code/SKILL.md` exited 0 with 22 mini rules, 22 skill guidance rules, 22 exact matches, zero missing/reworded rules, zero added/reworded rules, and `wording fidelity: exact`. An independent set check confirmed each mini rule occurs verbatim exactly once; the primary bias and all seven final-checklist items are also verbatim.
- Mapping coverage: deterministic checks found ordered, unique rows for every `M1`-`M22` and `N1`-`N10`; no mini merges or wording exceptions exist.
- Full-reference equality: `cmp -s` exited 0. Both canonical and copied files have SHA-256 `0ec945c383144e2eeb52bdd18cc87668bff73c13421e17cc6e4ba3fc5905965e`.
- Index validation: deterministic parsing found all 22 level-two full headings exactly once, with matching GitHub-style anchors, current start/end ranges, non-empty non-placeholder `Read when` guidance, and a valid `full.md` target.
- Catalog review: final-boundary evidence eliminates the observed Clean/Legacy/Refactoring and Legacy/Release It ownership collisions for this corpus.
- Invocation evaluation: E1 and E1b select Clean Code `3/3`; E2/E4 retain Clean-only results; E3 selects Legacy Code then allowed Refactoring and excludes both forbidden skills.
- Application evaluation: proportional E1, ordinary E1b, control-first E3, and comprehensive E4 pass; current strict-CQS E2 fails as recorded above.
- Result-path validation: all frozen and current GREEN results use only `.agents/skills/` paths. Nine baselines, six pre-routing snapshots, four pre-final snapshots, seven pre-narrowing snapshots, nine current GREEN files, and five case files are preserved.
- Remaining risks: `consulted_files` records files, not shell line ranges, so focused section use must be inferred from answer language and cannot be proven as directly as comprehensive file loading. APoSD, Code Complete, Clean Architecture, DDD, and Pragmatic Programmer are not live converted skills yet, so those collision cases remain compatibility-analysis evidence rather than runtime-tested catalog behavior.

## 2026-07-12 Final Retrofit Reconciliation

This section supersedes every earlier use of `current` above while retaining those generations as audit evidence.

- Final E2 run `019f55d6-df47-7cc0-b7f7-0b05836df43d` selected only `clean-code`, used focused disclosure, and passed the result-integrity check.
- The final E2 answer states that cache population is mutation, gives a strict `loadUser(id): void` command followed by a nonmutating `findCachedUser` query, and labels `getOrLoadUser` only as a strong-reason exception. The earlier `loadUser(): User` contradiction is closed.
- Final E3 run `019f55d4-25d0-72c1-a0e2-f68d8ab87a96` selected Legacy Code then allowed Refactoring and kept Clean Code absent, preserving the near-neighbor boundary after the final catalog changes.
- E1b remains the accepted ordinary Clean Code control at `3/3`; E1 remains pressure/application evidence whose disputed product interaction may legitimately trigger focused retrieval; E4 remains the comprehensive control.
- Final acceptance: **pass** for discovery, proportional application, ordinary/focused/comprehensive progressive disclosure, source fidelity, and near-neighbor exclusion. No pilot rewrite or additional Clean Code retrofit is required before the next conversion batch.

## Inline Reference Map Evaluation

### RM1: Ordinary local-hygiene control

- Contract version: 2
- Class: application and disclosure
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/ordinary-local-hygiene.md`
- Fixture SHA-256: `f6282cfcb4fb88d1c1e4906b027e6c02e877c4e4d44f3784e5489e34a8c4e92e`
- Required skills: `{clean-code}`
- Distinctive judgment: Improve local naming, function focus, and surprise-free behavior using the compact body alone.
- Neighbor ownership: Refactoring may describe a structural move, but the fixture's central decision is local readability and hygiene.
- Ownership review: PASS - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; fixture blindness, central ownership, and the ordinary tier premise were accepted.
- Reference expectation: ordinary
- Runs: `green-inline-map-1`; selected `clean-code`; `ordinary`; no reference sections
- Package fidelity trace: exact mini-derived naming and function guidance; router-only change
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: none

### RM2: Focused command-query control

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/focused-command-query.md`
- Fixture SHA-256: `bade0e9ce79858f47d07125e55d2ac72623fb5d89d19580ea2124bbb337646fa`
- Required skills: `{clean-code}`
- Distinctive judgment: Resolve hidden cache mutation and the command-query exception boundary without broad cleanup.
- Neighbor ownership: This is a Clean Code function contract dispute; Legacy Code and Refactoring are not needed to establish current behavior or choose a structural sequence.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture reveals the required source lens and cannot be reused unchanged.
- Reference expectation: focused
- Compact-body gap: The fixture asks for the source's strict command-query interpretation and strong-reason exception detail beyond the compact function rule.
- Intended index destinations: `Function rules` and `Hard rules`
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: the two named canonical full headings and exact mini-derived function guidance
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM2b; the frozen fixture, hash, and required set remain unchanged

### RM2b: Focused concurrency-validation replacement

- Contract version: 2
- Class: retrieval and application
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/focused-concurrency-validation-v2.md`
- Fixture SHA-256: `6a1dbba1d3b2bb88a9e7178cdfd40383d0cf6929e2213b720f060f75d1783d6f`
- Required skills: `{clean-code}`
- Distinctive judgment: Resolve the exact concurrency-validation dispute, including varied schedules, intermittent failures, explicit lifecycle behavior, ownership, and tunability, without widening to a general audit.
- Neighbor ownership: Code Complete may contribute general construction testing and Release It! runtime resilience, but the disputed local concurrency and async-work guidance is central.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, explicit source dispute, and the one-section destination were accepted.
- Reference expectation: focused
- Compact-body gap: none; the fixture explicitly disputes the source's concurrency-specific validation and lifecycle requirements and requires canonical checking.
- Intended index destinations: `Concurrency and async work`
- Runs: `green-inline-map-1`; selected `clean-code` and compatible `the-pragmatic-programmer`; `focused`; target sections `Concurrency and async work` and `Change Process`
- Package fidelity trace: canonical full heading `Concurrency and async work` and unchanged mini-derived concurrency guidance
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: one additional relevant target section plus bounded neighboring concurrency guidance; required target and focused access passed

### RM3: Comprehensive Clean Code control

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/comprehensive-audit.md`
- Fixture SHA-256: `114e8945371df220dfdc2cd6c705faf344c5fb5585e06a59c2b351aedea4a201`
- Required skills: `{clean-code}`
- Distinctive judgment: Apply the complete Clean Code lens rather than a bounded local subset.
- Neighbor ownership: The explicit complete-lens request owns this control even if neighboring guidance is compatible.
- Ownership review: REJECTED - independent inline-map pre-dispatch audit by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; the fixture exposes the required source lens and cannot be reused unchanged.
- Reference expectation: comprehensive
- Runs: not run; rejected before dispatch and preserved as contract evidence
- Package fidelity trace: all canonical full headings
- Attribution review: not run
- Behavioral result: not run
- Diagnostics: replaced by blind control RM3b; the frozen fixture, hash, and required set remain unchanged

### RM3b: Comprehensive local-code replacement

- Contract version: 2
- Class: retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/clean-code/comprehensive-local-code-audit-v2.md`
- Fixture SHA-256: `4b677f6c2c16ad5a43b711795830b5181b09770579ebaab3f48ef8e874b24edf`
- Required skills: `{clean-code}`
- Distinctive judgment: Apply the complete local readability, function, state, error, boundary, testing, concurrency, smell, and refinement lens end to end.
- Neighbor ownership: Refactoring or construction guidance may contribute compatible moves, but the fixture's explicit exhaustive local-code objective makes this skill central.
- Ownership review: PASS - independent current-policy inline-map review by agent `019f601d-5d0c-7133-99bd-40ed2cc9a304` on 2026-07-14; blindness, central ownership, and end-to-end comprehensive loading were accepted.
- Reference expectation: comprehensive
- Runs: `green-inline-map-1`; selected `clean-code`, `code-complete`, and `refactoring-guru`; each consulted skill reported `sections=["*"]`, including the required target
- Package fidelity trace: all canonical full headings
- Attribution review: PASS - independent final result review found no unsupported book attribution; general solver additions remained separate from packaged guidance
- Behavioral result: pass
- Diagnostics: permitted compatible selections; required target inclusion and end-to-end access passed
