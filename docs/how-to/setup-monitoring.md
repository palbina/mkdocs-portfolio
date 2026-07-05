# Cómo Montar Monitoreo y Alertas

Guía práctica para desplegar el stack LGTM (Loki, Grafana, Tempo, Prometheus) con Helm y configurar alertas a Telegram.

---

## Stack LGTM

### 1. Prometheus + Grafana + Alertmanager

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set grafana.enabled=true \
  --set alertmanager.enabled=true \
  --set prometheus.prometheusSpec.retention=15d
```

### 2. Loki + Promtail

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install loki grafana/loki-stack \
  --namespace monitoring \
  --set promtail.enabled=true \
  --set grafana.enabled=false \
  --set loki.persistence.enabled=true \
  --set loki.persistence.size=20Gi
```

### 3. Tempo

```yaml
# tempo-values.yaml
tempo:
  storage:
    trace:
      backend: local
      local:
        path: /var/tempo/traces
  receivers:
    otlp:
      protocols:
        grpc:
          endpoint: 0.0.0.0:4317
        http:
          endpoint: 0.0.0.0:4318
```

```bash
helm install tempo grafana/tempo --namespace monitoring --values tempo-values.yaml
```

---

## Data Sources en Grafana

| Data Source | URL | Puerto |
|:------------|:----|:-------|
| Prometheus | `http://prometheus-kube-prometheus-prometheus.monitoring` | 9090 |
| Loki | `http://loki.monitoring` | 3100 |
| Tempo | `http://tempo.monitoring` | 3100 |

---

## Alertas a Telegram

```yaml
# alertmanager-config.yaml
receivers:
  - name: 'telegram'
    telegram_configs:
      - bot_token: 'TU_BOT_TOKEN'
        chat_id: TU_CHAT_ID
        parse_mode: 'HTML'
```

```bash
kubectl apply -f alertmanager-config.yaml
```

---

## Comandos Útiles

```bash
# Acceder a Grafana
kubectl get secret prometheus-grafana -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80

# Query PromQL
kubectl exec -it deployment/prometheus-server -n monitoring -- \
  wget -qO- 'http://localhost:9090/api/v1/query?query=up'

# Logs de Loki
kubectl logs -f -n monitoring -l app=loki

# Ver targets de Prometheus
kubectl port-forward svc/prometheus-operated -n monitoring 9090:9090
```

---

## Dashboards Pre-configurados

| Dashboard | Métricas Clave |
|:----------|:---------------|
| Cluster Overview | CPU/Memory por nodo, pods por namespace |
| Kubernetes Pods | Restarts, OOMKills, resource usage |
| Traefik | RPS, latency p50/p95/p99, error rate |
| ArgoCD | Sync status, app health |

---

## PromQL para Alertas Clave

```promql
# Latencia p99
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Error rate > 1%
sum(rate(http_requests_total{status=~"5.."}[5m])) /
sum(rate(http_requests_total[5m])) > 0.01

# High memory usage
100 - (avg by (instance) (node_memory_MemAvailable_bytes /
  node_memory_MemTotal_bytes) * 100) > 85
```

---

## Troubleshooting

!!! bug "Prometheus no scrapea targets"
    Verificar ServiceMonitors con labels correctos. Revisar annotation `prometheus.io/scrape: "true"`. Verificar RBAC.

!!! bug "Loki no recibe logs"
    Verificar Promtail en todos los nodos (`kubectl get pods -n monitoring -l app=promtail`). Revisar client URL en Promtail.

---

## Ver también

- [Tutorial: Observabilidad LGTM](../tutorials/observability-lgtm.md)
- [Patrones de Observabilidad](../explanation/observability-patterns.md)
- [Referencia de comandos](../reference/kubernetes-commands.md)
- [Proyecto Observabilidad](../projects/observability.md)
