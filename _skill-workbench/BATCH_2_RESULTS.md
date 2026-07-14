# Rule-Book Skill Conversion Batch 2 Results

Date: 2026-07-12
Acceptance policy reclassified: 2026-07-13

## Verdict

All three skill packages are **accepted conversions**. They are structurally
complete and source-faithful after independent reverse-trace repair. Clean
Architecture passes independent semantic review. DDIA and Code Complete pass
package/source review after their compressed rule defects were repaired through
`_rule-workbench`.

Current positive discovery runs include every required target skill. Explicit
ordinary, focused, and comprehensive probes demonstrate all three disclosure
tiers. Additional skill selections, selection order, exact focused-section
counts, and solver-added general knowledge are retained as diagnostics rather
than conversion failures. No preserved runtime observation justifies adding
unsupported text to a package.

## Scope

This batch converted three deliberately different rule-book shapes under the
authoritative contracts in `_skill-workbench/PROCESS.md` and
`_skill-workbench/EVALUATION.md`:

| Shape | Conversion | Evaluation pressure |
| --- | --- | --- |
| Architectural boundary lens | `clean-architecture` | Separate policy/dependency direction from local readability, protected restructuring, legacy control, and production failure. |
| Distributed-data semantics lens | `designing-data-intensive-applications` | Separate correctness, ownership, replay, ordering, and coordination semantics from generic database work and operational resilience. |
| Broad construction lens | `code-complete` | Preserve broad construction and nano pressure triggers while distinguishing generic work, local readability, compatible overlap, and specialized architecture/data/reliability concerns. |

Each package contains one compact active body, a semantic reference router, a
byte-identical full rule, and UI/invocation metadata:

```text
.agents/skills/<book>/
  SKILL.md
  agents/openai.yaml
  references/index.md
  references/full.md
```

The canonical full files remain unchanged. Independent review found compressed
rules that were not supported by those full files, so the affected DDIA and Code
Complete mini/nano artifacts were repaired through `_rule-workbench` before the
skill packages were regenerated. The conversion mappings and evaluation
evidence remain outside the runtime package under `_skill-workbench/`.

## Conversion Results

| Skill | Lines | Mini/skill words | Packaging overhead | Mini wording | Nano mapping | Full sections | Full copy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `clean-architecture` | 66 | 758/908 | 150 | 23/23 exact | 12/12 | 18/18 | Byte-identical |
| `designing-data-intensive-applications` | 75 | 890/1049 | 159 | 27/27 exact | 11/11 | 26/26 | Byte-identical |
| `code-complete` | 82 | 921/1083 | 162 | 32/32 exact | 16/16 | 27/27 | Byte-identical |

All three primary biases, all 82 mini decision and trigger rules, and every
final-checklist item match the canonical mini wording and order exactly. The
skills reorganize complete rules by concern; they do not paraphrase them into a
new house style. Every nano item has an explicit description, early-guidance,
reference-router, final-check, or justified merged role.

The DDIA and Code Complete packages exceed the 150-word packaging soft target
by nine and twelve words. Both remain below the 200-word hard maximum. These
overages preserve explicit invocation boundaries and ordinary, focused, and
comprehensive routing instructions. Runtime disclosure is evaluated separately
and is not assumed from static clarity.

## Source-Fidelity Retrofit

Exact mini-to-skill wording initially hid defects inherited from mini/nano.
Independent reverse tracing found plausible but unsupported DDIA and Code
Complete mechanisms behind broadly related source citations. The batch stopped
skill acceptance, strengthened `_rule-workbench/PROCESS.md`, repaired mini,
nano, traceability, release metrics, and packages, then repeated review.

The DDIA repair removed or narrowed unsupported request/data-volume examples,
convergence, rollback, warehouse, routing/rebalancing, retention/bootstrap,
session, stale-authority, fencing, stale-leader, and over-broad anomaly or
replica/partition requirements. The Code Complete repair removed unsupported
tuning steps, table synchronization/categories, tooling caveats, recursion,
pre-refactoring tests/analysis, and data-model redesign. Canonical full files
were not edited.

The final independent acceptance review found no P1 or P2 source/package issue.
Its only P3 was stale Code Complete nano-to-description bookkeeping; that
mapping was corrected without changing runtime guidance. Final source/package
verdicts are PASS for all three skills.

The copied full references have these verified SHA-256 values:

- Clean Architecture: `1f0366be1720989c63df6da8f15f12e78f8786f6e712eeb16cf3690b4dab6cc4`
- Designing Data-Intensive Applications: `8c1bfe1529076fda8f828ed6939b63bc3016830ad3c705071699a250e98b8f25`
- Code Complete: `57ca8fab93baea0761eeeca6c491fe79b093df47feb4172c0917a96f8ddc95a4`

## Progressive Disclosure

The intended three-tier disclosure survived conversion:

1. Nano supplies activation vocabulary, salience, pressure triggers, and final
   checks without becoming another packaged reference.
2. Mini supplies complete normal-use guidance in `SKILL.md`.
3. Full remains exhaustive in `references/full.md` and is reached through a
   manually authored semantic index.

Explicit acceptance probes demonstrated all three tiers for every new skill:

| Skill | Ordinary | Focused | Comprehensive |
| --- | --- | --- | --- |
| `clean-architecture` | Skill body only | 4 of 18 coherent sections | `*`, full end-to-end read |
| `designing-data-intensive-applications` | Skill body only | 3 of 26 coherent sections | `*`, full end-to-end read |
| `code-complete` | Skill body only | 5 of 27 coherent sections | `*`, full end-to-end read |

The focused sets were reported as exact level-two headings through the v2 result
contract. Ordinary records have no reference files or reported reference
sections. Comprehensive records use `sections: ["*"]` only after reading the
complete full reference.

## Evaluation Record

The batch added durable raw cases for direct invocation, unnamed distinctive
symptoms, ordinary application, focused disputes, comprehensive retrieval,
pressure, near neighbors, compatible overlap, pair-specific negatives, and
catalog-null behavior. Historical mappings preserve their original exact
required, allowed, and forbidden partitions. Under the current policy, only the
required set is an acceptance contract: every required skill must be included
in the observed selected set, while additional selections are permitted.

The original evaluation runner could record a `full.md` path without proving
which sections were consulted. Batch 2 introduced a v2 result contract with:

- structured per-skill `consulted_reference_sections`;
- `*` reserved for comprehensive reads;
- empty arrays for ordinary or no-skill work;
- passive reporting instructions that prohibit extra reads merely to populate
  evidence fields;
- relational integrity validation across observed selected skills, consulted
  files, actual sections, and disclosure mode.

Exact observed-file reconciliation remains mandatory evidence integrity. It
does not imply that the observed selected set must exactly equal the case's
required set or that a focused run must read an exact expected section count.

Historical v1 records remain preserved. Malformed or superseded records remain
as diagnostic evidence and are not counted as acceptance runs.

## Historical Baseline Timing Note

The raw case fixtures and contracts were frozen before package authoring, but
the skill-disabled baseline executions occurred after draft packages existed,
using a package-free temporary workspace. That isolates the baseline runtime
correctly, but the runs occurred too late to serve as test-first evidence under
the former protocol.

The records remain useful diagnostics. Under the current protocol, a
skill-disabled baseline is optional because conversion acceptance proves source
faithfulness, required-skill discovery, and progressive disclosure rather than
requiring evidence that a pretrained model did not already know the book.

## Behavioral Findings

The pretrained baseline was strong across all three famous books. Many baseline
answers already reached the right broad conclusion. Runtime observations are
therefore used to verify required-skill inclusion and progressive disclosure,
and to diagnose answer variance; they are not required to prove an improvement
over general model knowledge.

### Clean Architecture

- Explicit ordinary work selected only Clean Architecture and used
  `SKILL.md` alone.
- A disputed interface-ownership case used the dependency rule to reject an
  infrastructure-owned abstraction and loaded only `Non-Negotiable Rules`,
  `Required Layer Responsibilities`, `Forbidden Patterns`, and
  `Final Instruction`.
- The comprehensive case read all 18 sections.
- Some application answers invented statuses or error details not supplied by
  the fixture. Those details are answer-level diagnostics, not source text that
  was added to or attributed to the skill.

### Designing Data-Intensive Applications

- Explicit ordinary work selected only DDIA and used `SKILL.md` alone.
- The bounded replica/coordination dispute loaded only `Consistency Rules`,
  `Replication Rules`, and `Distributed Fault, Clock, and Consensus Rules`.
- The comprehensive case read all 26 sections.
- The exactly-once consumer pressure fixture consistently selected DDIA, but
  current runs read 8, 8, and 14 sections instead of remaining ordinary. The
  observed expansion is retained for manual disclosure review. No run reported
  an end-to-end `*` read, so the evidence does not establish material tier
  collapse under the current policy.
- Current explicit runs reintroduced retention/bootstrap, session-token, or
  fencing mechanisms even though the repaired package contains none of them.
  These are general solver additions and remain diagnostics. They do not make
  the source-faithful package fail.

### Code Complete

- Explicit ordinary work selected only Code Complete and used `SKILL.md` alone.
- The table-driven decision dispute loaded only `Primary Directive`,
  `Statement, Conditional, and Loop Rules`, `Table-Driven and Data-Driven
  Rules`, `Testing Rules`, and `Final Instruction`.
- The comprehensive case read all 27 sections.
- One ordinary answer invented shipping values absent from the fixture. This is
  retained as an answer-level diagnostic; it does not justify adding defaults
  to the skill.
- Initial descriptions made the broad construction lens collide with local
  readability and Clean Architecture. An overcorrection then restricted the
  skill to pre-implementation work and suppressed canonical contexts. The final
  description restores construction contexts and nano pressure branches, gives
  Code Complete ownership of shared construction vocabulary, and requires an
  independently explicit objective for another lens.
- Refactoring plus Code Complete includes both required skills in `3/3`. The
  current Clean Code overlap replacement includes both required skills in
  `3/3`.
- Broad greenfield construction includes required Code Complete plus Clean
  Architecture and Clean Code in `3/3`, and local solution-first work includes
  required Code Complete while also adding Clean Code in `2/3`. The additional
  relevant selections are permitted under the current policy.
- The DDIA/Code Complete overlap includes both required skills in `3/3`. The
  diagnosis-only control includes required Legacy Code in `3/3`; its one extra
  Code Complete selection remains diagnostic.
- Generic implementation selects no book skill in `3/3`, and policy-only Clean
  Architecture excludes Code Complete in `3/3`.

## Invocation-Policy Experiment

The batch tested manual-only packaging because the skill-disabled baselines were strong.
Setting `allow_implicit_invocation: false` and front-loading `Explicit
invocation only` in the description did not prevent repo-local discovery:
unnamed matching cases still selected the skills.

The rejected experiment taught two separate lessons:

1. A metadata flag is not an enforceable policy until the target runtime proves
   it in repeated unnamed probes.
2. Leaving a discovered skill marked manual-only when the runtime ignores the
   gate is misleading.

Because these packages must live under the discovered `.agents/skills/`
directory, the final artifacts restore implicit invocation and use explicitly
tested descriptions. Their unnamed positive cases include the intended target
skills. A truly manual-only book must live outside the discovered directory on
this runtime, or wait for an enforceable runtime control.

## Current Evaluation Policy

The authoritative process and evaluation documents now require:

1. Source and package fidelity as the primary hard gate.
2. Exact wording checks plus independent semantic review for strengthening,
   weakening, omission, merging, and imported guidance.
3. Reverse tracing of every prescriptive compressed-rule detail to explicit
   canonical full-rule support.
4. An inventory and source trace for newly authored technical directives;
   packaging-only prose may organize or route but cannot add rules.
5. Positive discovery acceptance by inclusion:
   `required_skills <= selected_project_skills`.
6. Additional selected skills, selection order, and general solver knowledge
   as non-blocking unless they cause materially wrong or contradictory advice.
7. Optional broad, negative, and catalog-null diagnostics instead of exact live
   catalog partitions.
8. Passive evidence reporting so the evaluator never opens references merely
   to make its JSON look complete.
9. Actual per-skill full-section evidence for focused reads without exact
   section-count acceptance contracts.
10. Hard disclosure failure only for material tier collapse; smaller relevant
    over-reads receive manual diagnostic review.
11. Optional skill-disabled baselines for incremental-value studies, not as a
    prerequisite for accepting a faithful conversion.

The batch also confirms the pilot decision not to build an automatic prose
translator. Automation is valuable for copying, hashing, heading extraction,
line ranges, exact wording checks, required-target validation, and result
integrity.
Lens definition, concern grouping, description boundaries, `Read when`
guidance, application fidelity, and collision judgments remain manual work.

## Scaling Decision

Batch 2 passes the current conversion acceptance policy. The three packages
preserve progressive disclosure and need no further source or package
re-authoring. Broad Code Complete overlap, diagnosis-only extra selection,
DDIA/Code Complete disclosure variance, and answer-level solver additions stay
documented as runtime diagnostics.

The next books can use the corrected sequence: reverse-trace inputs, freeze the
fidelity inventory and positive cases, author one book per thread, reconcile the
complete description catalog, verify required-skill inclusion, run disclosure
probes, and review source fidelity independently.
