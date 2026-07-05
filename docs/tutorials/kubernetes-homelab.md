# Tutorial: HomeLab Kubernetes desde Cero

Aprende a construir un cluster Kubernetes de 3 nodos bare-metal con Talos Linux, Cilium eBPF e Istio Ambient. Este tutorial te guía desde cero hasta tener un cluster funcional con networking avanzado.

!!! info "Público objetivo"
    Este tutorial asume familiaridad básica con línea de comandos y conceptos de redes. No necesitas experiencia previa con Kubernetes ni Talos Linux.

!!! tip "¿Prefieres ir directo al resultado?"
    Si ya tienes experiencia y solo necesitas los pasos exactos, consulta la guía [Desplegar un Cluster Talos Linux](../how-to/deploy-talos-cluster.md).

---

## ¿Qué vas a construir?

Un cluster Kubernetes de 3 nodos con:

- **Talos Linux** como sistema operativo inmutable y API-driven
- **Cilium CNI** con eBPF reemplazando kube-proxy para networking de alto rendimiento
- **Istio Ambient** para service mesh sin sidecars
- **Longhorn** para almacenamiento distribuido

---

## Prerrequisitos

Antes de empezar, asegúrate de tener:

- [x] 3 máquinas físicas o VMs con al menos 4 CPU y 8GB RAM cada una
- [x] Acceso SSH/IPMI a las máquinas (para instalación inicial)
- [x] `talosctl` instalado en tu máquina local
- [x] `kubectl` instalado
- [x] `cilium` CLI instalado
- [x] Direcciones IP estáticas configuradas para los 3 nodos

!!! warning "Importante"
    Talos Linux **no tiene SSH**. Toda la administración se hace mediante `talosctl` y la API de Talos. Esto es intencional: el sistema operativo es inmutable y no permite acceso interactivo.

---

## Fase 1: Instalación de Talos Linux

### Paso 1: Generar la Configuración del Cluster

Primero, genera las configuraciones base para el control plane y los workers:

```bash
# Generar configuración para el cluster
# Reemplaza 192.168.1.10 con la IP de tu nodo control plane
talosctl gen config homelab-cluster https://192.168.1.10:6443 \
  --output-dir ./_out
```

Este comando crea tres archivos en `./_out/`:

| Archivo | Propósito |
|:--------|:----------|
| `controlplane.yaml` | Configuración para el nodo control plane |
| `worker.yaml` | Configuración para los nodos worker |
| `talosconfig` | Configuración del cliente talosctl |

### Paso 2: Aplicar Configuración al Control Plane

Aplica la configuración al primer nodo y haz bootstrap del cluster:

```bash
# Aplicar configuración al primer nodo (control plane)
talosctl apply-config --insecure \
  --nodes 192.168.1.10 \
  --file ./_out/controlplane.yaml

# Esperar a que el nodo esté listo (~2 minutos)
talosctl health --nodes 192.168.1.10

# Bootstrap el cluster (esto inicializa etcd y el control plane)
talosctl bootstrap --nodes 192.168.1.10 --endpoints 192.168.1.10

# Obtener el kubeconfig
talosctl kubeconfig --nodes 192.168.1.10 --endpoints 192.168.1.10

# Verificar que el nodo esté listo
kubectl get nodes
```

!!! success "¿Qué acaba de pasar?"
    - Talos Linux se instaló en el primer nodo como un SO inmutable
    - Se creó un cluster Kubernetes de un solo nodo con etcd
    - `kubeconfig` se descargó a tu máquina local, permitiéndote usar `kubectl`

---

## Fase 2: Configuración de Cilium CNI

Cilium usa eBPF para reemplazar kube-proxy, ofreciendo mejor rendimiento y observabilidad de red.

### Paso 3: Instalar Cilium CLI

```bash
# Descargar Cilium CLI
curl -L --remote-name-all \
  https://github.com/cilium/cilium-cli/releases/latest/download/cilium-linux-amd64.tar.gz

# Extraer e instalar
tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin

# Verificar instalación
cilium version
```

### Paso 4: Instalar Cilium en el Cluster

```bash
# Instalar Cilium con kube-proxy replacement (requiere kernel >= 5.10)
cilium install --version 1.15.0 \
  --set kubeProxyReplacement=true \
  --set k8sServiceHost=192.168.1.10 \
  --set k8sServicePort=6443

# Verificar estado de Cilium
cilium status --wait
```

!!! info "eBPF y kube-proxy replacement"
    Cilium reemplaza completamente kube-proxy usando programas eBPF. Esto significa que todas las reglas de networking (Service, EndpointSlices, NodePort) se manejan directamente en el kernel sin pasar por iptables, resultando en menor latencia y mayor throughput.

### Paso 5: Verificar la Instalación de Cilium

```bash
# Verificar conectividad entre nodos
cilium connectivity test

# Ver pods de Cilium
kubectl get pods -n kube-system -l k8s-app=cilium
```

---

## Fase 3: Agregar Worker Nodes

### Paso 6: Unir los Nodos Worker al Cluster

```bash
# Generar configuración para workers (si no se hizo en el paso 1)
# El archivo worker.yaml ya debería existir en ./_out/

# Aplicar configuración al worker 1
talosctl apply-config --insecure \
  --nodes 192.168.1.11 \
  --file ./_out/worker.yaml

# Aplicar configuración al worker 2
talosctl apply-config --insecure \
  --nodes 192.168.1.12 \
  --file ./_out/worker.yaml

# Esperar a que los workers estén listos (~1 minuto por nodo)
sleep 60

# Verificar que los 3 nodos aparezcan
kubectl get nodes -o wide
```

Deberías ver los 3 nodos en estado `Ready`:

```
NAME       STATUS   ROLES           AGE   VERSION
node-01    Ready    control-plane   5m    v1.35.0
node-02    Ready    <none>          1m    v1.35.0
node-03    Ready    <none>          1m    v1.35.0
```

---

## Fase 4: Verificación del Cluster

### Paso 7: Health Check Completo

```bash
# Health check de Talos en todos los nodos
talosctl health --nodes 192.168.1.10,192.168.1.11,192.168.1.12

# Verificar pods del sistema
kubectl get pods -n kube-system

# Verificar estado de Cilium en todos los nodos
cilium status

# Verificar conectividad
cilium connectivity test
```

---

## ¿Qué sigue?

- :fontawesome-solid-arrow-right: Instalar [ArgoCD para GitOps](../tutorials/gitops-argocd.md)
- :fontawesome-solid-arrow-right: Configurar el [stack de observabilidad LGTM](../tutorials/observability-lgtm.md)
- :fontawesome-solid-arrow-right: Implementar [seguridad Zero Trust](../tutorials/zero-trust-security.md)
- :fontawesome-solid-arrow-right: Leer la explicación de [arquitectura cloud-native](../explanation/cloud-native-architecture.md)

---

## Referencias

- [Talos Linux Documentation](https://www.talos.dev/)
- [Cilium Documentation](https://docs.cilium.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Proyecto HomeLab Kubernetes](../projects/homelab.md)
