# Rule-Book Skill Conversion Batch 3 Results

Date: 2026-07-13

## Verdict

All three DDD-family skill packages are **accepted source-faithful
conversions**. Independent reverse tracing repaired compressed source defects
before final package acceptance, all 81 mini rules remain verbatim in the
runtime bodies, and all three canonical full rules remain byte-identical in
`references/full.md`.

Current behavioral gates also pass after two bounded evaluation corrections:

- Implementing DDD's broad comprehensive-read trigger was narrowed without
  changing technical guidance, then its affected positive cases passed their
  separately frozen final-state gate.
- DDD fixtures that primarily exercised Distilled's investment decision were
  retained as failed diagnostics and replaced by pre-audited cases where the
  commitment to deeper modeling was already settled. Every corrected required
  target was then selected.

Historical misses, integrity failures, over-reads, and misclassified fixtures
remain in their mappings and result directories. They are not majority-voted
away or flattened into a new aggregate success ratio.

## Scope

This batch converted three deliberately overlapping books under the
authoritative contracts in `_rule-workbench/PROCESS.md`,
`_rule-workbench/RELEASE.md`, `_skill-workbench/PROCESS.md`, and
`_skill-workbench/EVALUATION.md`:

| Skill | Catalog role |
| --- | --- |
| `domain-driven-design-distilled` | Decide whether DDD investment is warranted and choose the smallest effective DDD practice. |
| `domain-driven-design` | Discover strategic boundaries, language, missing concepts, and deeper implementation-driving models. |
| `implementing-domain-driven-design` | Apply tactical and implementation-level DDD after the context and modeling commitment are settled. |

The complete ten-skill catalog was reconciled before behavioral execution.
The three descriptions state reciprocal boundaries rather than trying to make
overlapping books mutually exclusive. Evaluation requires every target skill,
not target-only selection.

Each runtime package contains one compact active body, a semantic router, a
byte-identical full reference, and UI metadata:

```text
.agents/skills/<book>/
  SKILL.md
  agents/openai.yaml
  references/index.md
  references/full.md
```

Mappings, fixtures, results, and conversion history remain outside runtime
packages under `_skill-workbench/`.

## Conversion Results

| Skill | Lines | Mini/skill words | Packaging overhead | Mini wording | Nano mapping | Full sections | Description |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `domain-driven-design` | 66 | 1,061/1,202 | 141 | 24/24 exact | 15/15 | 38/38 | 469 chars |
| `domain-driven-design-distilled` | 75 | 1,316/1,458 | 142 | 29/29 exact | 8/8 physical bullets | 19/19 | 489 chars |
| `implementing-domain-driven-design` | 79 | 1,511/1,678 | 167 | 28/28 exact | 12/12 | 19/19 | 488 chars |

All three primary biases, all 81 mini decision and trigger rules, and every
final-checklist item match canonical mini wording and order exactly. The
skills reorganize whole rules by concern; they do not paraphrase them into a
new style. Nano supplies salience, activation vocabulary, pressure triggers,
and checklist routing without becoming a duplicate runtime reference.

Implementing DDD exceeds the 150-word packaging soft target by 17 words but
remains below the 200-word hard maximum. Its mapping records the source-driven
size exception. No canonical wording was compressed to reduce overhead.

The copied full references have these verified SHA-256 values:

- Domain-Driven Design: `de806ceb828df4408e452361ab587d81f213443ad057017b1f6bed2334d5aaa6`
- Domain-Driven Design Distilled: `d665da3c697df36fe04f8bb266381e5b40d158aad5283c1d233d4c47319e5b1c`
- Implementing Domain-Driven Design: `cd2c1d404f60720cebca17fcffed9d68d94b1eef4a13bed63a4f59f01db005ad`

## Source-Fidelity Repair

Exact mini-to-skill wording is necessary but cannot prove that mini itself is
faithful. Independent reverse tracing therefore reviewed every prescriptive
compressed detail against the full source before accepting any package.

The DDD source repair restored conditions around domain complexity and Smart
UI, tactical-pattern use, Factories and Repositories, model-first design,
deeper-model migration tradeoffs, relationship-pattern selection, technical
representation boundaries, and checklist qualifiers. The Distilled repair
restored relationship-specific conditions and exceptions, simple-domain and
eventual-consistency defaults, translation qualifiers, application-service
scope, and selective-investment language. The Implementing DDD repair restored
the distinct predicates for Anticorruption Layers versus technical mappings,
Aggregate and Repository conditions, and the rule that Application Services
*may* own transaction and integration coordination rather than always doing so.

Mini, nano, traceability, release metrics, and generated public copies were
updated through `_rule-workbench`; canonical full files were never edited.
Each package was then regenerated from the accepted compressed source and
reviewed independently. Final source-to-package reviews report no P1, P2, or
P3 semantic findings and no imported technical guidance.

## Progressive Disclosure

The intended three levels remain intact:

1. Metadata and nano-derived description vocabulary support discovery.
2. Verbatim mini guidance in `SKILL.md` supports ordinary matched work.
3. `references/index.md` routes concrete source questions into the exhaustive
   byte-identical `references/full.md`.

All three packages demonstrate ordinary body-only use, bounded focused access,
and complete end-to-end access. Exact section counts are diagnostic rather than
acceptance contracts. Broad focused reads receive manual review; only material
tier collapse blocks acceptance.

| Skill | Ordinary evidence | Focused evidence | Comprehensive evidence |
| --- | --- | --- | --- |
| `domain-driven-design-distilled` | Body-only ordinary cases | Bounded source sections | Full `19/19` read |
| `domain-driven-design` | Body-only ordinary and pressure cases | Index plus 4 of 38 coherent sections in a direct run | Full `38/38` read |
| `implementing-domain-driven-design` | Body-only ordinary cases | Bounded implementation section sets | Full `19/19` read |

The final DDD focused replacement was resolved from the compact bodies and was
therefore correctly reported as ordinary. This is not a package disclosure
failure because the needed guidance was already active and another preserved
run demonstrates that the index reaches bounded source detail. It exposed a
fixture-design lesson: a narrow decision is not automatically a focused
reference question.

## Behavioral Results

### Domain-Driven Design Distilled

All `11/11` counted records include every required skill. Direct and unnamed
discovery each pass `3/3`; ordinary, focused, comprehensive, pressure, and DDIA
overlap cases pass their required subsets. Four invalid environment or evidence
records remain preserved and excluded under the integrity contract.

Some valid runs selected neighboring DDD skills or read additional coherent
sections. Those observations are permitted diagnostics. Manual attribution
review kept solver mechanisms such as outbox, saga, exact envelope, uniqueness,
and topology choices separate from Distilled guidance.

### Domain-Driven Design

The original matrix observed `6/11` required-subset inclusion. That record
remains immutable, but post-run ownership review found three misses were not
valid DDD acceptance probes: their central decisions belonged to Distilled's
language-boundary, smallest-investment, or relationship-selection role. The
original pressure fixture also left the modeling commitment open despite
intending to test deeper-model work.

Separately named, independently audited replacements produced this current
evidence:

- distinctive unnamed deeper-model discovery: target included `3/3`;
- ordinary committed-model work: target included `1/1`;
- competing deeper models: target included `1/1`;
- deadline and sunk-cost pressure after model commitment: target included
  `3/3`;
- existing direct discovery: target included `3/3`;
- existing comprehensive and DDIA-compatible probes: required subsets pass.

The four final replacement records have exact case hashes, unique thread IDs,
`exit_code=0`, and empty selection, integrity, and Codex error arrays. Each
selected both DDD and Implementing DDD and stayed body-only. Additional
selection is allowed because the cases combine model evolution with an
implementation slice.

Failed first-round replacements and all three generic-pricing pressure misses
remain diagnostics. They are not counted as evidence against the corrected
DDD ownership contract and did not trigger a description change.

### Implementing Domain-Driven Design

The original matrix observed `10/11` required-subset inclusion; its DDIA
overlap miss remains valid historical evidence. More importantly, two of three
ordinary direct runs read the full target reference because the router treated
any decision spanning several concern families as comprehensive. That was a
packaging-router defect.

The broad trigger was removed from `SKILL.md` and `references/index.md` without
changing any canonical rule, description branch, index row, or full-reference
content. Comprehensive loading now requires a comprehensive audit or explicit
complete-lens request.

The separately frozen current-state gate then passed:

- direct implementation includes the target and avoids end-to-end target reads
  `3/3`;
- the DDIA-compatible overlap includes both required skills `3/3`;
- the existing comprehensive control still reaches the complete target source.

Two final direct runs read broad but coherent `8/19` and `9/19` focused sets;
the third stayed ordinary. Neighboring DDIA over-reads remain diagnostics. The
original required-skill miss and original full-book reads remain preserved and
are not recomputed into the current gate.

## Evaluator Reliability

The first live Batch 3 runs failed before producing solver results because the
active structured-output endpoint rejected JSON Schema `uniqueItems`. The
failure initially left `result=null` and no useful stderr, so it could have
been mistaken for agent behavior.

The evaluator was repaired test-first:

- removed only the unsupported `uniqueItems` keyword from
  `result-v2.schema.json`;
- added regression coverage for the supported schema subset;
- retained Codex JSON-event failures as `codex_errors`;
- preserved every failed harness artifact and used uniquely named replacement
  records;
- added a required live GREEN preflight before parallel batch dispatch.

The evaluator unit suite now passes `31/31`. Harness, environment, and evidence
integrity failures remain distinct from valid skill-selection misses.

## Process Learnings

Batch 3 added four durable corrections to the conversion protocol:

1. **Freeze content before authoring, audit ownership after catalog assembly.**
   Raw fixtures remain immutable, but their required-skill assignments are
   provisional until sibling descriptions can be compared together.
2. **Require distinctive central judgment.** Shared vocabulary or a topic that
   appears somewhere in a book is insufficient to make that skill required.
3. **Replace, never rewrite.** A misclassified or invalid case remains with its
   original contract and result. A corrected current-state probe gets a new
   name, hash, review, and output path before execution.
4. **Do not infer disclosure from concern count.** A focused probe must require
   source detail absent from `SKILL.md`; several concerns do not by themselves
   justify reading a complete book.

Repetition diagnoses nondeterminism but does not majority-vote away a valid
miss. Additional selected skills remain permitted. Answer-level general
knowledge remains diagnostic unless the package itself imported, contradicted,
or falsely attributed it.

The batch further confirms that prose conversion should remain manual.
Automation is appropriate for copying, hashing, heading and line-range
extraction, anchor validation, wording diffs, required-target checks, schema
validation, and result integrity. Catalog boundaries, concern grouping,
source-detail routing, and semantic fidelity still require human or independent
agent judgment.

## Post-Batch Guidance Retrofit

Before selecting Batch 4, the remaining operational gaps were incorporated into
the authoritative process:

- New mappings declare `Evaluation contract version: 2`; a replacement inside
  a historical mapping can opt in at case level without rewriting old evidence.
- Version 2 cases record a repository fixture path and SHA-256, distinctive
  required-skill judgment, neighboring ownership boundary, independent
  ownership verdict, and structured behavioral fields. Focused cases also name
  the compact-body information gap and intended index destinations.
- Mappings now separate source/package verdict, immutable original behavioral
  observation, corrected current-state gate, and residual diagnostics.
- A change-impact matrix defines different rerun scopes for descriptions,
  routers, active guidance, fixture ownership, harness failures, and model or
  runtime changes.
- The live preflight uses a stable direct positive fixture. A valid selection
  miss is catalog evidence, while schema, runtime, and integrity failures remain
  process-boundary evidence.
- `validate_evaluation_contracts.py` remains backward-compatible with historical
  mappings and enforces versioned fields, repository containment, fixture
  existence, exact fixture hashes, focused-only fields, and mapping verdicts for
  v2 mappings.

## Final Verification

- `python3 -m unittest discover -s _skill-workbench/scripts/tests -p
  'test_*.py'`: `39/39` tests pass after the post-batch contract-validator
  additions.
- `validate_conversion.py` across all ten live project book skills: all pass.
  The documented packaging warnings remain below the 200-word hard maximum.
- `check_rule_wording.py` for all three Batch 3 skills: `81/81` mini rules
  match exactly, with exact primary biases and final checklist wording/order.
- `validate_evaluation_contracts.py`: durable required-skill and versioned
  evaluation contracts are valid.
- Official `quick_validate.py` for all three Batch 3 packages: `Skill is
  valid!` with exit 0.
- `cmp -s` and SHA-256 checks: all three packaged full references are
  byte-identical to their canonical full rules.
- README source metrics match the final files:
  - DDD mini `48/1061/7842` and nano `39/488/3552` lines/words/bytes.
  - Distilled mini `57/1316/9169` and nano `31/449/3222`.
  - Implementing DDD mini `59/1511/10887` and nano `37/556/4103`.
- `git diff --check`: exit 0; the scoped untracked-file whitespace scan found
  no trailing whitespace.

## Scaling Decision

Batch 3 is ready to serve as the accepted state for the next conversion batch.
The DDD-family packages require no further source, description, or active-body
changes. Historical misses and over-reading observations remain attached to
their exact contracts as regression evidence.

The next batch should use the corrected sequence: reverse-trace canonical
inputs, freeze raw fixtures, manually author packages, reconcile the complete
catalog, independently audit required-skill ownership and focused information
needs, run one live evaluator preflight, execute required-subset and disclosure
probes, and independently review source attribution before acceptance.

The selected Batch 4 books are:

| Book | Shape being tested | Primary catalog pressure |
| --- | --- | --- |
| `a-philosophy-of-software-design` | Focused module and interface design lens | Distinguish deep-module and complexity ownership from Clean Code readability, Code Complete construction, Clean Architecture boundaries, and Refactoring. |
| `patterns-of-enterprise-application-architecture` | Reference-heavy enterprise pattern catalog | Keep ordinary pattern-selection guidance compact while routing source-level pattern detail; separate it from DDD, Clean Architecture, and DDIA. |
| `the-pragmatic-programmer` | Broad engineering-practice and feedback lens | Preserve nano salience without becoming an always-selected umbrella over Clean Code, Code Complete, Release It!, or Legacy Code. |

`refactoring-guru` remains the only unconverted non-book source. Its 765-line,
478-rule catalog and direct overlap with the accepted `refactoring` skill make
it better suited to a separate final conversion and catalog-collision study
than to this three-book batch.
