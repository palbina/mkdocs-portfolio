---
hide:
  - navigation
  - toc
---

# Peter Albina { .hero-title }

**Senior DevOps/SRE Engineer • Cloud Native Specialist** { .tagline }

{{ skills_grid(['Kubernetes', 'Terraform', 'ArgoCD', 'GitOps', 'Prometheus', 'Istio', 'Cilium', 'Python', 'Go']) }}

[:fontawesome-brands-github: GitHub](https://github.com/palbina){ .md-button }
[:fontawesome-brands-linkedin: LinkedIn](https://linkedin.com/in/peteralbina){ .md-button }
[:material-file-document: CV](about.md){ .md-button .md-button--primary }

---

## :material-server-network: Proyectos Destacados

### :material-kubernetes: HomeLab Kubernetes { .project-header }

Cluster Kubernetes de 3 nodos bare-metal con Talos Linux, Cilium CNI (eBPF), Istio Ambient Mode y stack completo de observabilidad LGTM.

* Talos Linux { .tech-tag }
* K8s 1.35 { .tech-tag }
* Cilium { .tech-tag }
* Istio { .tech-tag }
* ArgoCD { .tech-tag }
* Prometheus { .tech-tag }
{ .tech-list }

[:octicons-arrow-right-24: Ver proyecto](projects/homelab.md)

---

### :material-git: GitOps con ArgoCD { .project-header }

Implementación completa de GitOps con ApplicationSets, sync waves, y patrón App-of-Apps para gestión declarativa de 30+ aplicaciones.

* ArgoCD { .tech-tag }
* Helm { .tech-tag }
* Kustomize { .tech-tag }
* Sealed Secrets { .tech-tag }
{ .tech-list }

[:octicons-arrow-right-24: Ver proyecto](projects/gitops.md)

---

### :material-chart-line: Observabilidad LGTM { .project-header }

Stack completo de observabilidad con Loki (logs), Grafana (visualización), Tempo (traces) y Prometheus (métricas) con correlación completa.

* Prometheus { .tech-tag }
* Loki { .tech-tag }
* Tempo { .tech-tag }
* Grafana { .tech-tag }
* Alertmanager { .tech-tag }
{ .tech-list }

[:octicons-arrow-right-24: Ver proyecto](projects/observability.md)

---

## :material-tools: Enfoque Técnico

!!! quote "Filosofía"
    **"Everything as Code"** - Infraestructura, configuración, políticas y documentación
    gestionadas como código, versionadas en Git, y aplicadas automáticamente.

| Área | Herramientas |
|:-----|:-------------|
| **Contenedores** | Kubernetes, Docker, containerd, Helm |
| **GitOps/CI-CD** | ArgoCD, GitHub Actions, Forgejo Actions |
| **Networking** | Istio, Cilium, Traefik, Cloudflare |
| **Observabilidad** | Prometheus, Grafana, Loki, Tempo |
| **IaC** | Terraform, Ansible, Talos machineconfig |
| **Seguridad** | CrowdSec, Authentik, Sealed Secrets, mTLS |

---

Última actualización: {{ build_time() }} •
[:material-react: Portfolio React](https://arkenops.cc) •
[:fontawesome-brands-github: Código fuente](https://github.com/palbina/mkdocs-portfolio)
{ .footer-text }
