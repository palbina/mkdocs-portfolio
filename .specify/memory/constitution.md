<!--
  ============================================================================
  SYNC IMPACT REPORT
  ============================================================================
  Version change: 1.0.0 → 1.1.0 (MINOR)
  Rationale: New "Migration & Tooling" section added documenting the MkDocs →
  Zensical SSG migration with feature gap analysis. Materially expands governance
  guidance without removing or redefining existing principles.

  Modified sections:
    - CI/CD: Expanded to document Zensical as sole build engine, removed
      ambiguous MkDocs references

  Added sections:
    - Migration & Tooling: Documents Zensical migration state, feature gaps
      (minify, git-revision-date-localized, macros), template engine (Tera vs
      Jinja2), and migration irreversibility rule

  Removed sections: None

  Templates requiring updates:
    ✅ .specify/templates/plan-template.md — No changes needed (Constitution
       Check placeholder is filled at runtime by /speckit.plan)
    ✅ .specify/templates/spec-template.md — No changes needed (no
       constitution-specific references)
    ✅ .specify/templates/tasks-template.md — No changes needed (no
       constitution-specific references)
    ✅ specs/001-landing-page-taxis/spec.md — Constitution reference remains
       valid
    ✅ specs/002-taxis-documentation-framework/spec.md — Valid
    ✅ specs/003-project-case-study-template/spec.md — Valid
    ✅ specs/004-neon-volt-design-system/spec.md — Zensical dependencies
       already documented
    ✅ specs/005-ci-cd-pipeline/spec.md — Zensical migration state already
       documented in spec

  Follow-up TODOs: None
  ============================================================================
-->

# ArkenOps Constitution

## Core Principles

### I. Docs as Code
Toda la documentación del portfolio se trata como código fuente: versionada en Git, sujeta a revisión,
y construida automáticamente mediante CI/CD. No se acepta documentación fuera del repositorio.
La documentación sigue el framework Diátaxis: tutoriales, how-to guides, referencia y explicación.

### II. Infrastructure as Code (IaC)
Toda la infraestructura del HomeLab se declara en Git y se sincroniza mediante GitOps (ArgoCD).
No se permite configuración manual en el cluster. El estado deseado = estado en Git.
Sealed Secrets para encriptación de secretos en repositorio.

### III. Zero Trust by Default
Seguridad multicapa obligatoria: Cloudflare WAF → CrowdSec IPS → Cilium NetworkPolicy → Istio mTLS → Authentik SSO.
Ningún servicio se expone sin autenticación. Default-deny en NetworkPolicies.
El perímetro de red no es un mecanismo de seguridad válido.

### IV. Observability Completa
Todo componente del stack debe exponer métricas, logs y traces. El stack LGTM (Loki, Grafana, Tempo, Prometheus)
es obligatorio. Las alertas se enrutan a Telegram vía Alertmanager. Sin observabilidad, el sistema
no está en producción.

### V. Simplicidad y Justificación
Cada tecnología en el stack debe tener una justificación documentada (ver docs/explanation/). 
YAGNI (You Ain't Gonna Need It): no se agrega complejidad sin un problema real que resolver.
Preferir herramientas nativas de Kubernetes sobre soluciones externas.

## Documentation Standards

### Diátaxis Framework
- **Tutoriales**: Aprendizaje práctico paso a paso. Orientados a principiantes.
- **How-To Guides**: Instrucciones para tareas específicas. Usuario competente.
- **Referencia**: Información técnica neutral. Tablas, comandos, configuraciones.
- **Explicación**: Contexto, background y decisiones arquitectónicas. El "por qué".

### Content Guidelines
- Idioma principal: Español.
- Código Python, YAML y HCL en bloques con sintaxis destacada.
- Diagramas de arquitectura en Mermaid.
- Cada página de proyecto incluye: Visión General, Arquitectura, Stack, Implementación, Operaciones, Resultados.

## Development Workflow

### Git Workflow
- Rama principal: `main` (protegida, requiere PR).
- Ramas de feature: `feat/<nombre>` o `docs/<nombre>`.
- Commits convencionales: `feat:`, `fix:`, `docs:`, `refactor:`, `style:`, `chore:`.
- No hacer push directo a `main`.

### CI/CD
- Build automático con **Zensical SSG** (Rust) como motor de build exclusivo. El comando de build es `zensical build`.
- `mkdocs.yml` se retiene como referencia histórica pero NO se usa en CI/CD. `scripts/main.py` fue eliminado
  durante la migración (marzo 2026).
- Deploy a registro Zot como imagen Docker multi-stage (Python 3.14 builder → Nginx 1.30 Alpine runtime).
- Nginx como servidor de producción con security headers, gzip level 6, caché de assets 1 año immutable,
  y protección de archivos ocultos.
- Renovate para actualización automática de dependencias.

### Migration & Tooling
- El proyecto completó su migración de MkDocs (Python) a **Zensical** (Rust) en marzo 2026.
  La migración es irreversible: no se contempla volver a MkDocs como build engine.
- **Feature gaps conocidos** (plugins de MkDocs sin equivalente en Zensical):
  - `mkdocs-minify-plugin`: Sin minificación HTML/JS/CSS en build. Delegado a Nginx/CDN.
  - `mkdocs-git-revision-date-localized`: Sin fechas de revisión automáticas en páginas.
  - `mkdocs-macros-plugin`: Eliminado intencionalmente. Contenido dinámico reemplazado por estático.
- El template engine cambió de Jinja2 (Python) a Tera (Rust). Los overrides en `docs/overrides/` son
  compatibles con ambos motores.
- `zensical.toml` es la configuración canónica. `mkdocs.yml` existe como referencia pero no se
  mantiene activamente; cualquier cambio en la configuración del sitio debe hacerse en ambos archivos
  o solo en `zensical.toml` si el feature no existe en MkDocs.
- Las dependencias de MkDocs en `requirements.txt` se retienen para testing de compatibilidad;
  no son necesarias para el build de producción.

### Spec-Driven Development (Speckit)
- Nuevas features/páginas se especifican con `/speckit.specify`.
- Plan técnico con `/speckit.plan`.
- Tasks con `/speckit.tasks`.
- Implementación con `/speckit.implement`.
- El spec vive en `specs/<feature>/spec.md`.

## Governance

Esta constitución rige todas las decisiones de desarrollo del portfolio ArkenOps.
Cualquier desviación debe documentarse y justificarse en el PR correspondiente.
Las enmiendas a la constitución requieren PR con revisión y aprobación.
La complejidad agregada al stack debe justificarse en `docs/explanation/`.
La migración de herramientas de build sigue el principio V (Simplicidad): cualquier propuesta
de cambiar el SSG debe demostrar una ventaja concreta sobre Zensical (velocidad, features, mantenibilidad).

**Version**: 1.1.0 | **Ratified**: 2026-07-05 | **Last Amended**: 2026-07-05
