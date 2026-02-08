---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Peter Albina

<p class="tagline">Senior DevOps/SRE Engineer • Cloud Native Specialist</p>

<div class="skills-grid">
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

<div class="hero-buttons">
<a href="https://github.com/palbina" class="md-button">
:fontawesome-brands-github: GitHub
</a>
<a href="https://linkedin.com/in/peteralbina" class="md-button">
:fontawesome-brands-linkedin: LinkedIn
</a>
<a href="about/" class="md-button md-button--primary">
:material-file-document: CV
</a>
</div>

</div>

---

## :material-server-network: Proyectos Destacados

<div class="projects-grid">

<div class="project-card">
<h3>:material-kubernetes: HomeLab Kubernetes</h3>
<p>Cluster Kubernetes de 3 nodos bare-metal con Talos Linux, Cilium CNI (eBPF), Istio Ambient Mode y stack completo de observabilidad LGTM.</p>
<div class="tech-tags">
<span class="tech-tag">Talos Linux</span>
<span class="tech-tag">K8s 1.35</span>
<span class="tech-tag">Cilium</span>
<span class="tech-tag">Istio</span>
<span class="tech-tag">ArgoCD</span>
</div>
<a href="projects/homelab/" class="project-link">Ver proyecto →</a>
</div>

<div class="project-card">
<h3>:material-git: GitOps con ArgoCD</h3>
<p>Implementación completa de GitOps con ApplicationSets, sync waves, y patrón App-of-Apps para gestión declarativa de 30+ aplicaciones.</p>
<div class="tech-tags">
<span class="tech-tag">ArgoCD</span>
<span class="tech-tag">Helm</span>
<span class="tech-tag">Kustomize</span>
<span class="tech-tag">Sealed Secrets</span>
</div>
<a href="projects/gitops/" class="project-link">Ver proyecto →</a>
</div>

<div class="project-card">
<h3>:material-chart-line: Observabilidad LGTM</h3>
<p>Stack completo de observabilidad con Loki (logs), Grafana (visualización), Tempo (traces) y Prometheus (métricas) con correlación completa.</p>
<div class="tech-tags">
<span class="tech-tag">Prometheus</span>
<span class="tech-tag">Loki</span>
<span class="tech-tag">Tempo</span>
<span class="tech-tag">Grafana</span>
</div>
<a href="projects/observability/" class="project-link">Ver proyecto →</a>
</div>

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
