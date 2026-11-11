# Skills

My Claude Code agent skills for working with Ripple Custody and day-to-day engineering.

## Quickstart

```bash
npx skills@latest add florent-uzio/skills
```

Pick the skills you want and which coding agents to install them on. Done.

## Reference

### Ripple

Skills specific to Ripple Custody instances.

- **[rc-version](./skills/ripple/rc-version/SKILL.md)** — Fetch the app version of a Ripple Custody instance from its OpenAPI spec. Handles both standard (`api.<hostname>`) and non-standard URLs (e.g. devboxes).

### Productivity

General-purpose skills for day-to-day work.

- **[excalidraw-recap](./skills/productivity/excalidraw-recap/SKILL.md)** — Create or update an Excalidraw diagram (`.excalidraw` file) that recaps work done: XRPL/MCP transactions, brainstorming, client meetings, system design. Saves to `~/excalidraw/` by default. Also mirrors to an Excalidraw MCP server when one is installed.
- **[post-merge-cleanup](./skills/productivity/post-merge-cleanup/SKILL.md)** — After a PR is merged, check out the default branch, pull, and delete the local branch you worked on. Handles squash/rebase merges.

### Plugins

- **[xrpl](./plugins/xrpl/README.md)** — Claude Code plugin that runs the XRPL MCP server locally (wallet seeds on test networks only). Install with `/plugin marketplace add florent-uzio/skills` then `/plugin install xrpl@florentuzio-plugins`.
