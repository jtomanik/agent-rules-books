# Refactoring Skill Mapping

## Scope

- Distinctive lens: improve the internal structure of existing code through small, behavior-preserving transformations, bounded by the current source of friction and an explicit stopping condition.
- Intended invocation: select when structural improvement without observable behavior change is central, including preparatory refactoring, smell treatment, and review of cleanup scope.
- Closest neighboring skills: `working-effectively-with-legacy-code` controls how to gain observation and test leverage before risky change; `clean-code` defines everyday readability and local code-shape pressure; `refactoring-guru` is a mostly overlapping smell-and-technique catalog.
- Invocation policy: model invocation is explicitly enabled because the agent must recognize structural-change intent even when the user does not name Refactoring.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Protected behavior-preserving work | `behavior-preserving structural change once observable behavior is known or protected` | Legacy control work whose first need is characterization, observation, or dependency substitution. |
| Named structural moves | `renaming, extracting, moving, splitting, or another current code smell drives a behavior-preserving change` | Clean Code's local-readability guidance and detached smell-catalog browsing without a concrete structural change. |
| Legacy seam exclusion | `Dependency-seam work whose purpose is to gain first feedback belongs to Legacy Code until control exists` | Prevents Refactoring from leading merely because safe legacy work may later contain a structural cleanup. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "Extract this long calculation and rename its variables without changing behavior; tests are green." | `refactoring` | The central task is an explicit behavior-preserving structural transformation with an existing safety net. |
| "This feature requires touching the same conditional in five places. Reshape the code first, preserve behavior, then add the feature." | `refactoring` | Preparatory refactoring and shotgun-surgery reduction are central; legacy control is not indicated. |
| "Add a billing rule to this untested class. It reads global time and constructs the database client internally; preserve today's behavior first." | `working-effectively-with-legacy-code`, then `refactoring` | Legacy guidance creates observation and a narrow seam; Refactoring governs the subsequent behavior-preserving extraction and ownership move. |
| "We do not know what this failing branch does and there are no tests. Find a safe observation point before fixing it." | `working-effectively-with-legacy-code` | Gaining control is the first-order problem; structural refactoring is conditional and should not lead invocation. |
| "Review these names, comments, parameter lists, and command-query separation in otherwise well-structured code." | `clean-code` | Local readability and function/API shape dominate; no structural transformation has been requested. |
| "Identify the smell category and show every catalog treatment for this code." | `refactoring-guru` when available; otherwise `refactoring` with its full catalog | Catalog breadth dominates over Fowler-style change sequencing, although the Refactoring full reference can supply the technique index. |
| "Design a new service API and module boundary from scratch." | Neither overlap-pilot skill | No existing-code structural transformation or weak-feedback legacy change is central. |
| "Add retry budgets and circuit breakers to a production client." | `release-it` when available, not `refactoring` | Operational stability behavior is central, not behavior-preserving structural work. |
| "Clean this up." | No automatic book skill until context shows structural intent | The prompt is too generic; code inspection must reveal a concrete smell, behavior-preservation requirement, or legacy-control problem. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance, final-check | Description; `Primary Bias`; `Preserve Behavior and Control Risk`; final checklist | Observable behavior and intent isolation define the skill's positive boundary. |
| `N2` | early-guidance, final-check | `Preserve Behavior and Control Risk`; final checklist | Keeps small buildable/testable/reviewable steps salient without creating a separate priority bucket. |
| `N3` | early-guidance, reference-router, final-check | `Preserve Behavior and Control Risk`; focused router; final checklist | Safety-net pressure is early; disputed verification strategy routes to `Safety Rules` or `Testing Rules`. |
| `N4` | description, early-guidance | Description current-smell branch; `Sequence and Bound the Change` | Promotes the complete current-blocking-smell rule rather than a shortened duplicate. |
| `N5` | early-guidance, reference-router | `Choose Small, Named Moves`; focused router | The complete technique-family guidance is early; exact move selection stays in the full catalog. |
| `N6` | early-guidance, reference-router | `Put Structure Around Ownership`; `Simplify with Evidence`; focused router | Ownership and anti-speculation remain colocated with their complete mini rules. |
| `N7` | early-guidance | `Put Structure Around Ownership` | Mutation and call-contract guidance remains a complete concern rather than a detached critical fragment. |
| `N8` | early-guidance, final-check | `Sequence and Bound the Change`; final checklist | The stop condition remains beside scope and rewrite pressure. |
| `N9` | early-guidance, reference-router | `Preserve Behavior and Control Risk`; focused router | Weak feedback alone belongs to legacy-code invocation; when a concrete refactoring is also central, this rule supplies characterization pressure and detailed questions route to the full reference. |
| `N10` | description, early-guidance | Description preparatory-refactor branch; `Sequence and Bound the Change` | The full preparatory/follow-up rule and its trigger stay together. |
| `N11` | early-guidance | `Choose Small, Named Moves` | Third repetition remains an ownership trigger, not a general abstraction mandate. |
| `N12` | early-guidance, reference-router | `Simplify with Evidence`; focused router | Keeps decomposition before heavier variation mechanisms and routes exact technique choice to the catalog. |
| `N13` | description, early-guidance, final-check | Description small-verified-cleanup branch; `Sequence and Bound the Change`; final checklist | Mixed-intent patch control is authoritative in one concern and only restated as a final check. |
| `N14` | early-guidance, final-check | `Sequence and Bound the Change`; final checklist | Rewrite pressure resolves to the next small behavior-preserving move. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Preserve Behavior and Control Risk` | Moved verbatim | Preserves observable behavior and isolates behavior change, migration, redesign, and cleanup. |
| `M2` | `Preserve Behavior and Control Risk` | Moved verbatim | Retains reversibility, buildability, testability, reviewability, and local patch splitting. |
| `M3` | `Preserve Behavior and Control Risk` | Moved verbatim | Retains characterization, test alignment, and the prohibition on deleting failing tests. |
| `M4` | `Sequence and Bound the Change` | Moved verbatim | Preparatory and follow-up refactoring remain one complete rule. |
| `M5` | `Sequence and Bound the Change` | Moved verbatim | Retains current-smell scope and the complete mini smell inventory. |
| `M6` | `Choose Small, Named Moves` | Moved verbatim | Retains all named move families; exact recipes route to the full catalog. |
| `M7` | `Choose Small, Named Moves` | Moved verbatim | Co-locates naming, coherent function purpose, abstraction level, scope, and phases. |
| `M8` | `Put Structure Around Ownership` | Moved verbatim | Retains ownership and separation of policy from technical mechanisms. |
| `M9` | `Put Structure Around Ownership` | Moved verbatim | Retains flags, argument order, parameter mutation, exposed collections, setters, fields, and state transitions. |
| `M10` | `Simplify with Evidence` | Moved verbatim | Retains the conditional techniques and the condition that they must clarify variation. |
| `M11` | `Simplify with Evidence` | Moved verbatim | Retains evidence-based abstraction and removal of layers that do not improve changeability. |
| `M12` | `Simplify with Evidence` | Moved verbatim | Preserves error semantics and main-path/duplicate-error-structure guidance. |
| `M13` | `Sequence and Bound the Change` | Moved verbatim | Keeps patch intent and giant mixed-change avoidance beside scope rules. |
| `M14` | `Sequence and Bound the Change` | Moved verbatim | Retains requested-change ease, smell removal, local improvement, and speculation stop. |
| `M15` | `Sequence and Bound the Change` | Moved verbatim | Keeps the behavior-addition trigger beside preparatory refactoring. |
| `M16` | `Preserve Behavior and Control Risk` | Moved verbatim | Keeps unclear-bug characterization before semantic change. |
| `M17` | `Preserve Behavior and Control Risk` | Moved verbatim | Keeps the weak-test trigger limited to the smallest structural move and testability improvement. |
| `M18` | `Choose Small, Named Moves` | Moved verbatim | Preserves the third-repetition threshold and clearer-ownership response. |
| `M19` | `Choose Small, Named Moves` | Moved verbatim | Co-locates mixed function symptoms with the available local transformations. |
| `M20` | `Put Structure Around Ownership` | Moved verbatim | Retains shotgun-surgery trigger and boundary/ownership response. |
| `M21` | `Simplify with Evidence` | Moved verbatim | Keeps intent decomposition before polymorphism, state, strategy, or tables. |
| `M22` | `Put Structure Around Ownership` | Moved verbatim | Retains domain movement and presentation synchronization. |
| `M23` | `Sequence and Bound the Change` | Moved verbatim | Keeps mixed intent and code-motion reviewability beside patch discipline. |
| `M24` | `Sequence and Bound the Change` | Moved verbatim | Preserves rewrite resistance through the next small behavior-preserving transformation. |

## Wording Fidelity

The required wording checker reports exact fidelity: the primary bias, all 24 mini guidance rules, and all seven final-checklist items in source order match verbatim, with zero missing, added, or reworded text. No `M*` or `N*` wording exception requires an original/final/reason record. Frontmatter, concern headings, and reference-router prose are skill metadata and routing additions rather than transformed mini rules.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 739 words.
- Before routing fix: `SKILL.md` 835 words; packaging overhead 96 words.
- Before final catalog boundary: `SKILL.md` 846 words; packaging overhead 107 words.
- Current: `SKILL.md` 842 words; packaging overhead 103 words.
- Decision: retain the source-driven exception. Description-only routing metadata changed while the mini-derived body stayed exact; the canonical mini already exceeds the 500-word target, every mini rule remains required for complete ordinary use, and current packaging overhead remains below the 150-word soft target. Do not paraphrase rules during conversion to reduce this count.

## Behavioral Scenarios

| Scenario | Expected invocation | Expected guidance | Reference behavior |
| --- | --- | --- | --- |
| Green-test extraction of a long method with no behavior change | `refactoring` | Preserve behavior, make a small named move, keep patch reviewable, stop at the blocking smell. | Ordinary: `SKILL.md` only. |
| Feature addition made awkward by duplicated conditional logic | `refactoring` | Use a minimal preparatory refactor, add behavior separately, then local follow-up cleanup. | Ordinary unless exact conditional technique is disputed. |
| Untested class with hidden clock and database construction | `working-effectively-with-legacy-code` and `refactoring` | Characterize and create the narrowest seam first; then apply the behavior-preserving structural move. | Focused: legacy dependency/seam sections plus Refactoring safety or move section. |
| Unknown failing behavior with no requested cleanup | `working-effectively-with-legacy-code`, not `refactoring` initially | Gain observation and control before deciding whether refactoring is needed. | Legacy focused reference only. |
| Naming/comment/API readability review | `clean-code`, not `refactoring` unless structural change becomes central | Improve local reasoning without inventing a refactoring program. | No Refactoring reference. |
| Time-pressured request to rewrite a working subsystem as cleanup | `refactoring` | Reject hidden behavior change; choose the next small verified transformation and record safety gaps. | Focused: `Primary Directive`, `Forbidden Patterns`, `Testing Rules`. |
| Complete Fowler-based audit of a large cleanup patch | `refactoring` | Apply all concerns and the final checklist, including interactions among smells, moves, safety, and stopping. | Comprehensive: read `references/full.md` end to end. |
| Generic request to implement a new endpoint | No automatic `refactoring` invocation | Do not impose a book lens without existing-code structural intent. | No reference. |

## Evaluation Cases

The retrofit cases below were recorded before GREEN execution. Case files contain only blind task input; this section is the sole location for selection, ordering, disclosure, and source expectations.

### O1: Well-tested structural cleanup

- Class: distinctive recognition and ordinary application
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/01-well-tested-structural-cleanup.md`
- Required skills: `{refactoring}`
- Allowed skills: `{clean-code}`
- Forbidden skills: `{working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required order: `refactoring`
- Reference mode: `ordinary`
- Expected sections: none; the Refactoring skill body is sufficient.
- Forbidden sections: every Refactoring and Legacy Code full-reference section.
- Baseline runs: retroactive baseline `019f5337-7279-7bb2-a8ce-e3d1df88ec35`, `019f5337-72ab-7292-aa76-3a086dccda9c`, and `019f5337-7279-72e2-a4e0-006be2738c15`. All three already preserved calculation order, proposed small extract-method steps, rejected speculative abstractions, and named a stopping point. No material application failure appeared; this RED arm establishes a retrieval/source-trace gap only and cannot by itself prove incremental recommendation value.
- Pre-fix GREEN snapshot: `019f5346-75c7-7192-aa7f-cea8aa124ba1` selected `[refactoring, working-effectively-with-legacy-code, clean-code]` with `ordinary` disclosure; `019f5346-758b-7923-aa68-72031d268e75` selected `[refactoring, working-effectively-with-legacy-code]` with `focused` disclosure; `019f5346-7595-74e1-9062-6da8f45aa5ec` selected the same pair with `focused` disclosure. These records are preserved as `green-before-routing-fix-1..3.json`.
- Pre-fix comparison: application was sound but no better than RED; Legacy Code was forbidden yet selected in `3/3`, and disclosure exceeded `ordinary` in `2/3`.
- Pre-fix reviewer trace: behavior preservation/small steps -> Refactoring `M1-M3/N1-N3`, `Primary Directive`, and `Safety Rules`; phase extraction -> `M6/M7/M19/N5`, `Preferred Refactoring Moves`, and `Function-Level Rules`; conditional order -> `M1/M10/M21`; stopping -> `M11/M14/N8`; reviewable slices -> `M2/M13`. Legacy Code and Clean Code supplied no unique material recommendation.
- Pre-fix verdict: **fail**.
- Before-final-boundary GREEN runs: `019f5354-1e96-75c2-9341-329086d2ff71` selected `[refactoring, clean-code]` with `focused` disclosure; `019f5354-1e96-7683-bf29-699d25295f19` selected the same pair with `ordinary` disclosure; `019f5354-1e99-7aa3-9542-b5927ff6ef0e` selected the same pair with `focused` disclosure. Every consulted path was under `.agents/skills/`.
- Before-final-boundary delta: Legacy Code improved from incorrect selection in `3/3` to `0/3`; Refactoring remained first in `3/3`. Ordinary disclosure remained unstable at `1/3`, and recommendation content still did not improve materially over RED.
- Final-boundary GREEN runs: `019f5365-3609-72c0-a81d-5fbb2018ecda` selected `[refactoring, clean-code]` with `focused` disclosure; `019f5365-3609-7662-9b76-de86ec3a152c` selected the same pair with `ordinary` disclosure; `019f5365-3623-7810-9fa5-832a9ed6fe60` selected only `[refactoring]` with `ordinary` disclosure. O1 was not rerun after the Release-only narrowing by explicit instruction.
- Final delta: Legacy Code and Release It remain absent in `3/3`; Refactoring remains first in `3/3`; ordinary disclosure improved from `1/3` to `2/3`; allowed Clean Code fell from `3/3` to `2/3`. RED already contained the same sound extraction sequence, behavior-preservation constraints, and stop condition.
- Independent reviewer trace: behavior preservation and small verified steps -> Refactoring `M1-M3/N1-N3` and `Safety Rules`; phase extraction and top-down ownership -> `M6/M7/M19/N5`, `Preferred Refactoring Moves`, and `Function-Level Rules`; conditional order -> `M1/M10/M21`; stopping and anti-speculation -> `M11/M14/N8`; reviewable slices -> `M2/M13`. Clean Code adds no unique material recommendation.
- Frozen-case verdict: **fail** because one final run over-reads focused references and RED already supplies the application result. The Legacy/Refactoring boundary itself passes `3/3`.
- Shared replacement control: Release It E3 current run `019f5362-edce-7ef2-aec4-d05bee43f715` selected `[clean-code, refactoring]`, consulted only both runtime `SKILL.md` files, used `ordinary` disclosure, and correctly performed a local behavior-preserving rename/split. It is the accepted ordinary Refactoring replacement; O1 remains frozen historical evidence rather than a current acceptance blocker.

### O2: Uncertain DB/time change without cleanup

- Class: distinctive recognition, focused application, and near-neighbor exclusion
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/02-uncertain-db-time-change.md`
- Required skills: `{working-effectively-with-legacy-code}`
- Allowed skills: `{}`
- Forbidden skills: `{refactoring, clean-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required order: `working-effectively-with-legacy-code`
- Reference mode: `focused`
- Expected sections: Legacy Code `Testing Strategy Rules`, `Seam Rules`, `Dependency Breaking Rules`, and `Handling Risky Areas`; `Default Workflow for Legacy Changes` and `Testing Rules` are permitted bounded additions.
- Forbidden sections: every Refactoring full-reference section; Legacy Code `Preferred Legacy Techniques`, `Review Rules`, and `Review Checklist`.
- Baseline runs: retroactive baseline `019f5337-727d-70f1-8b2e-17e2802c50f1`, `019f5338-588e-7ad2-9533-82e6ef7a2c6b`, and `019f5338-5895-7a11-9571-47531a6f346b`. All three identified boundary/time decisions and characterization needs, but they recommended fake or injected database/clock tests without consistently creating the constructor and time seams that make those tests possible; none distinguished seam purpose or recorded a temporary-seam cleanup obligation.
- Pre-fix GREEN snapshot: `019f5346-75a3-7ee2-b28b-3b3fa0406e37` selected `[working-effectively-with-legacy-code, release-it]`; `019f5347-f450-7bc3-a174-27344217de57` selected `[working-effectively-with-legacy-code, refactoring]`; `019f5347-f50e-7580-a081-9fffe7bdc95e` selected only `[working-effectively-with-legacy-code]`. All used `focused` disclosure and are preserved as `green-before-routing-fix-1..3.json`.
- Pre-fix comparison: Legacy Code closed the RED seam gap in `3/3`, but forbidden Refactoring and Release It each appeared in `1/3`.
- Pre-fix reviewer trace: characterization -> Legacy `M2/M4/M16/N2/N4/N9`; clock/database seams -> `M6/M7/M17/M18/N5/N10`; database verification -> `M20`; patch separation -> `M8/N7`; product decisions -> `M2/M16` plus general judgment. Release It supported rollout diagnostics in run 1; Refactoring supplied no unique recommendation in run 2.
- Pre-fix verdict: **fail**.
- Before-final-boundary GREEN runs: `019f5354-1e96-7802-ac75-77ede9f2f5eb` selected `[working-effectively-with-legacy-code, release-it]`; `019f5355-6a35-7942-a327-52eba29de7e8` selected only `[working-effectively-with-legacy-code]`; `019f5355-69ed-7510-bc60-3861a7e58637` selected `[working-effectively-with-legacy-code, refactoring, clean-code]`. Legacy Code led every run and all used `focused` disclosure.
- Before-final-Release snapshot: `019f5365-35ff-74d3-bf61-6a26c55dcb6d` and `019f5366-6613-73a3-a65c-77b65897d293` selected only `[working-effectively-with-legacy-code]`; `019f5366-660f-7f42-8652-0f8c780739d1` selected `[working-effectively-with-legacy-code, release-it]`. All used `focused` disclosure and are preserved as `green-before-final-release-narrowing-1..3.json`.
- Final GREEN runs after the money/transaction exclusion: `019f536c-2ae4-7111-acea-5d457c03c732` selected `[working-effectively-with-legacy-code, release-it, clean-code]`; `019f536c-2ae4-7372-af2e-ffd6d40356da` and `019f536c-2acd-76b3-a53a-1442aa83b99a` selected only `[working-effectively-with-legacy-code]`. Legacy Code led and disclosure was `focused` in `3/3`.
- Final delta: forbidden Refactoring improved to `0/3`, but Release It remained at `1/3` after its explicit database/money/transaction exclusion and Clean Code appeared in that same run. Required Legacy discovery, ordering, application, and focused disclosure pass `3/3`; near-neighbor exclusion passes only `2/3`.
- Independent reviewer trace: characterization and preserved outcomes -> Legacy `M2/M4/M16/N2/N4/N9`; database/clock seams -> `M6/M7/M17/M18/N5/N10`; real-boundary verification -> `M20`; patch separation -> `M8/N7`; product boundary, timezone, and rollout decisions -> `M2/M16` plus general judgment. These recommendations use `Testing Strategy Rules`, `Seam Rules`, `Dependency Breaking Rules`, `Handling Risky Areas`, and bounded `Testing Rules`; no forbidden review/catalog section is needed. Release It and Clean Code supply no unique material recommendation in final run 1.
- Current verdict: **fail**. The Refactoring/Legacy boundary now passes, but catalog exclusion remains stochastic despite the narrowed descriptions.

### O3: Dependency control then conditional extraction

- Class: ambiguous compatible co-invocation, focused application, and ordering
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/03-mixed-seam-and-conditional-extraction.md`
- Required skills: `{working-effectively-with-legacy-code, refactoring}`
- Allowed skills: `{clean-code}`
- Forbidden skills: `{release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required order: `working-effectively-with-legacy-code`, then `refactoring`
- Reference mode: `focused`
- Expected sections: Legacy Code `Testing Strategy Rules`, `Seam Rules`, and `Dependency Breaking Rules`; Refactoring `Safety Rules`, `Preferred Refactoring Moves` or `Rules for Working with Conditionals`, and `Testing Rules`.
- Forbidden sections: Legacy Code `Review Checklist`; Refactoring `Refactoring Catalog Index` and `Review Checklist`.
- Baseline runs: retroactive baseline `019f5338-588e-75c0-8cd5-622babcdf13e`, `019f5338-588f-7d02-b51a-e194293becb7`, and `019f5339-a3a0-7b40-88f5-ee6521c5252b`. All three gained dependency control and characterized behavior first. Two clearly separated seam, semantic rule, and structural extraction; one introduced the shared eligibility owner and the semantic rule in the same step, leaving the behavior-preserving extraction boundary less reviewable.
- Pre-fix GREEN snapshot: `019f5347-f53c-71e2-90a3-455856acf39e` selected `[working-effectively-with-legacy-code, refactoring, clean-code]` with `ordinary` disclosure; `019f5347-f574-7561-8604-fbe77ffbdda9` selected the same set with `focused` disclosure; `019f5349-adb2-71a2-84a5-487ef1ab048c` selected `[working-effectively-with-legacy-code, refactoring]` with `focused` disclosure. These are preserved as `green-before-routing-fix-1..3.json`.
- Pre-fix comparison: required Legacy-then-Refactoring discovery passed in `3/3`, but disclosure was focused in only `2/3` and the requested semantic-then-extraction order appeared in only `1/3`.
- Pre-fix reviewer trace: control and seams -> Legacy `M2-M7/M16-M18/N2-N5/N9-N10`; patch separation -> Legacy `M8/N7` plus Refactoring `M1-M4/M13/M23/N1-N3/N13`; ownership/conditional extraction -> Legacy `M22` plus Refactoring `M5/M6/M10/M18/M21/N5/N12`; product boundary decisions -> Legacy `M2/M16` plus general judgment.
- Pre-fix verdict: **fail**.
- Before-final-boundary GREEN runs: `019f5355-69db-7020-a3f0-e0f2b4f051f8` and `019f5355-6938-72f0-9844-2e9ca0eac964` selected `[working-effectively-with-legacy-code, refactoring, clean-code]`; `019f5356-f9b5-7913-9ea8-cd2f5ada3ad3` selected `[working-effectively-with-legacy-code, refactoring]`. Required lens order and `focused` disclosure held in `3/3`.
- Final-boundary GREEN runs: `019f5366-6611-7c20-96f4-db5f190ce2b6`, `019f5366-6634-7762-9cfb-b6bae9ce457a`, and `019f5367-b897-7093-93a6-830c0dd87303` each selected `[working-effectively-with-legacy-code, refactoring]` in that order with `focused` disclosure. O3 was not rerun after the Release-only narrowing by explicit instruction.
- Final delta: catalog selection, lens order, Release exclusion, and focused retrieval pass `3/3`; allowed Clean Code fell from `2/3` to `0/3`. All three final answers choose seams/characterization, then behavior-preserving eligibility extraction, then the semantic rule. That is source-supported preparatory refactoring but violates O3's frozen prompt order, which explicitly asks for the rule and then duplication elimination.
- Independent reviewer trace: control and seams -> Legacy `M2-M7/M16-M18/N2-N5/N9-N10`, `Testing Strategy Rules`, `Seam Rules`, and `Dependency Breaking Rules`; patch separation -> Legacy `M8/N7` plus Refactoring `M1-M4/M13/M23/N1-N3/N13`, `Safety Rules`, and `Testing Rules`; shared conditional ownership -> Legacy `M22` plus Refactoring `M5/M6/M10/M18/M21/N5/N12`, `Preferred Refactoring Moves`, and `Rules for Working with Conditionals`.
- Frozen-case verdict: **fail on prescribed patch order**, while discovery, lens order, disclosure, application safety, and fidelity pass `3/3`. O3b is the replacement control for agent-chosen ordering.

### O3b: Mixed change with agent-chosen patch order

- Class: ambiguous compatible co-invocation, focused application, and order choice
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/03b-mixed-order-choice.md`
- Required skills: `{working-effectively-with-legacy-code, refactoring}`
- Allowed skills: `{clean-code}`
- Forbidden skills: `{release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required lens order: `working-effectively-with-legacy-code`, then `refactoring`
- Required patch order: none; the answer must choose and justify the safest source-supported order.
- Reference mode: `focused`
- Expected sections: Legacy Code `Testing Strategy Rules`, `Seam Rules`, and `Dependency Breaking Rules`; Refactoring `Safety Rules` plus `Preferred Refactoring Moves` or `Rules for Working with Conditionals`.
- Forbidden sections: Legacy Code `Review Checklist`; Refactoring `Refactoring Catalog Index` and `Review Checklist`.
- Baseline runs: `019f5363-1013-7332-b1fd-ea13d058d87b`, `019f5363-1011-7563-b757-42613e956ae7`, and `019f5363-1013-7e40-b900-3218f681965e`. All gained dependency control first and separated patches; runs 1-2 chose extraction before semantics, while run 3 chose semantics before extraction. RED therefore demonstrates two defensible orders but has no local retrieval/source evidence.
- Before-final-Release GREEN runs: `019f5369-4634-7051-bd94-22a1ef0cfdb4` and `019f5369-45ec-7a01-bf33-f6ce75fe9f3d` selected `[working-effectively-with-legacy-code, refactoring]` with `focused` disclosure; `019f5369-4614-7992-8436-165089f66ed5` selected the same pair with `ordinary` disclosure.
- Final GREEN runs: `019f536d-7342-7c53-8223-3b36a2af0363` and `019f536d-7317-75e1-9207-12075aee0c5c` selected `[working-effectively-with-legacy-code, refactoring]` with `focused` disclosure; `019f536d-7341-7ba3-9afa-c9ae890a1a60` selected `[working-effectively-with-legacy-code, refactoring, clean-code]` with `ordinary` disclosure. Release It remained absent and required lens order held in `3/3`.
- Behavioral delta: every GREEN answer explicitly chooses and defends control -> preparatory extraction -> semantic rule, keeps all three intents separately reviewable, and makes product boundary/null/time decisions explicit. Compared with RED, the gain is consistent lens retrieval and a source-supported ordering rationale rather than a materially new safe sequence.
- Independent reviewer trace: characterization, first-barrier seams, and deterministic feedback -> Legacy `M2-M8/M16-M18/N2-N5/N7/N9/N10` and `Testing Strategy Rules`, `Seam Rules`, `Dependency Breaking Rules`; preparatory extraction, one conditional owner, mixed-intent separation, and stop scope -> Refactoring `M1-M6/M10/M13/M15/M21/M23/N1-N5/N10/N12/N13`, `Safety Rules`, `Preferred Refactoring Moves`, and `Rules for Working with Conditionals`. Clean Code supplies no unique recommendation in final run 2.
- Result: **fail narrowly under the predeclared focused contract**. Selection, lens order, Release exclusion, application, and fidelity pass `3/3`; focused disclosure passes `2/3`. O3b replaces O3's over-prescribed patch-order contract but does not yet close reference-tier acceptance.


### O4: Greenfield pair-specific negative

- Class: counterexample and pair-specific negative
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/04-greenfield-unit-converter-api.md`
- Required skills: `{}`
- Allowed skills: `{clean-code, code-complete}`
- Forbidden skills: `{refactoring, working-effectively-with-legacy-code, release-it, clean-architecture, designing-data-intensive-applications}`
- Required order: none
- Reference mode: `none`, or `ordinary` only when Clean Code is selected.
- Expected sections: none.
- Forbidden sections: every Refactoring and Legacy Code index and full-reference section.
- Baseline runs: retroactive baseline `019f5339-a3a2-7f33-a7d2-a5ff1cc7f015`. It produced a coherent immutable greenfield API with no existing-code lens; no positive behavioral weakness is required for this pair-specific negative.
- Pre-fix GREEN snapshot: `019f5349-ada1-7f30-a5af-f92bc6b29fa0` selected only `[clean-code]` with `ordinary` disclosure and is preserved as `green-before-routing-fix-1.json`.
- Pre-fix comparison: pair-specific discovery, ordinary disclosure, scope, and fidelity matched the contract.
- Pre-fix reviewer trace: small explicit API, immutable runtime state, typed errors, and contract tests -> Clean Code `Errors, Objects, and Boundaries` and `Tests and Emergent Design`; affine conversion details -> general judgment.
- Pre-fix verdict: **pass**.
- Before-final-boundary GREEN run: `019f5356-f9ba-7da2-ba97-73c7361c82af` selected `[clean-code, release-it]` with `focused` disclosure.
- Before-final-Release GREEN run: `019f5367-b88f-7a23-9ff7-b39d60d95a82` selected only `[clean-code]` with `focused` disclosure and is preserved as `green-before-final-release-narrowing-1.json`.
- Final GREEN run: `019f536c-2ade-7722-8f48-72c4459d59b5` again selected only `[clean-code]` with `focused` disclosure. Both overlap skills and Release It are absent.
- Final delta: the final catalog removed the Release It regression and the money/transaction narrowing preserved that exclusion. Pair-specific discovery now passes; the run still exceeds the predeclared `ordinary` ceiling.
- Independent reviewer trace: the compiled immutable API, explicit typed errors, validation boundary, concurrency model, and contract tests are supported by Clean Code `Errors, Objects, and Boundaries` and `Tests and Emergent Design`; affine conversion mathematics is general judgment. Neither overlap skill nor Release It supplies a recommendation.
- Current verdict: **fail under the frozen disclosure contract, pass for the pair-specific negative objective**. The prompt spans several Clean Code concerns, so the focused read is useful, but that cannot retroactively change its predeclared expectation.

### O5: Comprehensive Refactoring audit

- Class: direct invocation and comprehensive retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/05-comprehensive-refactoring-audit.md`
- Required skills: `{refactoring}`
- Allowed skills: `{}`
- Forbidden skills: `{working-effectively-with-legacy-code, clean-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required order: `refactoring`
- Reference mode: `comprehensive`
- Expected sections: all 20 Refactoring full-reference sections, read end to end.
- Forbidden sections: every Legacy Code full-reference section.
- Baseline runs: retroactive baseline `019f5339-a38d-73f2-8799-4a348627f4a8`. It caught the reversed gateway order, feature/API changes, speculative strategy/facade, small extraction sequence, and stop condition, but could not retrieve or demonstrate exhaustive coverage of the repository's 20-section Refactoring policy.
- Pre-fix GREEN snapshot: `019f5349-adaa-79b3-bb11-b673a469cb65` selected only `[refactoring]` with `comprehensive` disclosure and is preserved as `green-before-routing-fix-1.json`.
- Pre-fix comparison: solo discovery, comprehensive disclosure, application, and fidelity matched the contract.
- Pre-fix reviewer trace: classification/mixed intent -> Refactoring `M1/M13/N1/N13`; reversed side-effect order -> `M1/M12`; expedited flag/API change -> `M1/M9/M13`; speculative abstractions -> `M10/M11`; smallest extraction -> `M6/M7/N5`; verification/stopping -> `M2/M3/M14/N2/N3/N8`, supported across `Purpose`, `What Counts as Refactoring`, `Forbidden Patterns`, `Preferred Refactoring Moves`, `Testing Rules`, and `Stopping Rules`.
- Pre-fix verdict: **pass**.
- Before-final-boundary GREEN run: `019f5356-f9b5-7083-9380-93cd4efbddf1` selected `[refactoring, clean-code]` with `comprehensive` disclosure.
- Final-boundary GREEN run: `019f5367-b8b1-7c70-adb9-c4003f016835` selected only `[refactoring]`, read the full runtime reference end to end, and used `comprehensive` disclosure. O5 was not rerun after the Release-only narrowing by explicit instruction.
- Final delta: Refactoring remains first and comprehensive; forbidden Clean Code falls from selected to absent, and every other neighbor remains absent.
- Independent reviewer trace: mixed intent -> Refactoring `M1/M13/N1/N13`, `What Counts as Refactoring`, and `Forbidden Patterns`; reversed side-effect order -> `M1/M12`; feature flag and API changes -> `M1/M9/M13`; speculative abstractions -> `M10/M11`; smallest extraction -> `M6/M7/N5`; verification and stopping -> `M2/M3/M14/N2/N3/N8`, `Testing Rules`, and `Stopping Rules`. The comprehensive read covers all 20 sections.
- Current verdict: **pass**. Solo discovery, comprehensive retrieval, application, neighbor exclusion, and fidelity all match the frozen contract.

### O6: Comprehensive Legacy Code assessment

- Class: direct invocation and comprehensive retrieval
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/06-comprehensive-legacy-assessment.md`
- Required skills: `{working-effectively-with-legacy-code}`
- Allowed skills: `{release-it, designing-data-intensive-applications}`
- Forbidden skills: `{refactoring, clean-code, clean-architecture, code-complete}`
- Required order: `working-effectively-with-legacy-code`
- Reference mode: `comprehensive`
- Expected sections: all 18 Legacy Code full-reference sections, read end to end.
- Forbidden sections: every Refactoring full-reference section.
- Baseline runs: retroactive baseline `019f5339-a38b-7311-bd03-4217368e4114`. It gave a strong Feathers-style assessment, but could not retrieve the repository's complete 18-section policy and expanded toward several operational mechanisms and broad cleanup obligations without recommendation-level local-source support.
- Pre-fix GREEN snapshot: `019f5349-adb1-7b13-98ef-ae67e99147c8` selected `[working-effectively-with-legacy-code, release-it]` with `focused` disclosure and is preserved as `green-before-routing-fix-1.json`.
- Pre-fix comparison: Legacy Code led and Refactoring stayed absent, but the explicit comprehensive request routed to focused; Release It violated the frozen contract.
- Pre-fix reviewer trace: Legacy classification/control -> `M1-M3/N1-N3`; observation -> `M4/M5/M16/N4/N9`; seams -> `M6/M7/M10/M11/M17/M18/N5/N6/N10`; policy extraction -> `M9/M10/M20`; cleanup -> `M15/M21/N8`; duplicate/partial-failure advice -> Release It `Dependency Protection Rules` and `Operational Visibility Rules`.
- Pre-fix verdict: **fail**.
- Before-final-boundary GREEN run: `019f5356-f9c3-76e1-af8f-a96116579668` selected `[working-effectively-with-legacy-code, release-it]` with `comprehensive` disclosure.
- Before-final-Release GREEN run: `019f5367-b899-78e2-8633-fd35d9cc6691` selected the same ordered pair with `comprehensive` disclosure and is preserved as `green-before-final-release-narrowing-1.json`.
- Final GREEN run: `019f536d-72f9-73d3-adb4-df4fd0c31aea` again selected `[working-effectively-with-legacy-code, release-it]` with `comprehensive` disclosure. Refactoring and Clean Code remain absent.
- Final delta: the narrowed Release description correctly does not suppress Release It because duplicate invoices, partial insert/publish failure, retry ownership, idempotency, tax-service degradation, and incident diagnosis make production failure behavior central. Legacy remains first and its comprehensive route remains stable.
- Independent reviewer trace: Legacy classification/control -> `M1-M3/N1-N3`; observation and test points -> `M4/M5/M16/N4/N9`; seams and dependency barriers -> `M6/M7/M10/M11/M17/M18/N5/N6/N10`; policy extraction and cleanup -> `M9/M10/M15/M20/M21/N8`, supported across all 18 Legacy sections. Duplicate/partial-failure semantics, idempotency, retry ownership, tax-service failure, and diagnosis are uniquely supported by Release It `Dependency Protection Rules`, `Operational Visibility Rules`, and general judgment for an outbox/transaction decision.
- Frozen-case verdict: **fail because Release It is forbidden, but pass for overlap, disclosure, application, and current catalog semantics**. O6b is the Legacy-only comprehensive replacement control; O6 remains frozen evidence that its original contract excluded a genuinely relevant neighbor.


### O6b: Comprehensive local-only Legacy assessment

- Class: direct invocation, comprehensive retrieval, and Release It exclusion
- Prompt or artifact: `_skill-workbench/evaluations/cases/refactoring-legacy-overlap/06b-comprehensive-legacy-local.md`
- Required skills: `{working-effectively-with-legacy-code}`
- Allowed skills: `{}`
- Forbidden skills: `{refactoring, clean-code, release-it, clean-architecture, designing-data-intensive-applications, code-complete}`
- Required order: `working-effectively-with-legacy-code`
- Reference mode: `comprehensive`
- Expected sections: all 18 Legacy Code full-reference sections, read end to end.
- Forbidden sections: every Refactoring, Clean Code, and Release It reference section.
- Baseline run: `019f5363-102e-79e0-a043-2152526d3d0b`. It already produced a strong Feathers-style local assessment with change/test points, characterization, seams, dependency barriers, techniques, cleanup, and stop conditions, but had no local skill/reference retrieval and could not demonstrate exhaustive policy coverage.
- Before-final-Release GREEN run: `019f5369-45fe-7fa1-91fe-87082d3b4591` selected only `[working-effectively-with-legacy-code]` with `comprehensive` disclosure and is preserved as `green-before-final-release-narrowing-1.json`.
- Final GREEN run: `019f536e-b442-7390-b748-880c5420ff61` again selected only `[working-effectively-with-legacy-code]`, read the runtime Legacy index/full reference, and used `comprehensive` disclosure.
- Behavioral delta: GREEN adds explicit exhaustive retrieval and a more complete local inventory of observable behavior, constructor/static/time/template barriers, sensing/separation seams, Feathers techniques, temporary-seam cleanup, and stop conditions without importing production-survivability guidance. RED was already strong, so the primary gain is complete local policy coverage and source traceability.
- Independent reviewer trace: behavior delta and characterization -> Legacy `M1-M5/M16/N1-N4/N9`; constructor/static/time/template barriers and seams -> `M6/M7/M10/M11/M17-M21/N5/N6/N8/N10/N11`; local patch separation, cleanup, and stopping -> `M8/M12-M15/M21/M23/N7/N8/N12`. The comprehensive read covers all 18 full sections; footer wording, locale behavior, and presentation semantics are explicitly identified as general/product decisions.
- Result: **pass**. Required solo discovery, comprehensive retrieval, Release/Refactoring/Clean exclusion, application breadth, and fidelity all match. O6b is the accepted comprehensive Legacy replacement for O6.


## Evaluation Protocol Status

- RED baseline: 16 labeled skill-disabled `gpt-5.4` runs over eight durable blind raw-artifact cases: 12 original O1-O6 runs plus three O3b and one O6b replacement-control runs.
- Preserved GREEN evidence: 12 `green-before-routing-fix-<n>.json`, 12 `green-before-final-boundary-fix-<n>.json`, and nine `green-before-final-release-narrowing-<n>.json` records. The new O3b/O6b controls begin in the last of those generations.
- Current GREEN evidence: 16 `green-<n>.json` records. O2/O4/O6/O3b/O6b were rerun after the final Release money/transaction exclusion; O1/O3/O5 were intentionally retained from the immediately preceding final-boundary generation.
- Integrity: all 65 retained JSON artifacts use their case's exact SHA-256, all GREEN runs use explicit `gpt-5.4`, and every `consulted_files` entry resolves under the repository `.agents/skills` tree. No canonical book, workbench, case, or evaluation path was consulted.
- Independent fidelity review: completed recommendation by recommendation from each answer and its verified runtime files. No unsupported strengthening or book-rule rewording was found. General engineering judgments are identified rather than attributed to a source rule, and extra skill selections with no unique recommendation are called out.
- Invalidated evidence: the two earlier harness-biased GREEN sets remain deleted and excluded. Every retained GREEN generation was produced after both harness defects were removed.
- Current acceptance: **failed under the predeclared strict contracts**. O5 and O6b pass; Release E3 replaces O1 successfully; O6 is source-valid with Release and is replaced by O6b; O2 still has a forbidden Release/Clean co-selection; O3b still misses focused disclosure in `1/3`; O4 still exceeds its ordinary ceiling.

## Independent Review

- Reviewer: parent retrofit reviewer, separate from the overlap conversion worker and every blind solver run. The solver was not asked to source-trace; all traces above are reviewer-owned.
- Catalog snapshot: final descriptions for `clean-code`, `release-it`, `refactoring`, and `working-effectively-with-legacy-code`; mini-derived bodies, routers, indexes, and full references unchanged during this rerun.
- Refactoring/Legacy description verdict: the core overlap boundary now holds. O1 excludes Legacy `3/3`; O2 excludes Refactoring `3/3`; O3/O3b select Legacy then Refactoring `6/6`; O4 excludes both; O5 selects Refactoring only; O6/O6b keep Refactoring absent and Legacy first.
- Remaining description defect: final O2 run 1 selects Release It and Clean Code even though Release explicitly excludes work merely involving a database or money/transactions and Clean explicitly excludes a legacy-control task without a separate readability decision. Neither skill supplies a unique material recommendation. The negative descriptions reduce but do not deterministically prevent neighbor loading.
- Reference-router defect: tier choice remains unstable. O1 over-reads focused references in `1/3`; O3b under-reads ordinary in `1/3` against a focused contract; O4 reads focused Clean references against an ordinary ceiling. The answers remain source-supported, but the ordinary/focused decision boundary is not behaviorally reliable.
- Case-design finding: O3 prescribes semantic change before extraction even when the sources support a safer preparatory extraction after control exists. O3b correctly removes that answer from the prompt and should replace O3 for ordering evaluation, while O3 remains frozen historical evidence.
- Body/fidelity verdict: no defect found in either mini-derived body, index, or full reference, and no reworded source rule was detected. The open defects are catalog invocation and reference-tier routing, not guidance content.

## Validation Evidence

- Structural conversion: `SKILL.md` is 67 lines and 842 words against a 739-word canonical mini, for 103 words of packaging overhead. Folder/name/frontmatter, invocation policy, UI metadata, one-level reference links, and mapping identifiers remain structurally valid.
- Full-reference equality: canonical and runtime Refactoring full files remain byte-identical with SHA-256 `d7b9cf2b5ca26f3576943ff59cdeee61b65138213777b0e03bfe1075cbd966fc`.
- Index coverage: all 20 level-two full headings remain indexed once with matching anchors/ranges and nonempty `Read when` guidance; the index remains the single section router.
- Wording fidelity: 24 canonical mini guidance rules map to 24 exact runtime rules with zero missing, added, or reworded rules; the primary bias and final checks also remain exact.
- Current invocation matrix: O1 `[refactoring,(clean-code)]` `3/3`; O2 Legacy first `3/3`, with forbidden Release/Clean in one run; O3 Legacy then Refactoring focused `3/3`; O3b Legacy then Refactoring `3/3`, focused `2/3`, allowed Clean in one run; O4 Clean only focused; O5 Refactoring only comprehensive; O6 Legacy then source-relevant Release comprehensive; O6b Legacy only comprehensive.
- Current application matrix: O1 is sound but has no RED content delta; O2 closes the RED seam gap `3/3`; O3/O3b consistently gain control before a separately reviewable extraction and semantic change; O4 stays greenfield/local; O5 supplies the complete Fowler audit; O6 separates Legacy control from operational semantics; O6b supplies complete local Feathers coverage without Release.
- Remaining risks: negative catalog descriptions are probabilistic in O2; ordinary/focused routing remains unstable; O3b has not yet passed its focused tier `3/3`; O4's predeclared ordinary ceiling may be too strict for its multi-concern prompt; future `refactoring-guru` introduces another collision; index ranges still require regeneration after canonical full changes.

## 2026-07-12 Final Retrofit Reconciliation

This section supersedes every earlier use of `current` above while preserving frozen contracts and intermediate generations.

- O1 excluded Legacy Code in `3/3`; Refactoring remained first and Clean Code was only an allowed local-shape companion. Two runs were ordinary and one focused, so O1 remains a disclosure-boundary observation rather than the sole ordinary proof.
- O2 selected only Legacy Code in `3/3` final runs and excluded Release It!, Clean Code, and Refactoring from the selected set. This closes the earlier catalog leak while preserving Legacy ownership of first feedback.
- O3 and replacement O3b each selected Legacy Code then Refactoring with focused disclosure in `3/3`. O3's frozen prescribed patch-order failure remains historical; O3b validates the safer source-supported agent-chosen order.
- O4 selected only allowed Clean Code in ordinary mode, excluding both overlap skills and Release It!. O5 selected only Refactoring with comprehensive disclosure.
- O6 selected Legacy Code plus source-relevant Release It! comprehensively because production duplicate/partial-failure behavior is explicit. O6b selected only Legacy Code comprehensively and remains the local-only replacement.
- Result-integrity validation caught and preserved one contradictory O3b record and one O2 record before rerun; all final records have consistent selected-skill, consulted-file, and disclosure evidence.
- Final acceptance: **pass** for the Refactoring pilot's discovery, ordering, application, source fidelity, and progressive-disclosure roles. No body or reference rewrite is required before the next conversion batch.
