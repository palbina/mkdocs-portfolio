# Quickstart: Portfolio Improvements Validation

**Date**: 2026-07-05

Validation guide to verify all 8 functional requirements after implementation.

## Prerequisites

- Zensical SSG installed (`zensical --version`)
- Python 3.14+ and dependencies from `requirements.txt`
- Repository at `007-portfolio-improvements` branch
- Browser for visual inspection

## Validation Steps

### 1. Build the site

```bash
cd /home/peter/DEV/mkdocs-portfolio
zensical build --clean
```

**Expected**: Build completes with zero errors. Static files generated in `site/` directory.

### 2. Blog Content (FR-001, FR-002)

```bash
# Count blog posts
ls docs/blog/posts/*.md | wc -l

# Verify Talos post section 3 is NOT placeholder
grep -c "Aquí relataré" docs/blog/posts/2026-02-10-talos-linux-k8s.md

# Verify new posts follow template structure
grep -l "El Problema" docs/blog/posts/2026-07-*.md
grep -l "Cuándo Usar" docs/blog/posts/2026-07-*.md
```

**Expected**:
- At least 3 posts exist (`wc -l` ≥ 3)
- `Aquí relataré` count = 0 (placeholder removed)
- Both new posts have required template sections

### 3. Landing Page (FR-003, FR-004)

```bash
# Count project cards on landing page
grep -c "project-card" docs/index.md

# Verify hero-stats CSS removed
grep "hero-stats" docs/stylesheets/extra.css
```

**Expected**:
- 8 project cards (`grep -c` ≥ 8, including `.featured`)
- hero-stats grep returns zero lines (CSS removed)

### 4. CONTRIBUTING.md (FR-005)

```bash
# Verify Zensical commands, not MkDocs
grep -c "zensical build" CONTRIBUTING.md
grep -c "zensical serve" CONTRIBUTING.md
grep "mkdocs build" CONTRIBUTING.md | grep -v "migration\|historical\|ya no"
```

**Expected**:
- `zensical build` appears in CONTRIBUTING.md (≥ 1)
- `mkdocs build` only appears in historical/migration context or not at all

### 5. Residue File (FR-006)

```bash
# Verify residue file gone or gitignored
test -f =0.0.24 && echo "STILL EXISTS" || echo "REMOVED"
grep "=0.0.24" .gitignore
```

**Expected**: "REMOVED" (file deleted) OR file exists but is listed in `.gitignore`

### 6. mkdocs.yml Cleanup (FR-007, FR-008)

```bash
# Verify header comment added
head -5 mkdocs.yml

# Verify macros plugin removed
grep -c "scripts/main" mkdocs.yml
```

**Expected**:
- Header includes "historical reference" or "referencia histórica"
- `scripts/main` count = 0 (macros plugin removed)

## Browser Verification

After `zensical build`, open `site/index.html` in a browser or serve locally:

1. **Landing page**: 8 project cards in grid. No broken links. Responsive at 768px.
2. **Blog index**: 3 posts in grid. Clickable category links. Author avatars load.
3. **Blog posts**: Complete content, no placeholder text. Mermaid diagrams render.
4. **Navigation**: All existing nav links still work. Diátaxis docs accessible.

## Success Criteria Mapping

| SC | Validation |
|:---|:-----------|
| SC-001 (3 blog posts) | `ls docs/blog/posts/*.md \| wc -l` ≥ 3 |
| SC-002 (8 landing cards) | `grep -c "project-card" docs/index.md` ≥ 8 |
| SC-003 (no dead CSS) | `grep "hero-stats" docs/stylesheets/extra.css` = 0 |
| SC-004 (CONTRIBUTING.md accurate) | `grep "zensical build" CONTRIBUTING.md` ≥ 1 |
| SC-005 (no residue file) | `test -f =0.0.24` returns false |
| SC-006 (no broken macros) | `grep "scripts/main" mkdocs.yml` = 0 |
