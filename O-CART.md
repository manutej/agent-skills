# o-cart

> CARTO-inspired geospatial intelligence, recast for Ormus workflows.

This repository is the **seed** for **o-cart** (`Ormus-Solutions/o-cart`).

Connected GitHub identity `manutej` cannot create repositories under the **Ormus-Solutions** organization (GitHub 403: org admin required). The GitHub `create_repository` tool was also locked after that failed org attempt, so this seed exists as a **fork of [CartoDB/agent-skills](https://github.com/CartoDB/agent-skills)** on the personal account:

**https://github.com/manutej/agent-skills**

`CartoDB/agent-skills` is the closest public MIT-licensed CARTO source to Ormus practice: Claude Code / Codex / Gemini skills that drive location intelligence through the CARTO CLI and MCP Server, including `carto-create-workflow`.

## Rename + transfer (do this next)

Anyone with write on this repo (and later org admin on Ormus-Solutions):

```bash
# 1. Rename the fork to the requested name
gh repo rename o-cart --repo manutej/agent-skills

# 2. Transfer into the org (requires org admin to accept)
gh api -X POST repos/manutej/o-cart/transfer -f new_owner=Ormus-Solutions
```

Or GitHub UI:

1. Settings → General → Repository name → `o-cart`
2. Settings → General → Danger Zone → Transfer ownership → `Ormus-Solutions`

## Why this upstream, not a dump of every CartoDB repo

CARTO publishes 400+ repos. o-cart is not a monorepo of all of them. Lineage we treat as upstream inspiration:

| Upstream | Why it matters to o-cart |
|----------|--------------------------|
| [CartoDB/agent-skills](https://github.com/CartoDB/agent-skills) (**this fork**) | Agent skills + workflow authoring playbooks. MIT. |
| [CartoDB/workflows-extension-template](https://github.com/CartoDB/workflows-extension-template) | Extension-package shape for warehouse spatial DAGs. Metadata marks CARTO Proprietary — **do not copy `carto_extension.py` or other proprietary blobs.** |
| [CartoDB/analytics-toolbox-core](https://github.com/CartoDB/analytics-toolbox-core) | Spatial analytics UDFs across BigQuery / Snowflake / Redshift / Postgres / Databricks. |
| [CartoDB/cartoframes](https://github.com/CartoDB/cartoframes) | Python location-intelligence notebook workflow. |

## Ormus customization layer

Ormus workflows in this overlay:

- Agent-first skills (same grain as `ormus-agent-ops` and the Libre family)
- Explicit evidence, fail-closed on bad spatial inputs
- Warehouse-native analysis (no silent data movement)
- Transfer-ready public MIT © Ormus Solutions for *new* Ormus files

Start at [`skills/o-cart/SKILL.md`](skills/o-cart/SKILL.md).

## License

- Upstream CARTO agent-skills: MIT (see `LICENSE`)
- New Ormus overlay files: MIT © 2026 Ormus Solutions
