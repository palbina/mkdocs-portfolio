# Tutorial: GitOps con ArgoCD

Aprende a implementar GitOps para gestionar tu cluster Kubernetes de forma declarativa. Al final de este tutorial, tendrás ArgoCD gestionando aplicaciones automáticamente desde Git.

!!! info "Público objetivo"
    Necesitas un cluster Kubernetes funcional y familiaridad con `kubectl`. Este tutorial asume que tienes el cluster del tutorial [HomeLab Kubernetes](kubernetes-homelab.md) o uno similar.

!!! tip "¿Solo necesitas los pasos?"
    Consulta la guía [Configurar ArgoCD](../how-to/configure-argocd.md) para una referencia rápida sin explicaciones.

---

## ¿Qué vas a construir?

- **ArgoCD** como motor de continuous delivery declarativo
- **ApplicationSets** para gestionar múltiples aplicaciones desde directorios en Git
- **Sealed Secrets** para almacenar secretos encriptados en Git
- **Sync Waves** para controlar el orden de despliegue

---

## Prerrequisitos

- [x] Cluster Kubernetes funcional (3+ nodos recomendado)
- [x] `kubectl` configurado
- [x] `argocd` CLI instalado
- [x] Repositorio Git para la configuración del cluster
- [x] `kubeseal` instalado (para Sealed Secrets)

---

## Fase 1: Instalación de ArgoCD

### Paso 1: Desplegar ArgoCD

```bash
# Crear namespace
kubectl create namespace argocd

# Instalar ArgoCD desde los manifests oficiales
kubectl apply -n argocd -f \
  https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Esperar a que todos los pods estén listos
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=argocd-server -n argocd --timeout=300s
```

### Paso 2: Acceder a la UI de ArgoCD

```bash
# Obtener la contraseña inicial de admin
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

# Exponer la UI localmente
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Abre `https://localhost:8080` en tu navegador. Usuario: `admin`, contraseña: la que obtuviste arriba.

!!! info "¿Qué es ArgoCD?"
    ArgoCD es un controller de Kubernetes que monitorea un repositorio Git y sincroniza el estado declarado en Git con el estado real del cluster. Si alguien modifica algo manualmente en el cluster, ArgoCD lo detecta (drift) y puede revertirlo automáticamente (self-healing).

---

## Fase 2: ApplicationSets para Múltiples Aplicaciones

### Paso 3: Entender ApplicationSets

En lugar de crear una `Application` de ArgoCD por cada aplicación, usamos `ApplicationSet` que genera Applications automáticamente basándose en la estructura de directorios de tu repositorio Git.

### Paso 4: Crear el ApplicationSet

Crea un archivo `applicationset.yaml`:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: apps
  namespace: argocd
spec:
  generators:
    - git:
        repoURL: https://github.com/tu-usuario/tu-repo-infra
        revision: main
        directories:
          - path: k8s/02-apps/*
  template:
    metadata:
      name: '{{ "{{" }}path.basename{{ "}}" }}'
    spec:
      project: default
      source:
        repoURL: https://github.com/tu-usuario/tu-repo-infra
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

Aplica el ApplicationSet:

```bash
kubectl apply -f applicationset.yaml
```

!!! success "¿Qué hace esto?"
    - Escanea `k8s/02-apps/*` en tu repositorio Git
    - Por cada subdirectorio, crea una `Application` de ArgoCD
    - Cada Application sincroniza los manifests de ese directorio con el cluster
    - `prune: true` elimina recursos que ya no están en Git
    - `selfHeal: true` revierte cambios manuales automáticamente

---

## Fase 3: Sync Waves para Orden de Despliegue

### Paso 5: Entender las Sync Waves

Algunos componentes deben desplegarse antes que otros (ej. CRDs antes que los recursos que los usan). Las sync waves controlan este orden mediante anotaciones.

### Paso 6: Configurar Sync Waves

En tus manifests de Kubernetes, añade anotaciones para controlar el orden:

```yaml
# Wave 0: CRDs, Cilium CNI (fundamentos de red)
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "0"

# Wave 1-2: Istio Base + ControlPlane (service mesh)
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"

# Wave 3: Sealed Secrets (gestión de secretos)
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "3"

# Wave 5: Traefik, Cloudflared (ingress)
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "5"

# Wave 10: Bases de datos, Monitoreo
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "10"

# Wave 20+: Aplicaciones de usuario
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "20"
```

### Orden de Waves por Categoría

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

## Fase 4: Verificación

### Paso 7: Verificar el Funcionamiento

```bash
# Login al CLI de ArgoCD
argocd login localhost:8080 --username admin --password <tu-password> --insecure

# Listar todas las aplicaciones
argocd app list

# Ver estado de una aplicación específica
argocd app get <nombre-app>

# Verificar que no hay drift
argocd app list | grep -v Synced
```

Si todo funciona correctamente, deberías ver todas las aplicaciones en estado `Synced` y `Healthy`.

---

## ¿Qué sigue?

- :fontawesome-solid-arrow-right: Configurar [observabilidad con LGTM](../tutorials/observability-lgtm.md)
- :fontawesome-solid-arrow-right: Implementar [seguridad Zero Trust](../tutorials/zero-trust-security.md)
- :fontawesome-solid-arrow-right: Leer la [filosofía GitOps](../explanation/gitops-philosophy.md)
- :fontawesome-solid-arrow-right: Ver la [guía rápida de ArgoCD](../how-to/configure-argocd.md)

---

## Referencias

- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [GitOps Principles (OpenGitOps)](https://opengitops.dev/)
- [Proyecto GitOps con ArgoCD](../projects/gitops.md)
