# MkDocs Portfolio Implementation

**Type**: Feature
**Date**: 2026-02-08
**Status**: Complete

## Overview

Implementation of a minimalist DevOps portfolio using MkDocs with Material theme, featuring custom terminal-style aesthetics, automated builds, and Kubernetes deployment integration.

## Problem/Goal

The user wanted to replace or complement their existing Next.js portfolio with a static "Docs as Code" approach using MkDocs, maintaining a high-performance, easy-to-update technical portfolio in their HomeLab environment.

## Solution/Implementation

- **MkDocs Foundation**: Used `mkdocs-material` theme with `slate` (dark) color scheme.
- **Custom Branding**: Implemented a "Terminal/Cyber" aesthetic using `extra.css` with a focus on flat design, no shadows, and cyan accents.
- **Dynamic Content**: Developed Python macros (`scripts/main.py`) to inject GitHub repository stats and build timestamps.
- **Containerization**: Created a multi-stage `Dockerfile` to build the static site with Python/Cairo and serve it using an optimized Nginx Alpine image.
- **CI/CD**: Developed a GitHub Actions workflow (`deploy.yml`) that builds the Docker image, pushes it to GHCR, and automatically updates the Kubernetes manifests in the `HOMELAB-INFRA` repository.
- **SEO & Social**: Added JSON-LD schema via `main.html` overrides and configured social cards.

## Code Changes

- **Configuration**: `mkdocs.yml` configured with search, minify, and git-revision plugins.
- **Style**: `docs/stylesheets/extra.css` implements the dark terminal theme.
- **Nginx**: `nginx.conf` configured with Gzip, security headers, and health endpoints.
- **Pipeline**: `.github/workflows/deploy.yml` handles automated delivery and GitOps updates.

## Key Decisions

- **Separate App**: Decided to deploy as a separate application at `docs.arkenops.cc` rather than replacing the main portfolio.
- **Multi-stage Build**: Included Cairo dependencies in the build stage to support the `social` plugin card generation while keeping the final image small.
- **Sync Waves**: Integrated with the existing GitOps pattern for smooth deployment order.

## Tradeoffs

- **Pros**: Lightning fast performance, extremely easy technical documentation, GitOps native.
- **Cons**: Less interactive than the React/RAG version (doesn't include the AI Chat feature directly).

## Related Files

- `mkdocs.yml` - Main configuration
- `Dockerfile` - Container build process
- `docs/index.md` - Main landing page with hero section
- `scripts/main.py` - Python macros for dynamic data

## Testing / Verification

- [x] Local site generation
- [x] Docker build verification
- [x] GitHub Action push to GHCR
- [x] ArgoCD sync verification

## Notes

The ImagePullSecret (`ghcr-login`) must be regenerated per-namespace as it is a SealedSecret.
