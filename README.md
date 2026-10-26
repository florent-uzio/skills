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

### Plugins

- **[xrpl](./plugins/xrpl/README.md)** — Claude Code plugin that runs the XRPL MCP server locally (test networks only). Install with `/plugin marketplace add florent-uzio/skills` then `/plugin install xrpl@florentuzio-plugins`.
