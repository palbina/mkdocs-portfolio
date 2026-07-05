# Explicación

Contexto, background y análisis de las decisiones arquitectónicas. Aquí se responde la pregunta **¿por qué?** — el razonamiento detrás de cada elección técnica y los fundamentos conceptuales del stack.

!!! info "¿Qué es la explicación?"
    La explicación proporciona **contexto y background**. Sirve la necesidad de entender y poner las cosas en una perspectiva más amplia. Une conceptos y ayuda a responder la pregunta *¿por qué?* A diferencia de la referencia (que es neutral), la explicación puede contener opiniones y tomar perspectivas.

---

## Temas de Explicación

<div class="grid cards" markdown>

-   :material-cloud:{ .lg .middle } **Arquitectura Cloud Native**

    ---

    Fundamentos de cloud-native: infraestructura inmutable, eBPF, service mesh sin sidecars, GitOps y observabilidad. El *por qué* detrás de cada elección arquitectónica del HomeLab.

    [:octicons-arrow-right-24: Leer explicación](cloud-native-architecture.md)

-   :material-source-branch:{ .lg .middle } **Filosofía GitOps**

    ---

    Por qué Git como fuente única de verdad. Aplicación del patrón App-of-Apps, sync waves, self-healing y el flujo unidireccional que elimina la configuración manual.

    [:octicons-arrow-right-24: Leer explicación](gitops-philosophy.md)

-   :material-security:{ .lg .middle } **Modelo Zero Trust**

    ---

    Defensa en profundidad: de Cloudflare WAF a Istio mTLS. Por qué la seguridad basada en perímetro ya no funciona y cómo implementar verificación continua de identidad.

    [:octicons-arrow-right-24: Leer explicación](zero-trust-model.md)

-   :material-eye:{ .lg .middle } **Patrones de Observabilidad**

    ---

    Los tres pilares: métricas, logs y traces. Por qué la correlación entre señales es el verdadero superpoder y cómo Grafana LGTM hace posible el debugging end-to-end.

    [:octicons-arrow-right-24: Leer explicación](observability-patterns.md)

</div>

---

## El Diagrama Diátaxis

La explicación ocupa el cuadrante inferior izquierdo del mapa Diátaxis: contenido orientado a la **cognición** que sirve a la **adquisición de habilidades** mediante el estudio.

| Tipo | Orientación | Sirve a |
|:-----|:------------|:--------|
| Tutorales | Acción | Estudio |
| How-to | Acción | Trabajo |
| Referencia | Cognición | Trabajo |
| Explicación | Cognición | Estudio |
