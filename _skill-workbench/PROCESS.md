# Rule-to-Skill Conversion Process

## Goal

Convert each book's `full`, `mini`, and `nano` rule sets into a source-faithful Codex guidance skill with tested invocation and progressive disclosure, without flattening the book's distinctive judgment, losing the full rule's detail, or turning guidance into a generic repeatable workflow.

The conversion is semantic authoring, not mechanical translation. Perform one focused manual conversion per book. Automate only deterministic packaging and validation work.

## Skill Type

These skills are guidance/reference skills.

- They provide a decision lens for implementation, review, design, refactoring, testing, and other work relevant to the book.
- They do not prescribe a universal ordered process.
- They may contain a final checklist that binds application of the guidance, but they do not need workflow steps, a quick start, or per-step completion criteria.
- They are model-invoked by default so Codex can select a relevant book without the user naming it explicitly.
- Their descriptions are therefore the primary catalog router and must be authored with exceptional care.

## Progressive Disclosure Contract

Map the three rule versions onto Codex's three loading tiers:

| Canonical input | Skill role | Runtime loading |
| --- | --- | --- |
| `nano` | Invocation and salience source | Distilled into the description, guidance order, and reference-routing triggers |
| `mini` | Complete normal-use guidance | Manually reshaped into `SKILL.md` |
| `full` | Exhaustive guidance | Preserved in `references/full.md` and loaded selectively or end to end |

The skill package does not need separate copies of `mini.md` or `nano.md`. Their canonical files remain in the book directory as independent rule artifacts and conversion inputs.

Progressive disclosure must not become progressive omission:

- Ordinary matched work should be handled by `SKILL.md` alone.
- Focused ambiguity or a specific hotspot should route through `references/index.md` to the relevant full sections.
- A comprehensive audit, disputed interpretation, or explicit request for the complete book lens must route to an end-to-end read of `references/full.md`.

## Source of Truth

For a book named `<book>`:

- `<book>/<book>.md` is the canonical full rule.
- `<book>/<book>.mini.md` is the canonical normal-use compression.
- `<book>/<book>.nano.md` is the canonical high-salience compression.
- `_rule-workbench/<book>/traceability.md` supplies `M*` and `N*` mappings back to full sections.
- `_skill-workbench/PROCESS.md` is the canonical conversion contract.
- `_skill-workbench/EVALUATION.md` is the canonical behavioral evaluation contract.
- `_skill-workbench/<book>/mapping.md` records the manual conversion decisions and validation evidence.
- `.agents/skills/<book>/` is the generated and manually authored skill artifact.

Do not edit `full`, `mini`, or `nano` while converting a skill. If conversion exposes a source-rule defect, stop and fix it through `_rule-workbench/PROCESS.md` before resuming the skill conversion.

## Required Output

Each converted book produces:

```text
.agents/skills/<book>/
  SKILL.md
  agents/
    openai.yaml
  references/
    full.md
    index.md

_skill-workbench/<book>/
  mapping.md
```

Do not add README files, changelogs, installation guides, or conversion notes inside the skill directory. Keep authoring evidence in `_skill-workbench/<book>/mapping.md`.

## Manual Versus Automated Work

### Manual semantic work

An agent must perform these decisions manually:

- Define the skill's distinctive scope and leading vocabulary.
- Write its model-facing description.
- Compare that description against every existing book skill description.
- Decide which nano signals belong in invocation metadata, early guidance, or reference routing.
- Group mini rules into coherent concerns.
- Preserve each mini rule exactly once without splitting its meaning across distant sections.
- Co-locate each concept's rule, trigger, caveat, and tradeoff.
- Write the `Read when` guidance for every full section.
- Decide when targeted reading is enough and when the full reference must be read end to end.
- Design positive required-skill, application, and routing evaluation scenarios.
- Inventory every newly authored prescriptive sentence so it can be distinguished from packaging-only prose and traced to canonical source.
- Trace material application recommendations back to mini, nano salience, or full-reference sections.
- Reverse-trace prescriptive mini and nano details to explicit support in the canonical full rule; exact packaging fidelity cannot prove that the compressed source was faithful.
- Judge whether wording is a no-op, accidental strengthening, generic advice, or faithful book-specific pressure.

### Deterministic work suitable for scripts

Scripts may:

- Initialize a standard skill directory.
- Copy the canonical full rule into `references/full.md`.
- Record or verify a content hash for the copied full reference.
- Extract full-rule headings and Markdown anchors.
- Compute section start and end line numbers.
- Merge section metadata with manually authored `Read when` guidance.
- Detect new, removed, renamed, or unrouted full sections.
- Validate skill names, frontmatter, links, and `agents/openai.yaml`.
- Check UI field lengths and required `$skill-name` references.
- Check that every `M*` and `N*` identifier has a skill mapping.
- Detect duplicate mappings, stale ranges, missing files, and unresolved placeholders.
- Extract mini and skill rules and report exact wording changes without treating reordering as a change.
- Verify exact primary-bias and final-checklist wording and checklist order.
- Measure description length, skill word count, mini word count, and packaging overhead.
- Verify that every durable positive case names only live required skills.
- Validate selected skills, consulted files, per-skill full-reference sections, and disclosure mode as one evidence record.

Scripts must not write descriptions, group rules, select critical guidance, invent routing conditions, or rewrite book guidance automatically.

## Conversion Inputs

Before authoring, read all of the following completely:

1. `_skill-workbench/PROCESS.md`
2. `_skill-workbench/EVALUATION.md`
3. `<book>/<book>.md`
4. `<book>/<book>.mini.md`
5. `<book>/<book>.nano.md`
6. `_rule-workbench/<book>/traceability.md`
7. Every existing `.agents/skills/*/SKILL.md` frontmatter description
8. Relevant pairwise compatibility documents under `docs/compatibility/`

Read the existing skill body only when needed to compare organization or overlapping guidance. Do not imitate an existing skill blindly; the current pilot may itself be under review.

## Invocation Design

### Invocation policy

Book guidance skills are model-invoked by default. State that intent explicitly:

```yaml
policy:
  allow_implicit_invocation: true
```

Use `false` when a specific book skill is deliberately manual-only and the mapping document explains why. Also front-load `Explicit invocation only: use $<skill-name>` in the description and verify an unnamed policy probe `3/3`; repo-local runtime discovery may enforce neither control. If the probe still selects the skill, manual-only packaging is unavailable on that runtime: do not ship a misleading gate. Either keep the package outside the discovered skill directory or restore implicit invocation with a deliberately narrow, tested description. For automatic invocation, require an unnamed distinctive case to include the target skill in every acceptance run. Direct book-name retrieval proves explicit retrieval but does not test description-based discovery. Additional relevant skills in either case are permitted.

### Description responsibilities

The description is the always-visible router into the skill. It must:

1. Front-load the book's established leading term or distinctive lens.
2. Describe only the conditions under which the skill should be loaded, not its application sequence or a summary of its rules.
3. Name genuinely distinct invocation branches.
4. Include important nano-derived code or system symptoms when Codex may discover them after inspecting the task.
5. Audit distinctive full-only mechanisms that may be central even though nano does not name them.
6. Establish a positive activation threshold by saying what must be central or blocked before the skill applies.
7. Distinguish the skill from neighboring book skills.
8. Remain concise enough to survive description shortening.

Keep the description at or below 500 characters. The opening capability clause should identify the lens, not summarize its rules or application sequence.

Preferred shape:

```yaml
description: <Distinctive lens and capability>. Use when <branch one>, <branch two>, or <branch three> is central to the task.
```

Do not:

- Copy the nano file into the description.
- List synonyms as separate triggers.
- Use generic branches such as `maintainability`, `quality`, `best practices`, `coding`, or `review` without a book-specific qualifier.
- Summarize the entire skill body.
- Put discovery-only `When to use` prose in the body; the body is loaded after selection.
- Rely on the book title alone when users are unlikely to name it.

### Catalog collision review

Descriptions form one routing system. Review them as a catalog, not as isolated prose.

For every new description, record:

- Direct and unnamed prompts whose required set includes this skill.
- Prompts where another compatible skill may also be useful.
- Near-neighbor and generic prompts worth retaining as context-cost diagnostics.
- Terms shared with other descriptions and why each overlap is legitimate.

Resolve collisions by sharpening each skill's distinctive bias, not by adding longer synonym lists.

Prefer a positive activation test over a long negative trigger list. Negative clauses still place their vocabulary in the catalog and can increase accidental selection when a neighbor prompt contains the same words. Use a negative clause only for a high-risk boundary that the positive threshold cannot express clearly, and test both directions after every change.

For a parallel batch, freeze the complete batch catalog before behavioral execution. After all candidate descriptions exist, verify the required target set for every new and existing durable positive case, then run:

```bash
python3 _skill-workbench/scripts/validate_evaluation_contracts.py
```

Do not let concurrent converters evaluate against partial sibling catalogs. The batch-level reconciliation gate checks that every intended target remains discoverable after sibling descriptions are present. Extra selections, catalog-null behavior, and broad overlap remain diagnostic unless they cause materially wrong or contradictory guidance.

### Activation coverage audit

Nano is the default source of activation salience, not proof that every
distinctive discovery condition appears there. After the full-section inventory
and candidate index routes exist, inspect each full-only named mechanism or
decision family that could be central to a realistic task. The audit asks whether
an unnamed prompt can require this book's distinctive judgment without using the
book title, lens name, or nano vocabulary.

Record the audit in `mapping.md`:

```markdown
## Activation Coverage

| Full-only candidate | Source trace | Nano coverage | Neighbor boundary | Decision and evidence |
| --- | --- | --- | --- | --- |
```

Record `none found` when no candidate qualifies. Promote a full-only term into
the description only when all of these are true:

- The canonical full rule explicitly states or clearly entails the term and its
  activation condition.
- The mechanism can be central to a realistic task rather than merely a detail
  consulted after selection.
- The term contributes a distinct discovery branch instead of another synonym
  for an existing branch.
- Neighbor ownership and the 500-character description budget remain clear.
- The mapping gives an exact source trace and an unnamed positive fixture tests
  the promoted branch.

Do not summarize every index row in metadata or assume that any full-only topic
deserves activation. A promoted source-backed term changes description discovery
only; it does not rewrite mini or nano. Freeze the description catalog only after
this audit and rerun the normal description change-impact matrix after any
promotion.

## Translating Nano

Nano is a prioritization and routing input, not a second skill body.

For every `N*` item in traceability, assign one or more roles in `_skill-workbench/<book>/mapping.md`:

- `description`: contributes a distinct invocation branch or symptom.
- `early-guidance`: causes the corresponding complete mini rule or concern to appear early in `SKILL.md`.
- `reference-router`: identifies a condition that should open a full section.
- `final-check`: appears as an intentionally repeated completion scan.
- `not-used`: justified because another mapping already preserves the same operational effect.

Nano should influence ordering without fragmenting concepts. Prefer moving a complete mini rule or concern earlier. Do not split one mini rule into a short critical fragment and a distant remaining fragment.

## Translating Mini

Mini is the semantic inventory for `SKILL.md`.

### Coverage rule

Every `M*` item must appear exactly once as authoritative guidance in the skill body, unless the mapping document explicitly records a faithful merge with another `M*` item.

Traceability IDs are authoritative; physical mini bullets are not implicit ID ordinals. When one stable `M*` ID intentionally spans multiple separate mini bullets, map that ID once, record every represented bullet in the mapping, and preserve each bullet verbatim in `SKILL.md`. Do not merge or delete a bullet, or invent new IDs, merely to make the physical bullet count equal the traceability-ID count. The wording checker still validates every physical bullet independently.

A final checklist may intentionally restate a rule as a check. Record that as `final-check`, not as a second authoritative definition.

### Organization rule

Group guidance by the concerns an agent reasons about together, not by source labels such as `critical` and `remaining`.

Good concern groups include:

- Naming and local reasoning
- Functions, state, and side effects
- Errors and invalid states
- Boundaries and dependencies
- Tests and validation
- Concurrency and operations
- Refactoring scope and stopping conditions

Choose groups that reflect the book. Do not impose the Clean Code groups on every book.

Order groups by nano salience and likely decision timing. Within a group:

- Keep a decision rule beside its trigger.
- Keep a tradeoff beside the conditions that resolve it.
- Keep a caveat beside the rule it limits.
- Preserve the book's vocabulary when it carries distinctive meaning.
- Preserve source-relative order unless moving a rule beside its trigger, caveat, or tradeoff makes the concept more coherent; record non-obvious reordering in the mapping.
- Prefer positive target behavior; retain prohibitions only for necessary guardrails and pair them with the desired action.

### Fidelity rule

Preserve the exact wording of the primary bias, every mini rule, and every final-checklist item whenever possible. Preserve final-checklist order. The normal conversion operation is to move a complete rule under a better concern heading, not to paraphrase it.

Reword only when one of these conditions applies:

- A sentence needs a minimal grammatical adjustment after a faithful merge.
- Two mini rules have the same operational meaning and traceability supports merging them.
- Skill-specific reference wording is required to connect a rule to its routed full section.
- The original wording is ambiguous outside the standalone mini file and the full rule resolves that ambiguity.

For every reworded rule, record the original wording, final wording, reason, and affected `M*` or `N*` IDs in the mapping document. Do not paraphrase merely for tone, brevity, stylistic consistency, or preferred vocabulary.

The conversion must not:

- Strengthen `SHOULD` guidance into `MUST` guidance.
- Weaken a non-negotiable rule.
- Add modern preferences unsupported by the source.
- Import advice from another book.
- Replace a distinctive book bias with generic software advice.
- Remove a rule merely because it sounds obvious to a human.

An exact mini-to-skill match can still preserve a source-compression defect. During
independent review, reverse-trace concrete mechanisms, qualifiers, examples, and
failure semantics from mini and nano into the canonical full rule. If a retained
detail is merely plausible book knowledge but is not stated or clearly entailed
by the full rule, stop the conversion and repair mini, nano, and traceability
through `_rule-workbench/PROCESS.md` before regenerating the skill.

Treat the changed-clause diff as a locator, not the review boundary. Source/package
acceptance covers every prescriptive clause newly activated by `SKILL.md`, including
unchanged mini or nano text that predates the conversion branch.

Use the existing traceability IDs to settle fidelity questions.

### Wording fidelity check

Run the deterministic wording checker after every material edit:

```bash
python3 _skill-workbench/scripts/check_rule_wording.py \
  --mini <book>/<book>.mini.md \
  --skill .agents/skills/<book>/SKILL.md
```

The checker compares mini decision and trigger bullets as an unordered exact-text multiset against guidance bullets in `SKILL.md`. It separately requires exact primary-bias text and exact final-checklist wording and order. It reports missing rules, added rules, closest candidates, and word-level differences.

The preferred result is zero wording differences. A nonzero result is not automatically invalid because a faithful merge or minimal grammatical adjustment may be justified, but every reported difference must be removed or documented with original text, final text, reason, and traceability IDs in `mapping.md`.

Use `git diff --word-diff` or another focused diff when the checker identifies a candidate that needs human review. Automated similarity is a locator, not a semantic approval.

## SKILL.md Shape

These are guidance skills, so no workflow section is required. Use this default shape and adapt concern headings to the book:

```markdown
---
name: <book>
description: <model-facing capability and invocation branches>
---

# <Human-facing book or lens name>

## Primary Bias

<One concise corrective bias.>

## <Highest-salience concern>

<Complete mini-derived rules and colocated triggers.>

## <Additional concern>

<Complete mini-derived rules and colocated triggers.>

## Reference Router

<Focused and comprehensive reference-loading conditions.>

## Final Checklist

<Small scan derived from the mini/nano checklists.>
```

Constraints:

- Frontmatter contains only `name` and `description`.
- Use lowercase kebab-case for `name`, under 64 characters.
- Prefer the recognized book/lens term over a verb-led name when that term is the strongest invocation anchor.
- Keep `SKILL.md` under 100 lines by default. Exceed it only with a recorded reason.
- Target at most 500 words. If the canonical mini already exceeds that target, preserve its wording and add a `Size Exception` to the mapping instead of compressing during conversion.
- Target at most 150 words of packaging overhead beyond the canonical mini. Packaging includes frontmatter, headings, routing, and other skill-only prose. An overhead of 151-200 words may pass with the exact count and a clarity or routing rationale in `Size Exception`; above 200 words fails. Do not compress activation or routing guidance merely to hit the soft target.
- If mini is under 500 words but the skill exceeds it, prune packaging before accepting an exception.
- Use imperative guidance where practical.
- Do not add a body-level `When to Use` section.
- Do not add a workflow merely to satisfy a generic skill template.
- Do not add examples unless evaluation shows that an important rule is otherwise applied inconsistently.

## Reference Router

`SKILL.md` must link directly to both reference files so references remain one level deep.

Required routing branches:

1. `ordinary`: use `SKILL.md` guidance without loading references.
2. `focused`: read `references/index.md`, then the named sections of `references/full.md`.
3. `comprehensive`: read `references/full.md` end to end.

Suggested wording:

```markdown
## Reference Router

Use this file alone for ordinary matched work.

For an explicit disputed interpretation or demonstrated hotspot, read [references/index.md](references/index.md), then read the sections it identifies in [references/full.md](references/full.md). Also use that focused route when, after applying this file, one bounded book-specific question remains unresolved.

For a comprehensive audit or an explicit request for the complete book lens, read [references/full.md](references/full.md) end to end.
```

Tailor the conditions to the book. A pointer's wording determines whether the full guidance is actually reached.

Do not use bare `ambiguity`, `detail`, `decision`, or `hotspot` as generic focused triggers. Agents can treat any nontrivial implementation detail as satisfying them. State the evidence threshold, require ordinary work to stop after `SKILL.md` when it resolves the task, make the post-body unresolved condition explicit, and say that references are not opened merely to confirm or elaborate a body-supported answer.

Do not use the number of implicated rules, sections, or concern families as a proxy for comprehensive loading. A multi-concern implementation decision can still need only a bounded coherent subset. Reserve end-to-end loading for an explicitly exhaustive objective.

Evaluation must name the concrete source-detail question for focused cases, verify that `SKILL.md` does not already resolve it, identify the index destination before execution, and record the headings actually consulted. Classify every requested output: when the compact body resolves the central choice but a requested migration, compatibility, precondition, exact triad, or other source detail exists only in full, the whole case is focused. A narrow decision is not automatically a focused-reference case. Do not require an exact section set. If a focused route reads one-third or more of the full sections or spans several independent concern families, review it manually for material tier collapse; keep the bounded subset when it is coherent, and use an end-to-end read only when the task is explicitly exhaustive.

## references/index.md

The index is a semantic router, not merely a table of contents.

For every level-two heading in `full.md`, include:

- A stable Markdown anchor link.
- Generated start and end line numbers for shell-based targeted reading. Start at the level-two heading and end at the last non-empty line before the next level-two heading or end of file.
- Manually authored `Read when` guidance.

Preferred table:

```markdown
| Section | Lines | Read when |
| --- | ---: | --- |
| [Section name](full.md#section-name) | `10-24` | <Specific symptoms, decisions, or tradeoffs.> |
```

Add a symptom router only when it materially improves selection across several sections. Do not repeat the same routing guidance in both tables.

The generator must fail if:

- A full heading has no index entry.
- An index entry names a missing heading.
- A line range is stale.
- A `Read when` cell is empty or contains a placeholder.
- A Markdown anchor does not match the heading.

## references/full.md

Preserve the complete canonical full rule without semantic edits.

- Copy it deterministically from `<book>/<book>.md`.
- Verify byte-for-byte equality or a recorded content hash.
- Do not hand-edit the copied file.
- Regenerate it when the canonical full rule changes.
- Keep its verbosity; the purpose of this tier is exhaustive guidance.

If packaging later requires a generated table of contents, generate it outside the copied content or update the canonical full source through the rule workflow first.

## agents/openai.yaml

Create:

```yaml
interface:
  display_name: "<Human-facing name>"
  short_description: "<25-64 character UI description>"
  default_prompt: "Use $<skill-name> to <short example request>."

policy:
  allow_implicit_invocation: true
```

Requirements:

- Quote all string values.
- Keep keys unquoted.
- Keep `short_description` between 25 and 64 characters.
- Mention `$<skill-name>` exactly in `default_prompt`.
- Keep `default_prompt` to one short sentence.
- Add icons, colors, dependencies, or other optional fields only when explicitly designed.

## Mapping Document

Create `_skill-workbench/<book>/mapping.md` with this structure. New mappings
use evaluation contract version 2. Do not retrofit historical mappings merely
for formatting; a new replacement inside one of them opts in at case level as
specified by `EVALUATION.md`.

```markdown
# <Book> Skill Mapping

Evaluation contract version: 2

## Scope

- Distinctive lens:
- Intended invocation:
- Closest neighboring skills:

## Description Branches

| Branch | Trigger wording | Distinguishes from |
| --- | --- | --- |

## Activation Coverage

| Full-only candidate | Source trace | Nano coverage | Neighbor boundary | Decision and evidence |
| --- | --- | --- | --- | --- |

## Catalog Collision Cases

| Prompt | Expected skills | Reason |
| --- | --- | --- |

## Nano Mapping

| ID | Skill role | Destination | Notes |
| --- | --- | --- | --- |

## Mini Mapping

| ID | SKILL.md section | Transformation | Notes |
| --- | --- | --- | --- |

## Wording Fidelity

- Verbatim primary bias:
- Verbatim mini rules:
- Verbatim final checklist and order:
- Documented exceptions:

## Packaging Prose Fidelity

- Newly authored technical directives: <none | listed below>
- Review: <confirm that description, headings, transitions, and routing prose add no unsupported technical rule>

<When directives are listed, give each exact text plus its M*, N*, or full-heading source trace and explain why it is packaging rather than a duplicate active rule.>

## Size Exception

<Include when SKILL.md exceeds 500 words or packaging overhead exceeds the 150-word soft target. Record mini words, skill words, packaging overhead, and why the source or packaging should not be compressed.>

## Evaluation Cases

### E1: <short name>

- Class:
- Prompt or artifact: `<repository-relative fixture path>`
- Fixture SHA-256:
- Required skills:
- Distinctive judgment:
- Neighbor ownership:
- Ownership review:
- Reference expectation:
- Compact-body gap: <focused cases only>
- Intended index destinations: <focused cases only>
- Runs:
- Package fidelity trace:
- Attribution review:
- Behavioral result:
- Diagnostics:

## Independent Review

- Reviewer:
- Catalog snapshot:
- Semantic verdict:
- Unsupported or altered guidance:

## Validation Evidence

- Structural validation:
- Official skill validation:
- Full-reference equality:
- Index validation:
- Invocation evaluation:
- Application evaluation:
- Remaining risks:

## Verdicts

- Source/package verdict:
- Original behavioral observation:
- Current-state gate:
- Residual diagnostics:
```

The mapping file is authoring evidence, not runtime context. Keep it outside the skill package. Historical mappings may retain required/allowed/forbidden partitions, ordering, RED/GREEN, and exact-section contracts. Preserve them as historical diagnostics; only required-skill inclusion, package fidelity, and material disclosure collapse affect current acceptance.

`references/index.md` is the single source of truth for full-section `Read when` guidance. Do not duplicate every index row in `mapping.md`. Record only unusual routing rationale or disputed choices beside the relevant evaluation case.

## Manual Conversion Procedure

### 1. Freeze fidelity and evaluation evidence

Before authoring, inventory the canonical source, define representative positive discovery and disclosure cases, and freeze their raw fixtures. Follow `_skill-workbench/EVALUATION.md`. Fixture content is frozen at this point, but required-skill ownership remains provisional until the complete sibling catalog is reconciled.

Each positive case names the minimum required skill set. Do not classify every other live skill as allowed or forbidden. Define semantic ordinary, focused, or comprehensive expectations without requiring an exact selected-skill set or exact focused-section count. A skill-disabled baseline is optional diagnostic evidence; it is not needed to prove that the source conversion is faithful.

After all batch descriptions exist and before behavioral execution, require an independent fixture-ownership audit against the complete catalog. Each required skill must contribute a distinctive central judgment, not merely share topic vocabulary with the prompt. If the pre-run audit rejects a frozen fixture, preserve its content, hash, and contract as a not-run diagnostic, then freeze a separately named replacement. If later evidence rejects a fixture, preserve its runs too. Never rewrite evidence or retroactively relax a required set.

Record each new case's distinctive judgment, neighboring ownership boundary, independent ownership verdict, exact fixture hash, and intended disclosure mode using evaluation contract version 2. A focused probe also names the source-detail need absent from `SKILL.md` and its intended index destinations; a narrow implementation decision alone does not qualify.

Completion criterion: the conversion has a source-fidelity inventory, every positive case has an explicit required set and completed ownership review, fixture hashes validate, and the three progressive-disclosure tiers have representative probes.

### 2. Establish the lens

Read all inputs. Write one sentence naming the book's corrective bias and list its nearest neighboring skills.

Completion criterion: the mapping document names a distinctive lens and explains why at least three near-neighbor prompts belong to this or another skill.

### 3. Design invocation

Derive candidate branches from nano, the mini `When to use` statement, and distinctive full-rule triggers. Compare the candidate description with every existing skill description. Record provisional full-only candidates for the activation coverage audit.

Completion criterion: the description has a compact lens identifier, distinct trigger branches, a positive scope boundary, no workflow summary, provisional full-only candidates, and catalog collision cases with expected outcomes.

### 4. Map nano

Assign every `N*` item to description, early guidance, reference routing, final check, or a justified merge.

Completion criterion: every nano ID has an explicit destination and none creates a second authoritative copy of a mini rule.

### 5. Reshape mini

Assign every `M*` item to one concern group. Reorder groups according to nano salience. Merge only when operational meaning remains complete and traceable.

Completion criterion: every mini ID has exactly one authoritative destination, related rules and triggers are colocated, and no rule is split between priority buckets.

### 6. Build reference routing

Write `Read when` guidance for every full section. Define ordinary, focused, and comprehensive branches. Complete the activation coverage audit against the resulting full-section inventory, then finalize the description before the catalog freeze.

Completion criterion: every full section is reachable, focused scenarios identify a bounded set of sections, comprehensive scenarios require the full reference, and every full-only activation candidate has a source-traced promote/reject decision.

### 7. Write metadata and account for context

Write `agents/openai.yaml`, explicitly enabling or disabling implicit invocation according to the mapping decision.

Measure description characters, mini words, skill words, and packaging overhead. Do not paraphrase canonical mini guidance to meet a budget.

Completion criterion: UI metadata satisfies field constraints, the default prompt invokes the exact skill name, the description is at most 500 characters, and the body is at most 500 words or has a source-driven size exception. Packaging overhead targets 150 words; 151-200 requires a documented clarity rationale, and more than 200 fails.

### 8. Validate structurally

Run the wording fidelity checker and repository validator as mandatory gates. Run the official skill validator as a complementary check when it is installed with its dependencies. If it is unavailable, record the exact path or error in `mapping.md`; external tool availability does not override passing repository structure and source-fidelity gates.

Run the repository validator for one or more conversions:

```bash
python3 _skill-workbench/scripts/validate_conversion.py \
  clean-code release-it refactoring working-effectively-with-legacy-code
```

After the batch catalog is complete, validate every durable required-skill contract:

```bash
python3 _skill-workbench/scripts/validate_evaluation_contracts.py
```

Run the wording checker separately for each skill so a failure includes a useful nearest-rule diff:

```bash
python3 _skill-workbench/scripts/check_rule_wording.py \
  --mini clean-code/clean-code.mini.md \
  --skill .agents/skills/clean-code/SKILL.md
```

Completion criterion: all structural, mapping, equality, anchor, range, link, placeholder, required-skill, versioned case-field, fixture-hash, independent-review, and final-verdict-block checks pass, and every wording difference is removed or explicitly justified.

### 9. Run behavioral evaluation

Use fresh agents with the same prompts, artifacts, model, and configuration. When a skill-disabled baseline is useful, keep its configuration matched. Evaluate required-skill discovery, application, disclosure, and package fidelity separately. Do not reveal the expected answer, required skills, suspected weakness, source trace, or conversion rationale. Restrict runtime guidance reads to `.agents/skills/**`; canonical rule or workbench reads invalidate the run. The blind solver reports observed selection and consulted files, while an independent reviewer performs source tracing afterward.

After catalog and ownership review, create one immutable evaluation manifest per
acceptance run with `_skill-workbench/scripts/evaluation_manifest.py`. The builder
derives the exact required set from the version 2 mapping contract and freezes the
catalog payload, case and mapping hashes, runner and schema hashes, model,
configuration, run name, and output path. Review the generated required sets and
catalog hash before dispatch. Run each manifest through
`run_skill_eval.py --manifest <path>`; do not repeat those fields manually.

Before parallel dispatch, require one live GREEN preflight through the current CLI, model, result schema, and manifest path using a stable direct positive fixture as specified in `EVALUATION.md`. Preserve any failed harness record, repair the evaluator, and verify a uniquely named successful replacement before treating later runs as behavioral evidence. A valid required-skill miss is catalog evidence, not a harness failure; preserve it and stop parallel dispatch for diagnosis.

If the runner correctly rejects only a solver-produced reporting inconsistency,
preserve that JSON and use a uniquely named same-configuration replacement to
complete the missing sample. Do not overwrite the invalid record or treat the
replacement as a retry of a valid selection miss. A repeated inconsistency is a
stop condition for reporting-contract or harness diagnosis.

During that diagnosis, compare the observed file-access shape with every state
the result schema can express. If no state represents the evidence truthfully,
add a failing integrity test and minimally repair the reporting contract before
collecting a replacement. Do not relabel or rewrite historical JSON after the
schema clarification.

For acceptance evidence, the runner evaluates the manifest-derived
`required <= selected` contract after the blind result is recorded, so expected
targets never appear in the solver prompt. It rejects catalog, case, mapping,
runner, or schema drift before launching Codex, refuses to overwrite an existing
result, embeds the manifest and its hash in the result, and compares the result
envelope with the manifest afterward. Direct runner arguments and manual
`--required-skill` values remain available only for exploratory or historical
runs; they do not satisfy the current acceptance contract.

Completion criterion: every positive run includes all required skills, no disclosure probe shows material tier collapse, and the independent source review finds no unsupported package guidance. Extra skill selections, selection order, general solver knowledge, and exact focused-section differences are diagnostic.

### 10. Review independently and regress the catalog

Have an agent other than the converter review semantic fidelity. Compare all descriptions and choose reruns from the change-impact matrix in `EVALUATION.md`; description, router, active-guidance, fixture, harness, and model changes invalidate different evidence. Run direct and unnamed distinctive cases three times. Broad, null, and ambiguous prompts may be retained as context-cost diagnostics.

Completion criterion: the independent reviewer finds no unsupported strengthening, weakening, omission, or imported guidance; every repeated positive run includes its required skills; and progressive disclosure remains materially intact. Overlapping selection is not a failure by itself.

## Validation Matrix

### Structural checks

- Skill folder name equals frontmatter `name`.
- Name is valid lowercase kebab-case and under 64 characters.
- Frontmatter contains only `name` and `description`.
- `SKILL.md` is under 100 lines or has a documented exception.
- Description is at most 500 characters.
- `SKILL.md` is at most 500 words or has a documented `Size Exception`.
- Packaging overhead is at most 150 words beyond canonical mini.
- References are one level deep and directly linked from `SKILL.md`.
- `openai.yaml` parses and satisfies UI constraints.
- No placeholders, conversion notes, or auxiliary documentation exist inside the skill.

### Semantic checks

- Every `M*` item is represented exactly once or faithfully merged.
- Every `N*` item influences invocation, salience, routing, or final checking.
- Every wording change from mini is necessary and records original text, final text, and rationale.
- Every prescriptive mini/nano detail reverse-traces to explicit canonical full-rule support; a broad section citation is not sufficient.
- Every newly authored technical directive in the description, body, checklist, or router is inventoried and source-traced; packaging-only prose introduces no technical claim.
- The wording checker reports exact primary bias, mini-rule wording, and final-checklist wording and order, or only documented exceptions.
- Nano priority did not fragment a complete mini rule.
- Related guidance is colocated.
- No source modality was strengthened or weakened.
- The primary bias is recognizable without the book title.
- Generic no-op guidance has been removed unless evaluation shows models need it.
- Every material recommendation encoded in the package traces to `M*`, nano salience, or a full-reference heading; answer-level general judgment need not trace but must not be attributed to the book.

### Reference checks

- `references/full.md` matches the canonical full rule.
- Every full heading appears in the index.
- Every index heading, anchor, and line range resolves correctly.
- Every `Read when` condition is specific and actionable.
- The router distinguishes ordinary, focused, and comprehensive use.
- Focused cases name the semantic source detail they need without imposing an exact section set.
- A route selecting one-third or more of the full sections receives manual tier-collapse review.

### Invocation checks

- Direct book-name prompts include the skill in the selected set.
- Distinctive symptom prompts include the skill in the selected set.
- Compatible overlap may select any additional relevant book skills.
- Near-neighbor and generic prompts are retained as context-cost diagnostics when useful.
- Description branches do not merely repeat synonyms.
- Description remains useful if truncated from the end.
- Full-only activation candidates have source-traced promote/reject decisions; every promoted branch has an unnamed positive fixture.
- Every positive case has an explicit required skill set.
- Every version 2 case records distinctive judgment, neighbor ownership, completed ownership review, and a matching fixture hash.

### Guidance checks

- The agent applies early nano-prioritized guidance under schedule, authority, sunk-cost, or scope pressure.
- The agent uses the book's distinctive vocabulary and tradeoffs.
- The agent does not over-apply the lens outside its scope.
- The final checklist catches missed applicable guidance.
- A focused issue reaches relevant full sections without material tier collapse.
- A comprehensive request loads the full reference end to end.
- Focused fixtures identify information absent from `SKILL.md` and the intended index destinations before execution.

### Behavioral evaluation checks

- Optional baseline and packaged runs use the same prompt, artifact, model, and configuration.
- Required-skill discovery, application, disclosure, and package fidelity are judged separately.
- Raw artifacts are used for substantive application cases.
- Direct and distinctive unnamed positive cases include every required skill in three independent runs.
- The evaluator is not told expected skills, source IDs, or suspected weaknesses.
- An agent other than the converter performs final semantic review.
- Rerun scope follows the documented change-impact class; different models are never combined into one repetition count.
- Every acceptance run uses a mapping-derived manifest whose catalog, case, mapping, runner, and schema hashes validate before dispatch.
- Every result embeds the manifest and its hash, preserves the configured output name, and has no manifest-envelope error.
- Source/package, original behavioral, current-state, and residual-diagnostic verdicts remain separate.

## Pilot Validation Shapes

Validate this process against three deliberately different shapes before converting the full catalog:

1. `clean-code`: broad, high-frequency, local implementation and review guidance. Tests description precision and context salience.
2. `release-it`: specialized production-reliability guidance. Tests distinctive operational triggers and full-reference routing.
3. `refactoring` plus `working-effectively-with-legacy-code`: an overlapping pair. Tests catalog collision handling, compatible co-invocation, and scope discrimination.

The third shape is one conversion study with two skill artifacts. Use one agent so it must design both descriptions together.

After the pilots:

1. Review each skill independently against this process.
2. Run a catalog-level description and invocation comparison.
3. Record recurring misses as process defects.
4. Update this file before changing pilot skills for a cross-book issue.
5. Re-run affected pilots after process changes.
6. Preserve existing skill-disabled pilot controls as `retroactive baseline` diagnostics; new baselines are optional.
7. Freeze the process only when all three shapes pass the current evaluation protocol.

## Per-Thread Assignment Contract

Each conversion agent receives ownership only of:

- `.agents/skills/<assigned-book>/`
- `_skill-workbench/<assigned-book>/mapping.md`

For the overlap pilot, one agent owns both assigned skill and mapping directories.

Agents must:

- Read this process and every required input.
- Inspect existing work instead of deleting or reverting it blindly.
- Compare descriptions against the live catalog.
- Perform manual semantic conversion.
- Run available validation.
- Report changed files, validation evidence, and unresolved risks.
- Leave final semantic acceptance to an independent reviewer.

Agents must not:

- Edit `_skill-workbench/PROCESS.md` during a conversion.
- Edit canonical rule files.
- Edit another agent's skill or mapping files.
- Automate semantic authoring.
- Commit, push, or open a pull request unless explicitly requested.

## Definition of Done

A conversion is complete only when:

- The description includes the target skill for direct and distinctive unnamed positive prompts; additional relevant selections are permitted.
- The activation coverage audit records every full-only candidate and tests each promoted description branch.
- Every nano and mini traceability ID is mapped.
- Primary bias, mini rule wording, and final checklist wording and order are preserved verbatim except for documented, necessary changes.
- Every newly authored technical directive and prescriptive router condition traces to canonical source; packaging-only prose adds no technical claim.
- `SKILL.md` is guidance-only, concise, faithful, and conceptually colocated.
- Context budgets pass or a source-driven size exception is documented.
- The full rule is preserved verbatim and is reachable for focused and comprehensive use.
- The index covers every full section with valid anchors, ranges, and manually authored conditions.
- UI metadata is valid and invocation policy is explicit.
- Structural and semantic validation passes.
- Behavioral tests cover required-skill discovery, application, and all three disclosure tiers; near-neighbor and null behavior is diagnostic.
- Direct and distinctive unnamed positive cases include every required skill in three independent runs.
- Current acceptance runs use immutable mapping-derived manifests and preserve their manifest hashes in result evidence.
- Progressive disclosure has no material tier collapse; exact focused-section counts are not required.
- An independent reviewer approves semantic fidelity.
- Remaining risks are documented in the mapping file.
- No unrelated files were changed.
