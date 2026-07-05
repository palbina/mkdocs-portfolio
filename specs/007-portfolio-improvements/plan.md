# Implementation Plan: Portfolio Improvements

**Branch**: `007-portfolio-improvements` | **Date**: 2026-07-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/007-portfolio-improvements/spec.md`

## Summary

Four maintenance and content improvements to the ArkenOps portfolio: (1) complete the blog with 2 new posts and fix the existing incomplete one, (2) add 2 missing project cards to the landing page and remove dead CSS, (3) update CONTRIBUTING.md for Zensical workflow and clean up residue files, (4) mark mkdocs.yml as historical reference and remove the broken macros plugin entry. All changes are documentation content and config file edits — no new dependencies, no architectural changes.

## Technical Context

**Language/Version**: Markdown (Spanish), YAML, CSS, HTML — no programming language changes required.

**Primary Dependencies**: Zensical SSG v0.0.24+, Material for MkDocs theme (via Zensical), blog plugin, Tera template engine.

**Storage**: Git repository (filesystem). No database or external storage.

**Testing**: Manual verification via `zensical build` and browser inspection. No automated test suite needed for content changes.

**Target Platform**: Static site served via Nginx on Docker (Linux x86_64). Browser targets: Chrome, Firefox, Safari (latest 2 versions).

**Project Type**: Static documentation website (SSG-generated HTML/CSS with Markdown source).

**Performance Goals**: No regression in build time or page load. CSS file size should decrease after removing dead code. Blog index load unaffected by adding 2 posts.

**Constraints**: All changes must pass `zensical build` without errors. Must not break existing navigation, links, or the Diátaxis documentation structure. Blog posts must follow `TEMPLATE-BLOG-POST.md` contract.

**Scale/Scope**: 8 file modifications across 4 files. 2 new blog post files created. 1 residue file deleted or gitignored. CSS dead code removed (~20 lines). Zero new dependencies.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Assessment |
|:----------|:------|:-----------|
| I. Docs as Code | ✅ PASS | All changes are documentation files versioned in Git. Blog posts follow established template. |
| II. Infrastructure as Code | N/A | No infrastructure changes in this feature. |
| III. Zero Trust by Default | N/A | No security changes in this feature. |
| IV. Observability Completa | N/A | No observability changes in this feature. |
| V. Simplicidad y Justificación | ✅ PASS | CSS dead code removed (simplification). mkdocs.yml cleaned of broken references. Residue file removed. |
| Migration & Tooling | ✅ PASS | CONTRIBUTING.md updated to Zensical workflow. mkdocs.yml marked as historical. zensical.toml remains canonical. |
| Diátaxis Framework | ✅ PASS | New blog posts are categorized. Landing page cards link to existing project pages within the framework. |
| Spanish Language | ✅ PASS | Blog posts and documentation changes in Spanish per constitution. |
| Git Workflow | ✅ PASS | All changes on feature branch `007-portfolio-improvements`. Commits follow conventional format. |

**Gate Result**: ✅ ALL GATES PASS. No violations. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/007-portfolio-improvements/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

This feature modifies existing files and creates new blog posts. No new directories or code modules.

```text
docs/
├── index.md                     # MODIFY: Add 2 project cards (FR-003)
├── stylesheets/
│   └── extra.css                # MODIFY: Remove .hero-stats dead CSS (FR-004)
├── blog/
│   └── posts/
│       ├── 2026-02-10-talos-linux-k8s.md  # MODIFY: Complete section 3 (FR-001)
│       ├── 2026-07-05-gitops-real-world.md      # CREATE: New blog post (FR-002)
│       └── 2026-07-05-observability-correlation.md # CREATE: New blog post (FR-002)
mkdocs.yml                       # MODIFY: Add historical comment, remove macros (FR-007, FR-008)
CONTRIBUTING.md                  # MODIFY: Update to Zensical commands (FR-005)
.gitignore                       # MODIFY: Add =0.0.24 if not deleted (FR-006)
=0.0.24                          # DELETE: Residue file (FR-006)
```

**Structure Decision**: This is a documentation improvement feature. All changes are within existing `docs/` structure and config files at the repository root. No new directories or architectural components created. Blog posts follow existing convention `docs/blog/posts/YYYY-MM-DD-slug.md`.

## Complexity Tracking

> No constitution violations. This section intentionally empty.
