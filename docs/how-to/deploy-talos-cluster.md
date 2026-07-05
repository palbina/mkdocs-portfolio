# Cómo Desplegar un Cluster Talos Linux

Guía práctica para instalar un cluster Kubernetes con Talos Linux en bare-metal. Asume que ya tienes experiencia con Kubernetes y solo necesitas los pasos exactos.

!!! tip "¿Primera vez con Talos?"
    Si es tu primera vez con Talos Linux, te recomendamos seguir el [tutorial paso a paso](../tutorials/kubernetes-homelab.md) que incluye explicaciones detalladas.

---

## Prerrequisitos

- `talosctl` instalado
- `kubectl` instalado
- `cilium` CLI instalado
- 3 nodos con IPs estáticas y kernel >= 5.10

---

## Instalación

### 1. Generar Configuración

```bash
talosctl gen config homelab-cluster https://192.168.1.10:6443 \
  --output-dir ./_out
```

### 2. Bootstrap Control Plane

```bash
talosctl apply-config --insecure \
  --nodes 192.168.1.10 \
  --file ./_out/controlplane.yaml

talosctl bootstrap --nodes 192.168.1.10 --endpoints 192.168.1.10
talosctl kubeconfig --nodes 192.168.1.10 --endpoints 192.168.1.10
```

### 3. Instalar Cilium CNI

```bash
cilium install --version 1.15.0 \
  --set kubeProxyReplacement=true \
  --set k8sServiceHost=192.168.1.10 \
  --set k8sServicePort=6443

cilium status --wait
```

### 4. Unir Workers

```bash
talosctl apply-config --insecure \
  --nodes 192.168.1.11 \
  --file ./_out/worker.yaml

talosctl apply-config --insecure \
  --nodes 192.168.1.12 \
  --file ./_out/worker.yaml
```

### 5. Verificar

```bash
kubectl get nodes
cilium status
talosctl health --nodes 192.168.1.10,192.168.1.11,192.168.1.12
```

---

## Comandos de Operación

```bash
# Ver estado de nodos
kubectl get nodes -o wide

# Verificar Cilium
cilium status

# Health check de Talos
talosctl health --nodes 192.168.1.10

# Logs de un nodo
talosctl logs --nodes 192.168.1.10 kubelet

# Ver pods del sistema
kubectl get pods -n kube-system
```

---

## Troubleshooting

!!! bug "Nodo no se une al cluster"
    Verificar conectividad de red entre nodos. Revisar logs de kubelet (`talosctl logs kubelet`). Verificar que el token de bootstrap sea válido. Reintentar apply-config.

!!! bug "Cilium pods en CrashLoopBackOff"
    Verificar kernel >= 5.10 (`uname -r`). Verificar que kube-proxy esté deshabilitado. Revisar logs: `kubectl logs -n kube-system -l app.kubernetes.io/name=cilium-agent`.

---

## Configuración de Referencia

### Variables de Entorno

| Variable | Default | Requerido |
|:---------|:--------|:----------|
| `TALOS_ENDPOINT` | `192.168.1.10` | Sí |
| `KUBECONFIG` | `~/.kube/config` | Sí |
| `CILIUM_VERSION` | `1.15.0` | No |
| `ISTIO_VERSION` | `1.21.0` | No |

### Hardware Recomendado

| Nodo | Rol | CPU | RAM | Storage |
|:-----|:----|:----|:----|:--------|
| node-01 | Control Plane | 4+ cores | 16GB+ | 200GB+ NVMe |
| node-02 | Worker | 4+ cores | 16GB+ | 500GB+ NVMe |
| node-03 | Worker | 4+ cores | 16GB+ | 500GB+ NVMe |

---

## Ver también

- [Tutorial: HomeLab Kubernetes](../tutorials/kubernetes-homelab.md)
- [Referencia de comandos Kubernetes](../reference/kubernetes-commands.md)
- [Proyecto HomeLab](../projects/homelab.md)
