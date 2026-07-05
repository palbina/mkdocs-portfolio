# Quickstart: Homelab Portfolio Enrichment

**Feature**: 008-homelab-portfolio-enrichment
**Date**: 2026-07-05

## Prerequisites

- Zensical SSG v0.0.46 installed (`zensical --version`)
- Git repository clean (`git status` — no pending changes)
- Access to TalosLab repo at `/home/peter/DEV/talos-gitops/docs/`

## Validation Scenarios

### VS-1: Existing Project Pages Enriched (US1 — 6 pages)

```bash
# Verify each page has at least one TalosLab-specific data point
echo "=== homelab.md ===" && grep -c "Talos v1.13\|K8s v1.35\|SR630\|ThinkPad L14\|Geekom A7" docs/projects/homelab.md
echo "=== gitops.md ===" && grep -c "ArgoCD v3.4\|Flux v2.8\|Renovate v43\|ApplicationSet\|GitLab" docs/projects/gitops.md
echo "=== security.md ===" && grep -c "CrowdSec\|Authentik\|CiliumNetworkPolicy\|Zero Trust v2\|Istio Ambient" docs/projects/security.md
echo "=== database-ha.md ===" && grep -c "CNPG\|<10s failover\|SeaweedFS\|PITR\|8 buckets" docs/projects/database-ha.md
echo "=== observability.md ===" && grep -c "Loki\|Grafana\|Tempo\|Kiali\|k6\|AlertManager.*Telegram" docs/projects/observability.md
echo "=== backup-dr.md ===" && grep -c "629 líneas\|export-dr-backup\|1Password\|8 buckets S3" docs/projects/backup-dr.md
```

**Expected**: Each grep returns ≥1 (at least one unique TalosLab data point per page).

### VS-2: New Project Pages Created (US2 — 3 pages)

```bash
# Verify new files exist and have valid structure
for f in docs/projects/deployment-methodology.md docs/projects/zero-trust-networking.md docs/projects/compliance-dashboard.md; do
  test -f "$f" && echo "EXISTS: $f" || echo "MISSING: $f"
  grep -c "project-header\|project-meta-grid" "$f" 2>/dev/null
  grep -c "Visión General\|Arquitectura\|Stack Tecnológico" "$f" 2>/dev/null
done
```

**Expected**: All 3 files exist, each has `project-header` div, `project-meta-grid` div, and the 3 mandatory sections.

### VS-3: Reference Pages Aligned (US3 — 3 pages)

```bash
echo "=== tech-stacks.md ===" && grep -c "Talos v1.13\|K8s v1.35\|Cilium v1.18\|Istio Ambient v1.30\|ArgoCD v3.4" docs/reference/tech-stacks.md
echo "=== kubernetes-commands.md ===" && grep -c "argocd\|kubeseal\|fish" docs/reference/kubernetes-commands.md
echo "=== configuration-reference.md ===" && grep -c "Talos\|Cilium\|ArgoCD" docs/reference/configuration-reference.md
```

**Expected**: Each grep returns ≥1.

### VS-4: Build Integrity

```bash
# Full build with Zensical
zensical build --clean 2>&1 | tee /tmp/build-008.log
grep -i "error\|warning\|issue" /tmp/build-008.log || echo "BUILD CLEAN: 0 errors, 0 warnings"
```

**Expected**: "BUILD CLEAN: 0 errors, 0 warnings" or Zensical output says "No issues found".

### VS-5: Landing Page Updated

```bash
# Count project cards (each card starts with <div class="project-card">)
grep -c 'class="project-card"' docs/index.md
# Verify new pages are linked
grep -c "deployment-methodology\|zero-trust-networking\|compliance-dashboard" docs/index.md
```

**Expected**: Card count ≥ 11 (8 existing + 3 new). All 3 new pages referenced.

### VS-6: Success Criteria Verification

```bash
echo "=== SC-001: 9 existing pages with TalosLab data ==="
for p in homelab gitops security database-ha observability backup-dr progressive-delivery ai-rag index; do
  test -f "docs/projects/${p}.md" && count=$(grep -cE "Talos v1\.1[0-9]|K8s v1\.3[0-9]|Cilium v1\.1[0-9]|CNPG|ArgoCD v[0-9]|Molty|Longhorn v[0-9]|Istio|CrowdSec|Zero Trust v2" "docs/projects/${p}.md" 2>/dev/null || echo "0") && echo "  ${p}.md: $count data points" || echo "  ${p}.md: MISSING"
done

echo "=== SC-002: 3 new pages ==="
ls docs/projects/deployment-methodology.md docs/projects/zero-trust-networking.md docs/projects/compliance-dashboard.md 2>&1

echo "=== SC-003: Reference pages aligned ==="
grep -l "v1.13\|v1.35\|v1.18\|v3.4\|v1.30" docs/reference/tech-stacks.md docs/reference/kubernetes-commands.md docs/reference/configuration-reference.md 2>&1

echo "=== SC-006: Landing page cards ==="
grep -c 'project-card' docs/index.md
```

**Expected**: SC-001 shows ≥1 data point per page. SC-002 shows all 3 files. SC-003 shows all 3 files. SC-006 shows ≥11.
