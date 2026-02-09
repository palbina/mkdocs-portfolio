# MkDocs Portfolio Implementation

**Type**: Feature
**Date**: 2026-02-09
**Status**: Complete

## Overview

Implementation of a minimalist DevOps portfolio using MkDocs with Material theme, featuring custom terminal-style aesthetics, automated builds, and Kubernetes deployment integration. The homepage follows the "30-Second Test" and "Hero Section Formula" principles for maximum impact and conversion.

## Problem/Goal

The user wanted to replace or complement their existing Next.js portfolio with a static "Docs as Code" approach using MkDocs, maintaining a high-performance, easy-to-update technical portfolio in their HomeLab environment.

## Solution/Implementation

- **MkDocs Foundation**: Used `mkdocs-material` theme with `slate` (dark) color scheme.
- **Custom Branding**: Implemented a "Terminal/Cyber" aesthetic using `extra.css` with a focus on flat design, no shadows, and cyan accents.
- **Dynamic Content**: Developed Python macros (`scripts/main.py`) to inject GitHub repository stats and build timestamps.
- **Containerization**: Created a multi-stage `Dockerfile` to build the static site with Python/Cairo and serve it using an optimized Nginx Alpine image.
- **CI/CD**: Developed a GitHub Actions workflow (`deploy.yml`) that builds the Docker image, pushes it to GHCR, and automatically updates the Kubernetes manifests in the `HOMELAB-INFRA` repository.
- **SEO & Social**: Added JSON-LD schema via `main.html` overrides and configured social cards.
- **Homepage Enhancement**: Redesigned homepage following the interactive-portfolio skill principles:
  - Hero section with label, headline, subline, and impact statistics
  - Featured project badges and impact metrics
  - Value propositions section
  - Tech showcase with tech stack pills
  - Clear CTA section

## Code Changes

### Core Configuration

- **`mkdocs.yml`**: Configured with search, minify, git-revision, and macros plugins. Added CSS cache-buster (`?v=2.0`) for reliable updates.

### Styling

- **`docs/stylesheets/extra.css`**:
  - Implements the dark terminal theme with cyan accents
  - Hero section styling with gradient name, label badges, and stats
  - Project cards with featured badges and impact metrics
  - Dark mode button fixes for primary and secondary buttons
  - Value propositions and tech showcase styling

### Homepage

- **`docs/index.md`**: Complete redesign with:
  - Hero section with statistics (30+ Apps, 99.9% Uptime, 3 K8s Nodes)
  - Featured project highlighting
  - Value propositions and tech stack showcase
  - Clear call-to-action section

### Deployment

- **`nginx.conf`**: Configured with Gzip, security headers, and health endpoints
- **`.github/workflows/deploy.yml`**: Handles automated delivery and GitOps updates

## Key Decisions

- **Separate App**: Decided to deploy as a separate application at `docs.arkenops.cc` rather than replacing the main portfolio.
- **Multi-stage Build**: Included Cairo dependencies in the build stage to support the `social` plugin card generation while keeping the final image small.
- **Sync Waves**: Integrated with the existing GitOps pattern for smooth deployment order.
- **Interactive Portfolio Principles**: Applied "30-Second Test" and "Hero Section Formula" for homepage design.
- **CSS Cache-Busting**: Added version query parameter (`?v=2.0`) to force CSS reload after updates.

## Tradeoffs

- **Pros**: Lightning fast performance, extremely easy technical documentation, GitOps native, professional modern design.
- **Cons**: Less interactive than the React/RAG version (doesn't include the AI Chat feature directly).

## Related Files

- `mkdocs.yml` - Main configuration with theme settings and plugins
- `Dockerfile` - Multi-stage container build process
- `docs/index.md` - Main landing page with hero section and project showcase
- `docs/stylesheets/extra.css` - Custom dark theme with terminal aesthetics
- `scripts/main.py` - Python macros for dynamic data injection
- `.github/workflows/deploy.yml` - CI/CD pipeline for automated deployment

## Bug Fixes

### Dark Mode Button Hover (2026-02-09)

**Problem**: Button text became invisible on hover in dark mode (slate theme) due to MkDocs Material theme applying `color: var(--md-accent-bg-color)` which is `rgba(0, 229, 255, 0.1)` (nearly transparent).

**Solution**: Added aggressive CSS specificity overrides in `extra.css`:

```css
/* Primary buttons */
[data-md-color-scheme="slate"] .md-typeset .md-button--primary:hover {
    background-color: #00B8D4 !important;
    color: #000 !important;
}

/* Secondary buttons */
[data-md-color-scheme="slate"] .md-typeset .md-button:not(.md-button--primary):hover {
    background-color: #00E5FF !important;
    color: #000 !important;
}
```

**Root Cause**: The theme's `.md-typeset .md-button:hover` rule sets text color to a variable that resolves to near-transparent cyan in slate color scheme.

## Testing / Verification

- [x] Local site generation
- [x] Docker build verification
- [x] GitHub Action push to GHCR
- [x] ArgoCD sync verification
- [x] Dark mode button hover fix verified locally
- [x] Homepage redesign verified with all sections rendering correctly

## Notes

- The ImagePullSecret (`ghcr-login`) must be regenerated per-namespace as it is a SealedSecret.
- Local development requires Python venv with dependencies from `requirements.txt`.
- MkDocs dev server auto-reloads on file changes but may require restart for CSS changes to propagate.
- Browser cache can cause delays in seeing CSS updates; use cache-buster or hard refresh (Ctrl+Shift+R).
