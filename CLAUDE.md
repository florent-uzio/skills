Skills are organized into bucket folders under `skills/`:

- `ripple/` — Ripple Custody and Ripple-specific tools
- `engineering/` — daily code work
- `productivity/` — daily non-code workflow tools
- `misc/` — kept around but rarely used
- `in-progress/` — drafts not yet ready to ship
- `deprecated/` — no longer used

Every skill in `ripple/`, `engineering/`, `productivity/`, or `misc/` must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`. Skills in `in-progress/` and `deprecated/` must not appear in either.

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.
