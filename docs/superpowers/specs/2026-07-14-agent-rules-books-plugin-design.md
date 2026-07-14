# Agent Rules Books Plugin Design

Date: 2026-07-14

Status: Approved for implementation, simplified after scope review

## Goal

Distribute all fourteen accepted rule-book skills as one shareable Codex plugin,
install it from the user's fork, and remove the duplicate direct installations
only after the plugin is proven usable.

## Package Shape

```text
.agents/
  plugins/
    marketplace.json
  skills/
    <authoritative skill packages>

plugins/
  agent-rules-books/
    .codex-plugin/
      plugin.json
    skills/
      <exact copies of .agents/skills>
```

`.agents/skills/` remains authoritative. The plugin copy is a committed
distribution artifact. Packaging copies the complete tree without parsing or
rewriting any file.

The package set is exactly:

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

No meaningful content is removed because another bundled skill covers a similar
topic.

## Metadata

The plugin identity is `agent-rules-books`, version `0.1.0`. Its manifest keeps
the project's author, upstream repository, and MIT license attribution. It
declares only `./skills/`; it has no MCP server, app, hook, authentication,
credential, or runtime dependency.

The repository marketplace contains one local entry named
`agent-rules-books`, pointing to `./plugins/agent-rules-books` with category
`Engineering`.

## Packaging And Validation

No custom synchronizer or plugin validator is needed. The package is small,
version controlled, and already has source-fidelity tooling.

Package it with a direct recursive copy, then validate it with existing tools:

```bash
rm -rf plugins/agent-rules-books/skills
mkdir -p plugins/agent-rules-books
cp -R .agents/skills plugins/agent-rules-books/skills
diff -qr .agents/skills plugins/agent-rules-books/skills
```

Acceptance requires:

- `diff -qr` reports no source-to-plugin difference;
- neither tree contains symlinks;
- the existing workbench unit tests pass;
- all fourteen existing conversion and exact-wording checks pass;
- all fourteen plugin copies pass the official skill validator;
- Codex can load the repository marketplace and install the plugin;
- a fresh task explicitly invokes a namespaced bundled skill.

The forty-two-case behavioral matrix is not rerun because packaging does not
change skill bytes or behavior. The focused fresh-task smoke covers the only new
surface: plugin discovery and namespaced invocation.

## Distribution And Migration

Implementation is committed on `codex/rule-book-skills-checkpoint` and pushed
to a separate `fork` remote at
`https://github.com/jtomanik/agent-rules-books.git`. Upstream `origin` remains
unchanged and no upstream pull request is opened.

Installation order:

1. Validate and commit the package.
2. Push the branch to the fork.
3. Register `jtomanik/agent-rules-books` at the explicit implementation ref as
   a Codex marketplace.
4. Install `agent-rules-books@agent-rules-books`.
5. Compare the installed cache with the committed plugin package.
6. Run the fresh-task namespaced invocation smoke.
7. Remove only the fourteen duplicate direct directories under
   `~/.codex/skills`.
8. Repeat inventory and invocation checks.

Any failure before step 7 leaves the direct copies untouched. If a check fails
after step 7, restore all fourteen direct copies from `.agents/skills` before
ending the task. Unrelated global skills, plugins, marketplaces, caches, and
configuration remain untouched.

## Documentation

`README.md` provides the short install path. `docs/USAGE.md` records remote and
local installation, namespaced invocation, update, removal, direct-copy
migration, and the direct copy plus `diff -qr` maintenance workflow.
