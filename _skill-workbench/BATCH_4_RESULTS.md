# Rule-Book Skill Conversion Batch 4 Results

Date: 2026-07-14

## Verdict

All three Batch 4 packages are accepted source-faithful conversions. Independent
reverse tracing corrected defects in the compressed source before package
acceptance, all 88 mini rules remain verbatim in the runtime bodies, and all
three canonical full rules remain byte-identical in `references/full.md`.

A Philosophy of Software Design and Patterns of Enterprise Application
Architecture each pass an `11/11` valid behavioral matrix. The Pragmatic
Programmer's original matrix preserves one valid focused required-skill miss and
one invalid self-report record. A source-backed description correction adds the
missing blackboard-style coordination activation branch. The corrected catalog
and description passed independent review, and the complete post-description
matrix now passes `11/11` with no attribution finding.

Historical invalid fixtures, failed records, over-reads, extra selections, and
general-solver additions remain attached to their exact contracts. They are not
overwritten, retried into a majority result, or treated as source claims.

## Scope

This batch converted three different rule-book shapes under the authoritative
contracts in `_rule-workbench/PROCESS.md`, `_rule-workbench/RELEASE.md`,
`_skill-workbench/PROCESS.md`, and `_skill-workbench/EVALUATION.md`:

| Skill | Shape tested | Catalog role |
| --- | --- | --- |
| `a-philosophy-of-software-design` | Focused module and interface design lens | Own module depth, information hiding, interface complexity, and local complexity reduction. |
| `patterns-of-enterprise-application-architecture` | Reference-heavy enterprise pattern catalog | Choose force-fit application patterns and place business logic, persistence, transactions, state, and remote boundaries. |
| `the-pragmatic-programmer` | Broad engineering-practice and feedback lens | Own accountable, adaptable delivery when knowledge authority, change fan-out, reversibility, automation, feedback, or source-specific coordination are central across a change. |

The complete 13-skill description catalog and all 21 active Batch 4 fixture
contracts were audited together. Required sets are minimum central sets:
additional relevant skill selections remain permitted.

Each runtime package retains the accepted progressive-disclosure shape:

```text
.agents/skills/<book>/
  SKILL.md
  agents/openai.yaml
  references/index.md
  references/full.md
```

Mappings, fixtures, result records, and conversion history remain outside the
runtime packages under `_skill-workbench/`.

## Conversion Results

| Skill | Lines | Mini/skill words | Packaging overhead | Mini wording | Nano mapping | Full sections | Description |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `a-philosophy-of-software-design` | 61 | 841/981 | 140 | 23/23 exact | 14/14 | 24/24 | 496 chars |
| `patterns-of-enterprise-application-architecture` | 73 | 1,167/1,284 | 117 | 28/28 exact | 13/13 | 19/19 | 484 chars |
| `the-pragmatic-programmer` | 80 | 992/1,106 | 114 | 37/37 exact | 19/19 | 26/26 | 497 chars |

All three primary biases, all 88 mini decision and trigger rules, and every
final-checklist item match the repaired canonical mini wording and order exactly.
Rules are reorganized by concern but not paraphrased. Nano contributes discovery
vocabulary and salience without becoming a second runtime rules body.

The copied full references have these verified SHA-256 values:

- A Philosophy of Software Design: `b521814b9d050d0d12594e13aa291029148a971b6f7d5a5ac3e74219de6c8563`
- Patterns of Enterprise Application Architecture: `e7f30e7d65005924ec29cc0c6f032aedd0b1bffa22223d5386c5a3140cd76af0`
- The Pragmatic Programmer: `ea10063caff1989c1442c2aff501a942281fb5b06456e822ab856c701fc5e28d`

## Source-Fidelity Repair

Exact mini-to-skill wording cannot prove that mini itself is faithful. Reviewers
therefore reverse-traced every prescriptive compressed clause against the full
source, including unchanged clauses activated by the new package.

The APoSD repair restored source conditions around deep modules, information
hiding, interface design, complexity placement, comments, errors, exceptions,
and tactical versus strategic choices. The final rereview closed two P1 and two
P2 findings with no remaining unsupported package guidance.

The POEAA repair restored force predicates and applicability qualifiers for
business-logic, persistence, Unit of Work, loading, locking, transactions,
session state, integration, distribution, and tests. It also separated Remote
Facade from DTO scope and preserved two pre-run fixture defects as inactive
diagnostics. The final rereview closed two P1, five P2, one P3, and one mapping
placement correction with no remaining semantic finding.

The Pragmatic Programmer repair removed unsupported blame, routing, metadata,
regression-test, example, and recovery qualifiers; restored repeated-tool
friction; and corrected generated-code/formal-method and working-slice wording.
The source body passed rereview. The later description-only correction adds one
activation phrase directly supported by the canonical blackboard-style
coordination rule; mini, nano, body, router, and full reference remain unchanged.

Canonical full files were never edited. Repairs flow through `_rule-workbench`
mini, nano, traceability, generated public copies, mappings, and then packages.

## Fixture And Catalog Audit

The first catalog audit approved 21 active contracts but recorded the wrong
catalog hash. That proof was not accepted as current evidence. The corrected
snapshot is built by sorting all 13 skill names and hashing the exact UTF-8
payload `<skill-name>\t<description>\n` for every live description.

The final catalog SHA-256 is
`5d8299b7aa84498bc11c4120b790b07edd6485ebc21c60a0f280b541e4432e4d`.
Independent re-audit reproduced the 13-row, 6,335-byte payload, approved all
21 active ownership contracts with zero findings, and froze this snapshot
before the corrected Pragmatic matrix began.

Two POEAA fixtures demonstrate the replacement rule before any solver run:

- E4 revealed the private compact-body omission. It remains frozen and unrun;
  E4b is the independently audited blind focused replacement.
- E6 made DDIA and Release It! independently central despite declaring a
  target-only required set. It remains frozen and unrun; E6b removes those
  distributed and production-failure concerns without rewriting the old case.

All other active cases retain exact repository paths, SHA-256 hashes, distinctive
required judgments, neighboring ownership boundaries, disclosure expectations,
package-fidelity traces, and independent-review fields.

## Progressive Disclosure

The intended levels remain:

1. Description metadata uses nano-derived trigger vocabulary for discovery.
2. Verbatim mini guidance in `SKILL.md` supports ordinary matched work.
3. `references/index.md` routes unresolved source questions into bounded sections
   or the complete byte-identical `references/full.md`.

APoSD produced ordinary `7`, focused `3`, and comprehensive `1` valid records.
Its direct preflight read 7 of 24 sections and its pressure case read 10 of 24;
both are coherent nonblocking over-reads. The focused control read three relevant
sections instead of the smallest one, and the comprehensive control read `*`.

POEAA produced ordinary `7`, focused `2`, and comprehensive `2` valid records.
One direct run read 8 of 19 sections, while the broad DDIA overlap read 11 of 19
POEAA sections plus the complete DDIA source. Both are preserved high-context
diagnostics. The inheritance control reached exactly its one intended section,
and the comprehensive control read `*`.

The original Pragmatic records include a 17-section direct over-read and an
8-section target plus 6-section APoSD unnamed over-read. Its focused blackboard
case selected only DDIA, demonstrating that a valid router destination is not
enough when description metadata fails to activate the target skill. The
post-description matrix produced ordinary `8`, focused `2`, and comprehensive
`1`: direct and unnamed cases stayed body-only, the blackboard control reached
exactly `Resource and Coupling Rules`, the comprehensive control read `*`, and
the pressure case made one nonblocking 11/26-section focused over-read.

Exact section counts are diagnostics, not acceptance contracts. Manual review
blocks only material or systematic disclosure-tier collapse.

## Behavioral Results

### A Philosophy of Software Design

All `11/11` valid records include every required skill. Direct and unnamed
recognition each pass `3/3`; ordinary, focused, comprehensive, pressure, and
Refactoring-compatible overlap cases pass. The overlap includes both required
skills. One unnamed run additionally selected Clean Architecture, an allowed
source-backed extra. Independent attribution review found no unsupported or
crossed source claim.

### Patterns of Enterprise Application Architecture

All `11/11` valid records include every required skill. Direct and unnamed
recognition each pass `3/3`; ordinary, focused replacement, comprehensive,
pressure replacement, and DDIA overlap cases pass. The overlap includes both
required skills and applies their concerns independently.

One unnamed run additionally selected Clean Architecture. The ordinary customer
credit answer offered `FOR UPDATE` although the fixture did not establish
expected contention; it also supplied a guarded-update alternative, and the
review classifies the lock as conditional general-solver guidance rather than a
source or package defect. General outbox, retry, reconciliation, status, schema,
and API choices remain separately identified.

### The Pragmatic Programmer

The original stopped matrix contains seven valid records, one invalid direct
self-report record, and one valid focused required-skill miss. Three direct and
three unnamed valid recognition samples include the target. The invalid direct
record read the index while reporting ordinary mode; the unchanged runner
rejected it, the JSON remains preserved, and one uniquely named same-configuration
replacement completed the missing direct sample.

The focused blackboard case validly selected DDIA but omitted the required target.
It was not retried, outvoted, or reclassified. Independent diagnosis traced the
miss to the target description's missing source-backed coordination branch, not
to fixture ownership, compact guidance, router destination, or DDIA relevance.
After the description correction and corrected catalog freeze, the current
matrix passes `11/11`: direct and unnamed discovery are `3/3` each, E3-E6 include
the target, and E7 includes both required Pragmatic and Release It! guidance.
Independent attribution review found no unsupported, weakened, strengthened,
contradictory, or falsely attributed source claim.

The original miss and invalid integrity record remain immutable historical
evidence. The current rerun also preserves one invalid repeated reporting record
and one invalid wrong-required-set invocation; uniquely named replacements pass
after their documented process corrections.

## Process Learnings

Batch 4 adds these durable corrections:

1. **Review the activated package, not only changed source lines.** A conversion
   makes every prescriptive compact clause active. The source diff is a locator,
   not the semantic review boundary.
2. **Audit frozen fixtures before execution.** A rejected fixture remains with
   its original bytes, hash, and required set even when it has no solver output;
   a blind named replacement receives a separate contract.
3. **Keep focused-test rationale private.** Mappings may state the compact-body
   gap, but raw fixtures cannot reveal the omission or conversion hypothesis.
4. **Separate invalid reporting from valid behavior.** A correctly rejected
   self-report inconsistency may receive one named identical-config replacement;
   a valid required-skill miss may not.
5. **Treat the catalog hash as evidence.** Recompute the documented payload, void
   an incorrect snapshot, and re-audit all active ownership records after a
   description changes.
6. **Description discovery precedes routing.** Source detail and a correct index
   route cannot help when metadata never selects the skill. A source-backed
   activation correction invalidates discovery and every positive case requiring
   that skill, while leaving unrelated package evidence intact.
7. **Represent index-only access truthfully.** Focused disclosure begins when the
   router index is read and may stop there or continue into bounded full sections.
   An index-only focused record is an over-read diagnostic, not proof that a
   focused source-detail control reached its required section.
8. **Verify the executed required set.** A selection error is behavioral only
   when the JSON `required_project_skills` exactly matches the frozen case. One
   ordinary run accidentally required Release It!; its JSON remains invalid
   process evidence and a correctly configured named replacement passes.

The authoritative process and evaluator contract now encode these rules. The v2
contract validator also requires explicit `## Independent Review` fields and
requires `## Verdicts` to be the final level-two mapping section.

## Evaluator Reliability

All valid Batch 4 records use `gpt-5.4`, `green` mode, exact fixture hashes,
unique thread IDs, inner exit zero, and empty Codex and integrity error arrays.
The Pragmatic lane includes one documented reporting-contract clarification;
its earlier valid body-only record remains valid under the harness-repair rule
because its task fixture and ordinary evidence semantics were unaffected.
Selection acceptance checks `required <= selected`; it does not demand exactly
one skill or forbid general knowledge.

The repeated Pragmatic index-only/ordinary inconsistency exposed a missing
reporting state rather than a package defect. The evaluator was repaired
test-first while retaining the same three disclosure levels; the invalid records
remain preserved and a uniquely named live replacement passes. A separate
ordinary run accidentally required Release It!; its JSON exposed the dispatch
error, remained invalid process evidence, and a correctly configured replacement
passed. Ten POEAA records also contain the same nonfatal shell-snapshot cleanup
warning with empty `codex_errors`; attribution review classifies it as
environment cleanup noise rather than agent or package behavior.

## Final Verification

- `validate_conversion.py` across all 13 live skills: all pass; only documented
  packaging-overhead warnings remain below the 200-word hard maximum.
- `check_rule_wording.py` for Batch 4: `88/88` mini rules match exactly, with
  exact primary biases and final checklist wording/order.
- Official `quick_validate.py` for all three packages: `Skill is valid!`.
- `python3 -m unittest discover ...`: `42/42` tests pass.
- `validate_evaluation_contracts.py`: durable required-skill and v2 contracts
  pass.
- `cmp` and SHA-256 checks: all three full references are byte-identical to the
  canonical sources.
- README source metrics match the final mini and nano files.
- Final catalog ownership passes at `21/21`; the Pragmatic current matrix passes
  `11/11` with independent attribution review.
- All 44 Batch 4 result JSON files parse; the 11 current Pragmatic records have
  11 unique threads, no hard-gate error, and modes `8/2/1`.
- `git diff --check` passes; the scoped 113-file untracked-artifact scan found no
  trailing whitespace or missing final newline.

## Scaling Decision

Batch 4 is the accepted state. The repository now has 13 converted books and one
unconverted source: `refactoring-guru`. Its 765-line, 478-rule catalog directly
overlaps the accepted `refactoring` skill, so it should be treated as a separate
final conversion and collision study rather than padded into an artificial
three-book batch.
