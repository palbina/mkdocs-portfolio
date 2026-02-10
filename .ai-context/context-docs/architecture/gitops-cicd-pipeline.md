# GitOps CI/CD Pipeline Design

**Type**: Architecture
**Date**: 2026-02-09
**Status**: Complete

---

## Overview

Demonstration of modern CI/CD practices implementing GitOps principles for automated deployment. This pipeline showcases expertise in DevOps automation, container registries, and infrastructure-as-code workflows.

**Key Achievement**: Fully automated deployment pipeline from code commit to production in under 3 minutes, with zero manual intervention.

---

## DevOps Skills Demonstrated

| Domain | Technologies | Competency Level |
|--------|--------------|------------------|
| **CI/CD** | GitHub Actions, Workflows | Expert |
| **Containerization** | Docker, Multi-stage builds | Expert |
| **GitOps** | ArgoCD, Declarative deployments | Expert |
| **Registry Management** | GHCR, Image tagging strategies | Advanced |
| **Automation** | Shell scripting, Git operations | Advanced |

---

## Pipeline Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Developer │────▶│    GitHub   │────▶│   GitHub    │
│    Push     │     │   Repository│     │   Actions   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
                       ┌────────────────────────┼────────────────────────┐
                       │                        │                        │
                       ▼                        ▼                        ▼
               ┌──────────────┐      ┌──────────────────┐    ┌──────────────────┐
               │  Docker Build│      │  GitHub Container│    │  Update HOMELAB  │
               │  & Push      │      │  Registry (GHCR) │    │  INFRA Manifests │
               │  ~2 minutes  │      │  Image: sha-xxx  │    │  GitOps Repo     │
               └──────────────┘      └──────────────────┘    └──────────────────┘
                                                                            │
                                                                            ▼
                                                                  ┌──────────────────┐
                                                                  │  ArgoCD (K8s)    │
                                                                  │  Auto-Sync       │
                                                                  │  Production      │
                                                                  └──────────────────┘
```

---

## Pipeline Components

### 1. GitHub Actions Workflow
**File**: [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)

**Skills Demonstrated**:
- Workflow orchestration
- Event-driven automation
- Secret management
- Matrix builds and caching

**Triggers**:
- **Push to main**: Deploy on code changes
- **Schedule (daily)**: Update dynamic content (GitHub stats)
- **Manual**: On-demand deployments

### 2. Multi-Stage Docker Build
**File**: [`Dockerfile`](Dockerfile)

**Skills Demonstrated**:
- Build optimization
- Layer caching strategies
- Minimal production images
- Security scanning preparation

**Stages**:
| Stage | Base | Purpose | Size |
|:------|:-----|:--------|:-----|
| Builder | python:3.12-slim | Build static site | ~500MB |
| Runtime | nginx:1.27-alpine | Serve content | ~20MB |

### 3. GitOps Integration
**Pattern**: App-of-Apps with ArgoCD

**Skills Demonstrated**:
- Declarative infrastructure
- Git as single source of truth
- Automated manifest updates
- Rollback capabilities

**Flow**:
1. Build completes → Image pushed to GHCR
2. Workflow clones HOMELAB-INFRA repo
3. Updates deployment.yaml with new image tag
4. Commits and pushes change
5. ArgoCD detects drift → Auto-syncs

---

## Key Technical Decisions

### 1. GitHub Container Registry (GHCR)
**Decision**: Native GitHub integration vs Docker Hub

**Why**:
- Seamless GITHUB_TOKEN authentication
- No additional secrets management
- Integrated with GitHub Actions
- Free for public repositories

**Skills**: Registry selection, authentication patterns, cost optimization

### 2. Semantic Image Tagging
**Strategy**: Multiple tags for flexibility

```yaml
tags: |
  type=raw,value=latest      # General reference
  type=sha,prefix=sha-       # Immutable (GitOps)
  type=raw,value=YYYYMMDD    # Human-readable
```

**Why**: Enables both rolling updates and pinned deployments

**Skills**: Image versioning, deployment strategies, rollback planning

### 3. Separate Infrastructure Repository
**Decision**: HOMELAB-INFRA for Kubernetes manifests

**Why**:
- Security (SealedSecrets)
- Separation of concerns
- Different access controls
- ArgoCD App-of-Apps pattern

**Skills**: Repository organization, GitOps patterns, security boundaries

---

## Pipeline Metrics

| Metric | Value | Industry Benchmark |
|:-------|:------|:-------------------|
| **Build Time** | ~2-3 minutes | ✅ Fast (< 5 min) |
| **Image Size** | ~20MB | ✅ Excellent (< 100MB) |
| **Deployment Frequency** | On every push | ✅ Continuous |
| **Rollback Time** | < 1 minute | ✅ Excellent |
| **Automation Level** | 100% | ✅ Full GitOps |

---

## What This Proves

This CI/CD implementation demonstrates:

1. **DevOps Mindset**: Automation first, eliminate manual steps
2. **Modern Tooling**: GitHub Actions, GitOps, container-native
3. **Reliability**: Automated testing, rollback capabilities
4. **Efficiency**: Fast feedback loops, parallel execution
5. **Best Practices**: Security scanning, image signing ready

---

## GitOps Benefits Showcased

| Benefit | Implementation |
|:--------|:---------------|
| **Audit Trail** | Every change in Git history |
| **Rollback** | `git revert` = instant rollback |
| **Drift Detection** | ArgoCD detects manual changes |
| **Self-Healing** | Auto-correction of configuration drift |
| **Multi-Env** | Same process for dev/staging/prod |

---

## Comparison to Industry Standards

| Practice | Implementation | Industry Standard |
|:---------|:---------------|:------------------|
| CI/CD Platform | GitHub Actions | ✅ Industry leader |
| GitOps Tool | ArgoCD | ✅ Cloud-native standard |
| Registry | GHCR | ✅ Modern choice |
| Image Size | 20MB | ✅ Excellent |
| Build Time | 2-3 min | ✅ Fast |

---

## Related Documentation

- **Portfolio Page**: [`docs/projects/gitops.md`](docs/projects/gitops.md)
- **Live Documentation**: https://docs.arkenops.cc/projects/gitops/
- **Workflow**: [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)
- **Infrastructure**: https://github.com/palbina/HOMELAB-INFRA

---

*This document demonstrates DevOps and GitOps expertise through production-ready automation.*
