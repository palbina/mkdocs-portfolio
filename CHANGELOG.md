# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Estructura inicial de documentación
- README.md con quick start guide
- llms.txt para AI crawlers
- CHANGELOG.md inicial

### Changed
- Mejorada estructura de navegación en mkdocs.yml

---

## [1.0.0] - 2026-02-09

### Added
- **Homepage**: Hero section con estadísticas y proyectos destacados
- **Portfolio Projects**:
  - HomeLab Kubernetes (Talos Linux, Cilium, Istio)
  - GitOps con ArgoCD (App-of-Apps pattern)
  - Observabilidad LGTM (Prometheus, Loki, Tempo, Grafana)
  - Zero Trust Security (CrowdSec, Cilium, mTLS)
  - Progressive Delivery (Argo Rollouts)
  - Database HA con CloudNativePG
  - AI Chat con RAG (LangChain, LLM)
  - Backup & Disaster Recovery (Velero, Longhorn)
- **About Page**: Perfil profesional, timeline, stack tecnológico
- **Blog Section**: Estructura para artículos técnicos
- **Theme Customization**:
  - Paleta neon volt (lime accent)
  - Terminal-style CSS overrides
  - Dark mode default
  - Typography: Inter + JetBrains Mono
- **SEO & Performance**:
  - Meta tags y Open Graph
  - Minificación HTML/CSS/JS
  - Search functionality
  - Mermaid diagrams support
- **CI/CD**: GitHub Actions workflow para deploy automático
- **Docker**: Multi-stage build con Nginx

### Technical
- MkDocs 1.6+ con Material theme 9.5+
- Plugins: search, minify, git-revision-date-localized, macros
- Extensions: admonition, pymdownx, mermaid
- Python macros para contenido dinámico

---

## Template

### Added
- Nueva funcionalidad

### Changed
- Cambios en funcionalidad existente

### Deprecated
- Funcionalidad que será removida

### Removed
- Funcionalidad eliminada

### Fixed
- Bug fixes

### Security
- Mejoras de seguridad
