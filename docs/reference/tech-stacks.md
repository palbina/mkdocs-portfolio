# Stacks Tecnológicos

Catálogo de referencia de todas las tecnologías utilizadas, organizadas por dominio. Información neutral, precisa y completa.

---

## Infraestructura Base (HomeLab)

### Sistema Operativo y Kubernetes

| Componente | Tecnología | Versión | Descripción |
|:-----------|:-----------|:--------|:------------|
| OS | Talos Linux | v1.13.2 | Inmutable, API-driven, no-SSH |
| Kubernetes | Upstream | v1.35.0 | Vanilla, KubePrism @7445 |
| CNI | Cilium | v1.18.5 | eBPF, MTU 1230, Hubble |

### Service Mesh y Networking

| Componente | Tecnología | Versión | Descripción |
|:-----------|:-----------|:--------|:------------|
| Service Mesh | Istio Ambient | v1.30.0 | Sin sidecars, ztunnel, HBONE |
| Ingress | Traefik v3 + Cloudflare Tunnel | v3.7.1 | Zero-port exposure, CrowdSec bouncer |
| Storage | Longhorn | v1.10.2 | Distributed block storage, HDD+SSD tiers |

### Automatización

| Componente | Tecnología | Versión | Descripción |
|:-----------|:-----------|:--------|:------------|
| GitOps | ArgoCD v3.4.3 + Flux v2.8.8 | App of Apps + GitLab Agent sovereign |
| Secrets | Sealed Secrets | v2.19.0 | Encriptación asimétrica |
| Deps | Renovate | v43 | Auto-dependency updates (66 PRs) |
| Registry | Zot (sovereign) | Latest | Registro local sin dependencia GHCR |

---

## Observabilidad (LGTM Stack)

### Métricas

| Componente | Función | Retención |
|:-----------|:--------|:----------|
| **Prometheus Stack** | kube-prometheus-stack | v3.8.1 / 80.9.2 | Métricas + alertas |
| **Grafana** | Dashboard | 12.3.1 | Visualización unificada |
| **Loki** | Logs | 3.6.3 / 6.49.0 | Log aggregation |
| **Tempo** | Traces | 2.8.0 / 1.23.0 | Distributed tracing |
| **Kiali** | Mesh | v2.17.0 | Istio visualization |
| **k6 Operator** | Testing | - | Load generation |

### Logs

| Componente | Función | Retención |
|:-----------|:--------|:----------|
| Loki | Agregación y query | 30 días |
| Promtail | Collection agent | N/A |
| LogQL | Query language | N/A |

### Traces

| Componente | Función | Retención |
|:-----------|:--------|:----------|
| Tempo | Trace storage | 7 días |
| OpenTelemetry | Instrumentation | N/A |
| TraceQL | Query language | N/A |

### Visualización

| Componente | Función |
|:-----------|:--------|
| Grafana | Dashboards unificados |
| Explore | Query interactivo |
| Grafana Alerting | Reglas y notificaciones |

---

## Seguridad (Zero Trust)

### Edge Security

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| WAF | Cloudflare WAF | Protección DDoS, bot mitigation |
| SSL | Cloudflare SSL | Terminación TLS |
| Tunnel | Cloudflare Tunnel | Zero-port exposure |

### Ingress Security

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| IPS | CrowdSec | Detección colaborativa de amenazas |
| Bouncer | Traefik Plugin | Bloqueo automático de IPs |
| Middlewares | Rate Limiting | Protección contra abuse |

### Network Security

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Policies | CiliumNetworkPolicy | Default deny, whitelist explícita |
| L7 Filter | Cilium L7 | Filtrado HTTP/gRPC |
| Hubble | Cilium Hubble | Observabilidad de red |

### Service Security

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| mTLS | Istio Ambient | Encriptación automática pod-to-pod |
| AuthZ | AuthorizationPolicy | Control de acceso L7 |
| Identity | Authentik | SSO con OIDC/SAML |

---

## Database HA (CNPG)

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Operator | CloudNativePG | Lifecycle management |
| Engine | PostgreSQL 16 | Database engine |
| Pooler | PgBouncer | Connection pooling |
| Replication | Streaming | Sync replica lag < 1s |
| Failover | CNPG Operator | Promoción automática |
| WAL Archive | S3 | Continuous archiving |
| Base Backup | Barman | Scheduled full backups |
| PITR | WAL + Base | Point-in-time recovery |

---

## Progressive Delivery

### Rollout Engine

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Controller | Argo Rollouts | Gestión de Canary/Blue-Green |
| Analysis | AnalysisTemplate | Queries Prometheus para SLOs |
| Metrics | AnalysisRun | Ejecución de análisis |

### Traffic Management

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Mesh | Istio Ambient | Traffic splitting L7 |
| Gateway | Gateway API | Standard routing |
| VirtualService | Istio CRD | Weight-based routing |

---

## AI RAG

### RAG Pipeline

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Orchestration | LangGraph | Agentic workflow |
| Embeddings | nomic-embed-text | 768-dim vectors |
| Retrieval | Qdrant | Semantic search |
| Inference | Ollama | Local LLM serving |
| Model | Llama 3.1 8B | Response generation |
| API | FastAPI | REST endpoints |

---

## Backup & DR

### Kubernetes Backup

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Controller | Velero | K8s resource backup |
| Provider | AWS S3 | Object storage |
| Snapshotter | CSI Plugin | Volume snapshots |

### Volume Backup

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Storage | Longhorn | Distributed storage |
| Snapshots | Longhorn | Instant snapshots |
| Offsite | S3 Backend | Remote backup |

### Secret Backup

| Componente | Tecnología | Función |
|:-----------|:-----------|:--------|
| Script | export-dr-backup.sh | Credential export |
| Encryption | Sealed Secrets | At-rest encryption |
| Vault | 1Password | Secure storage |
