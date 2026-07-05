# Tasks: Homelab Portfolio Enrichment

**Input**: Design documents from `specs/008-homelab-portfolio-enrichment/`

**Prerequisites**: plan.md (technical context), spec.md (user stories), research.md (decisions), data-model.md (entities), quickstart.md (validation)

**Tests**: Not applicable — pure documentation feature. Validation via `zensical build --clean`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- All content changes in `docs/` directory
- Source data from `/home/peter/DEV/talos-gitops/docs/` (read-only)
- `docs/projects/` for project pages
- `docs/reference/` for reference pages
- `docs/explanation/` for explanation pages
- `docs/index.md` for landing page

---

## Phase 1: Source Data Extraction & Analysis

**Purpose**: Read TalosLab source documentation and extract key data points needed for all subsequent phases.

- [X] T001 [P] Read TalosLab `docs/INDEX.md` and extract cluster specs (node count 5→3+2, hardware models, Talos v1.13.2, K8s v1.35.0, GitLab sovereign, Zot registry, Flux experimental). Produce a data sheet of exact versions and metrics.
- [X] T002 [P] Read TalosLab `docs/reference/QUICK_REFERENCE.md` and extract versions table, SRE commands (fish shell, kubeseal-now, argocd sync workflow), backup buckets list (8 S3 buckets), and endpoint catalog. Strip internal IPs.
- [X] T003 [P] Read TalosLab `docs/compliance-dashboard.md` and extract compliance metrics (29/29 apps, 7 CronJobs, hardening table). Read `k8s/templates/README.md` for Molty Standard V2 deployment specification (9 manifests + validation script).

**Checkpoint**: All TalosLab source data extracted and ready for content authoring.

---

## Phase 2: User Story 1 — Enrich Existing Project Pages (Priority: P1) 🎯 MVP

**Goal**: Replace generic/placeholder data in 8 existing project pages with real TalosLab cluster data.

**Independent Test**: Run `grep` on each page to verify at least one TalosLab-specific data point exists (e.g., "Talos v1.13", "CNPG", "CrowdSec", "ArgoCD v3.4").

### Implementation for User Story 1

- [X] T004 [P] [US1] Update `docs/projects/homelab.md` — replace "3 nodos bare-metal" with 5 nodos reales (3 CP: ThinkPad L14, Geekom A7, Intel N305 + 2 Workers: Geekom A7/Coral TPU, Lenovo SR630 w/ 2x Xeon 320GB RAM). Add Talos v1.13.2, K8s v1.35.0, KubePrism @7445, consolidación SR630 post-decommission (N05/N06). Update Mermaid diagram to show real node topology and Cloudflare tunnel.
- [X] T005 [P] [US1] Update `docs/projects/gitops.md` — replace "ArgoCD v2.10" with ArgoCD v3.4.3 + Flux v2.8.8 experimental. Add GitLab como source primario (sovereign stack), ApplicationSets con exclusión de apps multi-source, Renovate v43, ArgoCD Image Updater, Sealed Secrets. Update Mermaid diagram to show GitLab → ArgoCD + Flux split.
- [X] T006 [P] [US1] Update `docs/projects/security.md` — add CrowdSec IPS, Authentik forwardAuth SSO, CiliumNetworkPolicies Zero Trust v2.1 (document the `- {}` → `[]` fix), Istio Ambient mTLS (ztunnel, HBONE, no sidecars), and Sealed Secrets. Add security agent guidelines link.
- [X] T007 [P] [US1] Update `docs/projects/database-ha.md` — add CNPG with 3 instances, `<10s` failover, SeaweedFS S3 offsite WAL streaming, PITR 7-day retention, Longhorn v1.10.2 with HDD/SSD StorageClasses. Reference 8 S3 backup buckets from TalosLab.
- [X] T008 [P] [US1] Update `docs/projects/observability.md` — add full LGTM stack (Loki, Grafana, Tempo/OpenTelemetry, Prometheus), Kiali for Istio mesh visualization, k6 operator for load testing, AlertManager → Telegram routing. Add Mermaid diagram of observability pipeline.
- [X] T009 [P] [US1] Update `docs/projects/backup-dr.md` — reference 629-line DR guide from TalosLab, `export-dr-backup.sh` for 1Password credential vaulting, differentiate 8 S3 buckets by purpose (CNPG, MariaDB, WordPress, Velero, Longhorn, etcd, Tempo, Forgejo). Add disaster recovery flow Mermaid diagram.
- [X] T010 [P] [US1] Update `docs/projects/progressive-delivery.md` — add Argo Rollouts with canary strategy, AnalysisRuns querying Prometheus metrics, automated rollback on metric degradation. Add Istio traffic splitting integration and k6 operator for load generation during analysis.
- [X] T011 [P] [US1] Update `docs/projects/ai-rag.md` — replace placeholder with real content or mark as WIP with explanation of planned RAG architecture (local LLM integration, vector DB, retrieval pipeline).

**Checkpoint**: All 8 existing project pages contain TalosLab-specific data. Each page independently verifiable via grep for unique version/hardware/tool identifiers.

---

## Phase 3: User Story 2 — Create New Project Pages (Priority: P2)

**Goal**: Create 3 new project pages documenting areas not yet represented in the portfolio.

**Independent Test**: Verify new `.md` files exist in `docs/projects/`, each follows the project template (frontmatter, `project-header`, `project-meta-grid`, 6 sections). Grep for `project-header` and `Visión General` in each file.

### Implementation for User Story 2

- [X] T012 [P] [US2] Create `docs/projects/deployment-methodology.md` — document Molty Standard V2: 9 mandatory manifests (namespace, service-account, network-policy with Zero Trust v2.1 `[]`, pdb, resource-quota, limit-range, deployment with full securityContext, ingress-route with CrowdSec+Authentik middlewares, optional servicemonitor). Include `validate-deployment-compliance.sh` script reference. Show 29/29 apps 100% compliance result. Include Mermaid workflow diagram of app creation pipeline.
- [X] T013 [P] [US2] Create `docs/projects/zero-trust-networking.md` — document NetworkPolicies evolution v1 → v2 → v2.1, the `- {}` false-deny bug discovery and fix, CiliumNetworkPolicy as enforcement layer, true `[]` default-deny pattern. Include architecture diagram showing defense-in-depth layers (Cloudflare → CrowdSec → CiliumNP → Istio mTLS → Authentik). Document Istio Ambient mode (ztunnel, waypoint proxies, HBONE protocol).
- [X] T014 [P] [US2] Create `docs/projects/compliance-dashboard.md` — document 29 applications at 100% Molty V2 compliance. Include hardening status table (App, Namespace, Status, Hardening level). List 7 CronJob auditors (compliance-auditor, traffic-auditor, cert-security-auditor, zot-registry-cleaner, cilium-policy-auditor, cnpg-backup-verifier, velero-backup-verifier). Show Mermaid diagram of automated compliance pipeline.

**Checkpoint**: 3 new project pages created and independently verifiable. Portfolio now has 11 project pages (8 existing + 3 new).

---

## Phase 4: User Story 3 — Update Reference & Explanation Pages (Priority: P3)

**Goal**: Align reference and explanation documentation with real TalosLab 2026 data.

**Independent Test**: Grep for version strings (`v1.13`, `v1.35`, `v1.18`, `v3.4`, `v1.30`) in reference pages. Grep for real-world examples (`bug - {}`, `multi-source`, `sovereign`) in explanation pages.

### Implementation for User Story 3

- [X] T015 [P] [US3] Update `docs/reference/tech-stacks.md` — replace generic versions with TalosLab 2026 exact versions: Talos v1.13.2, K8s v1.35.0, Cilium v1.18.5, Istio Ambient v1.30.0, ArgoCD v3.4.3, Flux v2.8.8, CNPG, Longhorn v1.10.2, Zot registry, GitLab + agentk, Renovate v43, Traefik v3.7.1, CrowdSec v1.7.7. Add sovereign stack architecture note.
- [X] T016 [P] [US3] Update `docs/reference/kubernetes-commands.md` — align with TalosLab operational practices: fish shell mandatory, no `kubectl apply` for permanent resources, `kubeseal-now` workflow, `argocd app sync` invocation, Talos-specific commands (`talosctl`). Add GitOps workflow section.
- [X] T017 [P] [US3] Update `docs/reference/configuration-reference.md` — replace generic configuration references with TalosLab-specific config patterns: Cilium MTU 1230, KubePrism port 7445, Istio Ambient ztunnel, Longhorn StorageClasses, CNPG cluster config, Traefik IngressRoute with CrowdSec middleware.
- [X] T018 [P] [US3] Update `docs/explanation/zero-trust-model.md` — replace generic Zero Trust explanation with real TalosLab architecture: 5-layer defense (Cloudflare → CrowdSec → Cilium → Istio mTLS → Authentik). Document the v2.1 `- {}` bug fix as a real-world lesson. Add "el perímetro de red no es mecanismo de seguridad" principle.
- [X] T019 [P] [US3] Update `docs/explanation/cloud-native-architecture.md` — replace generic concepts with sovereign stack architecture: GitLab (source primario) → ArgoCD + Flux (dual GitOps), Zot (registry local), CI/CD con Forgejo Actions en `network=host` + `insecure=true`. Document immutable infrastructure with Talos.
- [X] T020 [P] [US3] Update `docs/explanation/gitops-philosophy.md` — add real-world lessons: apps multi-source requieren Application manual (no ApplicationSet), ApplicationSet genérico usa exclude list, GitLab como source soberano, mirror a Forgejo/GitHub, Renovate dual config pattern (repo + ConfigMap). Document rule: "Git es la única fuente de verdad".

**Checkpoint**: All reference and explanation pages updated with TalosLab 2026 data. Cross-site consistency achieved.

---

## Phase 5: Landing Page & Polish

**Purpose**: Update landing page to reflect new projects, run full build validation.

- [X] T021 Update `docs/index.md` — add 3 new project cards to `.projects-grid` for new pages: Molty Standard V2 (icon: 🛡️, impact: "29 APPS COMPLIANT"), Zero Trust Networking (icon: 🔒, impact: "5-LAYER DEFENSE"), Compliance Dashboard (icon: 📊, impact: "7 CRONJOB AUDITORS"). Update hero section to reflect real cluster stats (5 nodos, Talos v1.13.2, K8s v1.35.0). Total cards: 11.
- [X] T022 [P] Update `docs/projects/index.md` — add entries for the 3 new project pages to the project listing/index.
- [X] T023 Run `zensical build --clean` and verify zero errors, zero warnings. Fix any broken links, missing references, or Mermaid syntax errors.
- [X] T024 Run full `quickstart.md` validation — execute all 6 verification scenarios (VS-1 through VS-6) and confirm all pass.

**Checkpoint**: All content created, build passing, quickstart validation successful.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Source Data)**: No dependencies — can start immediately. All 3 tasks [P] can run in parallel.
- **Phase 2 (US1)**: Depends on Phase 1 (needs extracted data). All 8 tasks [P] can run in parallel.
- **Phase 3 (US2)**: Depends on Phase 1 (needs data). Can run in parallel with Phase 2. All 3 tasks [P] independent.
- **Phase 4 (US3)**: Depends on Phase 1 (needs data). Can run in parallel with Phases 2-3. All 6 tasks [P] independent.
- **Phase 5 (Polish)**: Depends on Phases 2, 3, 4 completion. T021-T022 [P], then T023, then T024.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 1 — No dependencies on other stories
- **User Story 2 (P2)**: Can start after Phase 1 — Independent of US1 (different files)
- **User Story 3 (P3)**: Can start after Phase 1 — Independent of US1/US2 (different files)

### Parallel Opportunities

- Phase 1: All 3 source data tasks (T001-T003) can run in parallel
- Phase 2: All 8 project page updates (T004-T011) can run in parallel
- Phase 3: All 3 new page creations (T012-T014) can run in parallel
- Phase 4: All 6 reference/explanation updates (T015-T020) can run in parallel
- Phase 5: T021 and T022 can run in parallel (different files)

---

## Parallel Example: Phase 2 (US1)

```bash
# All 8 project page updates can launch together:
Task: "Update docs/projects/homelab.md with real cluster data"
Task: "Update docs/projects/gitops.md with ArgoCD v3.4.3 + Flux"
Task: "Update docs/projects/security.md with Zero Trust v2.1"
Task: "Update docs/projects/database-ha.md with CNPG + SeaweedFS"
Task: "Update docs/projects/observability.md with full LGTM stack"
Task: "Update docs/projects/backup-dr.md with DR guide + 8 buckets"
Task: "Update docs/projects/progressive-delivery.md with Argo Rollouts"
Task: "Update docs/projects/ai-rag.md with real content or WIP status"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Extract TalosLab source data (T001-T003)
2. Complete Phase 2: Enrich 8 existing project pages (T004-T011)
3. **STOP and VALIDATE**: Verify `zensical build --clean` passes. Each page has at least 1 TalosLab data point.
4. Portfolio already has 8 enriched pages — visible value delivered.

### Incremental Delivery

1. Phase 1: Extract data → Foundation ready
2. Phase 2: US1 → 8 pages enriched → Build & validate (MVP!)
3. Phase 3: US2 → 3 new pages → Build & validate (11 total)
4. Phase 4: US3 → reference + explanation updated → Build & validate
5. Phase 5: Landing page + final validation → Complete

### Full Parallel Strategy

With full parallelism:
1. Phase 1: 3 parallel reads (T001-T003)
2. Phases 2+3+4: 8 + 3 + 6 = 17 parallel file writes (T004-T020)
3. Phase 5: Landing page update (T021-T022) → Build (T023) → Validate (T024)

---

## Notes

- [P] tasks = different files, no dependencies on other writes
- [Story] label maps task to specific user story for traceability
- All project pages follow the 6-section template from research R6
- Sensitive data excluded per research R5 (no IPs, no .subetupaginacp.com domains)
- Build validation (T023) is the final gate before declaring Phase 5 complete
- Quickstart validation (T024) runs all 6 VS scenarios from quickstart.md
