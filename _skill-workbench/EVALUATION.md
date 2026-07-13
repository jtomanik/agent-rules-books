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
  checklist, or reference router has a source trace.
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

## 3. Progressive Disclosure

Question: did the package preserve useful access to normal, focused, and
exhaustive guidance?

- `ordinary`: `SKILL.md` alone is sufficient for routine matched work.
- `focused`: `references/index.md` routes a concrete question to relevant
  sections of `references/full.md`.
- `comprehensive`: an explicit exhaustive request reads the full reference end
  to end.

The solver record names the level-two headings it actually consulted. Use `*`
only for an end-to-end comprehensive read. These fields are access evidence,
not an instruction to open more files.

A disclosure failure blocks acceptance only when the progressive-disclosure
design materially collapses. Examples include:

- Routine ordinary work consistently causes an end-to-end `full.md` read.
- The router cannot reach source detail needed for a concrete focused question.
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

## Durable Case Record

Record cases in `_skill-workbench/<book>/mapping.md` before execution:

```markdown
### E1: <short name>

- Class: <recognition | application | pressure | retrieval | diagnostic>
- Prompt or artifact: <verbatim prompt or repository-relative path>
- Required skills: <explicit set; empty only for a diagnostic>
- Selection notes: <optional expected overlap or diagnostic question>
- Reference expectation: <ordinary | focused | comprehensive | diagnostic>
- Relevant sections: <semantic target or not applicable>
- Runs: <run IDs and observations>
- Package fidelity trace: <M*, N*, or full heading>
- Attribution review: <supported | unsupported | not applicable>
- Conversion result: <pass | fail>
- Diagnostics: <non-blocking runtime observations>
```

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

Ask the blind solver only for its answer, selected project skills, consulted
packaged files, consulted full-reference headings, and reference mode. Reporting
fields are passive evidence and must never cause an extra read.

Reject internally inconsistent records. The observed
`selected_project_skills` must exactly match consulted `SKILL.md` files; this is
record integrity, not an exact-selection expectation. Every reference must
belong to a consulted skill, every consulted book path must be under
`.agents/skills/**`, section records must match actual `full.md` reads, and the
reported reference mode must match the files opened.

The converter may run exploratory checks, but a different agent performs final
semantic review. Record the live catalog descriptions and relevant runtime
configuration with behavioral evidence.

## Catalog Regression

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
- Every active technical directive and prescriptive router condition traces to
  canonical source.
- Reverse tracing finds no unsupported compressed-source detail.
- Structural and mapping validation passes.
- An independent semantic reviewer finds no unsupported strengthening,
  weakening, omission, or imported guidance.
- Direct and unnamed positive discovery runs include every required skill.
- Progressive disclosure has no material tier collapse.

The following do not fail a faithful conversion by themselves:

- Selection of additional relevant skills.
- A different skill-selection order.
- General knowledge in the solver answer.
- No measurable improvement over a skill-disabled baseline.
- Extra relevant focused sections or an inexact section count.
- Selection in a broad, negative, or catalog-null diagnostic case.

Use `_skill-workbench/scripts/run_skill_eval.py` to record behavioral evidence.
It pins the model and read-only configuration, creates a project-skill-free
temporary baseline workspace when requested, restricts GREEN guidance to
packaged skills, records case hashes and thread IDs, and checks result integrity
against `_skill-workbench/evaluations/result-v2.schema.json`. Preserved v1
evidence continues to use `result.schema.json`.

For a positive GREEN run, pass `--required-skill <name>` once per required
target. The runner checks inclusion after the blind solver returns; the required
set is not injected into the solver prompt. Additional selected skills do not
produce a selection error.
