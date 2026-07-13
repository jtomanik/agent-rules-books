# Working Effectively with Legacy Code Skill Mapping

## Scope

- Distinctive lens: gain safe-change control over poorly understood or weakly tested existing code through characterization, focused feedback, narrow seams, and deliberate dependency breaking before improving design.
- Intended invocation: select when current behavior cannot be trusted from tests or local reasoning, or hidden/runtime dependencies prevent observing and changing the requested slice safely.
- Closest neighboring skills: `refactoring` governs behavior-preserving structural improvement after control exists; `clean-code` governs local readability and code shape; `refactoring-guru` supplies a smell-and-technique catalog but does not supply legacy observation and dependency-breaking leverage.
- Invocation policy: model invocation is explicitly enabled because the agent must recognize legacy-change risk from code and test conditions even when the user does not name the book.

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |
| Blocked semantic change | `a semantic change is blocked` | Refactoring after behavior is known or protected, and ordinary implementation where feedback already exists. |
| Unknown behavior or weak protection | `current behavior is materially unknown` or `no trustworthy focused tests exist` | Mere omission of test details and well-understood structural cleanup. |
| Observation or substitution barrier | `a dependency cannot be observed or substituted` | Runtime dependencies that exist but do not block first feedback. |
| First-feedback threshold | `must require gaining first feedback before changing behavior` | Requests to add tests after a policy or behavior decision has already been made. |
| Supplied-facts exclusion | `Do not use when observable behavior and operational facts are already supplied, or when first feedback is not blocked.` | Release It! failure-policy work and other supplied-evidence analysis that needs no Legacy control step. |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |
| "We do not know what this branch does and there are no tests. Add an observation point before fixing it." | `working-effectively-with-legacy-code` | Characterization and observation are central; no structural target is known yet. |
| "This class constructs a database client and reads global time, so a focused unit test cannot instantiate it." | `working-effectively-with-legacy-code` | Hard construction and hidden inputs block feedback and call for one narrow dependency break. |
| "Add a billing rule to this untested class, then extract its duplicated conditionals without changing existing behavior." | `working-effectively-with-legacy-code`, then `refactoring` | Legacy guidance establishes control; Refactoring governs the subsequent behavior-preserving structural improvement. |
| "Extract this long method without changing behavior; focused tests already cover it." | `refactoring` | Feedback is trustworthy and the central task is a known structural transformation, so legacy guidance adds no leverage. |
| "Review these names, comments, and command-query boundaries in newly written code." | `clean-code` | Local readability and code shape dominate; there is no weak-feedback legacy condition. |
| "List the code smells and candidate treatments in this well-tested module." | `refactoring-guru` when available, otherwise `refactoring` | Smell catalog and technique selection dominate rather than characterization, seams, or dependency breaking. |
| "Design a new service boundary from scratch." | Neither overlap-pilot skill | Existing-code risk, poor feedback, and behavior-preserving structural work are not central. |
| "The service times out under retry storms; add circuit breakers and bounded queues." | `release-it`, not `working-effectively-with-legacy-code` unless test barriers emerge | Production survivability is central; legacy techniques are conditional implementation support. |
| "Fix this old code." | No automatic book skill until context reveals legacy symptoms | Age alone is not the trigger; uncertainty, weak tests, hidden dependencies, or blocked feedback must be central. |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |
| `N1` | description, early-guidance, final-check | Description; `Primary Bias`; `Establish Control Before Design`; final checklist | Weak protection and behavior delta define the legacy scope. |
| `N2` | description, early-guidance, reference-router, final-check | Description; `Establish Control Before Design`; focused router; final checklist | Characterization is early and routes disputed behavior capture to the full testing guidance. |
| `N3` | early-guidance | `Establish Control Before Design` | The complete mini legacy-loop rule is moved intact rather than split into a workflow section. |
| `N4` | early-guidance, reference-router, final-check | `Build Fast, Trustworthy Feedback`; focused router; final checklist | Focused feedback remains early; test-level disputes route to full testing sections. |
| `N5` | description, early-guidance, reference-router, final-check | Description; `Create Narrow Seams at Real Barriers`; focused router; final checklist | Narrow seam and blocking-dependency guidance remains one concern. |
| `N6` | early-guidance, reference-router | `Use the Smallest Safe Technique`; focused router | Technique families remain intact; exact recipes stay in the full technique index. |
| `N7` | early-guidance, final-check | `Keep Change Local and Honest`; final checklist | Change-kind separation stays authoritative in one section and is restated only as a final check. |
| `N8` | early-guidance, reference-router, final-check | `Create Narrow Seams at Real Barriers`; focused router; final checklist | Cleanup obligations stay beside seam creation and are checked at completion. |
| `N9` | description, early-guidance | Description uncertain-behavior branch; `Establish Control Before Design` | The complete characterization trigger is moved intact. |
| `N10` | description, early-guidance, reference-router | Description feedback-blocking-dependency branch; `Create Narrow Seams at Real Barriers`; focused router | Detailed barrier and technique choice routes to dependency sections. |
| `N11` | early-guidance, reference-router | `Build Fast, Trustworthy Feedback`; focused router | Effect sketches and seams precede semantic edits when local reasoning fails. |
| `N12` | early-guidance, final-check | `Keep Change Local and Honest`; final checklist | Rewrite/broad-cleanup pressure resolves to the next smaller verified move. |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |
| `M1` | `Establish Control Before Design` | Moved verbatim | Keeps the untrusted-tests definition and anti-rewrite/module-cleanup boundary intact. |
| `M2` | `Establish Control Before Design` | Moved verbatim | Keeps behavior delta, preserved behavior, and characterization intact. |
| `M3` | `Establish Control Before Design` | Moved verbatim | Keeps the legacy loop intact under a concern heading rather than turning the skill into a workflow. |
| `M4` | `Build Fast, Trustworthy Feedback` | Moved verbatim | Keeps focused versus broader first-observation tradeoff intact. |
| `M5` | `Build Fast, Trustworthy Feedback` | Moved verbatim | Keeps the complete effect-tracing inventory intact. |
| `M6` | `Create Narrow Seams at Real Barriers` | Moved verbatim | Keeps substitution/observation/interception and sensing/separation distinctions intact. |
| `M7` | `Create Narrow Seams at Real Barriers` | Moved verbatim | Keeps the complete dependency categories and only-where-blocking caveat intact. |
| `M8` | `Keep Change Local and Honest` | Moved verbatim | Keeps separation, small-step verification, and scratch-refactoring restriction intact. |
| `M9` | `Use the Smallest Safe Technique` | Moved verbatim | Keeps technique families and post-test design cleanup intact. |
| `M10` | `Use the Smallest Safe Technique` | Moved verbatim | Keeps construction/use, side effects, pure computation, and policy/mechanism separation intact. |
| `M11` | `Use the Smallest Safe Technique` | Moved verbatim | Keeps barrier-specific selection and fallback seam limits intact. |
| `M12` | `Keep Change Local and Honest` | Moved verbatim | Keeps effect sketches, responsibility grouping, and design-pressure signals intact. |
| `M13` | `Leave Lasting Changeability` | Moved verbatim | Keeps the complete review-risk scan intact. |
| `M14` | `Leave Lasting Changeability` | Moved verbatim | Keeps hidden-dependency, mock-around, cosmetic, and premature-architecture rejections intact. |
| `M15` | `Leave Lasting Changeability` | Moved verbatim | Keeps the changeability target and temporary-technique caveat intact. |
| `M16` | `Establish Control Before Design` | Moved verbatim | Keeps uncertain/ugly/hard-to-prove behavior trigger intact. |
| `M17` | `Create Narrow Seams at Real Barriers` | Moved verbatim | Keeps excessive setup and hard-instantiation barrier list intact. |
| `M18` | `Create Narrow Seams at Real Barriers` | Moved verbatim | Keeps hidden input/output boundary inventory and wrap/inject response intact. |
| `M19` | `Build Fast, Trustworthy Feedback` | Moved verbatim | Keeps large-code effect, interception, pure extraction, and branch-restraint guidance intact. |
| `M20` | `Use the Smallest Safe Technique` | Moved verbatim | Keeps risky-boundary separation and real integration-test caveat intact. |
| `M21` | `Create Narrow Seams at Real Barriers` | Moved verbatim | Keeps temporary/magical seam cleanup obligation intact. |
| `M22` | `Keep Change Local and Honest` | Moved verbatim | Keeps incremental duplication removal under tests and anti-redesign boundary intact. |
| `M23` | `Keep Change Local and Honest` | Moved verbatim | Keeps the smallest safe technique response to rewrite pressure intact. |

## Wording Fidelity

The required wording checker reports exact fidelity: the primary bias, all 23 mini guidance rules, and all nine final-checklist items in source order match verbatim, with zero missing, added, or reworded text. No `M*` or `N*` wording exception requires an original/final/reason record. Frontmatter, concern headings, and reference-router prose are skill metadata and routing additions rather than transformed mini rules.

## Packaging Prose Fidelity

- Newly authored technical directives: none.
- Review: frontmatter, headings, transitions, and reference-routing prose organize discovery and loading only; independent review found no technical rule beyond canonical guidance.

## Size Exception

- Canonical mini: 796 words.
- Before routing fix: `SKILL.md` 909 words; packaging overhead 113 words.
- Before final catalog boundary: `SKILL.md` 914 words; packaging overhead 118 words.
- Current: `SKILL.md` 922 words; packaging overhead 126 words.
- Decision: retain the source-driven exception. Description-only routing metadata changed while the mini-derived body stayed exact; the canonical mini already exceeds the 500-word target, every mini rule remains required for complete ordinary use, and current packaging overhead remains below the 150-word soft target. Do not paraphrase rules during conversion to reduce this count.

## Behavioral Scenarios

| Scenario | Expected invocation | Expected guidance | Reference behavior |
| --- | --- | --- | --- |
| Unknown current branch behavior with no trustworthy tests | `working-effectively-with-legacy-code` | State the delta/preserved behavior, characterize first, and find the closest useful observation point. | Ordinary unless characterization strategy is disputed. |
| Constructor performs I/O and static time lookup, blocking focused tests | `working-effectively-with-legacy-code` | Break the first real barrier with the smallest sensing/separation seam and a cleanup obligation. | Focused: `Dependency Breaking Rules`, `Seam Rules`, and relevant `Handling Risky Areas`. |
| Untested feature addition followed by known duplication extraction | `working-effectively-with-legacy-code`, then `refactoring` | Gain control and feedback first; apply behavior-preserving structural improvement only inside the protected slice. | Focused sections from both indexes. |
| Green-test extraction with fully known behavior | `refactoring`, not legacy guidance | Use small named structural moves and stop at the blocking smell. | No legacy reference. |
| Readability review of new code | `clean-code`, not legacy guidance | Improve local code shape without introducing legacy seams. | No legacy reference. |
| Authority pressure to rewrite a fragile subsystem without characterization | `working-effectively-with-legacy-code` | Reject rewrite-first; choose characterization plus the narrowest seam/dependency break for today's change. | Focused: `Non-Negotiable Rules`, `Forbidden Patterns`, `Final Instruction`. |
| Complete Feathers-based assessment of a risky subsystem change | `working-effectively-with-legacy-code` | Apply all feedback, seam, dependency, technique, risky-area, cleanup, and review guidance. | Comprehensive: read `references/full.md` end to end. |
| Generic implementation request with adequate focused tests | No automatic legacy invocation | Do not impose legacy tactics without uncertainty or blocked feedback. | No reference. |

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
- Post-fix GREEN run: `019f5356-f9ba-7da2-ba97-73c7361c82af` selected `[clean-code, release-it]` with `focused` disclosure and consulted only runtime package paths.
- Routing delta: both overlap skills remained absent, but the catalog regressed from allowed Clean Code alone/ordinary to forbidden Release It plus focused Clean references.
- Post-fix reviewer trace: the answer's builder/immutable API, typed errors, concurrency model, and tests are supported by Clean Code `Errors, Objects, and Boundaries`, `Tests and Emergent Design`, and general judgment for affine mathematics. Release It supplied no material recommendation, and production failure behavior was not central.
- Current verdict: **fail** under the frozen pair-negative contract. The Refactoring/Legacy exclusion still passes, but Release It over-selected and disclosure exceeded the allowed tier.

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
- Post-fix GREEN run: `019f5356-f9b5-7083-9380-93cd4efbddf1` selected `[refactoring, clean-code]` with `comprehensive` disclosure and consulted only runtime paths.
- Routing delta: Refactoring remained first and comprehensive retrieval remained correct, but forbidden Clean Code was newly selected.
- Post-fix reviewer trace: every material recommendation remains fully supported by the same Refactoring IDs/headings as the pre-fix trace. Clean Code supplied no unique recommendation beyond concerns already covered by Refactoring.
- Current verdict: **fail** under the frozen solo-skill contract, despite passing the target Refactoring application and comprehensive-disclosure layers. The Clean Code description introduced a catalog regression for this direct Fowler audit.

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
- Post-fix GREEN run: `019f5356-f9c3-76e1-af8f-a96116579668` selected `[working-effectively-with-legacy-code, release-it]` with `comprehensive` disclosure and consulted only runtime paths.
- Routing delta: explicit comprehensive Legacy routing improved from `focused` to `comprehensive`; Legacy remained first and Refactoring remained absent. Release It remained selected.
- Post-fix reviewer trace: the Legacy recommendations remain supported by the same IDs and full headings as pre-fix. Operational diagnosis, idempotency, timeout/retry, metrics, and outbox/transaction questions are uniquely supported by Release It `Dependency Protection Rules`, `Operational Visibility Rules`, and general judgment; production failure behavior is central in this artifact.
- Current verdict: **fail under the frozen strict contract, but pass for the overlap and disclosure objectives**. If O6 is corrected to allow Release It, the post-fix run passes discovery, comprehensive retrieval, application, and fidelity.


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
- Baseline run: `019f5363-102e-79e0-a043-2152526d3d0b`. It already produced a strong local Legacy assessment but had no repository skill/reference retrieval and could not demonstrate exhaustive policy coverage.
- Final GREEN run: `019f55ce-183c-7691-b6ba-192388b77890` selected only `working-effectively-with-legacy-code`, read its index and full reference, used comprehensive disclosure, and passed result-integrity validation.
- Behavioral delta: GREEN adds exhaustive local retrieval across characterization, seams, dependency barriers, local techniques, cleanup obligations, and stop conditions without importing production-survivability guidance.
- Source trace: Legacy `M1-M21/M23`, `N1-N12`, and all 18 full-reference sections; local formatting and archived-customer semantics remain general judgment.
- Result: **pass**.


## Evaluation Protocol Status

- RED baseline: complete as 12 labeled retroactive skill-disabled runs over six durable raw-artifact cases; baselines were not rerun for the routing change.
- Pre-fix GREEN evidence: 12 valid `gpt-5.4` records preserved in place as `green-before-routing-fix-<n>.json`.
- Post-fix GREEN evidence: 12 fresh `gpt-5.4` records written as `green-<n>.json` over byte-identical cases. Across all 36 baseline/pre-fix/post-fix records, case hashes match; every pre/post `consulted_files` path is under `.agents/skills/`.
- Before/after: O1 eliminated Legacy over-selection (`3/3 -> 0/3`) but not reference over-reading; O2 selection instability persisted; O3 focused disclosure improved (`2/3 -> 3/3`) and requested patch order improved (`1/3 -> 2/3`) without stabilizing; O4 regressed through Release It; O5 regressed through Clean Code; O6 comprehensive routing was fixed.
- Fidelity trace: completed independently for every post-fix answer from only its answer and verified runtime files. No unsupported strengthening, canonical-source access, or mini-rule rewording was found; unnecessary skill selections are called out when they supplied no unique recommendation.
- Invalidated evidence: the two earlier biased GREEN sets remain deleted and excluded; only the final unbiased pre-fix snapshot and current post-fix runs are compared.
- Acceptance under the frozen case contracts: **failed**. Description routing improved the intended Legacy/Refactoring boundary but did not produce catalog-wide convergence. Mini-derived skill bodies remain unchanged and exact.

## Independent Review

- Reviewer: parent retrofit reviewer, separate from the overlap conversion worker and from every blind solver run.
- Catalog snapshot: updated descriptions for `clean-code`, `release-it`, `refactoring`, and `working-effectively-with-legacy-code`; mini-derived bodies and full references unchanged.
- Semantic verdict: the new description boundaries preserve source guidance, and reviewer traces found no unsupported or reworded book rule in material recommendations.
- Improvements: Legacy exclusion for well-tested cleanup now holds in O1; mixed-case focused disclosure now holds in O3; explicit comprehensive Legacy routing now holds in O6.
- Residual defects: O2 still selects Refactoring in `1/3`; O3 still reverses the requested semantic/extraction order in `1/3`; O1 still over-reads references.
- Regressions: Release It now over-selects O4 despite no central production-failure decision and supplies no unique advice; Clean Code now over-selects O5 and supplies no unique advice.
- Contract note: Release It is genuinely relevant in O6 because duplicate/partial-failure/idempotency behavior is central. O6 passes the intended overlap/disclosure study if Release It is allowed; O2 still fails even if Release It is allowed.

## Validation Evidence

- Structural validation: the official `quick_validate.py` passed through `uv run --with pyyaml`; `SKILL.md` is 71 lines; independent metadata validation confirmed folder/name equality, frontmatter keys, explicit implicit-invocation policy, quoted UI strings, a 46-character `short_description`, and one exact `$working-effectively-with-legacy-code` token in `default_prompt`.
- Full-reference equality: `cmp` passed and both files have SHA-256 `8b22bfc3d2851509d4cd8e05fbb9aca9e934f4b6915cb65fe8d6d9d241393fce`.
- Index validation: all 18 level-two full headings appear once with matching anchors and ranges from the heading through the last non-empty line before the next heading or EOF; every `Read when` cell is nonempty; both one-level reference links resolve. The index is the single source of truth for section routing.
- Wording fidelity: `23/23` exact mini guidance rules; zero missing, added, or reworded rules.
- Traceability validation: all `M1`-`M23` and `N1`-`N12` identifiers appear exactly once in their mapping tables.
- Invocation evaluation: after the routing fix, O1 selected Refactoring first and excluded Legacy in `3/3`; O2 selected Legacy first in `3/3` but still added Refactoring/Clean Code in `1/3`; O3 selected Legacy then Refactoring in `3/3`; O4 excluded both overlap skills but added Release It; O5 selected Refactoring first plus Clean Code; O6 selected Legacy first plus source-relevant Release It.
- Application evaluation: O1 remained sound but showed no RED improvement and over-read in `2/3`; O2 retained the DB/clock-seam improvement in `3/3`; O3 now used focused disclosure in `3/3` and followed requested patch order in `2/3`; O4 and O5 retained strong answers but regressed in catalog precision; O6 now obeyed comprehensive Legacy routing.
- Remaining risks: Refactoring/Clean Code still leak into one Legacy-only run; Release It can over-select greenfield concurrency despite its new negative boundary; Clean Code's boolean-mode/rewrite triggers can over-select explicit Refactoring audits; ordinary/focused tier choice remains unstable; O3 patch-order tie-breaking remains stochastic; future `refactoring-guru` adds another collision; index ranges still require regeneration after canonical full changes.

## 2026-07-12 Final Retrofit Reconciliation

This section supersedes every earlier use of `current` and the pending O6b text above while retaining them as historical evidence.

- The final positive-only description activates on blocked first feedback and avoids repeating neighbor-case keywords in negative clauses. It is 367 characters and preserves the nano triggers for unknown behavior, weak focused tests, and hard dependencies.
- O2 selected only Legacy Code with focused disclosure in `3/3`: `019f55ca-04d8-7fd3-9485-6bd29275d967`, `019f55c7-71ab-7fb0-b889-e0b88e021bd6`, and `019f55c7-71f4-7c73-8f32-9c7bc4fd7236`.
- Supervised-consumer E2 supplied behavior and operational facts, so Legacy Code remained absent while Release It! handled the failure policy in `3/3`.
- O1 excluded Legacy Code `3/3`; O3 and O3b selected Legacy Code before Refactoring with focused disclosure `6/6`; O4 and O5 excluded Legacy Code; O6 kept Legacy first with justified Release It! overlap.
- O6b final run `019f55ce-183c-7691-b6ba-192388b77890` selected only Legacy Code and used comprehensive disclosure. Its baseline and earlier final run remain preserved; the pending block above is obsolete.
- Final acceptance: **pass** for Legacy discovery, first-feedback ownership, overlap ordering, local-only comprehensive retrieval, and source fidelity. No body or reference rewrite is required before the next conversion batch.
