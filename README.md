# ArkenOps Portfolio

Portfolio profesional de DevOps/SRE construido con **Zensical** (generador rápido en Rust) y el tema Material. Se trata de un sitio estático de alto rendimiento con filosofía "Docs as Code" y un diseño terminal-style minimalista inspirado en interfaces Cyber/Volt.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Zensical](https://img.shields.io/badge/Zensical-0.0.24-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

## 🚀 Qué hace este proyecto

Este repositorio contiene la configuración, infraestructura como código, documentación y blog personal del ecosistema **ArkenOps**. Su propósito es doble:

1. Actuar como una carta de presentación profesional altamente técnica que demuestre mis habilidades en Kubernetes, GitOps, Observabilidad y arquitecturas Cloud-Native de manera viva.
2. Funcionar como una base de conocimiento rigurosa para estructurar toda la configuración del **HomeLab** interno y diversos proyectos de I+D (como Inteligencia Artificial RAG o High Availability).

## 🌐 Demo

El sitio es desplegado de forma automatizada y está vivo en: **[docs.arkenops.cc](https://docs.arkenops.cc)**

## 💻 Tech Stack

- **[Static Site Generator]**: **Zensical** - Elegido por estar basado en Rust para una compilación súper rápida, permitiendo un pipeline de CI casi instantáneo frente al backend previo de Python (MkDocs).
- **[Aesthetics]**: **Material Theme Overrides** - CSS custom extendido e inyectado con variables Cyber para un feel estilo "hacker terminal", logrando un contraste preciso.
- **[Content Parsing]**: **MarkdownLint** - Utilizado para estandarizar rígidamente la documentación y aplicar consistencia transversal a lo largo de todos los logs y bitácoras del sitio.
- **[Automation]**: **GitHub Actions** - Emparejado con imágenes nativas Dockerizadas para la etapa de Build y distribución del artefacto optimizado final.

## 🛠️ Getting Started

Puedes ejecutar el proyecto directamente de forma local para contribuir a la documentación, leer el código o testear integraciones y configuraciones CSS nuevas:

```bash
# Clonar repositorio
git clone https://github.com/palbina/mkdocs-portfolio.git
cd mkdocs-portfolio

# Construir sitio e inicializar entorno (Zensical virtual env recomendado)
zensical build --clean

# Servir localmente con Hot-Reloading
zensical serve
```

Visita `http://localhost:8000` para ver las actualizaciones en tiempo real. Opcionalmente, puedes utilizar el `Dockerfile` para ejecutarlo como en producción.

## 🧠 Arquitectura y Cómo Funciona

Bajo el capó, las carpetas y estructuras principales funcionan bajo la convención *docs-as-code*:

- **`docs/`**: Todo el corazón Markdown y assets. Separado por `projects/` (arquitecturas Cloud), `blog/` (artículos cronológicos), y sobre mí.
- **`zensical.toml`**: Configuración unificada equivalente al backend, define barra de navegación, el ruteo del blog, la inyección del plugin de búsqueda, Google Analytics y anulación CSS estricto.
- **`docs/stylesheets/extra.css`**: Modificaciones avanzadas de UI para forzar la estética deseada de las pestañas en fondos oscuros vs verdes neon de material (Zensical Layout Fixes).

## 📁 Estructura Principal

```
.
├── docs/                     # Documentación fuente
│   ├── index.md              # Homepage
│   ├── about.md              # Sobre mí
│   ├── projects/             # Documentación técnica por Arquitectura
│   ├── blog/                 # Entradas de blog organizadas
│   └── stylesheets/          # CSS custom para overrides del theme
├── docs/overrides/           # Custom templates HTML para inyecciones (ej: Layouts del anuncio)
├── zensical.toml             # Configuración Root (Navegación, Branding, Metadata)
├── .github/workflows/        # Pipelines CI/CD Serverless
└── Dockerfile                # Empaquetado de producción
```

## 📖 Lecciones Aprendidas de Ingeniería

- **Migración Python a Rust**: Transicionar exitosamente de MkDocs a Zensical requirió reconstruir arquitecturas dinámicas (macros de python que controlaban fechas a base del git rev hash) en implementaciones más estáticas y estables para evadir regresiones del backend puro de Zensical.
- **Control CSS Multi-Capa**: Adaptar el `scheme=slate` nativo de material con inyecciones forzadas que permitiesen un color `primary=lime` (Verde Brillante). Decouplar los headers para que la UI no generase "melting" (falta de contraste de negro sobre oscuridad o falta sobre el verde radioactivo de la barra nativa principal).

## 📝 Licencia

MIT © 2026 Peter Albina
