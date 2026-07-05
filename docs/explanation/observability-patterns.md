# Patrones de Observabilidad

Los tres pilares: métricas, logs y traces. Por qué la correlación entre señales es el verdadero superpoder y cómo el stack LGTM hace posible el debugging end-to-end.

---

## Más Allá del Monitoreo

El monitoreo tradicional responde una pregunta: **¿está funcionando?** (¿el CPU está alto?
¿hay suficiente disco?). La observabilidad responde preguntas que no sabías que ibas a necesitar
hacer: **¿por qué los usuarios en Europa están experimentando latencia 3x mayor que ayer
entre las 14:00 y 14:15?**

La diferencia está en la capacidad de explorar y correlacionar sin necesidad de haber
predefinido dashboards o alertas para ese escenario específico. Con observabilidad,
los datos están ahí; tú formulas la pregunta después.

---

## Los Tres Pilares

### Métricas (Prometheus + PromQL)

Responden **QUÉ** pasó. Series temporales numéricas que representan el estado del sistema
a lo largo del tiempo.

```
CPU del nodo-01 a las 14:03: 87.3%
Requests HTTP en los últimos 5 minutos: 12,450
Latencia p99 del servicio de API: 234ms
```

Las métricas son agregadas y precomputadas. Son baratas de almacenar y rápidas de consultar,
pero no contienen el contexto completo de una request individual.

### Logs (Loki + LogQL)

Responden **POR QUÉ** pasó. Registros inmutables con timestamp de eventos discretos.

```
[2026-03-03 14:03:22] ERROR payment-service: connection refused to database:5432
[2026-03-03 14:03:22] WARN database: max_connections (200) reached, rejecting new connections
[2026-03-03 14:03:23] ERROR api-gateway: upstream payment-service returned 502
```

Los logs contienen el contexto rico de un evento específico. Son la fuente más detallada,
pero también la más cara de almacenar e indexar.

### Traces (Tempo + TraceQL)

Responden **DÓNDE** pasó. Siguen una request a través de todos los servicios que toca,
midiendo la latencia en cada salto.

```
Request ID: abc123
├── api-gateway: 2ms
│   ├── auth-service: 15ms (verify JWT)
│   ├── payment-service: 234ms ← BOTTLENECK
│   │   └── database: 230ms (slow query)
│   └── notification-service: 5ms
└── Total: 256ms
```

Los traces muestran la ruta completa de una request y exactamente dónde se gasta el tiempo.
Sin traces, solo verías que la API tarda 256ms, sin saber que el 90% de ese tiempo es
una query lenta en la base de datos.

---

## El Verdadero Superpoder: Correlación

Cada pilar por separado es útil pero limitado. La magia ocurre cuando los correlacionas.

### Escenario Real: Debugging de una Incidente

**Paso 1 — Alerta de Grafana:** Latencia p99 de la API subió de 50ms a 500ms.

**Paso 2 — Métricas en Prometheus:** El spike coincide con un aumento de conexiones a
la base de datos. `cnpg_pg_stat_activity_count` pasó de 20 a 195 en segundos.

**Paso 3 — Saltar a Logs (Loki):** Desde el panel de Grafana, clic derecho → Explore → Loki
para el mismo timeframe. Encuentras: `ERROR: remaining connection slots are reserved for
superuser`. La base de datos se quedó sin conexiones.

**Paso 4 — Seguir el Trace (Tempo):** Un trace ID en los logs te lleva a Tempo. Ves que
una query específica (`SELECT * FROM orders WHERE status='pending'`) está tomando 450ms
porque la tabla no tiene índice en la columna `status`.

**Paso 5 — Solución:** Creas el índice. La query baja a 2ms. Latencia p99 vuelve a 50ms.

**Tiempo total:** ~3 minutos desde la alerta hasta la causa raíz.

!!! success "Sin correlación"
    Sin correlación, habrías visto una alerta de latencia, mirado dashboards de CPU
    (todo normal), mirado dashboards de memoria (todo normal), y pasado 30 minutos
    adivinando hasta encontrar el log de error en la base de datos.

### Cómo Funciona la Correlación en Grafana

Grafana LGTM implementa la correlación automáticamente:

1. **Loki → Tempo:** Los logs incluyen `traceID`. Al hacer clic en un trace ID en un log,
   Grafana te lleva directamente al trace en Tempo.
2. **Tempo → Loki:** Los traces incluyen etiquetas de servicio y timestamp. Puedes saltar
   a los logs de ese servicio exacto en ese momento exacto.
3. **Prometheus → Loki:** Desde un panel de métricas, "Explore" te lleva a los logs del
   mismo timeframe con un clic.

---

## El Stack LGTM

### ¿Por Qué Este Stack y No Otro?

| Alternativa | Stack Elegido | Razón |
|:------------|:--------------|:------|
| ELK (Elastic) | Loki + Tempo | Loki es más ligero y nativo de Kubernetes. No necesita Java. |
| Datadog/NewRelic | LGTM self-hosted | Sin costos recurrentes. Datos bajo tu control. |
| Jaeger standalone | Tempo | Tempo se integra nativamente con Grafana y Loki. |
| Solo Prometheus | LGTM completo | Métricas sin logs y traces da una visión parcial. |

### Retención y Costos

| Señal | Herramienta | Retención | Tamaño Estimado |
|:------|:------------|:----------|:----------------|
| Métricas | Prometheus | 15 días | ~5 GB |
| Logs | Loki | 30 días | ~20 GB |
| Traces | Tempo | 7 días | ~3 GB |

La retención está balanceada: las métricas (más baratas de almacenar) se guardan más tiempo.
Los traces (más detallados y costosos) se rotan más rápido.

---

## PromQL para Análisis

Algunas queries útiles que demuestran el poder de PromQL:

```promql
# Tasa de error por endpoint
sum(rate(http_requests_total{status=~"5.."}[5m])) by (path) /
sum(rate(http_requests_total[5m])) by (path)

# Latencia por percentil
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le, path))

# Predicción de disco lleno (cuántas horas hasta que se llene)
predict_linear(node_filesystem_free_bytes{mountpoint="/"}[1h], 24 * 3600)

# Uso de memoria real (excluyendo caché)
node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes
```

---

## Ver también

- [Tutorial: Observabilidad LGTM](../tutorials/observability-lgtm.md)
- [Guía: Configurar Monitoreo y Alertas](../how-to/setup-monitoring.md)
- [Referencia de comandos de observabilidad](../reference/kubernetes-commands.md)
- [Referencia de configuración](../reference/configuration-reference.md)
