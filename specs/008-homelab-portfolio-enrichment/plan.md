# Implementation Plan: Homelab Portfolio Enrichment

**Branch**: `008-homelab-portfolio-enrichment` | **Date**: 2026-07-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/008-homelab-portfolio-enrichment/spec.md`

## Summary

Enriquecer 9 páginas de proyecto existentes con datos reales del cluster TalosLab (versiones exactas, hardware, métricas), crear 3 nuevas páginas de proyecto (Molty Standard V2, Zero Trust Networking v2.1, Compliance Dashboard), y actualizar documentación de referencia y explicación con versiones alineadas a TalosLab 2026. Todo en Markdown + Mermaid, construido con Zensical SSG.

## Technical Context

**Language/Version**: Markdown + Mermaid (no código fuente ejecutable)

**Primary Dependencies**: Zensical SSG v0.0.46 (build engine), Material for MkWare theme (via Zensical)

**Storage**: N/A (archivos Markdown estáticos en `docs/`)

**Testing**: `zensical build --clean` (verifica integridad del build, links, estructura)

**Target Platform**: Static HTML site, served via Nginx en cluster TalosLab

**Project Type**: Documentación estática / portfolio site

**Performance Goals**: Build <5s, página <100KB, Lighthouse score >90

**Constraints**: Formato de proyecto existente debe preservarse (project-header, project-meta-grid, 6 secciones). Lenguaje español. Sin datos sensibles (IPs reales, dominios .subetupaginacp.com).

**Scale/Scope**: 9 páginas existentes a actualizar, 3 páginas nuevas, 3 páginas de referencia, 3 páginas de explicación, landing page. ~18 archivos modificados/creados. ~500 líneas de contenido neto nuevo.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|:----------|:------:|:---------|
| **I. Docs as Code** | ✅ PASS | Markdown versionado en Git, build automático con Zensical, revisión vía PR. |
| **II. Infrastructure as Code** | ✅ PASS | Los datos fuente (TalosLab) se gestionan 100% vía GitOps. El portfolio documenta el estado del cluster. |
| **III. Zero Trust by Default** | ✅ PASS | No se exponen datos sensibles. Domains reales reemplazados por placeholders. |
| **IV. Observability Completa** | ✅ PASS | La documentación de observabilidad cubre el stack LGTM completo con métricas reales. |
| **V. Simplicidad y Justificación** | ✅ PASS | Solo se agrega contenido derivado de sistemas reales en producción. Cada página justifica su stack en sección de explicación. |
| **Diátaxis Framework** | ✅ PASS | Contenido se clasifica correctamente: proyectos → reference/explicación, referencia → reference, explicación → explanation. |
| **Content Guidelines** | ✅ PASS | Español, bloques de código con sintaxis, diagramas Mermaid. Formato de 6 secciones. |
| **Spec-Driven Development** | ✅ PASS | Feature especificada via `/speckit.specify`, plan via `/speckit.plan`, tasks via `/speckit.tasks`. |
| **Migration & Tooling** | ✅ PASS | Solo se modifica `docs/` (Markdown). No se toca `zensical.toml`, `mkdocs.yml`, ni código Rust. |

**Gate Result**: ALL PASS — No violations. No complexity tracking needed.

## Project Structure

### Documentation (this feature)

```text
specs/008-homelab-portfolio-enrichment/
├── plan.md              # This file
├── research.md          # Phase 0: Source data analysis from TalosLab
├── data-model.md        # Phase 1: Document structure & entity model
├── quickstart.md        # Phase 1: Validation scenarios
└── tasks.md             # Phase 2: (/speckit.tasks, NOT created here)
```

### Source Code (repository root)

```text
docs/
├── projects/                        # Páginas de proyecto (US1 + US2)
│   ├── homelab.md                   # [UPDATE] 3 nodos → 5 nodos reales
│   ├── gitops.md                    # [UPDATE] ArgoCD v2.10 → v3.4.3 + Flux
│   ├── security.md                  # [UPDATE] Genérico → Zero Trust v2.1 real
│   ├── database-ha.md               # [UPDATE] Genérico → CNPG + 8 buckets S3
│   ├── observability.md             # [UPDATE] Básico → LGTM completo + Kiali
│   ├── backup-dr.md                 # [UPDATE] Básico → DR 629 líneas + 1Password
│   ├── progressive-delivery.md      # [UPDATE] Genérico → Argo Rollouts + Istio
│   ├── ai-rag.md                    # [UPDATE] Placeholder → Datos reales
│   ├── index.md                     # [UPDATE] Agregar links a nuevas páginas
│   ├── deployment-methodology.md    # [NEW] Molty Standard V2
│   ├── zero-trust-networking.md     # [NEW] NetworkPolicies v2.1
│   └── compliance-dashboard.md      # [NEW] 29/29 compliance
├── reference/
│   ├── tech-stacks.md               # [UPDATE] Versiones TalosLab 2026
│   ├── kubernetes-commands.md       # [UPDATE] Comandos SRE reales
│   └── configuration-reference.md   # [UPDATE] Configs reales
├── explanation/
│   ├── zero-trust-model.md          # [UPDATE] Capas reales + bug - {} fix
│   ├── cloud-native-architecture.md # [UPDATE] Arquitectura soberana real
│   └── gitops-philosophy.md         # [UPDATE] Lecciones multi-source
├── index.md                         # [UPDATE] Project cards grid
└── stylesheets/extra.css            # [NO CHANGE] CSS existente adecuado
```

**Structure Decision**: Documentación plana en `docs/` organizada por Diátaxis. Las páginas de proyecto comparten template HTML/CSS vía `project-header` y `project-meta-grid`. No se requiere nueva estructura de directorios.

## Complexity Tracking

> No constitution violations. Section empty.
