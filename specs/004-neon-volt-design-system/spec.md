# Feature Specification: Neon Volt Design System

**Feature Branch**: `004-neon-volt-design`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec)

**Input**: A complete CSS design system ("Neon Volt - SRE Edition") providing the visual identity for the ArkenOps portfolio. Built on CSS custom properties, Material for MkDocs theme overrides, and custom component classes. Defined in `docs/stylesheets/extra.css` (1442 lines) with design documentation in `DESIGN.md`.

---

## User Scenarios & Testing

### User Story 1 - Visual Identity Consistency (Priority: P1)

A visitor navigates the portfolio and experiences a consistent visual language: Electric Lime (#CCFF00) as the primary brand color, deep dark backgrounds (#050505), JetBrains Mono for data/code, Inter for body text. Every component uses the same design tokens.

**Why this priority**: Visual consistency is the foundation of professional presentation. Without it, the portfolio appears amateur regardless of content quality.

**Independent Test**: Verify all pages use the same `--brand-primary: #CCFF00` via CSS custom properties. Check that all headings use Inter font, all code/data uses JetBrains Mono. Verify dark mode is the default.

**Acceptance Scenarios**:

1. **Given** the site loads in dark mode (slate scheme), **When** any page renders, **Then** the background is deep obsidian (#050505), text is titanium (#F0F0F0), and brand elements use electric lime (#CCFF00) per the `:root` CSS custom properties.
2. **Given** the user toggles to light mode, **When** the `[data-md-color-scheme="default"]` selector activates, **Then** CSS variables remap to darker lime (#6a8a1a), lighter backgrounds (#F5F5F5), and all component styles adapt via the light mode override block.
3. **Given** any page contains code blocks, **When** the code renders, **Then** it uses JetBrains Mono font across all platforms.

---

### User Story 2 - Component Library Usage (Priority: P1)

A contributor wants to add new content that matches the existing visual style. They use the documented component classes (`.project-card`, `.tech-item`, `.diataxis-card`, etc.) defined in `DESIGN.md` and `extra.css`.

**Why this priority**: The component library enables consistent content creation without requiring deep CSS knowledge.

**Independent Test**: Create a test page using documented component classes. Verify the rendered output matches existing pages in style. Verify hover effects, responsive behavior, and dark/light mode adaptation work correctly.

**Acceptance Scenarios**:

1. **Given** a contributor uses `.project-card` class on a div, **When** the page renders, **Then** the card has: 3-column grid placement, hover scale(1.02) + lime border + glow, and responsive collapse at 1024px and 768px breakpoints.
2. **Given** a contributor uses `!!! impact` admonition, **When** the page renders, **Then** the custom admonition renders with 8px lime left border, rgba lime background, and glow box-shadow.
3. **Given** a contributor creates a data table, **When** the table renders, **Then** the first column uses JetBrains Mono brand-lime bold styling (identity column), headers use uppercase JetBrains Mono text, and mobile viewports get horizontal scroll.

---

### User Story 3 - Dark/Light Mode Adaptation (Priority: P2)

A user prefers light mode and toggles the theme. All pages adapt seamlessly without visual artifacts, flash, or broken component styles.

**Why this priority**: Accessibility and user preference. Some users require light themes for readability or work environment constraints.

**Independent Test**: Toggle between dark and light modes on multiple pages. Verify all components adapt: cards, buttons, admonitions, tables, tabs, code blocks, headers, footer. Verify no flash of unstyled content (FOUC) during toggle.

**Acceptance Scenarios**:

1. **Given** the user is in dark mode, **When** they click the "Cambiar a modo claro" toggle, **Then** the Material palette switches to `scheme: default` and all `[data-md-color-scheme="default"]` CSS overrides activate without page reload.
2. **Given** the user is in light mode viewing the header, **When** the header renders, **Then** the lime header background uses the light variant (#6a8a1a) with appropriate text contrast.

---

### Edge Cases

- What happens when CSS custom properties are not supported (IE11)? The site fails gracefully — Material theme falls back to its default colors. IE11 is not a supported browser.
- What happens with very long content in a `.project-card`? Cards have `min-height` defined by content. No overflow protection is needed as card content is constrained by template.
- What happens when both MkDocs and Zensical render the same CSS? Zensical-specific fixes (`.md-source__repository` hidden, search text hidden) are applied via `!important`. No known conflicts.
- What happens at extreme browser zoom levels (200%+)? Flexbox and grid layouts reflow naturally. No fixed pixel widths used in key layouts.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST define all design tokens as CSS custom properties on `:root` in `docs/stylesheets/extra.css`: brand colors (`--brand-primary`, `--brand-secondary`, `--brand-glow`), background colors (`--bg-dark`, `--bg-surface`, `--bg-card`), text colors (`--text-primary`, `--text-secondary`, `--text-muted`), and border colors (`--border-subtle`, `--border-default`, `--border-accent`).
- **FR-002**: System MUST provide a complete `[data-md-color-scheme="default"]` override block remapping all CSS custom properties for light mode compatibility.
- **FR-003**: System MUST define 2 Material palette schemes (`slate` dark mode default, `default` light mode) in both `mkdocs.yml` and `zensical.toml`.
- **FR-004**: System MUST use Inter font family for body text and JetBrains Mono for code/data content, configured in `mkdocs.yml` and `zensical.toml`.
- **FR-005**: System MUST provide the `!!! impact` custom admonition style (8px lime left border, rgba background, glow box-shadow) via `.admonition.impact` CSS rules.
- **FR-006**: System MUST style data tables with: lime header backgrounds, JetBrains Mono uppercase header text, identity column (first column brand-lime bold monospace), row hover highlight `rgba(204,255,0,0.02)`, and mobile horizontal scroll (`overflow-x: auto`).
- **FR-007**: System MUST style Mermaid diagrams with: `#080808` background, subtle border, 2rem padding, no border-radius, and inset box-shadow.
- **FR-008**: System MUST style content tabs with: transparent label background, JetBrains Mono labels, muted default color, lime underline and subtle background on active tab.
- **FR-009**: System MUST define z-index layer hierarchy: content elements at 10, header at 100, overlay at 200, sidebar/drawer at 300.
- **FR-010**: System MUST provide Zensical-specific layout fixes (documented in `docs/MIGRATION-ZENSICAL.md`): header text contrast (`color: rgba(0,0,0,0.7) !important`), active tab solid black 900-weight, sidebar active link brand-lime, repo name hidden (`display: none` on `.md-source__repository`), and un-styled search text hidden. These fixes compensate for rendering differences between Zensical's Rust-based Material theme implementation and the Python MkDocs original.
- **FR-011**: System MUST define the ArkenOps brand identity: `.arkenops-domain` styled element, `.cc-highlight` in lime with CSS `@keyframes cc-pulse` animation, and hover tooltip via `::after` pseudo-element.
- **FR-012**: System MUST document the complete design system in `DESIGN.md` covering: visual philosophy, color palette rules, typography rules, component specs, and layout principles.
- **FR-013**: All component hover states MUST include transition animations (0.2s-0.25s ease) for border color, background, transform, and box-shadow changes.

### Key Entities

- **CSS Custom Property**: A design token defined on `:root` and `[data-md-color-scheme="default"]` that maps to Material theme variables (`--md-default-bg-color`, etc.) and custom component styles.
- **Material Palette Scheme**: A theme variant (slate or default) with primary/accent color, toggle icon, and toggle name. Configured in mkdocs.yml / zensical.toml.
- **Zensical Fix**: An `!important` CSS override specifically required because the Zensical Rust SSG renders the Material theme differently from MkDocs Python SSG.
- **Design Document** (`DESIGN.md`): Reference document for the complete design system. Serves as the spec for visual contributors.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 23 Material theme features (navigation.instant, search.suggest, etc.) work correctly with the custom CSS applied.
- **SC-002**: Zero visual regressions when switching between dark and light modes on any page.
- **SC-003**: CSS file size is < 50KB uncompressed (currently ~1442 lines).
- **SC-004**: All 8 project pages, 4 tutorial pages, 5 how-to pages, 3 reference pages, 4 explanation pages, landing page, about page, and blog render with consistent Neon Volt styling.
- **SC-005**: Lighthouse accessibility score >= 90 with the custom theme applied.
- **SC-006**: Zero layout breakage on mobile viewports (360px - 768px wide).

---

## Assumptions

- Material for MkDocs theme v9.5+ is available via both MkDocs and Zensical builds.
- CSS custom properties are natively supported by all target browsers (no polyfill needed).
- Google Fonts (Inter, JetBrains Mono) are available at build time or fallback to system monospace/sans-serif.
- The `custom_dir: docs/overrides` points to valid Jinja2 template overrides.
- Zensical compatibility workarounds are maintained as the SSG evolves.

---

## Dependencies

- Material for MkDocs theme provides the base HTML structure, palette system, and feature set. The project builds primarily with **Zensical SSG** (Rust), not MkDocs (Python), but both engines consume the same Material theme and custom CSS.
- `mkdocs.yml` is retained as reference configuration; `zensical.toml` is the active build config used by CI/CD.
- Jinja2 template overrides (`docs/overrides/main.html`, `docs/overrides/partials/footer.html`) are interpreted by Zensical's Tera template engine (not Python Jinja2).
- Google Fonts CDN or local font files for Inter and JetBrains Mono.
- The `DESIGN.md` document serves as the human-readable reference for the CSS implementation.
- Zensical-specific CSS workarounds (header contrast, hidden repo/search text) compensate for rendering differences between the Rust and Python Material theme implementations.
