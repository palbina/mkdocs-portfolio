# Feature Specification: Diátaxis Documentation Framework

**Feature Branch**: `002-diataxis-framework`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec)

**Input**: A complete Diátaxis documentation framework organizing all technical content into 4 quadrants: Tutorials (learning-oriented), How-To Guides (task-oriented), Reference (information-oriented), and Explanation (understanding-oriented). Each quadrant has an index page explaining the Diátaxis positioning and cross-linking to its content pages.

---

## User Scenarios & Testing

### User Story 1 - Learn Through Tutorials (Priority: P1)

A beginner or learner wants to acquire hands-on experience with the DevOps stack. They navigate to the Tutorials section and follow a step-by-step guided experience.

**Why this priority**: Tutorials are the primary learning path for new users. They transform the portfolio from a showcase into an educational resource.

**Independent Test**: Navigate to `tutorials/`. Verify the index explains Diátaxis (upper-left: action + skill acquisition). Click "HomeLab Kubernetes desde Cero" and verify it guides through hardware to functional cluster with 4 phases, prerequisites checklist, and code examples.

**Acceptance Scenarios**:

1. **Given** a user navigates to `tutorials/`, **When** the page renders, **Then** the index shows 4 tutorial cards (Kubernetes HomeLab, GitOps ArgoCD, Observability LGTM, Zero Trust Security) with descriptions and CTA links, plus a Diátaxis quadrant reference table at the bottom.
2. **Given** a user opens "HomeLab Kubernetes desde Cero", **When** the tutorial renders, **Then** the page shows: "¿Qué vas a construir?" section, Prerrequisitos checklist, 4 numbered Fase sections with code blocks, cross-link to corresponding how-to guide, and "¿Qué sigue?" section with next tutorial links.
3. **Given** a user is an experienced engineer, **When** they see the tutorial's "¿Prefieres ir directo al resultado?" admonition, **Then** they can click to navigate to the corresponding how-to guide for efficiency.

---

### User Story 2 - Solve Tasks via How-To Guides (Priority: P1)

A competent engineer needs to accomplish a specific task (deploy Talos, configure ArgoCD, set up monitoring). They use the How-To section for direct, no-explanation instructions.

**Why this priority**: How-to guides serve the primary "at-work" use case for skilled users who need productivity, not pedagogy.

**Independent Test**: Navigate to `how-to/`. Verify the index explains Diátaxis (upper-right: action + skill application). Open "Desplegar un Cluster Talos Linux" and verify it provides direct numbered steps, commands, troubleshooting tips, and cross-link to tutorial.

**Acceptance Scenarios**:

1. **Given** a user navigates to `how-to/`, **When** the page renders, **Then** the index shows 5 guide cards with descriptions, plus a Diátaxis quadrant reference table.
2. **Given** a user opens a how-to guide, **When** the guide renders, **Then** it shows minimal preamble, numbered steps with code blocks, "Comandos de Operación" section, troubleshooting tips with `!!! bug` admonitions, and a "Ver también" section cross-linking to tutorial and reference.
3. **Given** a user opens a how-to guide, **When** they see the "¿Primera vez?" admonition, **Then** they can click to navigate to the corresponding tutorial for step-by-step learning.

---

### User Story 3 - Consult Technical Reference (Priority: P2)

An engineer at work needs to look up a specific command, configuration variable, or technology stack component. They use the Reference section for neutral, factual information.

**Why this priority**: Reference material is the "cheat sheet" that supports day-to-day work. High utility but lower urgency than tutorials and how-tos.

**Independent Test**: Navigate to `reference/`. Verify the index explains Diátaxis positioning. Open "Comandos Útiles" and verify commands are organized by tool (kubectl, talosctl, cilium, argocd, etc.) in neutral code blocks. Open "Stacks Tecnológicos" and verify all technology tables with version numbers.

**Acceptance Scenarios**:

1. **Given** a user navigates to `reference/`, **When** the page renders, **Then** the index shows 3 reference cards (Stacks, Comandos, Configuración), plus Diátaxis quadrant reference table.
2. **Given** a user opens "Comandos Útiles", **When** the page renders, **Then** commands are organized by tool heading with neutral code blocks (no opinions, no narrative).
3. **Given** a user opens "Configuración de Referencia", **When** the page renders, **Then** all environment variables, sync waves, SLOs, backup frequencies, and hardware specs are presented in neutral data tables.

---

### User Story 4 - Understand Architecture Decisions (Priority: P2)

A curious engineer or architecture reviewer wants to understand WHY specific technology choices were made. They use the Explanation section for deep background and decision rationale.

**Why this priority**: Explanation provides the "why" behind the "what" and "how". Essential for architecture reviews but lower urgency than task-oriented content.

**Independent Test**: Navigate to `explanation/`. Verify the index explains Diátaxis positioning. Open "Arquitectura Cloud Native" and verify it explains the rationale for Talos Linux, Cilium eBPF, Istio Ambient. Open "Modelo Zero Trust" and verify it shows the 5-layer defense strategy with a Mermaid diagram.

**Acceptance Scenarios**:

1. **Given** a user navigates to `explanation/`, **When** the page renders, **Then** the index shows 4 explanation cards, plus Diátaxis quadrant reference table.
2. **Given** a user opens "Arquitectura Cloud Native", **When** the page renders, **Then** it follows a "problem → solution → deep dive" structure, explains WHY Talos (immutability), WHY Cilium (eBPF scaling), WHY Istio Ambient (no sidecars), and includes a complete Mermaid system diagram.
3. **Given** a user opens "Modelo Zero Trust", **When** the page renders, **Then** it explains the failure of perimeter-based security, shows the 5 independent defense layers with Mermaid diagram, and includes concrete metrics (IPs blocked/day, mTLS coverage, false positive rate).

---

### Edge Cases

- What happens when all 4 quadrant index pages are visited? Each must display its Diátaxis reference table explaining the full 2x2 grid and highlighting the current quadrant's position.
- What happens when a tutorial references a how-to that doesn't exist? Currently all 4 tutorials cross-reference their corresponding how-to guides. The mapping is 1:1 for the 4 tutorials that have how-to counterparts. Tutorials 5+ would need corresponding how-tos.
- What happens when the Diátaxis cards on the landing page link to quadrant index pages? The links are relative (`tutorials/`, `how-to/`, etc.) and depend on `navigation.indexes` being enabled in the theme config.
- How does the nav structure display on mobile? The "Documentación" nav section has nested sub-items. Material theme's mobile nav collapses sections to preserve usability.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST provide 4 documentation quadrants: Tutorials, How-To Guides, Reference, and Explanation, each in its own directory (`docs/tutorials/`, `docs/how-to/`, `docs/reference/`, `docs/explanation/`).
- **FR-002**: Each quadrant MUST have an index page (`index.md`) that explains the Diátaxis positioning with a reference table showing all 4 quadrant types.
- **FR-003**: Each quadrant index MUST contain a `grid cards` layout linking to all content pages within that quadrant.
- **FR-004**: Tutorial pages MUST follow the structure: audience info admonition → "¿Qué vas a construir?" → Prerequisites checklist → Numbered Fase sections → "¿Qué sigue?" cross-links.
- **FR-005**: How-to guide pages MUST follow the structure: optional "Primera vez?" cross-link → numbered steps without explanation → "Comandos de Operación" → Troubleshooting → "Ver también" cross-links.
- **FR-006**: Reference pages MUST present information in neutral data tables or grouped code blocks with no narrative, opinions, or instructional language.
- **FR-007**: Explanation pages MUST follow the structure: problem statement → solution reasoning → deep dive analysis → complete architecture diagram → cross-references.
- **FR-008**: All quadrant pages MUST cross-link to their counterpart pages in other quadrants (tutorial ↔ how-to, reference ↔ explanation).
- **FR-009**: The navigation configuration (`mkdocs.yml`, `zensical.toml`) MUST include the "Documentación" top-level section with all 4 quadrants as sub-sections.
- **FR-010**: The landing page MUST include a Diátaxis banner section with 4 cards linking to each quadrant index.
- **FR-011**: Tutorials quadrant MUST contain 4 tutorials: Kubernetes HomeLab, GitOps ArgoCD, Observability LGTM, Zero Trust Security.
- **FR-012**: How-To quadrant MUST contain 5 guides: Deploy Talos Cluster, Configure ArgoCD, Setup Monitoring, Backup Velero, Deploy PostgreSQL HA.
- **FR-013**: Reference quadrant MUST contain 3 pages: Tech Stacks, Useful Commands, Configuration Reference.
- **FR-014**: Explanation quadrant MUST contain 4 pages: Cloud Native Architecture, GitOps Philosophy, Zero Trust Model, Observability Patterns.

### Key Entities

- **Quadrant Index**: A page explaining Diátaxis positioning with `!!! info` definition admonition, a `grid cards` listing of content pages, and a Diátaxis reference table (type | orientation | serves).
- **Tutorial Page**: Learning-oriented document following a pedagogical structure. Assumes no prior knowledge. Prioritizes learning over productivity.
- **How-To Guide Page**: Task-oriented document for competent users. Steps without explanation. Prioritizes productivity over learning.
- **Reference Page**: Neutral technical data organized by domain. Tables and code blocks. No narrative.
- **Explanation Page**: Understanding-oriented deep dive. Problem → Solution → Rationale → Diagram. Opinionated and analytical.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 4 quadrant index pages render correctly with their grid cards and Diátaxis reference tables.
- **SC-002**: All cross-links between quadrants resolve correctly (tutorial ↔ how-to, reference ↔ explanation) with no broken links.
- **SC-003**: The "Documentación" nav section in `zensical.toml` matches the structure in `mkdocs.yml` with zero discrepancies.
- **SC-004**: Total page count across all 4 quadrants = 20 pages (4 indexes + 16 content pages).
- **SC-005**: Each quadrant's content follows the Diátaxis distinction rules: tutorials don't explain "why", how-tos don't teach, reference contains no opinions, explanation contains no step-by-step instructions.

---

## Assumptions

- The Diátaxis framework (diataxis.fr) is accepted as the organizing principle per the project constitution.
- The 4-quadrant structure is sufficient; no additional documentation types are needed for this project.
- Spanish is the primary documentation language (per constitution).
- Material for MkDocs `grid cards` feature is available in both MkDocs and Zensical builds.
- Cross-linking between quadrants uses relative Markdown links (`../tutorials/kubernetes-homelab.md`).
- The content was extracted from existing project pages and enhanced, not created from scratch.

---

## Dependencies

- Landing page (spec 001) provides the Diátaxis banner with 4 cards linking to quadrant indexes.
- Navigation configuration (`zensical.toml` nav, mirrored in `mkdocs.yml` nav for reference) defines the URL structure. The active build uses Zensical exclusively.
- Material for MkDocs features (available in both MkDocs and Zensical): `grid cards`, `admonition`, `content.tabs.link`, `navigation.indexes`.
- CSS styling (`docs/stylesheets/extra.css` lines 1444-1531) provides the Diátaxis card component styles on the landing page.
