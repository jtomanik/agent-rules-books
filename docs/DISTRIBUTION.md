# Distribution

This repository uses four distribution surfaces with one source of truth:

1. GitHub is the canonical, versioned source.
2. skills.sh distributes the portable skills to many coding agents.
3. The Codex marketplace distributes the native Codex plugin.
4. The Claude marketplace distributes the native Claude Code plugin.

The guidance is not translated per platform. `.agents/skills/` is authoritative
for skill content. `plugins/agent-rules-books/skills/` is the committed Codex
and Claude distribution payload and must remain byte-for-byte identical.

## GitHub

The public source repository is:

```text
https://github.com/jtomanik/agent-rules-books
```

Use tagged releases for stable distribution. Platform manifests and the
repository marketplace must use the same plugin version. The current
development branch is `codex/rule-book-skills-checkpoint`.

## skills.sh

skills.sh discovers the fourteen packages directly from `.agents/skills/`. No
skills.sh-specific runtime dependency or duplicate skill tree is required.

Install the collection from the fork's default branch:

```bash
npx skills add jtomanik/agent-rules-books --all
```

Install one skill for a particular agent:

```bash
npx skills add jtomanik/agent-rules-books \
  --skill clean-code \
  --agent codex \
  --global
```

Test the current checkout without publishing it:

```bash
npx skills add . --list
npx skills add . --all
```

Use either the skills.sh installation or a native marketplace installation for
an agent. Installing both creates duplicate discovery paths for the same
guidance.

## Codex

Install the current fork branch:

```bash
codex plugin marketplace add jtomanik/agent-rules-books \
  --ref codex/rule-book-skills-checkpoint
codex plugin add agent-rules-books@agent-rules-books
```

After the package is merged into the default branch, omit `--ref`:

```bash
codex plugin marketplace add jtomanik/agent-rules-books
codex plugin add agent-rules-books@agent-rules-books
```

Invoke a bundled skill with its namespace:

```text
$agent-rules-books:clean-code
```

Update the marketplace and plugin after a versioned release:

```bash
codex plugin marketplace upgrade agent-rules-books --json
codex plugin remove agent-rules-books@agent-rules-books --json
codex plugin add agent-rules-books@agent-rules-books --json
```

## Claude Code

Install the current fork branch as a Git-hosted third-party marketplace:

```bash
claude plugin marketplace add \
  jtomanik/agent-rules-books@codex/rule-book-skills-checkpoint
claude plugin install agent-rules-books@agent-rules-books
```

After the package is merged into the default branch, omit the branch ref:

```bash
claude plugin marketplace add jtomanik/agent-rules-books
claude plugin install agent-rules-books@agent-rules-books
```

Claude namespaces the installed skills with the plugin name. For example:

```text
/agent-rules-books:clean-code
```

Refresh and update a release with:

```bash
claude plugin marketplace update agent-rules-books
claude plugin update agent-rules-books@agent-rules-books
```

## Release Checklist

When guidance changes:

1. Update `.agents/skills/` and validate the source-faithful conversion.
2. Rebuild `plugins/agent-rules-books/skills/` from `.agents/skills/`.
3. Bump the version in `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and both marketplace manifests.
4. Run the package and marketplace validation commands.
5. Commit, tag, and push the release to GitHub.

The package must not remove meaningful guidance because another skill covers a
similar topic. Platform packaging changes metadata and installation paths, not
the rules themselves.
