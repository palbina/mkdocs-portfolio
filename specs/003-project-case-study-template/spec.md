# Feature Specification: Project Case Study Template

**Feature Branch**: `003-project-template`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec)

**Input**: A standardized template and CSS component system for 8 DevOps project case study pages. Each project page documents a complete implementation with architecture diagrams, technology stacks, implementation phases, operational commands, monitoring configuration, and results. The template is defined in `TEMPLATE-PROJECT.md` and enforced across all 8 projects.

---

## User Scenarios & Testing

### User Story 1 - Create a New Project Page (Priority: P1)

A contributor wants to add a new DevOps project to the portfolio. They use the project template to generate a page that follows the established structure, ensuring consistency with existing projects.

**Why this priority**: The template is the contract that ensures all 8 project pages maintain structural consistency. Without it, each project would have arbitrary format.

**Independent Test**: Copy `TEMPLATE-PROJECT.md` to `docs/projects/nuevo-proyecto.md`, fill in each section. Verify the page renders correctly with `zensical build`. Verify all 14 sections are present and styled correctly.

**Acceptance Scenarios**:

1. **Given** a contributor creates a new project page from the template, **When** the page is built with Zensical, **Then** the project header renders with h1 title, subtitle, and 4-column meta-grid (Status, Environment, Category, Uptime) in JetBrains Mono lime values.
2. **Given** the template's "Visión General" section is filled, **When** the page renders, **Then** the `!!! impact` custom admonition displays with lime left border, rgba background, and glow box-shadow.
3. **Given** the template's "Arquitectura" section is filled, **When** the page renders, **Then** a Mermaid diagram renders with dark background (#080808), 2rem padding, and `!!! info` component breakdown admonition.

---

### User Story 2 - Browse a Project Case Study (Priority: P1)

A visitor navigates to a project page to assess the engineer's implementation quality. They scan the header for metadata, review the architecture diagram, check the technology stack, and evaluate results with metrics.

**Why this priority**: Project pages are the core content of the portfolio. Each one represents a complete DevOps competency demonstration.

**Independent Test**: Navigate to any of the 8 project pages (e.g., `projects/homelab/`). Verify all 14 sections render in order: header → overview → architecture → stack → implementation → config → operations → monitoring → results → roadmap → references → quote.

**Acceptance Scenarios**:

1. **Given** a visitor opens a project page, **When** the page renders, **Then** the project-header displays as a "cyber report dossier" with bottom lime border and 4 meta items in a responsive grid (`repeat(auto-fit, minmax(150px, 1fr))`).
2. **Given** the visitor scrolls to "Stack Tecnológico", **When** the content tabs render, **Then** tab labels use JetBrains Mono font with the active tab underlined in lime and a subtle lime background.
3. **Given** the visitor scrolls to "Operaciones", **When** the "Comandos Útiles" code block renders, **Then** commands are formatted in a code fence with syntax highlighting.

---

### User Story 3 - Reference Operations and Troubleshooting (Priority: P2)

An engineer deploying a similar setup needs operational commands and troubleshooting guidance. They navigate to the "Operaciones" section of a project page.

**Why this priority**: Operational content is the most practical value for engineers replicating the setup. It bridges the gap between "what was built" and "how to maintain it."

**Independent Test**: Open any project page (e.g., `projects/security/`), scroll to "Operaciones" → "Comandos Útiles" and "Troubleshooting". Verify commands are copy-paste ready and troubleshooting tips follow the standard format.

**Acceptance Scenarios**:

1. **Given** the "Comandos Útiles" section, **When** it renders, **Then** commands are grouped in a bash code fence, properly escaped for MkDocs/Material rendering.
2. **Given** a troubleshooting tip (`!!! tip`), **When** it renders, **Then** it shows "Síntoma:" description, "Solución:" with validation steps, formatted as a Material admonition.

---

### Edge Cases

- What happens when a project page has an empty section? The section heading renders but the content area is empty. This is acceptable per the template; not all projects need all sections (e.g., not all projects have configuration tables).
- What happens when a mermaid diagram fails to render? Material theme falls back to showing the raw mermaid code in a code block. No JavaScript error propagation.
- What happens when a project page's frontmatter lacks required fields (`title`, `description`)? MkDocs/Zensical build may fail or produce pages with missing SEO metadata. The template documents these as mandatory.
- What happens with very long technology stack tables on mobile? CSS table styles include `overflow-x: auto` for horizontal scroll on mobile viewports.

---

## Requirements

### Functional Requirements

- **FR-001**: Every project page MUST include YAML frontmatter with `title` and `description` fields.
- **FR-002**: Project pages MUST render a `project-header` div with: `<h1>` title, `<p>` subtitle, and `project-meta-grid` div containing 4 `meta-item` divs (Status, Environment, Category/Engine, Uptime/Target).
- **FR-003**: Project pages MUST include a "Visión General" section with a `!!! impact` custom admonition containing key metrics.
- **FR-004**: Project pages MUST include an "Arquitectura" section with a Mermaid diagram in a fenced code block (` ```mermaid `) and a `!!! info` component breakdown.
- **FR-005**: Project pages MUST include a "Stack Tecnológico" section using Material content tabs (`=== "Tab Name"`) with data tables.
- **FR-006**: Project pages MUST include an "Implementación" section with 3 phases, each using `!!! example` admonitions containing code blocks (bash or yaml).
- **FR-007**: Project pages MUST include a "Configuración" section with an environment variables table and optional additional configuration content.
- **FR-008**: Project pages MUST include an "Operaciones" section with "Comandos Útiles" code block and at least 2 troubleshooting `!!! tip` admonitions.
- **FR-009**: Project pages MUST include a "Monitoreo" section with a metrics table (metric, threshold, alert columns), dashboards list, and alert conditions.
- **FR-010**: Project pages MUST include a "Resultados" section with a success metrics table (metric, objective, actual, status) and a "Lecciones Aprendidas" `!!! info` admonition.
- **FR-011**: Project pages MUST include a "Roadmap" section with a markdown checkbox task list (`- [x]`, `- [ ]`).
- **FR-012**: Project pages MUST include a "Referencias" section with links to GitHub repo and official documentation.
- **FR-013**: Project pages MUST close with a `!!! quote` philosophy admonition and a last-updated footer.
- **FR-014**: The `TEMPLATE-PROJECT.md` file MUST document all 14 sections with Spanish-language comments explaining what each section is for.

### Key Entities

- **Project Page**: A Markdown file in `docs/projects/` following the 14-section template contract. Defines a single DevOps case study.
- **Project Header**: A styled div block (`project-header`) with h1, subtitle, and 4-column meta-grid. Styled as a cyber report dossier.
- **Meta Item**: A flex-column element inside `project-meta-grid` containing a `.meta-label` (uppercase muted text) and `.meta-value` (JetBrains Mono, brand-lime).
- **Impact Admonition**: A custom Material admonition type (`!!! impact`) with green tint, 8px lime left border, and glow box-shadow. Not a standard Material admonition type.
- **Content Tab**: A Material content tabs section (`=== "Label"`) with JetBrains Mono labels, lime active indicator, and data tables.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 8 existing project pages follow the template contract with all 14 sections present and correctly structured.
- **SC-002**: A new project page created from `TEMPLATE-PROJECT.md` renders identically to existing project pages in both structure and styling.
- **SC-003**: Mermaid diagrams render correctly on all 8 project pages with the custom dark styling (`#080808` background, border, 2rem padding).
- **SC-004**: Content tabs activate and deactivate correctly with JetBrains Mono styling in both dark and light modes.
- **SC-005**: Data tables render correctly on mobile viewports (< 768px) with horizontal scroll and identity column (first column) in brand-lime monospace.
- **SC-006**: Zero broken internal links between project pages and their cross-referenced documentation pages.

---

## Assumptions

- All project pages are written in Spanish with technical terms in English where appropriate per constitution.
- Mermaid rendering is handled by Material for MkDocs + pymdownx.superfences with the mermaid custom fence.
- The `!!! impact` admonition is a custom type defined only in `extra.css` — it's not a built-in Material type.
- Project pages assume the reader has access to a Kubernetes cluster and basic DevOps tooling (kubectl, helm).
- Code examples are illustrative of the implementation approach, not necessarily copy-paste production-ready.

---

## Dependencies

- Neon Volt Design System (spec 004) provides all CSS styling for project-header, meta-grid, impact admonition, Mermaid, tabs, and tables.
- Material for MkDocs features: `content.tabs.link`, `admonition`, `pymdownx.superfences` (mermaid), `pymdownx.tabbed`, `tables`.
- Navigation configuration defines the project pages' URLs in the "Proyectos" section.
- The Diátaxis framework (spec 002) provides cross-linked tutorials, how-tos, reference, and explanations that project pages reference.
