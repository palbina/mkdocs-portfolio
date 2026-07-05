# Zensical Migration Roadmap (Completed)

Este documento detalla el progreso y los pasos completados para la migración de este portafolio desde MkDocs a [Zensical](https://zensical.org/).

## Estado Actual

- **Zensical instalado y configurado**: Se reemplazó el uso de MkDocs por Zensical v0.0.46.
- **mkdocs.yml retenido como referencia**: La configuración canónica es `zensical.toml`. `mkdocs.yml` existe como documentación histórica con header de advertencia.
- **Compatibilidad de Markdown resuelta**: Las incompatibilidades de los plugins (como las macros de Python) fueron solucionadas insertando contenido estático.
- **CI/CD adaptado**: El build usa `zensical build --clean` exclusivamente.

## Limitaciones Conocidas de Zensical

### Tablas dentro de Content Tabs (`===`)

**Problema**: Zensical v0.0.46 no renderiza tablas Markdown dentro de bloques `===` (content tabs de `pymdownx.tabbed`). El renderer genera la estructura `<table>` con celdas vacías y emite el contenido como `<p>` fuera de la tabla.

**Síntoma**: Texto con pipes (`|`) visible fuera de los componentes de tabla.

**Workaround**: Convertir content tabs a headings H3 estándar y de-indentar el contenido:

```markdown
# ❌ No funciona en Zensical
=== "Título"

    | Col 1 | Col 2 |
    |-------|-------|
    | Data  | Data  |

# ✅ Alternativa compatible
### Título

| Col 1 | Col 2 |
|-------|-------|
| Data  | Data  |
```

**Archivos afectados**: 17 archivos en `docs/projects/`, `docs/reference/`, y `docs/explanation/` fueron convertidos (2026-07-05).

### CSS: Tablas con Scroll Horizontal

**Problema**: Tablas anchas desbordan el contenedor en pantallas pequeñas.

**Solución**: Reglas en `docs/stylesheets/extra.css`:

```css
.md-typeset__table {
    display: block;
    max-width: 100%;
    overflow-x: auto;
}

.md-typeset table:not([class]) {
    display: table !important;   /* Anula inline-block del theme */
    overflow: visible !important;
    width: max-content;
    min-width: 100%;
}
```

## Tareas Completadas

1. **Plugins de Python eliminados**: Se eliminó `scripts/main.py`. Zensical (Rust) genera el contenido directamente.
2. **Motor de Plantillas**: Las configuraciones de diseño (overrides y palette) se portaron a `zensical.toml`.
3. **Content tabs → headings**: 11 páginas de proyecto migradas de `===` tabs a `###` headings por incompatibilidad con tablas.
4. **Zensical.toml finalizado**: Se trasladaron todas las secciones (nav, extra, theme, features).

## Instrucciones para Build

```bash
# Build limpio (utilizado en el Dockerfile)
zensical build --clean

# Servir localmente
zensical serve --dev-addr localhost:8002
```

### Última actualización: 2026-07-05
