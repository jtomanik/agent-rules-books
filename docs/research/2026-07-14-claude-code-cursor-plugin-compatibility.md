# Claude Code and Cursor Plugin Compatibility

Date: 2026-07-14

## Executive Finding

The rule content and the plugin package are two different compatibility
problems.

The existing `SKILL.md` files are already close to portable Agent Skills:
each has `name` and `description` frontmatter, the name matches the skill
directory, and the supporting `references/` files live inside the skill
directory. There is no need to translate the book guidance into a second
Claude-specific or Cursor-specific wording.

What is missing is a native distribution wrapper for each editor:

| Surface | Native package marker | Skill location inside a package | Invocation shape |
| --- | --- | --- | --- |
| Codex | `.codex-plugin/plugin.json` | `skills/` | `$agent-rules-books:clean-code` |
| Claude Code | `.claude-plugin/plugin.json` | `skills/` | `/agent-rules-books:clean-code` |
| Cursor | `.cursor-plugin/plugin.json` | `skills/` | `/clean-code` or automatic discovery, subject to Cursor's UI/marketplace behavior |

Claude Code and Cursor use different plugin manifests and marketplace
catalogues. The same packaged `skills/` directory can serve both, but one
manifest cannot replace the other.

The practical design is therefore:

1. Keep `.agents/skills/` as the authoritative Agent Skills source.
2. Keep `plugins/agent-rules-books/skills/` as the release package, generated
   or checked for exact content parity with the source.
3. Add small Claude and Cursor manifest wrappers around that same release
   package.
4. Offer the generic `npx skills` installation path as a second option for
   users who want direct skills rather than a managed plugin.

This is packaging work, not another rule-conversion process.

## What The Standards Already Give Us

The Agent Skills specification defines a skill as a directory containing a
`SKILL.md` with at least `name` and `description` metadata, plus optional
scripts, references, and assets. It explicitly describes progressive
disclosure: the agent initially sees the name and description, then reads the
full skill when the task matches it.

Source: [Agent Skills specification](https://github.com/agentskills/agentskills)

That maps directly to this repository's current shape. The book's `nano`
version remains the source for activation-oriented description and top-level
guidance, the skill body contains the practical guidance, and the full rule
material remains available through the bundled reference router. This remains
one content model regardless of which editor loads it.

The current skills also use relative links such as
`references/index.md` and `references/full.md`. Those references are inside
each skill package, so they satisfy the important distribution constraint:
an installed plugin must not depend on files outside its own cached package.
Claude Code explicitly copies installed plugins into a cache and disallows
outside-directory references.

Source: [Claude Code plugin caching and file resolution](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)

## Claude Code Requirements

Claude Code distinguishes standalone skills from plugins. A plugin is a
directory containing `.claude-plugin/plugin.json`; its `skills/` directory is
at the plugin root, not inside `.claude-plugin/`.

For this repository, the native package would be:

```text
plugins/agent-rules-books/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    ├── clean-code/
    │   ├── SKILL.md
    │   └── references/
    └── ...
```

The manifest only needs to identify the package and can point at the package
skill directory:

```json
{
  "name": "agent-rules-books",
  "version": "0.1.0",
  "description": "Source-faithful software engineering guidance from fourteen books and references.",
  "author": {
    "name": "Maciej Ciemborowicz"
  },
  "repository": "https://github.com/ciembor/agent-rules-books",
  "license": "MIT",
  "skills": "./skills/"
}
```

Claude's plugin skills are always namespaced. That is a useful collision
avoidance feature, but it means the documentation must show the Claude form
`/agent-rules-books:clean-code`, not the Codex form.

For repository distribution, Claude Code expects a separate marketplace
catalogue at `.claude-plugin/marketplace.json`:

```json
{
  "name": "agent-rules-books",
  "owner": {
    "name": "Maciej Ciemborowicz"
  },
  "plugins": [
    {
      "name": "agent-rules-books",
      "source": "./plugins/agent-rules-books",
      "description": "Source-faithful engineering guidance from fourteen books."
    }
  ]
}
```

Users would then add the repository as a marketplace and install the plugin:

```text
/plugin marketplace add ciembor/agent-rules-books
/plugin install agent-rules-books@agent-rules-books
```

Claude Code provides `claude plugin validate .` for manifest, marketplace,
frontmatter, and path validation. Development can be tested with
`claude --plugin-dir ./plugins/agent-rules-books` before publishing.

Sources:

- [Claude Code plugin structure and skills](https://code.claude.com/docs/en/plugins)
- [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code plugin discovery and installation](https://code.claude.com/docs/en/discover-plugins)

## Cursor Requirements

Cursor has adopted Agent Skills and can discover `SKILL.md` files. Cursor's
plugin system is a separate packaging layer: a plugin has
`.cursor-plugin/plugin.json`, and a marketplace has
`.cursor-plugin/marketplace.json`.

The native Cursor package would reuse the same skill directories:

```text
plugins/agent-rules-books/
├── .cursor-plugin/
│   └── plugin.json
└── skills/
    ├── clean-code/
    │   ├── SKILL.md
    │   └── references/
    └── ...
```

A minimal Cursor plugin manifest is structurally similar to the Claude
manifest, but it is not interchangeable with it:

```json
{
  "name": "agent-rules-books",
  "displayName": "Agent Rules Books",
  "version": "0.1.0",
  "description": "Source-faithful software engineering guidance from fourteen books and references.",
  "author": {
    "name": "Maciej Ciemborowicz"
  },
  "repository": "https://github.com/ciembor/agent-rules-books",
  "license": "MIT",
  "skills": "./skills/"
}
```

The Cursor marketplace catalogue is also a separate file. The official Cursor
plugin repository uses a multi-plugin layout with each plugin under
`plugins/<name>/` and a root `.cursor-plugin/marketplace.json` listing those
directories:

```json
{
  "name": "agent-rules-books",
  "owner": {
    "name": "Maciej Ciemborowicz"
  },
  "plugins": [
    {
      "name": "agent-rules-books",
      "source": "plugins/agent-rules-books",
      "description": "Source-faithful engineering guidance from fourteen books."
    }
  ]
}
```

Cursor's official plugin examples confirm that `skills/` is a first-class
plugin component and that the per-plugin manifest declares the skill path.
Cursor's marketplace and plugin system are still evolving, so actual
marketplace submission and team/private distribution should be tested against
the current Cursor release rather than inferred solely from the file format.

Sources:

- [Cursor Agent Skills announcement](https://cursor.com/changelog/2-4)
- [Cursor plugin announcement](https://cursor.com/blog/marketplace)
- [Cursor official plugin repository](https://github.com/cursor/plugins)
- [Cursor official plugin manifest schema](https://github.com/cursor/plugins/blob/main/schemas/plugin.schema.json)
- [Cursor official marketplace manifest schema](https://github.com/cursor/plugins/blob/main/schemas/marketplace.schema.json)

## What `mattpocock/skills` Does

The current upstream `mattpocock/skills` repository uses two distribution
surfaces rather than trying to invent one universal plugin format.

### 1. Canonical Agent Skills source

The repository keeps its actual skills under the top-level `skills/` tree.
The skills are ordinary `SKILL.md` packages and are indexed by the
skills.sh installer. Its README describes the quick-start path:

```bash
npx skills@latest add mattpocock/skills
```

The installer lets the user choose the selected skills and target agents. The
underlying `vercel-labs/skills` tool documents support for Claude Code, Cursor,
and Codex, including these relevant destinations:

| Agent | Project destination | Global destination |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.codex/skills/` |
| Cursor | `.agents/skills/` | `~/.cursor/skills/` |

The installer can symlink a canonical checkout or copy the files. This gives
one content source and platform-specific discovery paths without changing the
skill wording.

Sources:

- [mattpocock/skills README](https://github.com/mattpocock/skills#quickstart-30-second-setup)
- [skills.sh repository and supported agents](https://github.com/vercel-labs/skills#supported-agents)
- [skills.sh installation options](https://github.com/vercel-labs/skills#options)

### 2. Native Claude Code plugin

The upstream repository also has a root `.claude-plugin/plugin.json` that
enumerates its skill directories. Users can install it as a managed Claude
plugin:

```text
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

The README explicitly presents this as a choice between editable copied
skills from skills.sh and a managed, read-only Claude bundle. It also says
that a native Codex plugin is on the roadmap. At the time of this research,
the upstream repository does not contain a `.cursor-plugin` wrapper or a
native Codex plugin; the cross-editor path is the generic skills.sh installer.

That is the important pattern: **portable content first, platform-specific
package metadata only where the platform has a native package system**.

Sources:

- [mattpocock/skills current repository](https://github.com/mattpocock/skills)
- [mattpocock/skills Claude plugin manifest](https://raw.githubusercontent.com/mattpocock/skills/main/.claude-plugin/plugin.json)
- [mattpocock/skills installation section](https://raw.githubusercontent.com/mattpocock/skills/main/README.md)

## Audit Of This Repository

The current repository already has the most important content-side pieces:

- `.agents/skills/` contains the authoritative portable skills.
- Each skill contains `SKILL.md`, `references/index.md`, and
  `references/full.md` where applicable.
- The full references are bundled inside each skill, so their relative links
  do not escape the package.
- `plugins/agent-rules-books/skills/` is an existing release copy used by the
  Codex plugin.
- `plugins/agent-rules-books/.codex-plugin/plugin.json` and
  `.agents/plugins/marketplace.json` already define the Codex package.
- The skill frontmatter currently uses the portable `name` and `description`
  fields and does not depend on Claude-only or Cursor-only body syntax.

The current gaps are packaging gaps:

- no `plugins/agent-rules-books/.claude-plugin/plugin.json`;
- no root `.claude-plugin/marketplace.json`;
- no `plugins/agent-rules-books/.cursor-plugin/plugin.json`;
- no root `.cursor-plugin/marketplace.json`;
- installation and invocation instructions currently focus on Codex.

The existing Codex package can therefore become the shared release payload for
all three native package wrappers. It should remain an exact-content copy of
`.agents/skills/`; the wrappers should not produce alternate rule text.

## Recommended Implementation Shape

### Preferred repository layout

```text
.
├── .agents/
│   ├── plugins/marketplace.json          # Codex marketplace
│   └── skills/                           # authoritative skill source
├── .claude-plugin/
│   └── marketplace.json                  # Claude marketplace
├── .cursor-plugin/
│   └── marketplace.json                  # Cursor marketplace
├── plugins/
│   └── agent-rules-books/
│       ├── .claude-plugin/plugin.json    # Claude wrapper
│       ├── .codex-plugin/plugin.json     # Codex wrapper
│       ├── .cursor-plugin/plugin.json    # Cursor wrapper
│       └── skills/                       # exact packaged skill copy
└── docs/
    └── USAGE.md                          # install choices and commands
```

### Keep one source of rule content

Do not create a Claude conversion and a Cursor conversion of each book. The
only platform-specific differences that belong in package metadata or usage
documentation are:

- manifest filename and schema;
- marketplace filename and source-path conventions;
- installation command;
- namespace or slash-command spelling;
- target discovery directory when using direct skills;
- optional platform metadata that does not change the guidance.

The `SKILL.md`, `references/index.md`, and `references/full.md` content should
remain byte-for-byte identical across generated packages. This is especially
important for this repository because source fidelity is the deliverable.

### Prefer two installation modes

Document both modes clearly:

1. **Managed plugin mode**: install the native Claude, Cursor, or Codex
   package. This is the best default for a stable read-only bundle and versioned
   updates.
2. **Direct Agent Skills mode**: use `npx skills add` or copy/symlink selected
   skill directories into the editor's native skills directory. This is useful
   when users want to edit, select, or scope individual skills.

Do not tell users to use both modes simultaneously. That creates duplicate
skill discovery and makes it unclear which version is active.

## Validation Plan

The compatibility work should be accepted only after these checks pass:

### Structural checks

- validate every `SKILL.md` with the Agent Skills reference validator or an
  equivalent repository check;
- validate `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json` with `claude plugin validate .`;
- validate the Cursor manifests against the official Cursor schemas;
- verify all three package skill trees contain the same files and bytes as the
  authoritative `.agents/skills/` tree;
- verify every relative link in a skill resolves inside that skill package;
- verify all three manifests carry the same release version.

### Installation checks

- Claude: load the package with `claude --plugin-dir` and invoke at least one
  skill using its namespaced command.
- Cursor: install the plugin through the available marketplace flow and
  verify both automatic discovery and slash-command visibility for a sample
  skill.
- Direct path: install one selected skill with `npx skills add` for each
  target and verify the expected destination.
- Check that installing a managed plugin and direct skills is documented as
  mutually exclusive for the same user/session.

### Content checks

- no rule sentence is removed or rewritten for platform reasons;
- no full reference is omitted from the native package;
- only package metadata, command examples, or installer documentation differ
  by platform;
- a diff against `.agents/skills/` is empty for each packaged skill tree.

## Scope And Effort

This is a small packaging extension, not another conversion batch.

| Work | Expected size | Risk |
| --- | --- | --- |
| Claude plugin manifest | small | low |
| Claude marketplace manifest | small | low |
| Cursor plugin manifest | small | low |
| Cursor marketplace manifest | small | low |
| version/parity validation | small to medium | medium |
| installation documentation and smoke tests | medium | medium, because editor versions and marketplace access vary |
| rewriting or translating the skills | none | should not be done |

The only part that deserves real end-to-end testing is the install/discovery
behavior in the installed Claude Code and Cursor versions. The rule content
does not need a second authoring pipeline.

## Decision

Proceed with a shared release payload and three thin native wrappers. Use the
generic Agent Skills installer as a fallback and convenience path, following
the model used by `mattpocock/skills`. Keep the full book-derived guidance and
the progressive-disclosure structure unchanged.

The next implementation should add only the missing manifests, parity/version
checks, and usage documentation, then test the installed package in Claude
Code and Cursor. It should not introduce automatic translation of
`SKILL.md`, a second rule hierarchy, or editor-specific copies of the book
guidance.
