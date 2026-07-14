# Guidance-Skill Evaluation Protocol

## Purpose

The primary evaluation objective is to prove that a converted skill is faithful
to its canonical book rules. Invented, strengthened, weakened, or unsupported
prescriptive guidance is a conversion failure.

Runtime evaluation has three narrower purposes: prove that the intended skill
can be discovered, show that its packaged guidance can be applied, and verify
that progressive disclosure remains useful. It does not require an agent to
select only one book skill or to avoid using general knowledge. Related books
overlap, so additional selected skills are expected.

Static checks, behavioral probes, and independent semantic review provide
different evidence. A good solver answer cannot compensate for an unfaithful
package, and a source-faithful package does not fail merely because a
nondeterministic solver selects another relevant skill or adds general
engineering judgment.

## Acceptance Priority

Evaluate in this order:

1. Source and package fidelity: hard gate.
2. Required-skill discovery: positive inclusion check.
3. Progressive disclosure: hard gate only for material tier collapse.
4. Application observations: supporting evidence and diagnostics.

Do not tune descriptions, routers, or skill prose to satisfy a lower-priority
signal by weakening source fidelity.

## 1. Source And Package Fidelity

Question: does the package preserve the canonical guidance without inventing
technical rules?

Require all of the following:

- `references/full.md` is byte-identical to the canonical full rule.
- The primary bias, every mini rule, and the final checklist retain their
  canonical wording and checklist order except for documented necessary
  exceptions.
- Every nano item affects invocation, salience, routing, or final checking
  without becoming a second or expanded rule.
- Every prescriptive mini and nano detail reverse-traces to explicit support in
  the canonical full rule.
- Every newly authored technical directive in the description, active body,
  checklist, reference map, or exhaustive index has a source trace.
- An independent reviewer checks semantic modality, scope, exceptions,
  mechanisms, examples, and guarantees, not just textual similarity.

New packaging prose is necessary for frontmatter, headings, priority labels,
transitions, and `Read when` routing. It is allowed only when it organizes or
routes canonical guidance. It must not add a technical mechanism, default,
example, guarantee, failure mode, exception, or preference that the source does
not support.

Use deterministic checks to find wording changes and candidate additions, then
review them semantically. Flag unsupported strengthening, weakened modality,
lost exceptions, merged rules whose conditions differ, imported modern
preferences, invented numeric defaults, and requirements stronger than the
source.

If an unsupported detail is copied exactly from mini or nano, classify it as a
source-compression defect. Stop acceptance, repair the compressed rule and
traceability under `_rule-workbench/PROCESS.md`, regenerate the package, and
repeat the affected fidelity checks. Exact packaging cannot legitimize an
unfaithful compressed source.

## 2. Required-Skill Discovery

Question: when a case tests one or more intended skills, did the solver select
at least those skills?

Record a `required` set for each positive case. Discovery passes when:

```text
required skills is a subset of selected skills
```

In set notation:

```text
required_skills <= selected_project_skills
```

Additional selected skills are permitted. Do not fail a case because another
relevant book skill was selected, because selection order differed, or because
the selected set was larger than expected. Books and skills intentionally cover
overlapping topics.

Near-neighbor, broad, pair-specific negative, and catalog-null cases may still
be retained to study description precision and context cost. They are
diagnostics, not conversion acceptance gates. Escalate an additional selection
only when it causes materially wrong or contradictory advice; then determine
whether the package or the general solver caused the problem before changing a
skill.

For an implicitly invoked skill, include at least one unnamed distinctive case
whose required set contains that skill. Direct invocation proves explicit
retrieval; unnamed invocation proves description-based discovery. Neither must
show that the skill was selected alone.

Nano supplies the default discovery vocabulary, but it is not assumed to be an
exhaustive catalog of distinctive activation conditions. Before freezing a new
description, audit full-only named mechanisms and decision families represented
by the reference index. Promote one only when it is source-backed, can be central
to a realistic unnamed task, contributes a distinct branch, and has an explicit
neighbor boundary. Record every promote/reject decision and source trace under
`## Activation Coverage` in the mapping. Every promoted branch requires an
unnamed positive discovery fixture; do not copy a full-topic inventory into the
description.

## 3. Progressive Disclosure

Question: did the package preserve useful access to normal, focused, and
exhaustive guidance?

- `ordinary`: `SKILL.md` alone is sufficient for routine matched work.
- `focused`: the inline map routes a common concrete question directly to
  relevant sections of `references/full.md`, or `references/index.md` routes
  any other bounded question there.
- `comprehensive`: an explicit exhaustive request reads the full reference end
  to end.

Record any index access or bounded `full.md` access as focused. When the solver
stops after inspecting only the index because `SKILL.md` already resolved the
task, `consulted_reference_sections` stays empty. Treat that as an over-read
diagnostic; it does not demonstrate that a focused source-detail fixture reached
the required full section.

A focused fixture must contain either a concrete source-detail need that the
compact body intentionally does not answer or an explicit source-interpretation
dispute whose exact proposition must be checked against canonical detail. The
inline map or exhaustive index must route that need to a bounded, coherent
section set. Generic disagreement, a narrow decision, or several related
concerns are not sufficient. If `SKILL.md` contains everything needed and no
source interpretation is disputed, record the run as ordinary and treat the
mistaken fixture expectation as a design diagnostic rather than forcing a
reference read.

Classify the complete requested deliverable, not only its central decision. A
case is focused when the compact body resolves the main choice but the prompt
also requires source detail available only in the full reference, such as a
migration sequence, compatibility condition, technique precondition, or exact
treatment triad. Record that exact secondary gap and its bounded destination in
the mapping before execution.

Keep the compact-body gap private in the mapping. The raw blind fixture may ask
for the concrete detail and a bounded reference read, but must not tell the
solver that `SKILL.md` omits it or reveal suspected conversion weaknesses.

The solver record names the level-two headings it actually consulted. Use `*`
only for an end-to-end comprehensive read. These fields are access evidence,
not an instruction to open more files.

A disclosure failure blocks acceptance only when the progressive-disclosure
design materially collapses. Examples include:

- Routine ordinary work consistently causes an end-to-end `full.md` read.
- Neither the inline map nor exhaustive index can reach source detail needed for a concrete focused question.
- An explicit comprehensive request cannot reach or does not read the complete
  reference.
- Router wording systematically sends routine work across broad, unrelated
  concern families.

Reading a few additional relevant sections, choosing focused rather than
ordinary for a plausible hotspot, or differing from an exact expected section
count is diagnostic. Do not require an exact section set. A focused read that
approaches one-third of the source or spans several independent concern
families should trigger manual review for tier collapse, not an automatic
failure.

Concern count alone never requires a comprehensive read. Reserve end-to-end
loading for an explicitly exhaustive objective, not merely a decision that
touches several related or independent parts of the source.

## 4. Application And Attribution

Question: can the solver use the packaged guidance without misrepresenting what
the book says?

Application cases should exercise the book's distinctive judgment, including
nano-prioritized pressure where useful. The answer may also use general
engineering knowledge. Do not require every answer sentence or incidental
recommendation to trace to the book.

Review source attribution separately:

- Fail the conversion when unsupported prescriptive content exists in the
  package.
- Fail book attribution when an answer claims unsupported advice came from the
  book or skill.
- Record unsupported or contradictory general solver additions as answer-level
  diagnostics unless evidence shows that packaged wording caused them.
- Never add an invented rule to the skill merely to make a solver's prior
  invention appear supported.

The blind solver must not inspect canonical source or mapping files to perform
this review. An independent reviewer compares the package with canonical source
after the run.

## Case Classes

Each skill should have:

1. Direct invocation by book or lens name.
2. Distinctive unnamed discovery.
3. Ordinary use from `SKILL.md` alone.
4. Focused reference retrieval.
5. Comprehensive end-to-end retrieval.
6. A nano-salience or pressure case when the source defines one.
7. A compatible overlap case when neighboring skills plausibly apply.

Near-neighbor, generic, pair-negative, and catalog-null cases are optional
catalog diagnostics. Use raw code, configuration, incident evidence, schemas,
or design artifacts for substantive application cases. A hypothetical prose
prompt is acceptable for direct invocation and narrow routing tests.

Freeze raw fixture content before package authoring, but treat its required-skill
ownership as provisional until the complete sibling catalog exists. Before any
behavioral run, have an independent reviewer verify that each positive fixture
makes every required skill's distinctive judgment central; shared vocabulary or
a topic covered somewhere in the book is insufficient. The audit must also
confirm that unnamed and disclosure fixtures do not reveal a required skill or
its book or lens name, including through a negated instruction. A neighboring
skill's ordinary vocabulary may remain when it is part of the raw task; its
selection is permitted and evaluated under the normal overlap policy.

If the pre-run audit proves a frozen positive fixture has the wrong owner,
reveals private evaluation rationale, or otherwise has an invalid contract,
preserve its fixture, hash, and required set as a not-run diagnostic. Author a
separately named replacement and independently audit it before execution. If
post-run review finds the defect, preserve the results too. Never edit the old
prompt, relax its required set, or credit it to a sibling after observing
selection; keep the replacement and reclassification explicit in the mapping.

## Durable Case Record

Mappings first authored after Batch 3 must declare
`Evaluation contract version: 2` immediately after the title. This opts every
case in that mapping into deterministic field and fixture-hash validation.
Historical mappings remain unchanged. A separately named replacement added to
a historical mapping opts in only that case with `Contract version: 2`.

Version 2 cases use repository fixture files rather than prose summaries in the
mapping. Record and validate the exact file hash before execution. The
`validate_evaluation_contracts.py` check requires the fields below, confirms the
fixture exists under the repository root, and compares its SHA-256 value.

Record cases in `_skill-workbench/<book>/mapping.md` before execution:

```markdown
### E1: <short name>

- Class: <recognition | application | pressure | retrieval | diagnostic>
- Prompt or artifact: `<repository-relative fixture path>`
- Fixture SHA-256: `<64-character digest>`
- Required skills: <explicit set; empty only for a diagnostic>
- Distinctive judgment: <the central judgment each required skill uniquely contributes>
- Neighbor ownership: <why plausible sibling skills are secondary, complementary, or outside the central decision>
- Ownership review: <independent reviewer and pre-run verdict>
- Reference expectation: <ordinary | focused | comprehensive | diagnostic>
- Compact-body gap: <focused only: exact absent source detail, or `none` plus the exact disputed source proposition>
- Intended index destinations: <focused only: bounded full-reference headings>
- Runs: <run IDs and observations>
- Package fidelity trace: <M*, N*, or full heading>
- Attribution review: <source-backed guidance versus fixture facts, neighboring guidance, and solver choices>
- Behavioral result: <pass | fail | pending>
- Diagnostics: <non-blocking runtime observations>
```

Before behavioral execution, `Ownership review` must be a completed independent
`PASS`, not `pending`. For a focused case, the reviewer must confirm either that
the compact body lacks the requested source detail or that the exact disputed
source proposition needs canonical checking, and that the intended index
destinations form the smallest coherent source set. Ordinary and comprehensive
cases omit the two focused-only fields.

Version 2 mappings include an independent-review block whose fields remain
explicitly pending until the review is complete:

```markdown
## Independent Review

- Reviewer: <reviewer or pending>
- Catalog snapshot: <complete catalog used or pending>
- Semantic verdict: <PASS | FAIL | pending>
- Unsupported or altered guidance: <findings, none, or pending>
```

After validation evidence, version 2 mappings end with a stable verdict block;
`## Verdicts` must be the final level-two section:

```markdown
## Verdicts

- Source/package verdict: <PASS | FAIL | pending>
- Original behavioral observation: <immutable first-run result or pending>
- Current-state gate: <current PASS | FAIL | pending, with correction named>
- Residual diagnostics: <preserved misses, over-reads, additions, or none>
```

The source/package verdict never derives from skill-selection variance. The
original behavioral observation is immutable. A current-state gate differs
from it only after a documented package, catalog, harness, or ownership-contract
correction with separately named evidence. Residual diagnostics never silently
disappear when the current-state gate passes.

Existing mappings may retain historical `Allowed skills`, `Forbidden skills`,
`Required order`, RED/GREEN, and exact-section fields. Preserve those records;
under this protocol they are diagnostic unless they establish required-skill
inclusion, package fidelity, or material disclosure collapse.

Do not replace a prompt with a vague scenario summary. Keep enough raw input
for another evaluator to rerun the case. Do not rewrite preserved observations
when policy changes; add a current-policy reclassification.

## Runs And Independence

- Run deterministic source/package validators for every conversion.
- Use an independent reviewer for final semantic fidelity.
- Run direct and distinctive unnamed discovery cases three times before
  acceptance; every run must include all required skills.
- Run each disclosure tier at least once. Repeat a case when a possible material
  tier collapse needs classification.
- Repetition may diagnose nondeterminism but does not erase a valid required-skill
  miss or turn it into a majority-vote pass. Count a uniquely named replacement
  as current-state evidence only after a documented package, catalog, harness, or
  ownership-contract correction; retain every superseded record.
- A solver self-report that the unchanged runner rejects only for internal
  evidence inconsistency is not a behavioral sample. Preserve the invalid JSON,
  then collect a uniquely named replacement with the same frozen fixture, model,
  and configuration. This replacement completes missing evidence; it does not
  retry or outvote a valid selection miss. If the same inconsistency repeats,
  stop and diagnose the reporting contract or runner before continuing.
- Use fresh solver contexts and the same model/configuration when comparing
  runs.
- Do not reveal required skills, source IDs, suspected omissions, or conversion
  rationale to the blind solver.
- Restrict runtime book guidance reads to `.agents/skills/**`; canonical full,
  mini, nano, mapping, and evaluation reads invalidate behavioral evidence.

Skill-disabled baselines may be used to measure incremental value or diagnose
model priors. They are not required for conversion acceptance, because the
deliverable is a faithful skill package rather than proof that a pretrained
model lacked the book's ideas.

## Evidence Integrity

### Execution manifest

Current acceptance runs use one immutable JSON manifest per run under
`_skill-workbench/evaluations/manifests/<book>/<case>/<run>.json`. Create it only
after the complete description catalog, fixture ownership review, mapping
contract, runner, and result schema are frozen:

```bash
python3 _skill-workbench/scripts/evaluation_manifest.py \
  --case _skill-workbench/evaluations/cases/<book>/<case>.md \
  --mode green \
  --run <run-name> \
  --output _skill-workbench/evaluations/results/<book>/<case>/<run-name>.json \
  --manifest _skill-workbench/evaluations/manifests/<book>/<case>/<run-name>.json

python3 _skill-workbench/scripts/run_skill_eval.py \
  --manifest _skill-workbench/evaluations/manifests/<book>/<case>/<run-name>.json
```

The builder derives the required set from the exact version 2 mapping case. It
records the sorted `<skill-name>\t<description>\n` catalog entries and SHA-256,
a complete package snapshot for every live `SKILL.md`, `references/index.md`, and
`references/full.md`, case and mapping hashes, runner and schema hashes, model,
fixed configuration, timeout, run name, and output path. The runner recomputes
all repository-derived values before dispatch, refuses an existing output path,
and embeds both the manifest and its file hash in the result. It then compares
the case, mode, run, model, configuration, and required set in the result
envelope with the manifest.

Any catalog, package file, fixture, mapping, runner, or schema change invalidates
an unrun manifest. Preserve it, create a separately named replacement after
review, and never edit it into agreement. A pre-dispatch manifest rejection is
process evidence, not solver behavior. Direct `run_skill_eval.py` arguments remain useful
for exploratory or historical diagnostics but are not current acceptance
evidence.

Ask the blind solver only for its answer, selected project skills, consulted
packaged files, consulted full-reference headings, and reference mode. Reporting
fields are passive evidence and must never cause an extra read.

Reject internally inconsistent records. The observed
`selected_project_skills` must exactly match consulted `SKILL.md` files; this is
record integrity, not an exact-selection expectation. Every reference must
belong to a consulted skill, every consulted book path must be under
`.agents/skills/**`, section records must match actual `full.md` reads, and the
reported reference mode must match the files opened.

Before classifying a `selection_errors` entry as behavioral evidence, compare
the record's `required_project_skills` with the frozen mapping contract for that
exact case. A CLI or dispatch mistake that adds, removes, or substitutes a
required skill is an invalid invocation record, not a valid selection miss.
Preserve it and collect a uniquely named correctly configured replacement; do
not rewrite the recorded required set.

The converter may run exploratory checks, but a different agent performs final
semantic review. Record the manifest path and catalog SHA-256 in the mapping's
catalog snapshot evidence.

## Change-Impact Reruns

Classify a change before scheduling reruns. Do not rerun the entire matrix by
habit, and do not reuse an unaffected run to claim evidence for changed
behavior.

| Change | Evidence invalidated | Required reruns |
| --- | --- | --- |
| Description change or new catalog neighbor | Discovery and catalog routing for affected skills | Direct and unnamed cases for the changed skill; every positive case requiring it; high-overlap cases involving the new or changed boundary. |
| `SKILL.md` reference-map or index router-loading prose only | Disclosure behavior reached after selection | Affected ordinary cases, focused source-detail probes, comprehensive controls, and any preserved over-read that motivated the change. Do not rerun discovery unless description metadata also changed. |
| Active technical guidance, canonical mini/nano, or a prescriptive index predicate | Source/package fidelity and affected application behavior | Repeat reverse tracing, exact wording and semantic review, then rerun affected application, pressure, attribution, and disclosure cases. Rerun discovery only if the description changed. |
| Fixture ownership or content correction | Only the corrected contract; old evidence stays historical | Preserve the old fixture and results, create a separately named versioned replacement, audit it, then execute its frozen runs. |
| Harness, schema, or CLI defect that prevented valid evidence | Invalid process-boundary records only | Preserve failed artifacts, repair and unit-test the harness, pass one live preflight, then use uniquely named replacements for invalid runs. Existing valid records remain valid when prompt, model, configuration, and result semantics are unchanged. |
| Solver self-report integrity failure with a correctly rejecting runner | The internally inconsistent record only | Preserve the invalid record and collect a uniquely named replacement under the identical frozen fixture, model, and configuration. No package or catalog correction is implied. Stop for diagnosis if the same inconsistency repeats. |
| Intentional model or material runtime-configuration change | Behavioral comparability for the current gate | Start a new named behavioral snapshot and rerun every case required for current acceptance. Never combine different models into one repetition count. |

Regenerate every unrun manifest affected by a row above. Historical result JSON
retains its embedded manifest and remains attached to the exact state it tested.

After adding or changing a description:

1. Rerun that skill's direct and unnamed positive discovery cases.
2. Rerun existing positive cases that require the changed skill.
3. Rerun high-overlap cases to confirm every intended required skill remains
   discoverable.
4. Review optional null and broad cases for context-cost diagnostics.
5. Recheck description length and duplicated activation branches.

For a parallel batch, freeze all descriptions before final discovery runs.
Validate that every durable case names only live required skills with
`_skill-workbench/scripts/validate_evaluation_contracts.py`. Do not partition
the complete catalog into required, allowed, and forbidden sets.

At five-skill increments, review the complete description catalog for missing
required selections and excessive context cost. Overlap by itself is not a
collision failure.

## Acceptance

A conversion passes only when:

- Full-reference equality passes.
- Mini wording, primary bias, and final checklist fidelity pass or have a
  source-supported documented exception.
- Nano salience is mapped without inventing or expanding rules.
- Full-only activation candidates have source-traced decisions, and every promoted branch has an unnamed discovery fixture.
- Every active technical directive and prescriptive map or router condition traces to
  canonical source.
- Reverse tracing finds no unsupported compressed-source detail.
- Structural and mapping validation passes.
- New mappings and opted-in replacement cases pass version 2 field and
  fixture-hash validation.
- An independent semantic reviewer finds no unsupported strengthening,
  weakening, omission, or imported guidance.
- Direct and unnamed positive discovery runs include every required skill.
- Current acceptance results embed a clean mapping-derived execution manifest and its hash.
- Progressive disclosure has no material tier collapse.
- Source/package, original behavioral, current-state, and residual-diagnostic
  verdicts remain separate.

The following do not fail a faithful conversion by themselves:

- Selection of additional relevant skills.
- A different skill-selection order.
- General knowledge in the solver answer.
- No measurable improvement over a skill-disabled baseline.
- Extra relevant focused sections or an inexact section count.
- Selection in a broad, negative, or catalog-null diagnostic case.

Use `_skill-workbench/scripts/evaluation_manifest.py` followed by
`run_skill_eval.py --manifest <path>` to record current behavioral evidence. The
manifest freezes the catalog and execution contract; the runner pins read-only
execution, creates a project-skill-free temporary baseline workspace when
requested, restricts GREEN guidance to packaged skills, records case hashes and
thread IDs, and checks result integrity against
`_skill-workbench/evaluations/result-v2.schema.json`. Preserved v1 evidence
continues to use `result.schema.json`.

Before dispatching parallel behavioral runs, execute one live GREEN preflight
through the current manifest, model, CLI, and result schema using a stable direct
positive fixture. Require a structured result, clean integrity, and successful
required-skill inclusion before starting the batch. A schema rejection,
model/runtime error, missing result, or other harness failure is environment
evidence, not a behavioral sample: preserve its JSON, repair the harness,
verify the preflight, and use a uniquely named replacement record rather than
overwriting the failed artifact. A structurally valid required-skill miss is
behavioral evidence, not a harness failure; preserve it and diagnose the
catalog contract before parallel dispatch. The runner must preserve Codex
JSON-event error messages as `codex_errors` in addition to cleaned stderr so a
process-boundary failure remains diagnosable.

For a positive GREEN acceptance run, required skills come only from the frozen
mapping through the manifest. The runner checks inclusion after the blind solver
returns; the required set is not injected into the solver prompt. Additional
selected skills do not produce a selection error.
