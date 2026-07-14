# Agent Rules Books Plugin Design

Date: 2026-07-14

Status: Approved for implementation

## Context

The repository contains fourteen source-faithful Codex skills under
`.agents/skills/`. Each skill preserves mini-derived active guidance, nano-derived
activation emphasis, an inline reference map, an exhaustive index, and an
unchanged full reference.

The collection is useful outside this repository, but direct installation as
fourteen user-level skill directories has three drawbacks:

- users must install and update each directory as an unmanaged copy;
- the collection has no single installable identity or version;
- direct copies would conflict with plugin-provided skills of the same names.

Codex plugins are the distribution boundary for a reusable collection of two or
more skills. The plugin must preserve the existing progressive-disclosure and
source-fidelity contracts rather than introducing another transformation layer.

## Goals

- Package all fourteen converted skills as one shareable Codex plugin.
- Expose the plugin through a repository marketplace.
- Keep `.agents/skills/` as the authoritative authoring location.
- Make plugin copies byte-for-byte reproducible and mechanically checkable.
- Install and verify the plugin on this machine.
- Replace the fourteen direct copies in `~/.codex/skills` only after the plugin
  installation is proven complete.
- Push the implementation branch to the authenticated user's fork without
  changing the upstream `origin` remote.
- Document installation and maintenance so the workflow remains discoverable.

## Non-Goals

- Rewording, compressing, merging, or otherwise changing any converted skill.
- Re-running the book-to-skill conversion process.
- Adding MCP servers, apps, connectors, hooks, credentials, or runtime services.
- Publishing to the public Plugins Directory.
- Opening an upstream pull request.
- Re-running the complete behavioral matrix when packaged skill bytes are
  unchanged.

## Chosen Architecture

Use a self-contained committed plugin package with enforced parity:

```text
.agents/
  plugins/
    marketplace.json
  skills/
    <authoritative fourteen skill packages>

plugins/
  agent-rules-books/
    .codex-plugin/
      plugin.json
    skills/
      <byte-identical copies of the fourteen skill packages>

_skill-workbench/
  scripts/
    sync_plugin_skills.py
    tests/
      test_sync_plugin_skills.py
```

This structure follows Codex's self-contained plugin convention. It keeps the
existing authoring and evaluation paths stable while making the plugin portable
without depending on files outside its root.

Rejected alternatives:

- Making the plugin tree authoritative and symlinking `.agents/skills` would
  avoid duplication but would relocate an established source boundary and add
  churn to validation and historical evidence.
- Treating the repository root as the plugin would avoid copies but would make
  installation package unrelated rules, workbench evidence, and repository
  files.
- Symlinking from the plugin to `.agents/skills` would not produce a
  self-contained shareable package.

## Plugin Metadata

The plugin manifest lives at
`plugins/agent-rules-books/.codex-plugin/plugin.json` and contains:

- name: `agent-rules-books`
- version: `0.1.0`
- skills path: `./skills/`
- project author, homepage, repository, and MIT license attribution
- engineering-focused keywords and install-surface descriptions
- display name: `Agent Rules Books`
- category: `Engineering`
- concise example prompts for code quality, architecture, domain modeling,
  data-system correctness, production resilience, and legacy-code work

The manifest does not declare MCP servers, apps, hooks, tool dependencies,
authentication dependencies, or presentation assets. Plugin versioning is
independent from the repository's rule-set release version and changes when the
distributed package or plugin metadata changes.

The repository marketplace lives at `.agents/plugins/marketplace.json`. It
contains one local entry named `agent-rules-books` whose source is
`./plugins/agent-rules-books`, installation policy is `AVAILABLE`, and category
is `Engineering`. Required marketplace authentication metadata uses the
standard `ON_INSTALL` policy, but the skill-only plugin performs no
authentication and requests no credentials.

## Source And Parity Contract

`.agents/skills/` remains the sole authoritative skill source. The plugin tree
is a generated distribution artifact, not a place for manual edits.

`sync_plugin_skills.py` supports two explicit modes:

- `--check` is read-only. It compares the expected skill names, relative file
  paths, file types, and file bytes. It fails on changed, missing, or unexpected
  content and prints actionable drift details.
- `--write` copies the complete authoritative packages without parsing or
  rewriting Markdown. It builds a temporary sibling tree, validates that tree,
  and replaces only `plugins/agent-rules-books/skills` after the complete copy
  succeeds.

The tool has a fixed repository-relative source and target. It must reject
symlinks or unsupported file types so a published plugin cannot depend on paths
outside its root. It must never edit `.agents/skills`, canonical rule files,
references, mappings, evaluation evidence, global Codex state, or unrelated
plugin files.

The expected package set is exactly:

1. `a-philosophy-of-software-design`
2. `clean-architecture`
3. `clean-code`
4. `code-complete`
5. `designing-data-intensive-applications`
6. `domain-driven-design`
7. `domain-driven-design-distilled`
8. `implementing-domain-driven-design`
9. `patterns-of-enterprise-application-architecture`
10. `refactoring`
11. `refactoring-guru`
12. `release-it`
13. `the-pragmatic-programmer`
14. `working-effectively-with-legacy-code`

No meaningful book content may be removed because another bundled skill covers
a similar topic. Every source package is copied in full.

## Installation Transaction

Installation is ordered so the existing direct copies remain available until
the plugin is proven usable:

1. Generate the plugin package with `sync_plugin_skills.py --write`.
2. Pass repository tests, parity checks, manifest checks, marketplace checks,
   source-fidelity checks, and all fourteen official skill validations.
3. Commit the implementation and push the current branch to a separate `fork`
   remote. Keep `origin` unchanged.
4. Register the fork and implementation branch as a Codex marketplace using
   `codex plugin marketplace add` with an explicit branch reference.
5. Install `agent-rules-books` using `codex plugin add --json`.
6. Resolve the installed cache path from CLI output rather than assuming a
   cache layout.
7. Verify the installed manifest and all fourteen installed skill packages
   against the committed plugin tree.
8. Run a fresh-session plugin discovery and explicit-invocation smoke check so
   the namespaced plugin skill identity is demonstrated.
9. Remove exactly the fourteen direct directories listed below.
10. Confirm plugin inventory and absence of duplicate direct copies.

The implementation may first register the local repository as a marketplace
for development, but final installation evidence must use the pushed fork and
branch that make the plugin shareable.

## Direct-Copy Removal Boundary

After successful plugin installation, installed-cache parity, and discovery
smoke validation, remove only these paths:

```text
~/.codex/skills/a-philosophy-of-software-design
~/.codex/skills/clean-architecture
~/.codex/skills/clean-code
~/.codex/skills/code-complete
~/.codex/skills/designing-data-intensive-applications
~/.codex/skills/domain-driven-design
~/.codex/skills/domain-driven-design-distilled
~/.codex/skills/implementing-domain-driven-design
~/.codex/skills/patterns-of-enterprise-application-architecture
~/.codex/skills/refactoring
~/.codex/skills/refactoring-guru
~/.codex/skills/release-it
~/.codex/skills/the-pragmatic-programmer
~/.codex/skills/working-effectively-with-legacy-code
```

Do not remove or modify any unrelated global skill, system skill, plugin,
marketplace, cache entry, configuration entry, or repository file.

## Failure And Rollback Behavior

- A generation, validation, commit, push, marketplace, installation, cache, or
  discovery failure stops the transaction before direct-copy removal.
- A failed `--check` never mutates files.
- A failed `--write` leaves the previous complete plugin skill tree in place.
- A failed plugin installation does not remove or disable direct skills.
- If final inventory fails after direct-copy removal, restore the fourteen
  direct copies from the authoritative `.agents/skills` tree before ending the
  task.
- Existing unrelated configuration warnings are reported separately and do not
  become reasons to rewrite global Codex state.

## Validation Strategy

Deterministic validation includes:

- unit tests for the exact package list;
- unit tests for clean parity, changed bytes, missing files, unexpected files,
  rejected symlinks, `--check`, and transactional `--write` behavior;
- JSON parsing and required-field checks for both plugin and marketplace
  manifests;
- resolution of every manifest and marketplace path;
- byte-for-byte source-to-plugin parity;
- the existing workbench unit tests and conversion validators;
- exact mini-derived wording checks;
- official skill validation for all fourteen plugin-packaged skills;
- `git diff --check` and a staged-scope review;
- successful marketplace registration and plugin installation;
- installed-cache parity with the committed plugin tree;
- one fresh-session namespaced discovery and explicit-invocation smoke check;
- final confirmation that direct duplicates are absent and unrelated global
  skills remain.

The complete forty-two-case behavioral matrix is not rerun because the plugin
copies are byte-identical to already evaluated skill packages. Plugin discovery
and namespaced invocation receive a focused smoke check because distribution
changes skill identity and discovery context even when instruction bytes are
unchanged.

## Documentation And Distribution

Implementation updates:

- `README.md` with a short plugin installation entry point;
- `docs/USAGE.md` with marketplace registration, installation, update, removal,
  direct-skill migration, and verification commands;
- this design document as the durable rationale and safety contract.

The authenticated user's GitHub fork is added as a separate `fork` remote if it
is not already configured. The current implementation branch is pushed there.
The upstream `origin` URL and branch are not changed, and no upstream pull
request is opened unless separately requested.

## Acceptance Criteria

The work is complete when:

- the repository contains a valid self-contained `agent-rules-books` plugin;
- the repository marketplace exposes exactly that plugin;
- plugin skill bytes exactly match all fourteen authoritative packages;
- sync and validation tests pass;
- installation and maintenance instructions are discoverable;
- the implementation commit exists on the user's fork;
- Codex installs the plugin from that fork and branch;
- a fresh task can discover and explicitly invoke a namespaced bundled skill;
- the fourteen direct global copies are removed only after successful plugin
  verification;
- unrelated global skills and Codex state remain untouched.
