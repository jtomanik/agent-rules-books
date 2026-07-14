# Agent Skills and Coding-Agent Plugin Distribution

**Snapshot:** 2026-07-14

This note compares four first-party distribution surfaces using official product documentation, official marketplace/repository source, and first-party metrics where published. “Skill” means a reusable `SKILL.md` instruction package; “plugin” means a larger package that may bundle skills with MCP/apps, agents, hooks, rules, or other capabilities.

## Executive Summary

- **skills.sh / `vercel-labs/skills`** has the broadest reach and the clearest public traction signal. One CLI installs the same skill format into dozens of agents, and the leaderboard exposes anonymous install counts. It is the best distribution multiplier for portable, skill-only guidance, but it is not a capability-security boundary and its ecosystem quality is not guaranteed.
- **Claude Code plugin marketplaces** provide the most complete open marketplace protocol: public or private Git-hosted catalogs, multiple source types, project/user scopes, version detection, auto-update, team configuration, managed allowlists, and container seeding. The official directory has strong GitHub traction, but Anthropic does not publish marketplace install counts in the reviewed sources.
- **Cursor Marketplace** is a product-integrated, curated distribution channel for plugins that combine skills with tools and agent primitives. Its catalog expanded by more than 30 plugins in March 2026 and includes a large visible partner catalog. It is attractive for discovery and integrations, but its public marketplace is more centrally curated and less reproducible than a Git-based catalog; private team marketplaces are plan-dependent.
- **OpenAI Codex plugin marketplace** is the most integrated with the Codex desktop app, CLI, IDE extension, ChatGPT Work, workspace roles, and app permissions. It supports curated, repo, personal, Git-backed, local, and npm-backed catalogs. It is newer and more governance-oriented: availability can depend on workspace, role, app authentication, product surface, and rollout state. The official `openai/plugins` repository is a useful traction proxy, but no per-plugin install counts were found.

## Comparison

| Surface | Primary reach | Traction signal available | Install/update model | Main limitation |
| --- | --- | --- | --- | --- |
| skills.sh / `vercel-labs/skills` | OpenCode, Claude Code, Codex, Cursor, and dozens of other agents | Public leaderboard with per-skill install telemetry; the directory exposes all-time, trending, and hot views | `npx skills add`; project or global; symlink or copy; `skills check`/`update` | Anonymous telemetry is opt-out, ecosystem quality/security is not guaranteed, and agent-specific features vary |
| Claude Code marketplaces | Claude Code on macOS, Linux, Windows/WSL; terminal and desktop/IDE workflows | Official marketplace repository showed 32.1k stars, 3.6k forks, 2,172 commits; no install count | Add a catalog, install by `name@marketplace`, refresh catalog, update plugin or auto-update | Plugins execute with user privileges; cached copies cannot reference arbitrary files outside the plugin directory |
| Cursor Marketplace | Cursor editor, including desktop product surfaces and Cursor cloud/automations | Cursor announced 30+ new plugins in March; marketplace showed a broad partner catalog; no install count | Browse/install from Marketplace; build and submit plugins; team marketplaces for Teams/Enterprise | Curated submission channel; private team marketplace capability is plan-dependent; public docs do not expose a comparable update/lockfile workflow |
| Codex plugin marketplace | ChatGPT web Work, ChatGPT desktop Work/Codex, Codex CLI, IDE extension, and Codex environments | Codex reported 5M+ weekly users; `openai/plugins` showed 4.6k stars, 667 forks, 299 commits; no install count | Browse configured/curated catalogs; `codex plugin marketplace add`, `upgrade`, `remove`; app installs into a versioned cache | Plugin availability can depend on workspace role, enabled apps, authentication, product, or rollout; local changes require refresh/restart/new session |

The counts above are not directly comparable: skills.sh reports install telemetry, while the repository figures are social activity proxies and the Codex user figure is product-wide, not plugin adoption.

## 1. skills.sh / `vercel-labs/skills`

### Traction and discovery

The official [skills.sh documentation](https://www.skills.sh/docs) says the leaderboard is ranked from anonymous CLI telemetry and tracks which skills are installed. The [live directory](https://www.skills.sh/) exposes install counts plus all-time, trending, and hot views; at the time checked, leading entries had reached the hundreds of thousands or millions of installs. These are the strongest directly measured adoption signals among the four surfaces reviewed. The values are dynamic and should be treated as a current snapshot, not as a durable market-size statistic.

The [official `vercel-labs/skills` README](https://github.com/vercel-labs/skills/blob/main/README.md) describes the project as an open agent-skills CLI and lists support for OpenCode, Claude Code, Codex, Cursor, and dozens of additional agents. It also provides per-agent project/global paths, so a source repository can be distributed once and materialized for several consumers.

### Installation and updates

Typical installation is `npx skills add owner/repo`, a Git URL, a direct skill path, a local path, or a GitLab URL. Users can select agents and skills, install globally or in the current project, and choose symlinks or copies. `npx skills list`, `find`, `remove`, `check`, and `update` form the management flow. Symlinking gives one canonical copy and makes local updates visible across linked agents; copying is the fallback when symlinks are unsuitable.

The CLI records install state in a lock file for tracked installs and uses a server-side hash check for updates. The [official CLI source/docs](https://github.com/vercel-labs/skills/blob/main/README.md) documents `skills check` and `skills update`; the open [update/sync issue](https://github.com/vercel-labs/skills/issues/283) is evidence that a fully reproducible “ensure this lock file is installed” workflow was still an open design gap in the reviewed project state.

### Coverage and limitations

The format is intentionally portable, but feature support is not uniform. The README’s compatibility table marks basic skills as broadly supported while `allowed-tools`, `context: fork`, and hooks have agent-specific support. The CLI also relies on each agent’s documented loading conventions and correct target directories.

The [CLI documentation](https://www.skills.sh/docs/cli) says anonymous telemetry is used to rank skills and can be disabled with `DISABLE_TELEMETRY=1`; `DO_NOT_TRACK` is an alternative. The [official security guidance](https://www.skills.sh/docs) explicitly says routine audits occur but quality or security of every listed skill is not guaranteed. This makes skills.sh a discovery and transport layer, not a trust endorsement or sandbox.

## 2. Claude Code Plugin Marketplace

### Traction and discovery

Anthropic’s [official marketplace repository](https://github.com/anthropics/claude-plugins-official) is a curated directory with separate internal and external plugin trees. At snapshot time GitHub showed 32.1k stars, 3.6k forks, 2,172 commits, and 41 contributors. That is a substantial public traction signal, but it measures interest and contribution activity rather than installs. No official per-plugin or total marketplace install metric was located.

The official marketplace is automatically available in Claude Code and can be browsed through `/plugin` or [claude.com/plugins](https://claude.com/plugins). Third-party marketplaces are independently hosted catalogs, normally on GitHub, GitLab, Bitbucket, or a self-hosted Git service.

### Installation and updates

The [marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces) defines a `marketplace.json` catalog. Users add a marketplace with `/plugin marketplace add`, install a plugin with `/plugin install plugin@marketplace`, and refresh with `/plugin marketplace update`. Plugins can be installed at user, project, or local scope; project scope records enabled plugins in `.claude/settings.json` for collaborators. The CLI exposes equivalent non-interactive commands.

Version resolution uses `plugin.json` version, marketplace version, or the Git commit SHA. Omitting a version on a Git source makes each new commit an update; specifying a version pins updates until it changes. Official marketplaces enable auto-update by default, while third-party and local marketplaces default to auto-update off. Teams can declare `extraKnownMarketplaces` and `enabledPlugins` in project settings, and administrators can restrict sources with `strictKnownMarketplaces`.

### Coverage and limitations

Claude plugins can bundle skills, agents, hooks, MCP servers, LSP servers, and commands. Claude Code supports macOS, Linux, and Windows through WSL or Git for Windows according to its [setup documentation](https://docs.anthropic.com/en/docs/claude-code/getting-started).

Marketplace plugins are copied into `~/.claude/plugins/cache` rather than used in place. The [plugin reference](https://code.claude.com/docs/en/plugins-reference) limits file references outside the plugin directory; shared content requires in-plugin symlinks that resolve within the allowed boundary. Plugins and marketplaces are trusted components that can execute arbitrary code with user privileges, and Anthropic states that it does not control or verify third-party contents. Offline and seeded-container operation is supported, but seeded marketplaces are read-only and cannot be updated by the user.

## 3. Cursor Marketplace

### Traction and discovery

Cursor launched its Marketplace in February 2026 with a highly curated partner set including Amplitude, AWS, Figma, Linear, and Stripe. The official [launch announcement](https://cursor.com/blog/marketplace) says plugins can combine MCP servers, skills, subagents, rules, and hooks. The [March expansion announcement](https://cursor.com/blog/new-plugins) says more than 30 new plugins were added from partners including Atlassian, Datadog, GitLab, Glean, monday.com, and PlanetScale.

The [official marketplace](https://cursor.com/marketplace) displayed featured, recently added, infrastructure, productivity, data, and other categories at snapshot time, with many first-party or partner integrations. Cursor does not expose public install counts in the reviewed marketplace pages, so catalog breadth and release cadence are the available first-party traction signals.

### Installation and updates

Users discover and install from the Marketplace product surface. Authors build a plugin and submit it through the [publish flow](https://cursor.com/marketplace/publish); Cursor’s launch post says community plugin submissions are accepted. A plugin is a bundle of one or more skills, subagents, MCP servers, hooks, or rules rather than a skill-only artifact.

The reviewed first-party sources do not document a public CLI equivalent to `npx skills add` or Claude’s marketplace commands, nor a public lockfile/update command. The operational model is therefore product-mediated Marketplace installation and Cursor-managed distribution. Authors should treat Cursor’s current Marketplace submission and review path as the source of truth for publishing requirements.

### Coverage and limitations

Cursor’s main advantage is integrated tool access: skills can be paired with MCP servers and agent orchestration primitives, including cloud-agent automations. Its main constraint for broad distribution is platform coupling: the plugin package targets Cursor’s primitives and is not itself a generic cross-agent transport.

Cursor initially described private team marketplaces as “coming soon” in February, while the March announcement states that Teams and Enterprise admins can create team marketplaces for private plugin distribution and management. This indicates that private distribution is available in an enterprise/team path, not equivalent to an unrestricted public catalog. The reviewed sources publish no comparable anonymous adoption metric or detailed version/update protocol.

## 4. OpenAI Codex Plugin Marketplace

### Traction and discovery

OpenAI reported in June 2026 that [more than 5 million people use Codex weekly](https://openai.com/index/codex-for-every-role-tool-workflow/), but that is product-wide usage, not plugin usage. The official [`openai/plugins` repository](https://github.com/openai/plugins) is the strongest public ecosystem proxy found: GitHub showed 4.6k stars, 667 forks, and 299 commits at snapshot time. It contains a curated collection of plugins with skills, apps, MCP configuration, agents, commands, hooks, and assets. No official install counts were found.

The Codex plugin directory is available in ChatGPT Work on the web, ChatGPT desktop Work/Codex, Codex CLI, and the IDE extension. The [official plugin documentation](https://learn.chatgpt.com/docs/plugins) says the CLI uses `/plugins`, the IDE uses Settings > Plugins, and installed bundled skills/tools become usable after a new CLI session, chat, or task as appropriate.

### Installation and updates

Codex supports a curated marketplace plus repo-scoped and personal `marketplace.json` catalogs. The [build documentation](https://learn.chatgpt.com/docs/build-plugins) defines local catalogs under `$REPO_ROOT/.agents/plugins/marketplace.json` or `~/.agents/plugins/marketplace.json`, and supports GitHub shorthand, HTTP(S)/SSH Git URLs, local roots, Git refs, sparse checkouts, local sources, Git-backed plugin sources, and npm packages. CLI management is `codex plugin marketplace add`, `list`, `upgrade`, and `remove`.

The desktop app installs plugins into a versioned cache under `~/.codex/plugins/cache`; a local plugin uses a `local` version. The app can enable or disable each plugin, and local development changes require updating the pointed-to directory and restarting the app. Workspace sharing keeps plugins within the organization boundary and does not publish them to the public directory. Plugins that include apps inherit workspace role access, app action controls, authentication, and the user’s permissions in the connected source system.

### Coverage and limitations

Codex packages can contain skills plus apps/MCP servers, browser extensions, hooks, and scheduled-task templates. This is a richer product integration than a portable `SKILL.md`, but it introduces more policy and authentication dependencies. For Business, Enterprise, and Edu workspaces, plugin availability can depend on workspace settings, feature access, role assignment, and whether required apps are enabled; the [OpenAI Help Center](https://help.openai.com/en/articles/20001256) documents these constraints.

The marketplace model is more controlled than a general public registry. Publicly shareable distribution is possible through marketplace sources and the official directory submission flow, but repo/personal catalogs and workspace sharing are distinct paths. The official docs also require a new session/chat after installation before bundled skills/tools are available. The open Codex repository contains active implementation and issue evidence around marketplace scope and cache behavior, so exact behavior should be verified against the installed Codex version before relying on it for reproducible team onboarding.

## Practical Recommendation

For a guidance-only package intended to reach multiple coding agents, publish a canonical `SKILL.md` source and make **skills.sh / `vercel-labs/skills`** the broad discovery and installation path. Keep platform-specific metadata and feature use conservative because compatibility varies.

For a Claude-first package that needs commands, hooks, agents, MCP, private Git sources, team configuration, or controlled update policy, use a **Claude Code marketplace**. It has the clearest public protocol for third-party catalogs and lifecycle management.

For a Cursor-specific integration whose value comes from MCP plus skills and agent orchestration, submit to the **Cursor Marketplace** and treat Cursor’s catalog/review process as the distribution contract.

For a Codex-native bundle that uses apps, workspace roles, or ChatGPT desktop integration, use a **Codex marketplace**. Keep a repo-local marketplace for reproducible project distribution and use the curated directory or submission flow for broader discovery; do not assume that a plugin available in the catalog is available to every workspace role or authentication mode.

## Sources

- [skills.sh documentation](https://www.skills.sh/docs)
- [skills.sh CLI reference](https://www.skills.sh/docs/cli)
- [`vercel-labs/skills` README](https://github.com/vercel-labs/skills/blob/main/README.md)
- [Vercel Labs skills directory](https://www.skills.sh/vercel-labs)
- [Anthropic Claude Code plugin discovery](https://code.claude.com/docs/en/discover-plugins)
- [Anthropic Claude Code marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces)
- [Anthropic Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference)
- [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)
- [Cursor Marketplace launch](https://cursor.com/blog/marketplace)
- [Cursor Marketplace expansion](https://cursor.com/blog/new-plugins)
- [Cursor Marketplace](https://cursor.com/marketplace)
- [Cursor plugin publishing](https://cursor.com/marketplace/publish)
- [OpenAI Codex plugins documentation](https://learn.chatgpt.com/docs/plugins)
- [OpenAI Codex plugin build/distribution documentation](https://learn.chatgpt.com/docs/build-plugins)
- [OpenAI Codex plugin Help Center](https://help.openai.com/en/articles/20001256)
- [`openai/plugins`](https://github.com/openai/plugins)
- [OpenAI: Codex for every role, tool, and workflow](https://openai.com/index/codex-for-every-role-tool-workflow/)
