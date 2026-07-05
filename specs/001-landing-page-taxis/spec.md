# Feature Specification: Landing Page & Diátaxis Banner

**Feature Branch**: `001-landing-page-diataxis`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec)

**Input**: Portfolio landing page serving as the primary entry point for visitors. Features a hero section, project showcase grid, engineering philosophy, Diátaxis documentation navigation, technology arsenal display, and call-to-action section.

---

## User Scenarios & Testing

### User Story 1 - Portfolio Discovery (Priority: P1)

A recruiter or potential employer visits the site to assess the engineer's DevOps/SRE capabilities. They scan the hero section for role/identity, browse project highlights in the card grid, and navigate to detailed project case studies.

**Why this priority**: The landing page IS the site's primary interface. Without it, visitors cannot discover the portfolio's content.

**Independent Test**: Navigate to `https://docs.arkenops.cc`. Verify the hero section displays with name, role, headline, and CTA buttons. Verify project cards render in a responsive grid. Click a project link and confirm navigation to the project detail page.

**Acceptance Scenarios**:

1. **Given** a visitor loads the homepage, **When** the page renders, **Then** the hero section displays: "DevOps Engineer" badge, "Peter Albina" name at 5rem weight 900, headline in brand-lime with glow, subtitle, and 3 CTA buttons (Explorar Proyectos, Ver Documentación, View GitHub).
2. **Given** the project cards grid is visible, **When** a visitor clicks a project card link, **Then** they navigate to the corresponding `docs/projects/<project>/` page.
3. **Given** the visitor scrolls past the hero, **When** the philosophy section becomes visible, **Then** 3 value cards display (Infraestructura Real, Open Strategy, Zero Trust) in a responsive 3-column grid.

---

### User Story 2 - Documentation Navigation (Priority: P1)

A technical visitor wants to learn from the portfolio's Diátaxis documentation (tutorials, how-to guides, reference, explanation). They use the Diátaxis banner cards on the landing page to navigate to the appropriate documentation quadrant.

**Why this priority**: The Diátaxis framework is the core organizational structure of all technical documentation. The landing page serves as the primary entry point to this content.

**Independent Test**: Locate the Diátaxis banner section below the philosophy cards. Verify 4 cards render (Tutorials, How-To, Reference, Explanation) with color-coded accent bars. Click each card's CTA button and verify navigation to the correct quadrant index page.

**Acceptance Scenarios**:

1. **Given** the Diátaxis banner section is visible on the landing page, **When** the page renders, **Then** 4 cards display with colored top accent bars: tutorials (blue), how-to (green), reference (amber), explanation (purple), each with an Material icon, title, description, and CTA button.
2. **Given** a visitor clicks a Diátaxis card's CTA button, **When** the link is followed, **Then** they land on the correct quadrant index page (e.g., `tutorials/`, `how-to/`, `reference/`, `explanation/`).
3. **Given** the viewport is mobile width (< 768px), **When** the Diátaxis grid renders, **Then** cards stack in a single column.

---

### User Story 3 - Technology Arsenal Display (Priority: P2)

A visitor wants to quickly understand the engineer's technology stack without reading full project pages. They browse the "Arsenal Tecnológico" section for categorized technology pills.

**Why this priority**: Provides at-a-glance tech stack visibility, critical for technical recruiters.

**Independent Test**: Scroll to the "Arsenal Tecnológico" section. Verify 4 category cards display (Cloud Native, Automation, Networking, Monitoring) with technology pills. Verify pills have hover effects.

**Acceptance Scenarios**:

1. **Given** the tech showcase section is visible, **When** a visitor views the page, **Then** 4 category cards display with `::before` left lime accent bars, `[ SYSTEM_OK ]` headers, and flex-wrapped technology pill badges in JetBrains Mono font.
2. **Given** a visitor hovers over a tech pill, **When** the hover state activates, **Then** the pill border changes to lime with a subtle box-shadow glow.

---

### User Story 4 - Brand Identity Display (Priority: P2)

A visitor sees the "arkenops.cc" domain concept and understands the dual meaning (Complex Code + Cloud Computing) without external explanation.

**Why this priority**: Brand identity differentiates the portfolio. The `.cc` TLD concept is unique and should be immediately understandable.

**Independent Test**: Locate the "About the Domain" section. Verify the `arkenops.cc` domain renders with lime-highlighted `.cc`. Hover over `.cc-highlight` to see the CSS tooltip explaining "Cloud Computing & Complex Code".

**Acceptance Scenarios**:

1. **Given** the domain concept section is visible, **When** the page renders, **Then** `arkenops.cc` displays with the `.cc` in brand-lime with a pulse animation, and a 2-column grid explains "Complex Code" and "Cloud Computing".
2. **Given** a visitor hovers over the `.cc-highlight`, **When** the hover triggers, **Then** a CSS pseudo-element tooltip appears showing "Cloud Computing & Complex Code".

---

### Edge Cases

- What happens when a linked project page (`projects/homelab/`) returns 404? MkDocs/Material theme handles this with its built-in 404 page.
- How does the page render when JavaScript is disabled? The page is fully static HTML/CSS; no JavaScript is required for rendering.
- How does the grid behave with only 6 project cards (vs 8 actual projects)? The CSS grid auto-fills, leaving 2 empty slots that collapse naturally. The 6-of-8 asymmetry is currently by design.
- What happens on extremely narrow viewports (< 360px)? Media queries collapse grids to single column; buttons stack vertically.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST render a hero section with name, role badge, headline, subtitle, and 3 CTA buttons on the landing page (`docs/index.md`).
- **FR-002**: System MUST hide navigation sidebar and table of contents on the landing page via frontmatter `hide: [navigation, toc]`.
- **FR-003**: System MUST display a 3-column responsive grid (`grid-template-columns: repeat(3, 1fr)`) of 6 project cards with emoji icons, impact metrics, tech tags, and navigation links.
- **FR-004**: System MUST render a 3-column philosophy section with value cards (Infraestructura Real, Open Strategy, Zero Trust).
- **FR-005**: System MUST render a 4-column Diátaxis banner grid with color-coded accent bars (tutorials=blue, how-to=green, reference=amber, explanation=purple) linking to respective quadrant indexes.
- **FR-006**: System MUST display the "arkenops.**cc**" domain concept with lime-highlighted `.cc` span, CSS pulse animation, and hover tooltip.
- **FR-007**: System MUST render 4 tech category cards with left lime accent bars, `[ SYSTEM_OK ]` status pseudo-elements, and flex-wrapped tech pill badges.
- **FR-008**: System MUST render a CTA section with lime border, glow box-shadow, centered text, and 3 buttons (Profile, LinkedIn, AI Interface).
- **FR-009**: System MUST display a subtle footer text with JetBrains Mono font showing "BUILD: AUTOMATED" and a source code link.
- **FR-010**: Card hover effects MUST include `transform: translateY(-2px)` or `scale(1.02)`, lime border color transition, and box-shadow glow.
- **FR-011**: All landing page CSS MUST be defined in `docs/stylesheets/extra.css` using CSS custom properties (`--brand-primary`, `--bg-card`, etc.).
- **FR-012**: Dark mode MUST be the default rendering (Material `scheme: slate`), with a light mode alternative activated via palette toggle.

### Key Entities

- **Landing Page** (`docs/index.md`): Single-page entry point with frontmatter hiding navigation and TOC. Contains raw HTML `<div>` blocks for precise layout.
- **Diátaxis Card**: A styled card representing one of the 4 documentation quadrants. Has a color-coded top accent bar, Material icon, heading, description, and CTA button.
- **Project Card**: A styled card in a 3-column grid representing a project case study. Has emoji icon with drop-shadow glow, impact metric callout, tech tags, and navigation link.
- **Tech Category Card**: A styled card with left lime accent pseudo-element, `[ SYSTEM_OK ]` status header, and flex-wrapped technology pill badges.
- **Value Card**: A styled card representing one of 3 engineering philosophy values.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Landing page renders correctly in all major browsers (Chrome, Firefox, Safari) with < 2s time-to-interactive on desktop and mobile.
- **SC-002**: All project card links navigate to their correct `docs/projects/<project>/` destination with zero broken links.
- **SC-003**: All 4 Diátaxis banner card CTAs navigate to the correct quadrant index pages (`tutorials/`, `how-to/`, `reference/`, `explanation/`).
- **SC-004**: Responsive layout adapts correctly at breakpoints 1024px (2 columns) and 768px (1 column) with no horizontal overflow.
- **SC-005**: Dark/light mode toggle applies correct CSS variable overrides with no visual artifacts or flash of unstyled content.
- **SC-006**: Page renders identically via both `mkdocs build` and `zensical build` within Zensical-known compatibility limits (CSS version differs: `?v=4.0` vs `?v=4.2`; missing plugins in Zensical do not affect rendering of the landing page).

---

## Assumptions

- The site is built with Material for MkDocs theme (via Zensical SSG) which handles the base HTML template, navigation, and theme infrastructure.
- CSS custom properties are supported by all target browsers (Chrome 49+, Firefox 31+, Safari 9.1+, Edge 15+).
- The visitor has a stable internet connection for font loading (Inter, JetBrains Mono via Google Fonts or bundled).
- Mermaid diagrams elsewhere on the site do not affect landing page rendering.
- The 6-of-8 project card asymmetry is intentional and not a bug.
- The `hide: [navigation, toc]` frontmatter is supported by both MkDocs Material and Zensical Material theme implementations.

---

## Dependencies

- Material for MkDocs theme (`mkdocs.yml` lines 21-78, `zensical.toml` lines 33-63) provides base template, features, and palette system.
- CSS custom properties (`extra.css` lines 9-54) define design tokens used by all landing page components.
- Navigation configuration (`mkdocs.yml` lines 83-120, `zensical.toml` lines 13-53) defines the URL structure that card links reference.
- Template overrides (`docs/overrides/main.html`) provide JSON-LD structured data and announcement banner.
- Footer partial (`docs/overrides/partials/footer.html`) provides the site-wide footer that appears on all pages including landing.
