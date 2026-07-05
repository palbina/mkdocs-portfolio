# Research: Homelab Portfolio Enrichment

**Feature**: 008-homelab-portfolio-enrichment
**Date**: 2026-07-05
**Source**: `/home/peter/DEV/talos-gitops/docs/`

## Research Tasks & Findings

### R1: What real cluster data is available from TalosLab?

**Decision**: TalosLab `docs/INDEX.md` + `docs/reference/QUICK_REFERENCE.md` + `docs/architecture/overview.md` + `docs/compliance-dashboard.md` provide comprehensive source data.

**Findings**:
- **Cluster**: 5 nodos (3 CP + 2 workers, 2 decommissioned en Mayo 2026). Hardware: ThinkPad L14 (CP1), Geekom A7 (CP2), Intel N305 (CP3), Geekom A7 + Coral TPU (W1), Lenovo SR630 2x Xeon Gold 6230/320GB RAM (W4). Workers N05/N06 decommissioned.
- **OS/Platform**: Talos Linux v1.13.2 (immutable, no-SSH, no package manager). K8s v1.35.0. KubePrism @ 7445.
- **Networking**: Cilium v1.18.5 (eBPF, MTU 1230). Istio Ambient v1.30.0 (ztunnel, no sidecars). Traefik v3 + CrowdSec WAF + Authentik SSO. Cloudflare Tunnel (CG-NAT bypass).
- **GitOps**: ArgoCD v3.4.3 + Flux v2.8.8 experimental. ApplicationSet + exclusion list for multi-source apps. GitLab como source primario (sovereign stack). Renovate v43. ArgoCD Image Updater. Sealed Secrets.
- **Storage**: Longhorn v1.10.2 (HDD + SSD tiers). CNPG 3-instance HA (<10s failover). SeaweedFS S3 offsite WAL + PITR 7 días. 8 buckets S3 para backup.
- **Observability**: LGTM stack (Loki, Grafana, Tempo, Prometheus). Kiali (Istio). k6 operator. AlertManager → Telegram.
- **Apps**: 29 apps, 100% Molty V2 compliance. Compliance Dashboard con 7 CronJobs de auditoría.
- **DR**: Guía de 629 líneas. `export-dr-backup.sh` → 1Password.

**Rationale**: INDEX.md + QUICK_REFERENCE.md + overview.md contienen los datos más autoritativos y actualizados. Cubren todos los requerimientos del spec.

**Alternatives considered**: Leer archivos k8s/ YAML directamente → demasiado granular y disperso. La documentación de TalosLab ya está curada y estructurada.

---

### R2: What is the current state of each portfolio project page?

**Decision**: Leer cada `docs/projects/*.md` existente para identificar gaps entre contenido actual y datos reales.

**Findings**:

| Page | Current State | Gap |
|:-----|:--------------|:----|
| `homelab.md` | "3 nodos bare-metal", genérico | Falta 5 nodos reales, hardware específico, Talos v1.13.2, consolidación SR630 |
| `gitops.md` | "ArgoCD v2.10", GitHub source | Versión real v3.4.3, falta Flux, GitLab sovereign, Renovate v43, Image Updater |
| `security.md` | Genérico, menciona conceptos | Falta CrowdSec, Authentik forwardAuth, CiliumNP v2.1 fix, Istio Ambient mTLS |
| `database-ha.md` | Conceptos generales de HA | Falta CNPG específico, 3 instancias, <10s failover, SeaweedFS, 8 buckets S3 |
| `observability.md` | Stack básico | Falta LGTM completo, Kiali, k6 operator, AlertManager→Telegram |
| `backup-dr.md` | Conceptos generales | Falta guía DR 629 líneas, export-dr-backup.sh, 1Password, 8 buckets |
| `progressive-delivery.md` | Genérico | Falta Argo Rollouts, AnalysisRuns con Prometheus, canary automático |
| `ai-rag.md` | Placeholder | Necesita datos reales o marcarse como WIP |
| `index.md` | 8 project cards | Necesita cards para nuevas páginas (Molty V2, Zero Trust, Compliance) |

**Rationale**: El gap analysis revela que las páginas contienen conceptos correctos pero genéricos. Faltan datos específicos, versiones exactas, y métricas reales que demuestren experiencia práctica.

**Alternatives considered**: Reescribir páginas desde cero → innecesario. La estructura es sólida, solo falta contenido específico.

---

### R3: What new project pages should be created?

**Decision**: 3 nuevas páginas basadas en los diferenciadores más fuertes de TalosLab.

**Findings**:

1. **Deployment Methodology (Molty Standard V2)**: Documenta el estándar de despliegue obligatorio. 9 manifiestos requeridos (namespace, service-account, network-policy, pdb, resource-quota, limit-range, deployment, ingress-route, servicemonitor). Script `validate-deployment-compliance.sh`. 29/29 apps en 100% compliance. 7 CronJobs de auditoría.

2. **Zero Trust Networking (NetworkPolicies v2.1)**: Evolución v1→v2→v2.1. Fix del bug `- {}` → `[]` verdadero default-deny. CiliumNetworkPolicy como enforcement layer. Arquitectura en capas: Cloudflare→CrowdSec→Cilium→Istio mTLS→Authentik. Principio: "el perímetro de red no es mecanismo de seguridad".

3. **Compliance Dashboard**: Tabla de hardening por aplicación (29 apps). Métricas de compliance históricas. CronJobs de auditoría (`compliance-auditor`, `traffic-auditor`, `cert-security-auditor`, `zot-registry-cleaner`, `cilium-policy-auditor`, `cnpg-backup-verifier`, `velero-backup-verifier`).

**Rationale**: Estos tres temas son los diferenciadores más fuertes: metodología estandarizada, seguridad avanzada, y métricas cuantificables de compliance. Ningún portfolio genérico los tiene.

**Alternatives considered**: Crear página por app (WordPress, GitLab, etc.) → demasiado granular, no escala. Agrupar en 3 páginas temáticas es mejor.

---

### R4: What reference and explanation pages need updating?

**Decision**: Actualizar `tech-stacks.md`, `kubernetes-commands.md`, `configuration-reference.md` (reference) y `zero-trust-model.md`, `cloud-native-architecture.md`, `gitops-philosophy.md` (explanation).

**Findings**:

- **tech-stacks.md**: Las versiones actuales son genéricas. Deben reflejar: Talos v1.13.2, K8s v1.35.0, Cilium v1.18.5, Istio Ambient v1.30.0, ArgoCD v3.4.3, Flux v2.8.8, CNPG, Longhorn v1.10.2, Zot registry, GitLab + agentk, Renovate v43.
- **kubernetes-commands.md**: Los comandos deben alinearse con las prohibiciones de TalosLab (no kubectl apply, fish shell obligatorio, workflow kubeseal-now).
- **configuration-reference.md**: Referencias de configuración genéricas → específicas del cluster.
- **zero-trust-model.md**: Descripción genérica → arquitectura en capas real con el fix v2.1 documentado.
- **cloud-native-architecture.md**: Conceptos generales → arquitectura soberana concreta (GitLab, Zot, Flux, ArgoCD).
- **gitops-philosophy.md**: Filosofía general → lecciones reales (apps multi-source, ApplicationSet con exclude, sovereign stack).

**Rationale**: La consistencia cross-site requiere que referencia y explicación reflejen el mismo estado que las páginas de proyecto.

**Alternatives considered**: Crear nuevas páginas de referencia en lugar de actualizar → duplicación innecesaria. Las páginas existentes son el lugar correcto.

---

### R5: What sensitive data must be excluded?

**Decision**: Aplicar filtro de exclusión a todos los datos de TalosLab.

**Rules**:
- **Excluir**: IPs LAN (192.168.x.x, 10.x.x.x), dominios `.subetupaginacp.com`, nombres reales de endpoints internos, credenciales, tokens, secrets cifrados.
- **Reemplazar con**: Placeholders descriptivos (`<cluster-domain>`, `<internal-ip>`, `<s3-endpoint>`).
- **Conservar**: Versiones de software, nombres de herramientas, conteos, métricas de compliance, nombres de scripts, decisiones arquitectónicas, flujos de trabajo documentados.

**Rationale**: Seguridad Zero Trust (constitution III). El portfolio es público; TalosLab es privado. Las métricas y arquitectura demuestran experiencia sin exponer superficies de ataque.

**Alternatives considered**: Publicar todo con un disclaimer → viola constitution III (Zero Trust by Default).

---

### R6: What is the project page template format?

**Decision**: El formato canónico es el usado por `homelab.md` y `gitops.md`.

**Template structure** (6 secciones requeridas):
1. Frontmatter YAML: `title`, `description`
2. `project-header` div: `<h1>`, `<p>`, `project-meta-grid` con 4 meta-items (Status, Environment, etc.)
3. `## Visión General` + `!!! impact` admonition
4. `## Arquitectura` + diagrama Mermaid + `!!! info` admonition
5. `## Stack Tecnológico` + tabs con tablas
6. `## Implementación` + detalles técnicos
7. `## Operaciones` + runbooks/lecciones
8. `## Resultados` + métricas

**Rationale**: Consistencia visual y estructural. El template ya está probado en 9 páginas existentes.

**Alternatives considered**: Simplificar template para páginas nuevas → rompería consistencia. Mantener el template existente es la opción correcta.

---

## Summary of Decisions

| # | Decision | Rationale |
|:--|:---------|:----------|
| R1 | INDEX.md + QUICK_REFERENCE.md + overview.md como fuentes primarias | Datos más autoritativos, curados, y actualizados (2026-06-23) |
| R2 | Gap analysis por página: conservar estructura, reemplazar datos genéricos | Minimiza reescritura, maximiza precisión |
| R3 | 3 nuevas páginas: Molty V2, Zero Trust v2.1, Compliance Dashboard | Diferenciadores más fuertes del cluster |
| R4 | Actualizar 3 reference + 3 explanation existentes | Consistencia cross-site |
| R5 | Filtro estricto: excluir IPs, dominios, credenciales | Constitution III (Zero Trust) |
| R6 | Template de 6 secciones como formato canónico | Consistencia con 9 páginas existentes |
