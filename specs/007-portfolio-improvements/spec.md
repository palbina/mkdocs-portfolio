# Feature Specification: Portfolio Improvements

**Feature Branch**: `007-portfolio-improvements`

**Created**: 2026-07-05

**Status**: Draft

**Input**: User description: "recomeindame mejoras al proyecto"

---

## User Scenarios & Testing

### User Story 1 - Blog Content Completion (Priority: P1)

A visitor navigates to the blog section and finds substantive technical content with complete articles, not placeholder text. The single existing post (Talos Linux) has its incomplete section filled. At least 2 additional blog posts are published demonstrating the blog system's value.

**Why this priority**: The blog infrastructure exists (plugin, template, authors, categories) but is nearly empty — 1 post with an incomplete section undermines the portfolio's credibility. Completing the blog demonstrates the system works end-to-end.

**Independent Test**: Navigate to the blog index. Verify at least 3 posts are visible with complete content. Open the Talos Linux post and verify section 3 ("Mi Experiencia de Migración") has real content, not placeholder text.

**Acceptance Scenarios**:

1. **Given** a visitor opens the blog index, **When** the page renders, **Then** at least 3 posts appear in the grid cards layout with complete excerpts, author info, and category tags.
2. **Given** a visitor opens the Talos Linux post, **When** they scroll to section 3 ("Mi Experiencia de Migración"), **Then** the section contains real migration experience content with concrete metrics (boot time comparison, migration steps, challenges encountered), not placeholder text `(Aquí relataré brevemente...)`.
3. **Given** new blog posts are created, **When** they follow the `TEMPLATE-BLOG-POST.md` structure, **Then** each post includes "El Problema", "La Solución", "Arquitectura" (Mermaid), "Implementación Paso a Paso", "Mi Experiencia en Producción" (metrics table), and "Cuándo Usar (y Cuándo No)" (tabbed).

---

### User Story 2 - Landing Page Consistency (Priority: P1)

A visitor sees all 8 project case studies represented on the landing page, not just 6. The unused hero-stats CSS component is either implemented in HTML or removed from the stylesheet. The landing page accurately reflects the full portfolio scope.

**Why this priority**: The landing page is the primary entry point. Showing only 6 of 8 projects creates an incomplete portfolio presentation. The unused CSS is dead code that increases stylesheet size without value.

**Independent Test**: Load the landing page. Verify 8 project cards render in the `.projects-grid`. Verify all cards link to correct project pages. Verify no unused CSS selectors for `.hero-stats` remain in `extra.css` unless the component is implemented.

**Acceptance Scenarios**:

1. **Given** the landing page renders, **When** the project cards grid is visible, **Then** 8 cards display (adding Progressive Delivery and Database HA that are currently missing), each with correct emoji icon, impact metric, tech tags, and navigation link.
2. **Given** the `.hero-stats` CSS is defined in `extra.css`, **When** the page is inspected, **Then** EITHER the hero-stats HTML component is implemented in `index.md` with stat numbers/labels OR the `.hero-stats` CSS is removed from `extra.css` (removing dead code).
3. **Given** a visitor clicks any of the 8 project cards, **When** the link is followed, **Then** they navigate to the correct project detail page.

---

### User Story 3 - Maintenance & Tooling Cleanup (Priority: P1)

The project's development tooling is consistent and free of vestigial artifacts. The CONTRIBUTING.md guide is accurate for the current Zensical-based workflow. Vestigial files are cleaned up.

**Why this priority**: Broken or outdated development documentation causes confusion for contributors. Vestigial CI configs and residue files create ambiguity about what's active vs historical.

**Independent Test**: Read CONTRIBUTING.md. Verify it references `zensical build` (not `mkdocs build`). Verify the residue file `=0.0.24` no longer exists at the project root. Verify CI workflow documentation is accurate.

**Acceptance Scenarios**:

1. **Given** a contributor reads CONTRIBUTING.md, **When** they follow the local dev instructions, **Then** they use `zensical build --clean` and `zensical serve` (not `mkdocs build` or `mkdocs serve`).
2. **Given** the project root directory, **When** inspected, **Then** the residue file `=0.0.24` no longer exists (either deleted or added to `.gitignore`).
3. **Given** the CI documentation in specs and contributions guide, **When** reviewed, **Then** it clearly states GitLab CI is the active pipeline and GitHub Actions + Forgejo workflows are vestigial/disabled.

---

### User Story 4 - SSG Configuration Simplification (Priority: P2)

The project has a single clear configuration source (`zensical.toml`). The retained `mkdocs.yml` is either clearly marked as historical reference in source comments, or the broken `macros` plugin reference (`scripts/main.py`) is removed to prevent confusion.

**Why this priority**: Dual configuration files create maintenance burden and confusion about which config is canonical. The broken macros reference in mkdocs.yml is misleading.

**Independent Test**: Inspect `mkdocs.yml`. Verify either: a header comment stating "This file is retained for historical reference only. Active config is zensical.toml" exists at the top, OR the broken `macros` plugin block is removed.

**Acceptance Scenarios**:

1. **Given** a developer opens `mkdocs.yml`, **When** they read the file, **Then** the macros plugin reference to `scripts/main` (which was deleted during Zensical migration) is either removed from the config or clearly commented as non-functional.
2. **Given** both config files exist, **When** a developer needs to change site configuration, **Then** CONTRIBUTING.md or the file header comments clearly indicate `zensical.toml` is the canonical config and `mkdocs.yml` is reference-only.

---

### Edge Cases

- What happens if the hero-stats HTML is implemented but the CSS classes don't match? The new section will render unstyled. Implementation MUST verify CSS class mapping before deploying.
- What happens when new blog posts are added but the author avatar URL is broken? The Material blog plugin falls back to a default avatar. Author avatars should use stable GitHub URLs.
- What happens if `=0.0.24` is a build artifact that gets recreated on each `zensical build`? Then it should be added to `.gitignore` instead of deleted. Need to verify the source before choosing strategy.
- What happens if GitHub Actions is actually needed (deployed via GitHub Container Registry)? Before removing, verify the workflow is truly vestigial and not used in any deployment path.

---

## Requirements

### Functional Requirements

- **FR-001**: The Talos Linux blog post (`docs/blog/posts/2026-02-10-talos-linux-k8s.md`) section 3 ("Mi Experiencia de Migración") MUST be completed with real migration experience content replacing the placeholder `(Aquí relataré brevemente...)`.
- **FR-002**: System MUST have at least 2 additional blog posts beyond the existing Talos Linux post, following the `TEMPLATE-BLOG-POST.md` structure.
- **FR-003**: The landing page (`docs/index.md`) project cards grid MUST display 8 cards (adding Progressive Delivery and Database HA that currently have project pages but no landing card).
- **FR-004**: The `.hero-stats`, `.stat`, `.stat-number`, `.stat-label` CSS classes in `docs/stylesheets/extra.css` MUST either have corresponding HTML markup in `docs/index.md` or be removed from the stylesheet.
- **FR-005**: `CONTRIBUTING.md` MUST reference `zensical build` and `zensical serve` commands (not `mkdocs build` or `mkdocs serve`).
- **FR-006**: The residue file `=0.0.24` at the project root MUST be removed or added to `.gitignore`.
- **FR-007**: `mkdocs.yml` MUST include a header comment indicating it is retained for historical reference and `zensical.toml` is the active configuration.
- **FR-008**: The broken `macros` plugin reference (`module_name: scripts/main`) in `mkdocs.yml` MUST be removed or explicitly commented as non-functional since `scripts/main.py` was deleted during Zensical migration.

### Key Entities

- **Blog Post**: A Markdown file in `docs/blog/posts/` following `YYYY-MM-DD-slug.md` naming with mandatory frontmatter (date, authors, categories) and standardized 10-section structure from `TEMPLATE-BLOG-POST.md`.
- **Project Card**: A styled HTML div block in `docs/index.md` representing a project case study with emoji icon, impact metric, tech tags, and navigation link.
- **Residue File**: The file `=0.0.24` at the project root — likely a Zensical version pin artifact or build output.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Blog section contains at least 3 complete posts (1 existing + 2 new), all with zero placeholder text.
- **SC-002**: Landing page displays 8 project cards matching the 8 project pages in `docs/projects/`.
- **SC-003**: `extra.css` contains zero unused CSS class definitions for landing page components.
- **SC-004**: `CONTRIBUTING.md` local development section accurately reflects the Zensical-only workflow with zero references to `mkdocs build` or `mkdocs serve` as the primary command.
- **SC-005**: Project root contains zero residue or build artifact files outside of tracked version control.
- **SC-006**: `mkdocs.yml` has no broken plugin references (macros pointing to deleted `scripts/main.py`).

---

## Assumptions

- The residue file `=0.0.24` is safe to delete and is not recreated by `zensical build`. If it is regenerated, it should be added to `.gitignore`.
- GitHub Actions workflow (`.github/workflows/deploy.yml`) is confirmed vestigial before removal. Investigation should verify it's not used in any active deployment path.
- New blog posts will be written in Spanish (per constitution language guideline) with technical terms in English where appropriate.
- The 2 missing project cards (Progressive Delivery, Database HA) follow the same HTML structure as the existing 6 cards.
- The hero-stats component was intended but never implemented; CSS removal is preferred over HTML implementation to avoid adding untested components.

---

## Out of Scope

- Full redesign of the landing page layout
- Adding new project case study pages beyond the 8 existing ones
- Creating a CI/CD bridge between GitHub Actions and GitLab CI
- Migrating to a different SSG (constitution v1.1.0 establishes Zensical as irreversible)
- Implementing hero-stats component (out of scope; the CSS is removed rather than implemented, per assumption)
- Multilingual/i18n support beyond Spanish
