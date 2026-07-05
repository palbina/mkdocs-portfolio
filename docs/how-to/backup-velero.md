# Cómo Respaldar Workloads con Velero

Guía práctica para configurar backup automatizado de recursos Kubernetes y volúmenes persistentes usando Velero y Longhorn.

---

## Instalación de Velero

### 1. Instalar CLI y Desplegar en el Cluster

```bash
# Instalar Velero CLI
wget https://github.com/vmware-tanzu/velero/releases/download/v1.12.0/velero-v1.12.0-linux-amd64.tar.gz
tar -xvf velero-v1.12.0-linux-amd64.tar.gz
sudo mv velero /usr/local/bin/

# Instalar en el cluster
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.8.0 \
  --bucket homelab-backups \
  --backup-location-config region=us-east-1 \
  --snapshot-location-config region=us-east-1 \
  --secret-file ./credentials-velero
```

---

## Schedules de Backup

### Backup Diario del Cluster

```yaml
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: daily-cluster-backup
  namespace: velero
spec:
  schedule: "0 3 * * *"  # 3 AM diario
  template:
    includedNamespaces:
      - "*"
    excludedNamespaces:
      - kube-system
      - velero
    includeClusterResources: true
    storageLocation: default
    ttl: 720h  # 30 días de retención
    volumeSnapshotLocations:
      - aws-default
```

### Backup de Volúmenes Longhorn (cada 6h)

```yaml
apiVersion: longhorn.io/v1beta2
kind: RecurringJob
metadata:
  name: backup-volumes
  namespace: longhorn-system
spec:
  cron: "0 */6 * * *"
  task: backup
  retain: 28
  concurrency: 2
  groups:
    - default
```

---

## Frecuencias de Backup

| Tipo | Frecuencia | Retención | Destino |
|:-----|:-----------|:----------|:--------|
| Full Cluster | Diario 3 AM | 30 días | S3 |
| Longhorn Volumes | Cada 6h | 7 días | S3 |
| WAL Archive (DB) | Cada 5 min | 30 días | S3 |
| DR Secrets | Manual | Indefinida | 1Password |

---

## Comandos de Operación

```bash
# Listar backups
velero backup get

# Backup manual
velero backup create manual-backup-$(date +%Y%m%d) \
  --include-namespaces portfolio

# Restaurar namespace
velero restore create --from-backup daily-cluster-backup-20240201 \
  --include-namespaces portfolio \
  --restore-volumes=true

# Ver estado de restauración
velero restore get

# Logs de Velero
kubectl logs -f deployment/velero -n velero
```

---

## Troubleshooting

!!! bug "Backup falla con error de snapshots"
    Verificar que el CSI driver soporte snapshots. Revisar volúmenes en estado "Terminating". Para Longhorn, verificar backup target S3.

!!! bug "Restauración tarda demasiado"
    Considerar backup de volúmenes más frecuente. Usar Velero con restic para file-level restore. Verificar latencia de red al bucket S3.

---

## Variables de Entorno

| Variable | Default | Requerido |
|:---------|:--------|:----------|
| `VELERO_S3_BUCKET` | `homelab-backups` | Sí |
| `VELERO_REGION` | `us-east-1` | Sí |
| `LONGHORN_BACKUP_TARGET` | `s3://backups` | Sí |
| `DR_VAULT` | `HomeLab DR` | Sí |

---

## Métricas de Éxito

| Métrica | Objetivo | Actual |
|:--------|:---------|:-------|
| RPO | < 1 hora | 6h (vol), 5min (DB) |
| RTO | < 30 min | ~15 min |
| Backup Success Rate | 99.9% | 100% |
| Restore Tests | Mensual | ✅ |

---

## Ver también

- [Proyecto Backup & DR](../projects/backup-dr.md)
- [Referencia de configuración](../reference/configuration-reference.md)
