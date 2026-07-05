# Tutorial: Observabilidad con LGTM

Aprende a implementar un stack completo de observabilidad con Grafana LGTM (Loki, Grafana, Tempo, Mimir/Prometheus). Al final, tendrás métricas, logs y traces correlacionados con alertas a Telegram.

!!! info "Público objetivo"
    Necesitas un cluster Kubernetes funcional con ArgoCD o Helm. Este tutorial asume conocimiento básico de Prometheus y Grafana.

---

## ¿Qué vas a construir?

El stack LGTM — los 3 pilares de observabilidad integrados:

- **L**oki: Agregación y consulta de logs (LogQL)
- **G**rafana: Dashboards unificados con correlación de señales
- **T**empo: Distributed tracing (TraceQL)
- **M**imir/Prometheus: Métricas de series temporales (PromQL)

---

## Prerrequisitos

- [x] Cluster Kubernetes funcional
- [x] `helm` instalado y configurado
- [x] `kubectl` configurado
- [x] Telegram Bot Token (para alertas)

---

## Fase 1: Instalación de Prometheus + Grafana

### Paso 1: Desplegar Prometheus Stack

```bash
# Agregar repositorio Helm de Prometheus Community
helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts
helm repo update

# Instalar kube-prometheus-stack (incluye Prometheus, Grafana, Alertmanager)
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set grafana.enabled=true \
  --set alertmanager.enabled=true \
  --set prometheus.prometheusSpec.retention=15d

# Esperar a que los pods estén listos
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=grafana \
  -n monitoring --timeout=300s
```

### Paso 2: Acceder a Grafana

```bash
# Obtener contraseña de admin
kubectl get secret prometheus-grafana -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d

# Port-forward a Grafana
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80
```

Abre `http://localhost:3000`. Usuario: `admin`, contraseña: la del comando anterior.

---

## Fase 2: Agregación de Logs con Loki

### Paso 3: Instalar Loki Stack

```bash
# Agregar repositorio de Grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Instalar Loki con Promtail como agente de recolección
helm install loki grafana/loki-stack \
  --namespace monitoring \
  --set promtail.enabled=true \
  --set grafana.enabled=false \
  --set loki.persistence.enabled=true \
  --set loki.persistence.size=20Gi
```

!!! info "¿Qué es Promtail?"
    Promtail es el agente que se ejecuta en cada nodo del cluster y recolecta logs de los contenedores. Los envía a Loki, que los indexa y los hace consultables con LogQL (similar a PromQL pero para logs).

### Paso 4: Configurar Loki como Data Source en Grafana

En la UI de Grafana:

1. Ve a **Configuration → Data Sources → Add data source**
2. Selecciona **Loki**
3. URL: `http://loki:3100`
4. Haz clic en **Save & Test**

---

## Fase 3: Distributed Tracing con Tempo

### Paso 5: Desplegar Tempo

Crea un archivo `tempo-values.yaml`:

```yaml
tempo:
  storage:
    trace:
      backend: local
      local:
        path: /var/tempo/traces
  receivers:
    jaeger:
      protocols:
        thrift_http:
          endpoint: 0.0.0.0:14268
    otlp:
      protocols:
        grpc:
          endpoint: 0.0.0.0:4317
        http:
          endpoint: 0.0.0.0:4318
```

Instala Tempo:

```bash
helm install tempo grafana/tempo \
  --namespace monitoring \
  --values tempo-values.yaml
```

### Paso 6: Configurar Tempo en Grafana

En la UI de Grafana:

1. Ve a **Configuration → Data Sources → Add data source**
2. Selecciona **Tempo**
3. URL: `http://tempo:3100`
4. Haz clic en **Save & Test**

---

## Fase 4: Alertas a Telegram

### Paso 7: Configurar Alertmanager para Telegram

```yaml
# alertmanager-config.yaml
apiVersion: v1
kind: Secret
metadata:
  name: alertmanager-prometheus-kube-prometheus-alertmanager
  namespace: monitoring
stringData:
  alertmanager.yaml: |
    global:
      telegram_api_url: "https://api.telegram.org"
    route:
      receiver: 'telegram'
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 4h
    receivers:
      - name: 'telegram'
        telegram_configs:
          - bot_token: 'TU_BOT_TOKEN'
            chat_id: TU_CHAT_ID
            parse_mode: 'HTML'
            message: |
              <b>{{ .Status | toUpper }}</b>
              <b>Alert:</b> {{ .CommonLabels.alertname }}
              <b>Severity:</b> {{ .CommonLabels.severity }}
              <b>Description:</b> {{ .CommonAnnotations.description }}
```

### Paso 8: Verificar las Alertas

```bash
# Verificar que Alertmanager esté corriendo
kubectl get pods -n monitoring -l app=alertmanager

# Probar envío de alerta (crea una alerta de prueba en Grafana)
```

---

## Fase 5: Correlación de Señales en Grafana

### El Verdadero Superpoder: Grafana Explore

Con los 3 data sources configurados, puedes:

1. **Empezar con una métrica**: Ver un spike de latencia en Prometheus
2. **Saltar a logs**: Desde el panel de Grafana, hacer clic derecho → Explore → Logs (Loki) para el mismo timeframe
3. **Seguir el trace**: Desde los logs, encontrar un trace ID y abrirlo en Tempo
4. **Debug end-to-end**: Ver exactamente qué servicio causó la latencia

!!! success "Correlación de señales"
    Sin correlación, métricas, logs y traces son piezas aisladas. Con Grafana LGTM, puedes navegar entre ellas fluidamente. De una métrica a los logs del mismo momento, al trace específico que muestra qué microservicio causó el problema.

---

## ¿Qué sigue?

- :fontawesome-solid-arrow-right: Implementar [seguridad Zero Trust](../tutorials/zero-trust-security.md)
- :fontawesome-solid-arrow-right: Leer [patrones de observabilidad](../explanation/observability-patterns.md)
- :fontawesome-solid-arrow-right: Consultar la [guía de monitoreo](../how-to/setup-monitoring.md)

---

## Referencias

- [Grafana Documentation](https://grafana.com/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Loki Documentation](https://grafana.com/docs/loki/)
- [Tempo Documentation](https://grafana.com/docs/tempo/)
- [Proyecto Observabilidad LGTM](../projects/observability.md)
