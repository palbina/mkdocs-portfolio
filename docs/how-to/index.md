# Guías How-To

Guías prácticas orientadas a resolver problemas específicos. Cada guía asume que ya tienes experiencia con las herramientas y te da los pasos exactos para lograr un objetivo concreto.

!!! info "¿Qué es una guía how-to?"
    Una guía how-to resuelve un **problema real** proporcionando direcciones prácticas a un usuario que ya es competente. A diferencia de un tutorial, la guía how-to se enfoca en el **trabajo** (lograr un resultado), no en el **estudio** (aprender un concepto).

---

## Guías Disponibles

<div class="grid cards" markdown>

-   :material-server:{ .lg .middle } **Desplegar un Cluster Talos Linux**

    ---

    Instalación paso a paso de Talos Linux en bare-metal: generación de configs, bootstrap del cluster y join de worker nodes.

    [:octicons-arrow-right-24: Ver guía](deploy-talos-cluster.md)

-   :material-sync:{ .lg .middle } **Configurar ArgoCD con GitOps**

    ---

    Instalación de ArgoCD, configuración de ApplicationSets, sync waves y gestión de secrets con Sealed Secrets.

    [:octicons-arrow-right-24: Ver guía](configure-argocd.md)

-   :material-bell-ring:{ .lg .middle } **Montar Monitoreo y Alertas**

    ---

    Despliegue del stack LGTM con Helm: Prometheus, Loki, Tempo y Grafana. Configuración de alertas a Telegram.

    [:octicons-arrow-right-24: Ver guía](setup-monitoring.md)

-   :material-backup-restore:{ .lg .middle } **Respaldar Workloads con Velero**

    ---

    Configuración de Velero para backup de recursos Kubernetes, snapshots de volúmenes y restore tests periódicos.

    [:octicons-arrow-right-24: Ver guía](backup-velero.md)

-   :material-database:{ .lg .middle } **Desplegar PostgreSQL HA con CNPG**

    ---

    Instalación del operador CloudNativePG, creación de clusters PostgreSQL, replicación síncrona y WAL archiving a S3.

    [:octicons-arrow-right-24: Ver guía](deploy-postgresql-ha.md)

</div>

---

## El Diagrama Diátaxis

Las guías how-to ocupan el cuadrante superior derecho del mapa Diátaxis: contenido orientado a la **acción** que sirve a la **aplicación de habilidades** en el trabajo.

| Tipo | Orientación | Sirve a |
|:-----|:------------|:--------|
| Tutorales | Acción | Estudio |
| How-to | Acción | Trabajo |
| Referencia | Cognición | Trabajo |
| Explicación | Cognición | Estudio |
