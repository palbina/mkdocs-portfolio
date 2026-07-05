---
date: 2026-02-10
authors:
  - peter
categories:
  - Kubernetes
  - OS
tags:
  - Talos Linux
  - Security
  - Bare Metal
description: >-
  Descubre por qué migré mi HomeLab a Talos Linux: el sistema operativo inmutable, seguro y diseñado 100% para Kubernetes. Adiós al SSH, hola a la API.
---

# Talos Linux: El Sistema Operativo Inmutable para Kubernetes

**¿Alguna vez has roto un nodo de Kubernetes por una actualización de `apt-get` o un cambio de configuración en `/etc`?**

Yo también. Por eso migré todo mi HomeLab a [Talos Linux](https://www.talos.dev/).

En este artículo, exploraremos qué hace a Talos diferente, por qué es el futuro de la infraestructura inmutable y cómo simplificó drásticamente la gestión de mi clúster bare-metal.

<!-- more -->

## 1. ¿Qué es Talos Linux?

A diferencia de las distribuciones tradicionales (Ubuntu, Debian, CentOS), Talos Linux es un sistema operativo **diseñado exclusivamente para Kubernetes**.

### Principios Clave

* **Inmutable:** El sistema de archivos es de solo lectura. No puedes instalar paquetes, no hay `bash`, no hay `ssh`.
* **API-Driven:** Todo se configura a través de una API gRPC. Si quieres cambiar la red, el disco o el kubelet, lanzas un comando `talosctl`, no editas un archivo de texto.
* **Mínima Superficie de Ataque:** Al eliminar SSH y la shell, se eliminan clases enteras de vulnerabilidades.

## 2. La Diferencia: "Pet" vs "Cattle"

### El Viejo Mundo (Ubuntu/Debian)

En un clúster tradicional, tratamos a los nodos como "mascotas" (pets):

1. Instalamos el OS.
2. Hacemos hardening manual.
3. Instalamos dependencias (Docker/Containerd, CNI, kubeadm).
4. Mantenemos actualizaciones de paquetes con `apt upgrade`.

### El Nuevo Mundo (Talos)

En Talos, los nodos son "ganado" (cattle). La configuración se define en un archivo YAML (MachineConfig).

```yaml title="ejemplo-talos-coifg.yaml"
version: v1alpha1
machine:
  type: worker
  token: <token-secreto>
  network:
    hostname: k8s-worker-01
    interfaces:
      - interface: eth0
        dhcp: true
```

Si necesito actualizar la versión de Kubernetes, simplemente le digo a Talos que descargue la nueva imagen del sistema operativo. Si algo falla, el nodo se reinicia en la partición anterior automáticamente.

## 3. Mi Experiencia de Migración

El proceso de migración desde Ubuntu Server con K3s hacia Talos Linux fue más suave de lo que esperaba. Aquí el paso a paso real:

### Preparación

1. **Backup completo con Velero** de todos los recursos del cluster antiguo (namespaces, deployments, PVCs, secrets).
2. **Exportación de CRDs y configuraciones** de Cilium, Longhorn y Cert-Manager que no se migrarían automáticamente.
3. **Generación de MachineConfigs** con `talosctl gen config` apuntando al nuevo VIP del control plane.

### Ejecución (Ventana de 4 horas)

1. **Drené el worker-02** del cluster K3s, lo apagué, y arranqué con la ISO de Talos via PXE.
2. **Apliqué la config de worker** con `talosctl apply-config --insecure`. En ~15 segundos el nodo apareció como Ready.
3. **Repetí con worker-01** — ahora tenía 2 workers Talos hablando con el control plane K3s aún activo.
4. **Drené el control plane K3s** (el momento de verdad). Arranqué el nuevo nodo Talos como control plane.
5. **Bootstrap del cluster** con `talosctl bootstrap` y recuperación del kubeconfig.
6. **Restauración con Velero** de todos los recursos. Longhorn detectó los discos automáticamente y recreó los volúmenes.

### Lo que funcionó mejor de lo esperado

- **Velero restore fue flawless.** Todos los deployments, services e ingresses volvieron exactamente como estaban. Cero intervención manual.
- **Cilium se instaló en segundos** con el CLI. La migración de Calico (K3s default) a Cilium eBPF fue transparente para las aplicaciones.
- **Longhorn reconoció los discos** sin configuración adicional. Solo tuve que asegurarme de que los workers tuvieran un disco sin particionar (`/dev/sdb`).

### Lo que costó más

- **Cert-Manager:** Los certificados de Let's Encrypt emitidos antes de la migración quedaron inválidos porque el cluster cambió de identidad. Tuve que re-emitirlos todos (unos 15 certificados). Tiempo: ~30 minutos.
- **Actualización del kubeconfig:** Todos los CI/CD pipelines (GitLab CI, GitHub Actions) y mis estaciones locales necesitaban el nuevo kubeconfig generado por Talos.

### Métricas de la Migración

| Métrica | Valor |
|:--------|:------|
| **Downtime total** | ~45 minutos (ventana planificada de 4h) |
| **Nodos migrados** | 3 (1 control plane, 2 workers) |
| **Recursos restaurados** | 120+ (deployments, services, PVCs, secrets, ingresses) |
| **Data loss** | 0 bytes (Longhorn snapshots intactos) |
| **Certificados re-emitidos** | 15 |
| **Tiempo de bootstrap por nodo** | < 20 segundos |

La migración confirmó lo que la teoría prometía: **la infraestructura inmutable elimina el drift de configuración y hace el cluster verdaderamente reproducible.** Si tuviera que repetir la migración hoy, tomaría menos de 30 minutos.

### Desafíos Encontrados

* **Gestión de Discos:** Configurar Longhorn requirió entender cómo Talos monta los discos epímeros.
* **Sin SSH:** La primera vez que algo "falla", el instinto es querer entrar por SSH. Con Talos, aprendes a usar `talosctl dmesg` y `talosctl service`.

## 4. Beneficios en Producción (HomeLab)

| Característica | Antes (K3s sobre Ubuntu) | Ahora (Talos Linux) |
| :--- | :--- | :--- |
| **Tiempo de Boot** | ~2 minutos | < 20 segundos |
| **Actualizaciones OS** | Manual (`apt update`), riesgo de rotura | Atómica (1 comando), rollback automático |
| **Seguridad** | Depende de mi hardening | Hardening por defecto, read-only FS |
| **Gestión** | Ansible + Scripts | `talosctl` + GitOps |

## 5. Conclusión

Talos Linux ha eliminado la "fatiga de mantenimiento" de mi capa de sistema operativo. Ahora, mi OS es solo otro recurso definido en código, permitiéndome enfocarme en lo que importa: **las aplicaciones y la plataforma**.

---

### Recursos Adicionales

* [Documentación Oficial de Talos](https://www.talos.dev/v1.9/introduction/)
* [Repo de mi Infraestructura](https://github.com/palbina/HOMELAB-INFRA)
