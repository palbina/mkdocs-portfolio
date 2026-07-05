# Data Model: Homelab Portfolio Enrichment

**Feature**: 008-homelab-portfolio-enrichment
**Date**: 2026-07-05

## Entity 1: Project Page (`docs/projects/*.md`)

Represents a technical project or capability documented in the portfolio.

### Attributes

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `title` (frontmatter) | string | ✅ | Display title in Spanish |
| `description` (frontmatter) | string | ✅ | One-line summary for SEO/open graph |
| `status` (meta-grid) | enum | ✅ | PRODUCTION\_READY, OPERATIONAL, or WIP |
| `domain` (meta-grid) | string | ✅ | Technical domain label (e.g., BARE\_METAL\_CLUSTER) |
| `key_tech_1` (meta-grid) | string | ✅ | Primary technology identifier |
| `key_tech_2` (meta-grid) | string | ✅ | Secondary technology or metric |
| `overview` | markdown | ✅ | Vision section with `!!! impact` admonition |
| `architecture_diagram` | mermaid | ✅ | System architecture as Mermaid graph |
| `architecture_notes` | markdown | ✅ | Explanatory admonitions (`!!! info`) |
| `tech_stack_tables` | markdown tables | ✅ | Technology choices organized by category |
| `implementation` | markdown | ✅ | Technical implementation details |
| `operations` | markdown | ✅ | Operational procedures, runbooks, lessons learned |
| `results` | markdown | ✅ | Quantified outcomes and metrics |

### State Transitions

```
Draft → [content written] → Operational → [data updated] → Updated
  ↓                            ↓
WIP                         Production_Ready
```

### Validation Rules

- All 6 sections must be present (Visión General, Arquitectura, Stack Tecnológico, Implementación, Operaciones, Resultados)
- Mermaid diagram must render without syntax errors
- At least one data point must be traceable to TalosLab source material
- No internal IPs or real domain names (`.subetupaginacp.com`)
- `title` and `description` in frontmatter must be populated

### Relationships

- **References** → `docs/reference/` pages (for detailed technical info)
- **Explained by** → `docs/explanation/` pages (for architectural rationale)
- **Linked from** → `docs/index.md` (landing page project cards)
- **Linked from** → `docs/projects/index.md` (project index page)

---

## Entity 2: Reference Page (`docs/reference/*.md`)

Technical reference material: commands, versions, configurations.

### Attributes

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `title` | string | ✅ | Reference page title |
| `content_sections` | markdown | ✅ | Organized technical data |
| `version_table` | markdown table | ✅ | Software versions with dates |
| `last_updated` | date | ✅ | Source data currency date |

### State Transitions

```
Generic → [TalosLab data applied] → Aligned
```

### Validation Rules

- All versions must match TalosLab `QUICK_REFERENCE.md` (as of 2026-06-23)
- No placeholder versions (e.g., "vX.Y" or "latest")
- Commands must reflect real TalosLab operational practices (fish shell, no kubectl apply)

### Relationships

- **Supports** → Project Pages (detailed technical reference)
- **Sourced from** → TalosLab `docs/reference/QUICK_REFERENCE.md`

---

## Entity 3: Explanation Page (`docs/explanation/*.md`)

Architectural rationale, design decisions, and "why" documentation.

### Attributes

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `title` | string | ✅ | Explanation topic title |
| `core_concept` | markdown | ✅ | Central idea explained |
| `real_world_example` | markdown | ✅ | Concrete example from TalosLab |
| `lessons_learned` | markdown | ✅ | Practical takeaways from real operations |
| `architecture_decision` | markdown | ✅ | ADR-style decision record |

### State Transitions

```
Generic → [TalosLab lessons applied] → Enriched
```

### Validation Rules

- Must include at least one concrete example from TalosLab operations
- Must reference at least one architectural decision from `docs/architecture/` of talos-gitops
- No generic/abstract descriptions without real-world anchoring

### Relationships

- **Explains** → Project Pages (the "why" behind technical choices)
- **References** → Reference Pages (for specific versions/configs)
- **Sourced from** → TalosLab `docs/architecture/*.md`

---

## Entity 4: Landing Page (`docs/index.md`)

Portfolio entry point with project cards grid.

### Attributes

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `hero_section` | markdown + HTML | ✅ | Main headline and tagline |
| `project_cards` | HTML grid | ✅ | Array of project card entries |
| `card_count` | integer | ✅ | Must match actual project pages |

### State Transitions

```
8_cards → [new projects added] → 11+_cards
```

### Validation Rules

- Card count must equal number of project pages in `docs/projects/` (excluding `index.md`)
- Each card must have: icon, title, description, tech tags, link
- Links must resolve to existing `.md` files

### Relationships

- **Links to** → All Project Pages
- **Links to** → Project Index (`docs/projects/index.md`)

---

## Entity Relationship Summary

```
TalosLab Sources (external, read-only)
    ↓ provides data for
Project Pages (9 existing + 3 new)
    ← explained by —— Explanation Pages (3 updated)
    ← referenced by — Reference Pages (3 updated)
    ← linked from —— Landing Page (1 updated)
```
