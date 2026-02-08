---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Peter Albina

<p class="tagline">Senior DevOps/SRE Engineer • Cloud Native Specialist</p>

<div class="skills-grid" markdown>
<span class="skill-badge">Kubernetes</span>
<span class="skill-badge">Terraform</span>
<span class="skill-badge">ArgoCD</span>
<span class="skill-badge">GitOps</span>
<span class="skill-badge">Prometheus</span>
<span class="skill-badge">Istio</span>
<span class="skill-badge">Cilium</span>
<span class="skill-badge">Python</span>
<span class="skill-badge">Go</span>
</div>

<div class="hero-buttons" markdown>
[:fontawesome-brands-github: GitHub](https://github.com/palbina){ .md-button }
[:fontawesome-brands-linkedin: LinkedIn](https://linkedin.com/in/peteralbina){ .md-button }
[:material-file-document: CV](about.md){ .md-button .md-button--primary }
</div>

</div>

---

## :material-server-network: Proyectos Destacados

<div class="grid cards" markdown>

- :material-kubernetes:{ .lg .middle } **HomeLab Kubernetes**

    ---

    Cluster Kubernetes de 3 nodos bare-metal con Talos Linux, Cilium CNI (eBPF), Istio Ambient Mode y stack completo de observabilidad LGTM.

    <div class="tech-tags">
    <span class="tech-tag">Talos Linux</span>
    <span class="tech-tag">K8s 1.35</span>
    <span class="tech-tag">Cilium</span>
    <span class="tech-tag">Istio</span>
    <span class="tech-tag">ArgoCD</span>
    </div>

    [:octicons-arrow-right-24: Ver proyecto](projects/homelab.md)

- :material-git:{ .lg .middle } **GitOps con ArgoCD**

    ---

    Implementación completa de GitOps con ApplicationSets, sync waves, y patrón App-of-Apps para gestión declarativa de 30+ aplicaciones.

    <div class="tech-tags">
    <span class="tech-tag">ArgoCD</span>
    <span class="tech-tag">Helm</span>
    <span class="tech-tag">Kustomize</span>
    <span class="tech-tag">Sealed Secrets</span>
    </div>

    [:octicons-arrow-right-24: Ver proyecto](projects/gitops.md)

- :material-chart-line:{ .lg .middle } **Observabilidad LGTM**

    ---

    Stack completo de observabilidad con Loki (logs), Grafana (visualización), Tempo (traces) y Prometheus (métricas) con correlación completa.

    <div class="tech-tags">
    <span class="tech-tag">Prometheus</span>
    <span class="tech-tag">Loki</span>
    <span class="tech-tag">Tempo</span>
    <span class="tech-tag">Grafana</span>
    </div>

    [:octicons-arrow-right-24: Ver proyecto](projects/observability.md)

</div>

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

<p class="footer-text">
Última actualización: {{ build_time() }} •
<a href="https://arkenops.cc">Portfolio React</a> •
<a href="https://github.com/palbina/mkdocs-portfolio">Código fuente</a>
</p>
