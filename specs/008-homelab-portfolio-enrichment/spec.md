# Feature Specification: Homelab Portfolio Enrichment

**Feature Branch**: `008-homelab-portfolio-enrichment`

**Created**: 2026-07-05

**Status**: Implemented (2026-07-05)

**Input**: User description: "analiza mi proyecto cluster homelabinfra y añade mas contenido a mi portfolio y refina el actual. /home/peter/DEV/talos-gitops/docs/INDEX.md"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Enriquecer páginas de proyecto existentes con datos reales (Priority: P1)

Un visitante del portfolio (reclutador, colega DevOps, cliente potencial) lee las páginas de proyecto y encuentra información genérica y placeholder. Quiere ver métricas concretas, configuraciones reales, y decisiones de arquitectura documentadas que demuestren experiencia práctica en producción.

**Why this priority**: Las páginas de proyecto son el contenido principal del portfolio y actualmente usan datos genéricos/placeholder. Enriquecerlas con datos reales de TalosLab es el mayor impacto inmediato en credibilidad.

**Independent Test**: Abrir cada página de proyecto (`docs/projects/*.md`) y verificar que contiene datos específicos extraídos de TalosLab (versiones exactas, conteo de nodos, nombres de herramientas, métricas reales) en lugar de placeholders o datos genéricos.

**Acceptance Scenarios**:

1. **Given** la página `docs/projects/homelab.md` actualmente describe "3 nodos bare-metal", **When** se actualiza con datos reales de TalosLab, **Then** muestra 5 nodos (3 CP + 2 workers), hardware específico (ThinkPad L14, Geekom A7, Intel N305, Lenovo SR630), Talos v1.13.2, K8s v1.35.0, y arquitectura de consolidación post-decommission.
2. **Given** la página `docs/projects/gitops.md` actualmente dice "ArgoCD v2.10", **When** se actualiza con datos reales, **Then** menciona ArgoCD v3.4.3 + Flux v2.8.8 experimental, ApplicationSets con exclusión de apps multi-source, GitLab como source primario, Renovate v43, y ArgoCD Image Updater.
3. **Given** la página `docs/projects/security.md`, **When** se actualiza, **Then** incluye CrowdSec IPS, Authentik forwardAuth SSO, CiliumNetworkPolicies Zero Trust v2.1 (fix del bug `- {}`), Istio Ambient mTLS, y Sealed Secrets.
4. **Given** la página `docs/projects/database-ha.md`, **When** se actualiza, **Then** incluye CNPG con 3 instancias, `<10s failover`, SeaweedFS S3 offsite WAL streaming, PITR 7 días, y 8 buckets S3 de backup.
5. **Given** la página `docs/projects/observability.md`, **When** se actualiza, **Then** menciona stack LGTM completo (Loki, Grafana, Tempo/OpenTelemetry, Prometheus/Mimir), Kiali para Istio, k6 operator, y AlertManager → Telegram.
6. **Given** la página `docs/projects/backup-dr.md`, **When** se actualiza, **Then** referencia la guía DR de 629 líneas, export-dr-backup.sh para credenciales en 1Password, y los 8 buckets S3 diferenciados por propósito.

---

### User Story 2 - Agregar nuevas páginas de proyecto no representadas (Priority: P2)

Un visitante técnico busca evidencia de madurez operativa más allá del stack básico. Quiere ver metodologías de despliegue estandarizadas, dashboards de compliance, y arquitectura de red Zero Trust documentada como proyectos independientes.

**Why this priority**: Varios logros significativos de TalosLab no están representados en el portfolio actual. Estas páginas nuevas demuestran profundidad en áreas que diferencian un homelab avanzado de uno básico.

**Independent Test**: Verificar que existen nuevos archivos `.md` en `docs/projects/` para cada área no representada y que cada uno sigue el template de proyecto (`project-header`, `project-meta-grid`, `Visión General`, `Arquitectura`, `Stack Tecnológico`, `Implementación`, `Operaciones`, `Resultados`).

**Acceptance Scenarios**:

1. **Given** que TalosLab tiene el Molty Standard V2 como estándar de despliegue obligatorio, **When** se crea `docs/projects/deployment-methodology.md`, **Then** documenta los 9 manifiestos requeridos (namespace, service-account, network-policy, pdb, resource-quota, limit-range, deployment, ingress-route, servicemonitor), el script de validación `validate-deployment-compliance.sh`, y el resultado de 29/29 apps en compliance.
2. **Given** que TalosLab implementó Zero Trust v2.1 con fix del bug `- {}`, **When** se crea `docs/projects/zero-trust-networking.md`, **Then** documenta la evolución de NetworkPolicies v1 → v2 → v2.1, el principio de default-deny con `[]` verdadero, y CiliumNetworkPolicy como enforcement layer.
3. **Given** el compliance dashboard con 29/29 apps al 100%, **When** se crea `docs/projects/compliance-dashboard.md`, **Then** muestra la tabla de hardening por aplicación, los 7 CronJobs de auditoría, y métricas de compliance históricas.
4. **Given** que TalosLab usa Istio Ambient Mesh sin sidecars, **When** se crea la sección correspondiente en la página de networking, **Then** explica ztunnel, HBONE, y la eliminación de sidecar overhead.

---

### User Story 3 - Actualizar documentación de referencia y explicación con lecciones reales (Priority: P3)

Un lector de las guías de referencia (tech-stacks, comandos, configuración) o explicación (filosofía, arquitectura) encuentra versiones desactualizadas y conceptos genéricos. Quiere ver las versiones exactas que corren en producción y las lecciones aprendidas de incidentes reales.

**Why this priority**: El contenido de referencia y explicación complementa las páginas de proyecto. Actualizarlo asegura consistencia cross-site y añade profundidad con lecciones reales.

**Independent Test**: Verificar que `docs/reference/tech-stacks.md`, `docs/reference/kubernetes-commands.md`, y `docs/explanation/zero-trust-model.md` contienen versiones y conceptos alineados con TalosLab 2026.

**Acceptance Scenarios**:

1. **Given** `docs/reference/tech-stacks.md` lista versiones genéricas, **When** se actualiza, **Then** refleja el stack exacto de TalosLab: Talos v1.13.2, K8s v1.35.0, Cilium v1.18.5, Istio Ambient v1.30.0, ArgoCD v3.4.3, Flux v2.8.8, CNPG, Longhorn v1.10.2, Zot registry, GitLab + agentk.
2. **Given** `docs/explanation/zero-trust-model.md` describe Zero Trust genérico, **When** se actualiza, **Then** incluye la arquitectura en capas real (Cloudflare → CrowdSec → Cilium → Istio mTLS → Authentik), el fix v2.1 del bug `- {}`, y el principio de "el perímetro de red no es mecanismo de seguridad".
3. **Given** `docs/explanation/gitops-philosophy.md`, **When** se actualiza, **Then** incluye lecciones reales: apps multi-source requieren Application manual, ApplicationSet genérico usa exclude, GitLab como source soberano, mirror a Forgejo/GitHub.

---

### Edge Cases

- ¿Qué pasa si una página de proyecto existente tiene contenido genérico que entra en conflicto con los datos reales? → Se reemplaza el contenido genérico, preservando la estructura (secciones, diagramas Mermaid) pero actualizando datos.
- ¿Qué pasa si TalosLab tiene información que no encaja en ninguna página existente? → Se crea una página nueva (User Story 2).
- ¿Qué pasa si el formato de las páginas existentes no soporta bien el nuevo contenido? → Se adapta el contenido al formato existente; si es imposible, se propone una extensión del template.
- ¿Qué pasa si hay datos sensibles en TalosLab que no deben publicarse? → Se excluyen IPs internas, dominios `.subetupaginacp.com`, y nombres reales de endpoints. Se usan placeholders descriptivos.
- **Descubierto**: ¿Qué pasa si las tablas están dentro de content tabs (`===`)? → Zensical v0.0.46 no renderiza tablas dentro de content tabs. Ver [Implementation Discoveries](#implementation-discoveries). Resolución: convertir tabs a headings `###` y de-indentar el contenido.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema de documentación DEBE reflejar el estado real del cluster TalosLab con versiones exactas de software, conteo de nodos real, y hardware específico en todas las páginas de proyecto.
- **FR-002**: Cada página de proyecto (`docs/projects/*.md`) DEBE contener datos verificables extraídos de `docs/INDEX.md`, `docs/reference/QUICK_REFERENCE.md`, y `docs/compliance-dashboard.md` del repositorio TalosLab.
- **FR-003**: Las páginas de proyecto DEBEN preservar la estructura existente (frontmatter YAML, `project-header`, `project-meta-grid`, secciones: Visión General, Arquitectura con Mermaid, Stack Tecnológico, Implementación, Operaciones, Resultados).
- **FR-004**: Se DEBEN crear nuevas páginas de proyecto para áreas no representadas: metodología de despliegue (Molty Standard V2), Zero Trust Networking (NetworkPolicies v2.1), y Compliance Dashboard.
- **FR-005**: Los diagramas Mermaid en páginas existentes DEBEN actualizarse para reflejar la arquitectura real de TalosLab (nodos correctos, flujo de tráfico Cloudflare → Traefik → Istio → Pod, componentes soberanos).
- **FR-006**: Las páginas de referencia (`docs/reference/tech-stacks.md`, `docs/reference/kubernetes-commands.md`, `docs/reference/configuration-reference.md`) DEBEN actualizarse con versiones y configuraciones alineadas a TalosLab 2026.
- **FR-007**: Las páginas de explicación (`docs/explanation/zero-trust-model.md`, `docs/explanation/cloud-native-architecture.md`, `docs/explanation/gitops-philosophy.md`) DEBEN incluir lecciones aprendidas y decisiones arquitectónicas reales del cluster.
- **FR-008**: El landing page (`docs/index.md`) DEBE actualizarse para reflejar las nuevas páginas de proyecto y el stack tecnológico real.

### Key Entities

- **Página de Proyecto**: Documento Markdown en `docs/projects/`. Atributos: título, status, métricas de impacto, stack tecnológico, diagrama de arquitectura, secciones de implementación/operaciones/resultados. Existentes: 9. Nuevas: 3 (target: 12).
- **Página de Referencia**: Documento en `docs/reference/`. Atributos: comandos, versiones, configuraciones. Debe ser información técnica neutral y verificable.
- **Página de Explicación**: Documento en `docs/explanation/`. Atributos: contexto, decisiones arquitectónicas, lecciones aprendidas, "por qué".
- **Datos Fuente (TalosLab)**: Metadatos extraídos de `docs/INDEX.md`, `docs/reference/QUICK_REFERENCE.md`, `docs/compliance-dashboard.md`, `docs/architecture/*.md` del repositorio `talos-gitops`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Las 9 páginas de proyecto existentes contienen al menos un dato verificable de TalosLab (versión exacta, nombre de herramienta, métrica de cluster) que antes era genérico o placeholder.
- **SC-002**: Existen al menos 3 nuevas páginas de proyecto documentando áreas no representadas (Molty Standard V2, Zero Trust Networking, Compliance Dashboard).
- **SC-003**: Las 3 páginas de referencia principales (`tech-stacks.md`, `kubernetes-commands.md`, `configuration-reference.md`) reflejan versiones alineadas con TalosLab 2026.
- **SC-004**: Todas las páginas de proyecto (existentes + nuevas) siguen el template consistente con `project-header`, `project-meta-grid`, y las 6 secciones estándar.
- **SC-005**: `zensical build --clean` completa sin errores ni warnings después de todos los cambios.
- **SC-006**: El landing page (`docs/index.md`) referencia las nuevas páginas de proyecto en el grid de project cards.

## Assumptions

- Los datos de TalosLab están actualizados a 2026-06-23 (última actualización del INDEX.md fuente).
- El formato de páginas de proyecto (template con `project-header`, `project-meta-grid`, secciones estándar) existente en `docs/projects/homelab.md` y `docs/projects/gitops.md` es el template canónico a seguir.
- No se requiere modificar `zensical.toml` ni `mkdocs.yml` para agregar nuevas páginas — Zensical descubre automáticamente archivos `.md` en `docs/`.
- Se excluyen datos sensibles: IPs internas, dominios reales (`.subetupaginacp.com`), credenciales. Se usan placeholders descriptivos donde sea necesario.
- El lenguaje principal sigue siendo español (constitution I.1).
- Los diagramas Mermaid se mantienen como formato de arquitectura (constitution: "Diagramas de arquitectura en Mermaid").
- Las guías How-To y Tutoriales existentes no requieren actualización en este spec — el foco es proyectos, referencia, y explicación.
- La migración GitLab/Forgejo/GitHub (sovereign stack) es material relevante para las páginas de GitOps y arquitectura.

## Implementation Discoveries

### Zensical Content Tabs Bug (Resolved 2026-07-05)

Durante la implementación se descubrió un bug en Zensical v0.0.46: **las tablas Markdown dentro de bloques `===` (content tabs) no se renderizan correctamente.** El renderer genera la estructura `<table>` con celdas vacías y emite el contenido de las celdas como `<p>` fuera de la tabla, causando que el texto aparezca fuera del componente visual.

**Causa raíz**: El renderer de Zensical no procesa correctamente tablas Markdown dentro de bloques `pymdownx.tabbed`. Los ejemplos oficiales de la documentación de Zensical solo muestran código y listas dentro de content tabs — nunca tablas.

**Resolución — 2 cambios aplicados a 17 archivos**:

1. **Content tabs → headings**: `=== "Título"` convertido a `### Título` en 11 páginas de proyecto afectadas (`docs/projects/*.md`). Esto elimina los content tabs y los reemplaza por headings H3 estándar que sí renderizan tablas correctamente.

2. **De-indentación**: El contenido dentro de `===` tabs estaba indentado con 4 espacios (requerido por la sintaxis de tabs). Al eliminar los tabs, esa indentación se interpreta como code block en Markdown estándar. Se removieron los 4 espacios iniciales de todas las líneas de tabla en 16 archivos afectados (11 projects + 3 reference + 2 explanation).

**CSS complementario**: Se agregó `overflow-x: auto` a `.md-typeset__table` y `.tabbed-block` en `docs/stylesheets/extra.css` para scroll horizontal en tablas anchas. También se forzó `display: table !important` y `overflow: visible !important` en `.md-typeset table:not([class])` para anular el `display: inline-block` que impone el theme de Material, el cual rompe el layout de tabla en ciertos contextos.

**Archivos modificados**:
- `docs/projects/*.md` (11 archivos): tabs → headings + de-indent
- `docs/reference/tech-stacks.md`, `configuration-reference.md`: de-indent
- `docs/explanation/gitops-philosophy.md`, `observability-patterns.md`, `zero-trust-model.md`: de-indent
- `docs/stylesheets/extra.css`: reglas de scroll y `display: table`

**Lección**: Las tablas dentro de content tabs (`===`) no son compatibles con Zensical v0.0.46. Si se necesitan tabs con tablas, usar headings (`###`) como alternativa.
