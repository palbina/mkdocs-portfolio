# MkDocs Portfolio

Portfolio profesional de DevOps/SRE construido con MkDocs y Material theme. Sitio estático de alto rendimiento con filosofía "Docs as Code" y diseño terminal-style minimalista.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![MkDocs](https://img.shields.io/badge/MkDocs-1.6+-blue)
![Material](https://img.shields.io/badge/Material-9.5+-purple)

---

## Quick Start

```bash
# Clonar repositorio
git clone https://github.com/palbina/mkdocs-portfolio.git
cd mkdocs-portfolio

# Instalar dependencias
pip install -r requirements.txt

# Servir localmente
zensical serve

# Construir sitio
zensical build
```

Visita `http://localhost:8000` para ver el sitio.

---

## Features

- **Diseño Terminal-Style**: Estética minimalista con acentos neon volt
- **Material for MkDocs**: Tema moderno con dark/light mode
- **Docs as Code**: Documentación versionada en Git
- **SEO Optimizado**: Meta tags, sitemap, robots.txt automáticos
- **Alto Rendimiento**: Minificación HTML/CSS/JS, lazy loading
- **Responsive**: Optimizado para todos los dispositivos
- **Search Integrado**: Búsqueda en tiempo real con lunr.js
- **Mermaid Diagrams**: Diagramas de arquitectura embebidos

---

## Configuration

### Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `SITE_URL` | URL del sitio | `https://docs.arkenops.cc` |
| `GOOGLE_ANALYTICS` | ID de GA | `G-XXXXXXXXXX` |

### Estructura de Archivos

```
.
├── docs/                     # Documentación fuente
│   ├── index.md             # Homepage
│   ├── about.md             # Sobre mí
│   ├── projects/            # Proyectos
│   │   ├── index.md
│   │   ├── homelab.md
│   │   └── ...
│   ├── blog/                # Blog posts
│   ├── stylesheets/         # CSS custom
│   └── javascripts/         # JS custom
├── docs/overrides/          # Templates overrides
├── scripts/                 # Macros y utilidades
├── mkdocs.yml              # Configuración MkDocs
└── requirements.txt        # Dependencias Python
```

---

## Documentation

- [Arquitectura](./docs/architecture.md)
- [Guía de Contribución](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)

---

## Deployment

### GitHub Pages (Automático)

El sitio se despliega automáticamente via GitHub Actions en cada push a `main`.

### Docker Local

```bash
# Construir imagen
docker build -t mkdocs-portfolio .

# Ejecutar
docker run -p 8080:80 mkdocs-portfolio
```

### Kubernetes

```bash
kubectl apply -f k8s/
```

---

## Tech Stack

| Componente | Tecnología |
|:-----------|:-----------|
| **Static Site** | MkDocs + Material |
| **Hosting** | GitHub Pages |
| **CI/CD** | GitHub Actions |
| **Container** | Docker + Nginx |
| **CDN** | Cloudflare |

---

## License

MIT © 2026 Peter Albina
