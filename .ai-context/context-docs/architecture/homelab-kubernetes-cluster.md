# HomeLab Kubernetes Cluster

**Type**: Architecture
**Date**: 2026-02-09
**Status**: Complete

---

## Overview

Demonstration of production-grade Kubernetes cluster design and operation. This 3-node bare-metal cluster showcases enterprise-level infrastructure skills including immutable OS management, eBPF networking, service mesh implementation, and GitOps workflows.

**Key Achievement**: Operating a production-like environment 24/7 with 30+ applications, demonstrating real-world infrastructure expertise beyond theoretical knowledge.

---

## Technical Skills Demonstrated

| Domain | Technologies | Competency Level |
|--------|--------------|------------------|
| **Container Orchestration** | Kubernetes, Helm, Kustomize | Expert |
| **Operating Systems** | Talos Linux (immutable infrastructure) | Advanced |
| **Networking** | Cilium CNI (eBPF), Istio Service Mesh | Expert |
| **Storage** | Longhorn distributed storage | Advanced |
| **GitOps** | ArgoCD, ApplicationSets, Sync Waves | Expert |
| **Security** | Zero Trust networking, mTLS, NetworkPolicies | Advanced |

---

## Architecture Highlights

### 3-Node Bare-Metal Design

```
┌─────────────────────────────────────────────────────────────┐
│                    HOME LAB CLUSTER                          │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Control     │  │   Worker     │  │   Worker     │      │
│  │  Plane       │  │   Node 1     │  │   Node 2     │      │
│  │  (etcd)      │  │              │  │              │      │
│  │  i5-12400    │  │  i5-12400    │  │  i5-12400    │      │
│  │  32GB RAM    │  │  32GB RAM    │  │  32GB RAM    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  Technologies: Talos Linux | Cilium eBPF | Istio Ambient   │
└─────────────────────────────────────────────────────────────┘
```

### Why This Matters

- **Real Hardware**: Physical servers, not cloud VMs - demonstrates bare-metal skills
- **High Availability**: 3-node quorum tolerates single node failure
- **Production Workload**: 30+ applications running 24/7 with real traffic
- **Enterprise Stack**: Same tools used in Fortune 500 companies

---

## Key Technical Decisions

### 1. Talos Linux - Immutable Infrastructure
**Decision**: API-driven immutable OS instead of traditional Linux distributions

**Skills Demonstrated**:
- Infrastructure as Code philosophy
- Immutable infrastructure patterns
- API-driven operations
- Minimal attack surface design

**Why It Matters**: Shows understanding of modern OS design principles and security-first thinking.

### 2. Cilium with eBPF - Advanced Networking
**Decision**: Replace kube-proxy with Cilium's eBPF-based dataplane

**Skills Demonstrated**:
- eBPF (Extended Berkeley Packet Filter) technology
- Kernel-level networking optimization
- Network policy implementation (L3-L7)
- Observability with Hubble

**Why It Matters**: eBPF is cutting-edge technology used by Netflix, Meta, Google. Demonstrates deep Linux networking knowledge.

### 3. Istio Ambient Mode - Modern Service Mesh
**Decision**: Sidecar-less service mesh using Istio's Ambient architecture

**Skills Demonstrated**:
- Service mesh architecture patterns
- mTLS implementation
- Zero-trust networking
- Traffic management

**Why It Matters**: Shows awareness of latest cloud-native trends and ability to implement complex distributed systems.

---

## Project Portfolio

This infrastructure hosts multiple demonstration projects:

| Project | Technologies | Purpose |
|:--------|:-------------|:--------|
| **This Portfolio** | MkDocs, Material, Nginx | Documentation showcase |
| **GitOps Demo** | ArgoCD, Helm, Kustomize | CI/CD patterns |
| **Observability Stack** | Prometheus, Grafana, Loki, Tempo | Monitoring expertise |
| **Security Platform** | CrowdSec, Authentik, Cilium | Defense in depth |
| **AI Chat with RAG** | Python, Vector DB, LLM | Modern AI integration |

---

## Measurable Results

| Metric | Achievement |
|:-------|:------------|
| **Uptime** | 99.9% target with real monitoring |
| **Applications** | 30+ services in production |
| **Security** | Zero successful intrusions, daily threat blocking |
| **Automation** | 100% GitOps - zero manual changes |
| **Learning** | Hands-on with enterprise tools daily |

---

## Learning Outcomes

This HomeLab demonstrates:

1. **Production Operations**: Real experience with incidents, updates, and maintenance windows
2. **Architecture Design**: Decision-making for scalable, secure systems
3. **Troubleshooting**: Complex distributed system debugging
4. **Automation**: Everything-as-code mindset
5. **Security**: Defense-in-depth implementation

---

## Related Documentation

- **Portfolio Page**: [`docs/projects/homelab.md`](docs/projects/homelab.md)
- **Live Cluster**: https://docs.arkenops.cc/projects/homelab/
- **Infrastructure Code**: https://github.com/palbina/HOMELAB-INFRA

---

*This document showcases infrastructure engineering capabilities through a real production environment.*
