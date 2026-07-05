# Cómo Configurar ArgoCD con GitOps

Guía práctica para instalar y configurar ArgoCD con ApplicationSets, Sealed Secrets y sync waves en un cluster Kubernetes existente.

!!! tip "¿Nuevo en GitOps?"
    Consulta el [tutorial de GitOps con ArgoCD](../tutorials/gitops-argocd.md) para una introducción paso a paso con explicaciones.

---

## Instalación

### 1. Desplegar ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f \
  https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 2. Obtener Credenciales

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

### 3. Configurar CLI

```bash
argocd login argocd.local --username admin --password <password>
```

---

## ApplicationSets

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: apps
  namespace: argocd
spec:
  generators:
    - git:
        repoURL: https://github.com/tu-usuario/tu-repo
        revision: main
        directories:
          - path: k8s/02-apps/*
  template:
    metadata:
      name: '{{ "{{" }}path.basename{{ "}}" }}'
    spec:
      project: default
      source:
        repoURL: https://github.com/tu-usuario/tu-repo
        targetRevision: main
        path: '{{ "{{" }}path{{ "}}" }}'
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{ "{{" }}path.basename{{ "}}" }}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

---

## Sync Waves

| Wave | Componentes |
|:----:|:------------|
| **0** | CRDs, Cilium CNI |
| **1-2** | Istio Base + CP |
| **3** | Sealed Secrets |
| **4** | Longhorn |
| **5** | Traefik, Cloudflared |
| **10** | DBs, Monitoring |
| **20+** | User Applications |

```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "5"
```

---

## Comandos Útiles

```bash
argocd app list                          # Listar aplicaciones
argocd app sync <app>                    # Sincronizar manualmente
argocd app get <app>                     # Ver estado detallado
argocd app get <app> --hard-refresh      # Forzar refresh
kubectl logs -f deployment/argocd-application-controller -n argocd
```

---

## Troubleshooting

!!! bug "Drift no se corrige automáticamente"
    Verificar `selfHeal: true` en syncPolicy. Revisar que el Application Controller esté funcionando. Revisar logs por errores RBAC.

!!! bug "ApplicationSet no genera Applications"
    Verificar path en el generator. Revisar conexión del repositorio en ArgoCD. Verificar permisos del token de Git.

---

## Variables de Entorno

| Variable | Default | Requerido |
|:---------|:--------|:----------|
| `ARGOCD_SERVER` | `argocd.local` | Sí |
| `ARGOCD_AUTH_TOKEN` | - | Sí |
| `REPO_URL` | - | Sí |
| `SYNC_INTERVAL` | `3m` | No |

---

## Ver también

- [Tutorial: GitOps con ArgoCD](../tutorials/gitops-argocd.md)
- [Filosofía GitOps](../explanation/gitops-philosophy.md)
- [Proyecto GitOps](../projects/gitops.md)
