# Feature Specification: Blog System

**Feature Branch**: `006-blog-system`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec) — Underpopulated

**Input**: A technical blog system integrated into the portfolio using Material for MkDocs' blog plugin. Supports categorized technical posts with authors, tags, archives, and a standardized template for content creation.

---

## User Scenarios & Testing

### User Story 1 - Publish a Technical Blog Post (Priority: P1)

An author writes a technical article about a DevOps topic and publishes it to the portfolio blog. The post appears in the blog index with correct metadata (date, author, categories, tags).

**Why this priority**: The blog is the primary mechanism for sharing technical insights beyond project documentation. Without publishing capability, the blog system is useless.

**Independent Test**: Create a new post following the `YYYY-MM-DD-slug.md` naming convention with proper frontmatter. Run `zensical build`. Verify the post appears in the blog index with its excerpt, date, author, and category links.

**Acceptance Scenarios**:

1. **Given** a new Markdown file is created at `docs/blog/posts/2026-07-15-nuevo-post.md` with frontmatter (date, authors, categories, tags), **When** the site builds, **Then** the post appears in `blog/index.md` with its `<!-- more -->` excerpt, publication date, author name with avatar, and clickable category/tag links.
2. **Given** the post's frontmatter includes `draft: true`, **When** the site builds, **Then** the post is excluded from the published blog index but still accessible directly if the URL is known (default Material blog plugin behavior).

---

### User Story 2 - Browse Blog by Category (Priority: P2)

A visitor wants to find all posts about Kubernetes. They navigate to the blog and filter by the "Kubernetes" category.

**Why this priority**: Category navigation is core blog functionality but lower priority than publishing capability.

**Independent Test**: Configure at least 2 posts with different categories. Build the site. Verify the blog index renders category links. Click a category link and verify only posts with that category are shown. Verify the archive page lists posts by year.

**Acceptance Scenarios**:

1. **Given** the blog plugin is configured with `categories: true`, **When** a visitor opens the blog index, **Then** category links are rendered and clickable.
2. **Given** the blog plugin is configured with `archive: true`, **When** a visitor views the archive, **Then** posts are grouped by year.

---

### User Story 3 - Consistent Post Structure (Priority: P2)

The author uses the `TEMPLATE-BLOG-POST.md` to ensure every post follows a consistent structure (Problem → Solution → Architecture → Implementation → Production Experience → Decision Framework → Conclusion).

**Why this priority**: Template enforcement ensures the blog maintains professional quality. Without it, posts would have arbitrary structure.

**Independent Test**: Copy `TEMPLATE-BLOG-POST.md` to a new post file. Fill in each section. Verify the rendered post follows the structure: "El Problema", "La Solución", "Arquitectura" (Mermaid), "Implementación Paso a Paso", "Mi Experiencia en Producción" (metrics table), "Desafíos Encontrados", "Cuándo Usar (y Cuándo No)" (tabbed), "Conclusión", "Recursos".

**Acceptance Scenarios**:

1. **Given** a post follows the template, **When** it renders, **Then** the "El Problema" section explains the motivation, "La Solución" presents the approach, and "Arquitectura" includes a Mermaid diagram.
2. **Given** the "Mi Experiencia en Producción" section is filled, **When** it renders, **Then** it includes a real metrics table with metric/valor/benchmark columns differentiated by green checkmarks or orange warnings.
3. **Given** the "Cuándo Usar (y Cuándo No)" section is filled, **When** it renders, **Then** it uses Material content tabs with "Ideal Para" and "No Recomendado Para" tabs providing decision guidance.

---

### Edge Cases

- What happens when a post has no `<!-- more -->` excerpt delimiter? The blog plugin shows the full post content in the index listing.
- What happens when an author avatar URL is broken? The blog plugin falls back to a default avatar or shows the author name without an image.
- What happens when a post date is in the future? The blog plugin may exclude it or show it as "upcoming" depending on configuration.
- What happens when categories have spaces or special characters? Material blog plugin handles URL-encoding of category names in navigation links.
- What happens with zero posts? The blog index renders empty with a message or the grid cards layout collapses gracefully.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST use the Material for MkDocs `blog` plugin configured in both `mkdocs.yml` and `zensical.toml` with: `blog_dir: blog`, `post_dir: "{blog}/posts"`, `archive: true`, `categories: true`, `authors: true`.
- **FR-002**: Blog posts MUST follow the naming convention `YYYY-MM-DD-slug.md` and reside in `docs/blog/posts/`.
- **FR-003**: Blog posts MUST include YAML frontmatter with: `date` (ISO format), `authors` (referencing `.authors.yml`), `categories` (list), `tags` (optional list), `description` (SEO), and optional fields: `draft`, `pin`, `readtime`, `slug`.
- **FR-004**: The blog index (`docs/blog/index.md`) MUST display posts using Material `grid cards` layout.
- **FR-005**: The `<!-- more -->` HTML comment MUST delimit the post excerpt displayed on the index page.
- **FR-006**: Author metadata MUST be configured in `docs/blog/.authors.yml` with: `name`, `description`, `avatar` (URL), and `url` (GitHub/social link).
- **FR-007**: The blog template (`TEMPLATE-BLOG-POST.md`) MUST define a standardized 10-section structure: El Problema, La Solución, Arquitectura (Mermaid), Implementación Paso a Paso, Mi Experiencia en Producción (metrics), Desafíos Encontrados, Cuándo Usar (tabs), Conclusión, Recursos.
- **FR-008**: The template MUST include Spanish-language instructional comments (`# Comentario`) guiding authors on what to fill in each section.
- **FR-009**: The "Mi Experiencia en Producción" section MUST include a real metrics table (| Métrica | Valor | Benchmark |) with green/orange status indicators.
- **FR-010**: The "Cuándo Usar (y Cuándo No)" section MUST use Material content tabs (`=== "Ideal Para"` / `=== "No Recomendado Para"`).
- **FR-011**: The blog MUST be accessible from the main navigation under "Blog" in both `mkdocs.yml` and `zensical.toml`.

### Key Entities

- **Blog Post**: A Markdown file in `docs/blog/posts/` following `YYYY-MM-DD-slug.md` naming with mandatory frontmatter and optional `<!-- more -->` excerpt delimiter.
- **Author** (`.authors.yml`): A named entity with avatar URL, description, and social link. Referenced by the `authors` frontmatter field using the author key.
- **Category**: A topic classification defined in frontmatter that generates filterable index pages. Standard categories include: Kubernetes, GitOps, Observability, Security, Networking, Storage, CI/CD, OS, Cloud Native.
- **Blog Template**: The `TEMPLATE-BLOG-POST.md` file providing a fill-in-the-blanks structure for consistent post creation.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: The Material blog plugin renders posts correctly in both Zensical and MkDocs builds.
- **SC-002**: Category archive pages list all posts with correct category tag without broken links.
- **SC-003**: The blog index page loads in under 1 second with up to 50 posts.
- **SC-004**: A new author can create and publish a post using only the template, without needing to understand the Material blog plugin internals.
- **SC-005**: All existing posts (currently 1) render with correct metadata, excerpt, and structure.
- **SC-006**: The "Talos Linux" post's incomplete section 3 ("Mi Experiencia de Migración") is addressed (either completed or marked as draft).

---

## Assumptions

- The Material blog plugin is available and functionally equivalent in both MkDocs and Zensical builds.
- Authors are familiar with Markdown and YAML frontmatter.
- The blog is a secondary feature; the primary focus is project case studies and Diátaxis documentation.
- Blog posts may contain both Spanish and English content (Spanish preferred per constitution).
- Author avatars are hosted on GitHub (referenced via `https://github.com/<user>.png`).

---

## Dependencies

- Material for MkDocs blog plugin (configured in `mkdocs.yml` and `zensical.toml`).
- Material `grid cards` feature for blog index layout.
- Navigation configuration defines the "Blog" top-level section.
- Author avatar hosting (GitHub, Gravatar, or local).
