# Comandos Útiles

Referencia rápida de comandos organizados por herramienta. Información neutral para consulta durante el trabajo.

---

## Kubernetes

```bash
# Nodos
kubectl get nodes -o wide                    # Estado de nodos con detalles

# Pods
kubectl get pods -n <namespace>              # Listar pods
kubectl get pods -A                          # Todos los pods en todos los namespaces
kubectl logs -f <pod> -n <namespace>         # Logs en tiempo real
kubectl describe pod <pod> -n <namespace>    # Detalles del pod

# Services
kubectl get svc -n <namespace>               # Listar servicios
kubectl port-forward svc/<svc> <local>:<remote> -n <namespace>
```

---

## Talos Linux

```bash
# Gestión de nodos
talosctl health --nodes <ip>                 # Health check
talosctl logs --nodes <ip> kubelet           # Logs de kubelet
talosctl apply-config --insecure \
  --nodes <ip> --file <config.yaml>          # Aplicar configuración
talosctl bootstrap --nodes <ip>              # Bootstrap cluster
talosctl kubeconfig --nodes <ip>             # Obtener kubeconfig
```

---

## Cilium

```bash
# Estado y verificación
cilium status                                # Estado general
cilium status --wait                         # Esperar hasta que esté listo
cilium connectivity test                     # Test de conectividad
cilium policy get                            # Ver NetworkPolicies

# Hubble (observabilidad de red)
hubble observe                               # Ver tráfico en tiempo real
hubble observe --namespace <ns>              # Filtrar por namespace
```

---

## ArgoCD

```bash
# CLI
argocd login <server> --username admin       # Login
argocd app list                              # Listar aplicaciones
argocd app sync <app>                        # Sincronizar manualmente
argocd app get <app>                         # Ver estado detallado
argocd app get <app> --hard-refresh          # Forzar refresh

# kubectl
kubectl logs -f deployment/argocd-application-controller -n argocd
```

---

## Argo Rollouts

```bash
kubectl argo rollouts get rollout <name> -n <ns>      # Estado del rollout
kubectl argo rollouts promote <name> -n <ns>           # Promover manualmente
kubectl argo rollouts abort <name> -n <ns>             # Abortar/Rollback
kubectl argo rollouts get analysisrun <name> -n <ns>   # Ver análisis
```

---

## Observabilidad

```bash
# Prometheus
kubectl exec -it deployment/prometheus-server -n monitoring -- \
  wget -qO- 'http://localhost:9090/api/v1/query?query=up'

# Grafana
kubectl get secret prometheus-grafana -n monitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80

# Loki
kubectl logs -f -n monitoring -l app=loki
```

---

## CrowdSec

```bash
cscli decisions list                         # Ver IPs bloqueadas
cscli decisions add --ip <ip> --duration 4h  # Ban manual
cscli alerts list                            # Ver alertas recientes
cscli metrics                                # Estadísticas
cscli bouncers list                          # Ver bouncers activos
```

---

## Istio

```bash
istioctl authn tls-check                     # Verificar mTLS
istioctl proxy-status                        # Estado de proxies
istioctl analyze                             # Análisis de configuración
```

---

## Velero

```bash
velero backup get                            # Listar backups
velero backup create <name> --include-namespaces <ns>  # Backup manual
velero restore create --from-backup <name> \
  --include-namespaces <ns> --restore-volumes=true     # Restaurar
velero restore get                           # Estado de restauración
kubectl logs -f deployment/velero -n velero  # Logs
```

---

## CloudNativePG (PostgreSQL)

```bash
kubectl cnpg status <cluster> -n <ns>        # Estado del cluster
kubectl cnpg psql <cluster> -n <ns>          # Conectar al Primary
kubectl cnpg promote <cluster> <pod> -n <ns> # Promover replica
kubectl get pods -n <ns> -l cnpg.io/cluster=<cluster>
```

---

## AI RAG

```bash
# Qdrant
curl http://localhost:6333/collections      # Estado de colecciones

# Servicio RAG
curl http://rag-service/api/health           # Health check

# Indexación
python scripts/index_docs.py --collection <name> --path ./docs

# Logs
kubectl logs -f deployment/rag-service -n ai
```
