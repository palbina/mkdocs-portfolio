# Research: Portfolio Improvements

**Date**: 2026-07-05

## Research Tasks

All technologies used in this feature are already established in the project. No external research required.

### Decision Log

| Decision | Rationale | Alternatives Considered |
|:---------|:----------|:------------------------|
| Remove `.hero-stats` CSS vs implement HTML | CSS removal is simpler, removes dead code, and adds no untested component. Implementing hero-stats would require design decisions about what metrics to show and verification across browsers. Per constitution V (Simplicidad + YAGNI): remove unused code. | Implement hero-stats HTML — rejected because the component was never designed/populated, no metrics defined, adds complexity without clear purpose. |
| Delete `=0.0.24` vs add to `.gitignore` | Delete the file permanently. If it regenerates on `zensical build`, add to `.gitignore` in the same PR. Current evidence (git log) suggests it's a stale artifact, not a regeneration target. | Add to `.gitignore` only — rejected because if the file is never regenerated, `.gitignore` becomes dead config. Delete first, add `.gitignore` only if needed. |
| 2 new blog posts vs more | 2 new posts plus fixing the existing one brings the total to 3 — sufficient to demonstrate the blog system's value and populate category archives. The spec's SC-001 requires "at least 3". More posts can follow in separate features. | 3+ new posts — rejected to keep scope manageable. Blog content creation is unbounded; this feature establishes the baseline. |
| Blog post topics | **GitOps Real-World** (ArgoCD ApplicationSets + sync waves from the GitOps project) and **Observability Signal Correlation** (Loki + Tempo + Prometheus debugging workflow from the observability project). Both topics come from existing project content, ensuring factual accuracy and code examples that match the documented HomeLab. | Other topics considered: Progressive Delivery (overlaps with GitOps), CNPG (too narrow for broad audience). Chosen topics have broadest DevOps appeal. |
| mkdocs.yml historical comment vs removal | Add header comment marking it as historical reference. The file is retained per constitution (CI/CD section) and removing it would break the principle of documented migration trail. | Remove mkdocs.yml entirely — rejected because the constitution explicitly states it's retained as reference. Full removal is a separate governance decision. |
| Macros plugin: comment out vs remove from mkdocs.yml | Remove the entire `macros` plugin block. The referenced file `scripts/main.py` doesn't exist. A commented-out block that references a non-existent file is more confusing than simply removing it. The migration is documented in `docs/MIGRATION-ZENSICAL.md`. | Comment out — rejected because a commented broken reference is still confusing. Clean removal is clearer. |
| CONTRIBUTING.md: update vs rewrite | Targeted update of the local development section only. The rest of the file (style guide, PR process, conventions) is still accurate. Full rewrite is out of scope. | Full rewrite — rejected as unnecessary. Only the `mkdocs build`/`mkdocs serve` references are outdated. |

## Verification Strategy

Since this is a content/config feature without code changes, verification is manual:

1. `zensical build` must complete with zero errors
2. Browser inspection: blog index shows 3 posts, landing page shows 8 cards, hero-stats CSS gone
3. `grep -r "mkdocs build" CONTRIBUTING.md` returns zero matches (except in historical migration docs)
4. `grep "scripts/main" mkdocs.yml` returns zero matches
5. `ls =0.0.24` returns "No such file or directory"
6. `head -10 mkdocs.yml` shows the historical reference comment
