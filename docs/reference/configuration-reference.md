# Configuración de Referencia

Variables de entorno, parámetros de configuración y valores de referencia para todos los componentes del stack.

---

## HomeLab Kubernetes

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `TALOS_ENDPOINT` | Endpoint del API de Talos | `192.168.1.10` | Sí |
| `KUBECONFIG` | Path al kubeconfig | `~/.kube/config` | Sí |
| `CILIUM_VERSION` | Versión de Cilium | `1.15.0` | No |
| `ISTIO_VERSION` | Versión de Istio | `1.21.0` | No |

### Hardware del Cluster

| Nodo | Rol | CPU | RAM | Storage |
|:-----|:----|:----|:----|:--------|
| node-01 | Control Plane | Intel i5-12400 | 32GB DDR5 | 500GB NVMe |
| node-02 | Worker | Intel i5-12400 | 32GB DDR5 | 1TB NVMe |
| node-03 | Worker | Intel i5-12400 | 32GB DDR5 | 1TB NVMe |

---

## GitOps (ArgoCD)

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `ARGOCD_SERVER` | URL del servidor ArgoCD | `argocd.local` | Sí |
| `ARGOCD_AUTH_TOKEN` | Token de autenticación | - | Sí |
| `REPO_URL` | URL del repositorio Git | - | Sí |
| `SYNC_INTERVAL` | Intervalo de sincronización | `3m` | No |

### Sync Waves

| Wave | Componentes | Descripción |
|:----:|:------------|:------------|
| **0** | CRDs, Cilium CNI | Fundamentos de red |
| **1-2** | Istio Base + CP | Service mesh |
| **3** | Sealed Secrets | Gestión de secrets |
| **4** | Longhorn | Storage distribuido |
| **5** | Traefik, Cloudflared | Ingress y túneles |
| **10** | DBs, Monitoring | Datos y observabilidad |
| **20+** | User Applications | Apps de usuario |

---

## Observabilidad (LGTM)

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `PROMETHEUS_RETENTION` | Retención de métricas | `15d` | No |
| `LOKI_RETENTION` | Retención de logs | `30d` | No |
| `TEMPO_RETENTION` | Retención de traces | `7d` | No |
| `ALERTMANAGER_WEBHOOK` | URL para alertas | - | Sí |

### Métricas de Monitoreo

| Métrica | Umbral | Alerta |
|:--------|:-------|:-------|
| Node CPU | > 80% | Warning |
| Node Memory | > 85% | Critical |
| Disk Usage | > 80% | Warning |
| Pod Restarts | > 5 en 1h | Warning |
| API Server Latency | > 1s | Critical |
| Prometheus Scrape Failures | > 10% | Warning |
| Loki Ingestion Rate | Anomalía | Info |
| Tempo Trace Errors | > 5% | Warning |

### PromQL para Alertas

```promql
# Latencia p99
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) /
sum(rate(http_requests_total[5m])) > 0.01

# High memory usage
100 - (avg by (instance) (node_memory_MemAvailable_bytes /
  node_memory_MemTotal_bytes) * 100) > 85
```

---

## Seguridad (Zero Trust)

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `CLOUDFLARE_API_TOKEN` | Token para WAF | - | Sí |
| `CROWDSEC_API_KEY` | Key para bouncers | - | Sí |
| `AUTHENTIK_URL` | URL del IdP | `auth.homelab.local` | Sí |
| `ISTIO_MTLS_MODE` | Modo mTLS | `STRICT` | No |

### Escenarios CrowdSec

```yaml
scenarios:
  - crowdsecurity/http-bad-user-agent
  - crowdsecurity/http-probing
  - crowdsecurity/ssh-bf
  - crowdsecurity/http-crawl-non_statics
```

### Métricas de Seguridad

| Métrica | Valor | Tendencia |
|:--------|:------|:----------|
| IPs bloqueadas (24h) | ~150 | 📈 |
| Escenarios CrowdSec activos | 12 | - |
| Namespaces con mTLS STRICT | 100% | ✅ |
| NetworkPolicies aplicadas | 45+ | 📈 |

---

## Database HA (CNPG)

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `POSTGRES_DB` | Database inicial | `app` | No |
| `POSTGRES_USER` | Superuser | `postgres` | No |
| `POSTGRES_PASSWORD` | Password superuser | - | Sí |
| `AWS_ACCESS_KEY_ID` | S3 Access Key | - | Sí |
| `AWS_SECRET_ACCESS_KEY` | S3 Secret Key | - | Sí |

### Databases en Producción

| Database | Aplicación | Tamaño | Replicas |
|:---------|:-----------|:-------|:---------|
| odoo-db | Odoo ERP | 2.5 GB | 2 |
| authentik-db | Authentik SSO | 150 MB | 1 |
| wordpress-db | WordPress Sites | 500 MB | 1 |
| forgejo-db | Forgejo Git | 300 MB | 1 |

### Métricas de Monitoreo DB

| Métrica | Umbral | Alerta |
|:--------|:-------|:-------|
| Replication Lag | > 5s | Warning |
| Active Connections | > 180 | Warning |
| Transactions/sec | Anomalía | Info |
| Storage Usage | > 80% | Critical |
| Backup Age | > 25h | Warning |

---

## Progressive Delivery

### SLOs Definidos

| Métrica | Umbral | Ventana | Acción |
|:--------|:-------|:--------|:-------|
| Success Rate | ≥ 95% | 2 min | Promote |
| Latency P95 | < 500ms | 5 min | Promote |
| Error Rate | < 1% | 1 min | Rollback |

### Variables de Análisis

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `success-threshold` | Porcentaje mínimo de éxito | `0.95` | Sí |
| `analysis-interval` | Intervalo de query | `30s` | No |
| `rollback-on-failure` | Auto-rollback si falla | `true` | No |

---

## Backup & DR

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `VELERO_S3_BUCKET` | Bucket S3 para backups | `homelab-backups` | Sí |
| `VELERO_REGION` | Región AWS | `us-east-1` | Sí |
| `LONGHORN_BACKUP_TARGET` | Endpoint S3 | `s3://backups` | Sí |
| `DR_VAULT` | Vault de 1Password | `HomeLab DR` | Sí |

### Frecuencias de Backup

| Tipo | Frecuencia | Retención | Destino |
|:-----|:-----------|:----------|:--------|
| Full Cluster | Diario 3 AM | 30 días | S3 |
| Longhorn Volumes | Cada 6h | 7 días | S3 |
| WAL Archive (DB) | Cada 5 min | 30 días | S3 |
| DR Secrets | Manual | Indefinida | 1Password |

### Métricas de Backup

| Métrica | Umbral | Alerta |
|:--------|:-------|:-------|
| Backup Success Rate | < 95% | Critical |
| Restore Test Age | > 35 days | Warning |
| Backup Size Growth | > 20% semanal | Warning |
| RPO Breach | > 1 hora | Critical |

---

## AI RAG

### Variables de Entorno

| Variable | Descripción | Default | Requerido |
|:---------|:------------|:--------|:----------|
| `QDRANT_URL` | URL del servidor Qdrant | `http://localhost:6333` | Sí |
| `OLLAMA_URL` | URL del servidor Ollama | `http://localhost:11434` | Sí |
| `EMBEDDING_MODEL` | Modelo de embeddings | `nomic-embed-text` | No |
| `LLM_MODEL` | Modelo LLM | `llama3.1:8b` | No |

### Colecciones de Conocimiento

| Colección | Documentos | Descripción |
|:----------|:-----------|:------------|
| docs_portfolio | 2,500 | Documentación del portfolio |
| blog_posts | 150 | Artículos técnicos |
| homelab_infra | 4,000 | Configuración del cluster |
| projects | 3,500 | Código y arquitectura |
| context_docs | 1,850 | Context documentation |
