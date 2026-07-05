# Feature Specification: CI/CD Pipeline

**Feature Branch**: `005-cicd-pipeline`

**Created**: 2026-07-05

**Status**: Implemented (Brownfield Spec)

**Input**: Complete CI/CD pipeline for building, containerizing, and deploying the ArkenOps portfolio. **Fully migrated from MkDocs to Zensical SSG** (Rust) as the primary build system. Uses Kaniko/Docker for container builds, Nginx for serving, and a private Zot registry for image storage. Orchestrated via GitLab CI. `mkdocs.yml` is retained for reference only; the build command is `zensical build`.

---

## User Scenarios & Testing

### User Story 1 - Automated Build on Push (Priority: P1)

A contributor pushes to the `main` branch. The CI pipeline automatically builds the site, creates a Docker image, and pushes it to the registry for deployment.

**Why this priority**: Automation is the core CI/CD value proposition. Without it, every deployment requires manual intervention.

**Independent Test**: Push a change to `main`. Verify GitLab CI triggers the pipeline. Verify `zensical build` executes successfully. Verify the Docker image is pushed to the Zot registry with both `latest` and commit SHA tags.

**Acceptance Scenarios**:

1. **Given** a commit is pushed to `main`, **When** GitLab CI triggers, **Then** the `build` job runs Kaniko builder with the Dockerfile, builds the site with `zensical build`, creates a Docker image, and pushes to `registry-taloslab.subetupaginacp.com:5000/palbina/mkdocs-portfolio` with tags `$CI_COMMIT_SHORT_SHA` and `latest`.
2. **Given** the build completes successfully, **When** the image is pushed, **Then** the pipeline status is green and the image is available for deployment.

---

### User Story 2 - Production-Grade Serving (Priority: P1)

The built site is served via Nginx with proper security headers, compression, caching, and health checking. Visitors access the site at `docs.arkenops.cc` with secure defaults.

**Why this priority**: The Nginx configuration defines the production serving contract. Security headers and caching directly impact user experience and security posture.

**Independent Test**: Deploy the Docker image. Verify the site serves on port 80 with gzip compression. Verify security headers (X-Frame-Options, X-Content-Type-Options, X-XSS-Protection, Referrer-Policy) are present. Verify static assets are cached for 1 year with immutable. Verify `/health` returns 200.

**Acceptance Scenarios**:

1. **Given** the Docker container is running, **When** a request is made to `/`, **Then** the response includes gzip compression, `Cache-Control: no-cache` for HTML, and all 4 security headers.
2. **Given** static assets (`/stylesheets/extra.css`, `/assets/javascripts/*.js`) are requested, **When** the response is served, **Then** `Cache-Control: public, max-age=31536000, immutable` is set.
3. **Given** a request is made to `/.git/config` or any hidden file path, **When** Nginx processes the request, **Then** `403 Forbidden` is returned.

---

### User Story 3 - Multi-Stage Docker Build (Priority: P2)

The Dockerfile separates build dependencies (Python, Cairo libs, pip packages) from runtime dependencies (only Nginx and static files), producing a minimal production image.

**Why this priority**: Multi-stage builds reduce image size and attack surface. Important for production but not critical for functionality.

**Independent Test**: Build the Docker image. Verify the final image does not contain Python, pip, or build-time dependencies. Verify only `/usr/share/nginx/html` (static files) and `/etc/nginx/conf.d/default.conf` (Nginx config) exist in the runtime stage. Verify HEALTHCHECK is configured.

**Acceptance Scenarios**:

1. **Given** the Dockerfile is built, **When** the multi-stage build completes, **Then** the final image (`nginx:1.30-alpine` base) contains only static files, Nginx config, and the Nginx binary — no Python, Cairo, or build tools.
2. **Given** the Docker container is running, **When** Docker's HEALTHCHECK executes `wget -q --spider http://localhost/health`, **Then** it returns exit code 0 within the configured interval.

---

### Edge Cases

- What happens when `zensical build` fails (e.g., broken markdown syntax)? The Kaniko build step fails with a non-zero exit code, the pipeline fails, and no image is pushed. The previous deployment remains active.
- What happens when the Zot registry is unreachable? Kaniko's push step fails. The pipeline fails. The previous deployment remains active.
- What happens when the GitLab CI runner encounters MTU issues with Cilium VXLAN? The pipeline invokes `ip link set dev eth0 mtu 1400` as a before_script workaround.
- What happens when GitHub Actions and GitLab CI both trigger on the same push? Both pipelines execute independently. Both push to the same registry with potentially conflicting tags. This is an architectural risk that should be resolved by decommissioning one.
- What happens when `requirements.txt` has dependency conflicts? The `pip install` step fails during the Docker build, the build stage fails, and the pipeline fails.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST build the static site using `zensical build` (not `mkdocs build`) in the Dockerfile's builder stage.
- **FR-002**: System MUST use a multi-stage Docker build: `python:3.14-slim` for building, `nginx:1.30-alpine` for serving.
- **FR-003**: The builder stage MUST install Cairo development libraries (`libcairo2-dev`, `libfreetype6-dev`, `libffi-dev`, `libjpeg-dev`, `libpng-dev`, `libz-dev`) for social card generation support.
- **FR-004**: The builder stage MUST install Python dependencies from `requirements.txt` using pip.
- **FR-005**: The runtime stage MUST copy only `nginx.conf` and the `site/` build output directory from the builder stage.
- **FR-006**: The runtime stage MUST include a HEALTHCHECK using `wget` against `http://localhost/health`.
- **FR-007**: Nginx MUST serve on port 80 with gzip compression (level 6) for text/css/js/json/xml/svg MIME types.
- **FR-008**: Nginx MUST set security headers: `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `X-XSS-Protection: 1; mode=block`, and `Referrer-Policy: strict-origin-when-cross-origin`.
- **FR-009**: Nginx MUST cache static assets (CSS, JS, images, fonts, media) for 1 year with `immutable` directive.
- **FR-010**: Nginx MUST serve HTML with `Cache-Control: no-cache` for instant content updates.
- **FR-011**: Nginx MUST deny access to hidden files (paths starting with `\.`).
- **FR-012**: Nginx MUST support SPA-style fallback with `try_files $uri $uri/ $uri.html /index.html`.
- **FR-013**: GitLab CI MUST trigger on `main` branch pushes, merge request events, and tag pushes.
- **FR-014**: GitLab CI MUST use Kaniko executor (`gcr.io/kaniko-project/executor:debug`) with `--context`, `--dockerfile`, `--destination`, and authentication via `config.json`.
- **FR-015**: GitLab CI MUST apply MTU 1400 workaround (`ip link set dev eth0 mtu 1400`) for Cilium VXLAN compatibility before Kaniko execution.
- **FR-016**: GitLab CI MUST push to the Zot registry with tags `$CI_COMMIT_SHORT_SHA` and `latest`.
- **FR-017**: The GitHub Actions workflow (`.github/workflows/deploy.yml`) MUST be documented as potentially vestigial given the active GitLab CI pipeline.

### Key Entities

- **Dockerfile**: Multi-stage build file defining the build (Python + Zensical) and runtime (Nginx + static files) stages.
- **Nginx Configuration** (`nginx.conf`): Production web server config with security headers, compression, caching strategy, hidden file protection, and SPA fallback.
- **GitLab CI Pipeline** (`.gitlab-ci.yml`): Single-stage pipeline with Kaniko-based Docker build and push to Zot registry.
- **Zot Registry**: Private container registry at `registry-taloslab.subetupaginacp.com:5000` storing the built Docker images.
- **Kaniko**: Google's container image builder that runs in unprivileged Kubernetes pods (no Docker daemon required).

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Pipeline completes in under 5 minutes from push to registry (building + pushing Docker image).
- **SC-002**: Final production Docker image size is under 50MB (Nginx alpine base + static files).
- **SC-003**: Security headers are present on all responses as verified by `curl -I`.
- **SC-004**: `/health` endpoint returns HTTP 200.
- **SC-005**: Static asset requests return `Cache-Control: public, max-age=31536000, immutable`.
- **SC-006**: Hidden file requests (e.g., `/.env`) return `403 Forbidden`.
- **SC-007**: Zero failed builds due to pipeline configuration (MTU issues addressed, auth configured).

---

## Assumptions

- The target deployment environment pulls images from the Zot registry and redeploys on new `latest` tag.
- The Zot registry is accessible from both the GitLab runner and the deployment target.
- Kaniko successfully authenticates to Zot using the base64-encoded `ZOT_DOCKER_CONFIG` CI variable.
- The Cilium VXLAN MTU issue persists and requires the 1400 MTU workaround.
- GitHub Actions may be decommissioned in favor of GitLab CI per the Forgejo migration precedent.

---

## Zensical Migration State

The project completed migration from MkDocs to Zensical SSG (v0.0.24) in March 2026. Key migration artifacts:

| Component | MkDocs Status | Zensical Status |
|:----------|:--------------|:----------------|
| Build command | `mkdocs build` (disabled) | `zensical build` (active) |
| Configuration | `mkdocs.yml` (retained as reference) | `zensical.toml` (primary, active) |
| Plugins: search | ✅ | ✅ (ported) |
| Plugins: blog | ✅ | ✅ (ported) |
| Plugins: minify | ✅ | ❌ **MISSING** — minification not available in Zensical |
| Plugins: git-revision-date-localized | ✅ | ❌ **MISSING** — no date plugin equivalent |
| Plugins: macros | ❌ (scripts/main.py deleted) | N/A (removed) |
| Template engine | Jinja2 (Python) | Tera (Rust) |
| CSS version | `extra.css?v=4.0` | `extra.css?v=4.2` |
| Markdown linting | Standard | Zensical-adapted (`.markdownlint.json`) |

### Known Feature Gaps (Zensical vs MkDocs)

**FR-017**: System MUST document that Zensical lacks 3 MkDocs plugins present in `mkdocs.yml`:
- **No minify plugin**: HTML/JS/CSS minification is not performed at build time. Must be handled at the Nginx or CDN layer.
- **No git-revision-date-localized**: The `{{ git_revision_date_localized }}` template variable renders empty or as literal text in Zensical builds.
- **No macros plugin**: Dynamic content generation (Python macros) was intentionally removed; static content replaced it.

## Dependencies

- **Zensical SSG v0.0.24+** (`requirements.txt`) — primary static site generator. Replaces MkDocs entirely for builds.
- `requirements.txt` retains `mkdocs`, `mkdocs-material`, and MkDocs plugins for reference/compatibility, but they are not invoked during the build pipeline.
- `mkdocs.yml` is retained in the repository as a reference configuration but is NOT used by CI/CD. Builds use `zensical.toml` exclusively.
- Python 3.14 base image for the builder stage. Cairo/Freetype libs installed for social cards support (Material plugin dependency).
- Nginx 1.30 Alpine for the runtime stage.
- GitLab CI with Kubernetes runner tag and MTU 1400 workaround for Cilium VXLAN.
- Private Zot registry for Docker image storage.
