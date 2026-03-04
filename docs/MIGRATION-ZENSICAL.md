# Zensical Migration Roadmap (Completed)

Este documento detalla el progreso y los pasos completados para la migración de este portafolio desde MkDocs a [Zensical](https://zensical.org/).

## Estado Actual

- **Zensical instalado y configurado**: Se reemplazó el uso de MkDocs por Zensical v0.0.24.
- **mkdocs.yml eliminado**: Se reemplazó por completo con `zensical.toml`.
- **Compatibilidad de Markdown resolta**: Las incompatibilidades de los plugins (como las macros de Python) fueron solucionadas insertando contenido estático, logrando builds más limpios y rápidos.
- **Linting de Markdown ajustado**: Se añadió `.markdownlint.json` para definir reglas de compatibilidad con las especificaciones de MkDocs Material bajo Zensical.
- **CI/CD adaptado**: El build en Docker ahora usa `zensical build` exclusivamente, logrando mayor velocidad y mitigando problemas de compatibilidad.

## Tareas Completadas

1. **Plugins de Python eliminados**: Se eliminó `scripts/main.py`. Zensical (escrito en Rust) genera el contenido directamente mucho más rápido.
2. **Motor de Plantillas**: Las configuraciones de diseño (overrides y palette) se portaron a `zensical.toml`.
3. **Escapado de Macros**: Las variables de Kubernetes/ArgoCD se mantienen funcionales.
4. **Zensical.toml finalizado**: Se trasladaron todas las secciones (nav, extra, theme, features).

## Instrucciones para Build (Zensical)

El proceso de build está estandarizado y sin dependencias de Python innecesarias a nivel de SSG.

```bash
# Build limpio (utilizado en el Dockerfile)
zensical build --clean
```

### Última actualización: 2026-03-03
