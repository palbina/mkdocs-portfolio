# Data Model: Portfolio Improvements

**Date**: 2026-07-05

This feature modifies existing entities and creates new entities within the established data model of a static documentation site. No database involved — all "entities" are filesystem artifacts.

## Entities

### Blog Post (File)

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `date` | ISO date (YYYY-MM-DD) | Yes | Publication date, matches filename prefix |
| `authors` | List of author keys | Yes | References entries in `.authors.yml` |
| `categories` | List of strings | Yes | Standardized categories: Kubernetes, GitOps, Observability, Security, Networking, Storage, CI/CD, OS, Cloud Native |
| `tags` | List of strings | No | Free-form tags for search filtering |
| `description` | String | Yes | SEO meta description |
| `draft` | Boolean | No | If `true`, excluded from published index |
| `pin` | Boolean | No | If `true`, pinned to top of index |
| `readtime` | Integer | No | Estimated read time in minutes |
| `slug` | String | No | URL slug override (defaults to filename) |
| `content` | Markdown body | Yes | Must include `<!-- more -->` excerpt delimiter and follow TEMPLATE-BLOG-POST.md 10-section structure |

**Validation Rules**:
- Filename must match `YYYY-MM-DD-{slug}.md` pattern
- `authors` keys must exist in `docs/blog/.authors.yml`
- `categories` values should use established categories (avoid ad-hoc categories)
- `date` must not be in the future for published posts

**State Transitions**: draft → published (remove `draft: true`); published → archived (add to archive)

### Project Card (HTML Component)

A styled `<div>` block inside `docs/index.md` `projects-grid` container.

| Attribute | Type | Description |
|:----------|:-----|:------------|
| `.project-card` | CSS class | Standard card or `.featured` for first card |
| `.project-icon` | CSS class | Unicode emoji icon with drop-shadow glow |
| `h3` | Element | Project name |
| `.project-impact` | CSS class | Uptime/status metric in JetBrains Mono |
| `.tech-tags` | CSS class | Container for `.tech-tag` pills |
| `.project-link` | CSS class | Anchor linking to project detail page |

**Validation Rules**:
- Must exist for all 8 project pages in `docs/projects/`
- Link href must match the actual project page path
- Tech tags should match the project's documented stack
- Impact metric should reflect the project header meta-grid values

### Configuration File (YAML)

`mkdocs.yml` and `zensical.toml` are site configuration files.

| Property | Type | Description |
|:----------|:-----|:------------|
| `plugins` | Array/Object | Plugin configuration |
| `nav` | Array/Object | Navigation tree |
| `theme` | Object | Material theme settings |
| `extra_css` | Array | Stylesheet references |

**Changes in this feature**:
- `mkdocs.yml`: Remove `macros` plugin block (lines referencing `scripts/main`). Add header comment.
- No changes to `zensical.toml` (canonical config).

### CSS Class (Stylesheet Rule)

A defined but unused CSS rule in `docs/stylesheets/extra.css`.

**Removal target**: `.hero-stats`, `.stat`, `.stat-number`, `.stat-label` — defined in CSS (approximately lines 195-208) but never rendered in `docs/index.md` HTML.

**Validation Rule**: After removal, `grep "\.hero-stats" docs/stylesheets/extra.css` returns zero matches.

## Relationships

```
Landing Page (docs/index.md)
├── contains → 8 Project Cards
│   └── links to → Project Pages (docs/projects/*.md)

Blog Index (docs/blog/index.md)
├── contains → Blog Posts (docs/blog/posts/*.md)
│   └── authored by → Author (docs/blog/.authors.yml)

Site Config
├── zensical.toml ← CANONICAL (active build)
└── mkdocs.yml    ← REFERENCE (historical, not used in build)
```
