# Cómo Desplegar PostgreSQL HA con CNPG

Guía práctica para instalar CloudNativePG Operator y crear clusters PostgreSQL de alta disponibilidad con failover automático y backups a S3.

---

## Instalación del Operator

### 1. Desplegar CloudNativePG

```bash
kubectl apply -f \
  https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.22/releases/cnpg-1.22.0.yaml

# Verificar instalación
kubectl get deployment -n cnpg-system cnpg-controller-manager

# Instalar CLI
curl -sSfL \
  https://github.com/cloudnative-pg/cloudnative-pg/raw/main/hack/install-cnpg-plugin.sh | \
  sudo sh -s -- -b /usr/local/bin
```

---

## Crear un Cluster PostgreSQL

```yaml
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: postgres-cluster
  namespace: database
spec:
  instances: 3

  postgresql:
    parameters:
      max_connections: "200"
      shared_buffers: "256MB"
      effective_cache_size: "512MB"

  storage:
    storageClass: longhorn
    size: 20Gi

  backup:
    barmanObjectStore:
      destinationPath: s3://homelab-backups/cnpg/
      s3Credentials:
        accessKeyId:
          name: s3-creds
          key: ACCESS_KEY_ID
        secretAccessKey:
          name: s3-creds
          key: SECRET_ACCESS_KEY
      wal:
        compression: gzip
    retentionPolicy: "30d"
```

### Aplicar Configuración

```bash
kubectl apply -f postgres-cluster.yaml
```

---

## Servicios de Conexión

CNPG crea automáticamente 3 servicios:

| Servicio | Propósito | Endpoint |
|:---------|:----------|:---------|
| `<cluster>-rw` | Read/Write (solo Primary) | Conexiones de escritura |
| `<cluster>-ro` | Read Only (balanceado) | Conexiones de lectura |
| `<cluster>-r` | Any instance | Operaciones de mantenimiento |

```bash
kubectl get svc -n database | grep postgres-cluster
```

---

## Comandos de Operación

```bash
# Ver estado del cluster
kubectl cnpg status postgres-cluster -n database

# Listar pods del cluster
kubectl get pods -n database -l cnpg.io/cluster=postgres-cluster

# Conectar al Primary
kubectl cnpg psql postgres-cluster -n database

# Promover un Replica (manual)
kubectl cnpg promote postgres-cluster postgres-cluster-2 -n database

# Verificar lag de replicación
kubectl cnpg status postgres-cluster -n database | grep "Replication Info"
```

---

## Métricas Prometheus

```promql
# Lag de replicación
cnpg_pg_replication_lag_seconds

# Conexiones activas
cnpg_pg_stat_activity_count

# Transacciones por segundo
rate(cnpg_pg_stat_database_xact_commit[5m])

# Espacio libre
cnpg_pg_database_size_bytes / cnpg_pg_settings_disk_size_bytes
```

---

## Troubleshooting

!!! bug "Failover no ocurre automáticamente"
    Verificar el CNPG Operator (`kubectl get pods -n cnpg-system`). Revisar logs del operator. Promover manualmente: `kubectl cnpg promote`.

!!! bug "Lag de replicación alto"
    Verificar recursos de nodos (CPU/Memory). Revisar red entre nodos. Ajustar `max_wal_size` y `checkpoint_timeout`. Investigar queries largas en el Primary.

---

## Variables de Entorno

| Variable | Default | Requerido |
|:---------|:--------|:----------|
| `POSTGRES_DB` | `app` | No |
| `POSTGRES_USER` | `postgres` | No |
| `POSTGRES_PASSWORD` | - | Sí |
| `AWS_ACCESS_KEY_ID` | - | Sí |
| `AWS_SECRET_ACCESS_KEY` | - | Sí |

---

## Ver también

- [Proyecto Database HA](../projects/database-ha.md)
- [Referencia de stacks tecnológicos](../reference/tech-stacks.md)
- [Referencia de comandos](../reference/kubernetes-commands.md)
