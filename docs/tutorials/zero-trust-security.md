# Tutorial: Zero Trust Security

Aprende a construir una arquitectura de seguridad multicapa siguiendo el principio Zero Trust: "nunca confiar, siempre verificar". Defensa en profundidad desde el edge hasta el pod.

!!! info "Público objetivo"
    Necesitas un cluster Kubernetes funcional con acceso a Cloudflare para la capa de edge. Conocimiento básico de conceptos de red y seguridad.

---

## ¿Qué vas a construir?

Una arquitectura de seguridad en 5 capas independientes:

1. **Edge**: Cloudflare WAF + Tunnel (zero-port exposure)
2. **Ingress**: CrowdSec IPS con bloqueo colaborativo de amenazas
3. **Network**: Cilium NetworkPolicies con default-deny
4. **Service**: Istio mTLS automático entre servicios
5. **Identity**: Authentik SSO con OIDC

---

## Prerrequisitos

- [x] Cluster Kubernetes con Cilium CNI y Istio Ambient
- [x] Cuenta de Cloudflare con dominio configurado
- [x] `helm` instalado
- [x] `cloudflared` CLI instalado

---

## Fase 1: Cloudflare Edge Protection

### Paso 1: Configurar Cloudflare WAF

En el dashboard de Cloudflare, configura las reglas de WAF:

- **Rate Limiting**: 100 requests/minuto por IP
- **Bot Fight Mode**: Enabled
- **DDoS Protection**: Automatic (incluido en todos los planes)

### Paso 2: Crear Cloudflare Tunnel (Zero-Port Exposure)

```bash
# Autenticar cloudflared
cloudflared tunnel login

# Crear el túnel
cloudflared tunnel create homelab

# Configurar DNS para el túnel
cloudflared tunnel route dns homelab homelab.example.com

# Desplegar cloudflared en el cluster
kubectl create secret generic tunnel-credentials \
  --from-file=credentials.json=/home/tu-usuario/.cloudflared/<tunnel-id>.json

# El túnel expone tus servicios sin abrir puertos en el firewall
```

!!! info "Zero-Port Exposure"
    Cloudflare Tunnel crea una conexión saliente desde tu cluster hacia Cloudflare. No necesitas abrir puertos en tu firewall ni exponer IPs públicas. Cloudflare maneja el tráfico entrante y lo enruta por el túnel de forma segura.

---

## Fase 2: CrowdSec IPS

### Paso 3: Instalar CrowdSec

```bash
# Instalar CrowdSec Agent
helm install crowdsec crowdsec/crowdsec \
  --namespace security \
  --create-namespace \
  --set agent.acquisition[0].namespace=ingress \
  --set agent.acquisition[0].podName=traefik-*
```

### Paso 4: Instalar el Bouncer para Traefik

```bash
# Obtener API key de CrowdSec
kubectl exec -n security deployment/crowdsec -- \
  cscli bouncers add traefik-bouncer

# Instalar el bouncer que bloquea IPs maliciosas en Traefik
helm install crowdsec-traefik-bouncer \
  crowdsec/crowdsec-traefik-bouncer \
  --namespace security \
  --set crowdsec.lapiKey=<API_KEY_DEL_PASO_ANTERIOR>
```

### Paso 5: Verificar CrowdSec

```bash
# Ver decisiones de bloqueo
kubectl exec -n security deployment/crowdsec -- cscli decisions list

# Ver estadísticas
kubectl exec -n security deployment/crowdsec -- cscli metrics
```

!!! success "Inteligencia Colaborativa"
    CrowdSec comparte señales de ataque de forma anónima con una red global. Si una IP ataca a otro usuario de CrowdSec, tu instancia la bloquea automáticamente sin haberla visto antes. Es inmunidad colectiva para ciberseguridad.

---

## Fase 3: Cilium NetworkPolicies

### Paso 6: Aplicar Default-Deny

Crea una política que bloquee todo el tráfico por defecto y solo permita lo necesario:

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: default-deny-all
  namespace: default
spec:
  endpointSelector: {}
  ingress:
    - fromEndpoints:
        - matchLabels:
            io.kubernetes.pod.namespace: istio-system
  egress:
    - toEndpoints:
        - matchLabels:
            k8s:io.kubernetes.pod.namespace: kube-system
      toPorts:
        - ports:
            - port: "53"
              protocol: UDP
```

Aplica la política:

```bash
kubectl apply -f default-deny-policy.yaml
```

### Paso 7: Verificar las Políticas

```bash
# Ver políticas de Cilium
cilium policy get

# Visualizar tráfico con Hubble
hubble observe --namespace default
```

---

## Fase 4: Istio mTLS

### Paso 8: Habilitar mTLS Estricto

```yaml
# peer-authentication.yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

Aplica la autenticación:

```bash
kubectl apply -f peer-authentication.yaml

# Verificar estado de mTLS
istioctl authn tls-check
```

!!! info "¿Qué hace mTLS?"
    Mutual TLS encripta y autentica ambas direcciones de la comunicación entre servicios. Cada servicio presenta un certificado que prueba su identidad. Incluso si un atacante compromete un pod, no puede comunicarse con otros servicios sin un certificado válido emitido por Istio.

---

## Fase 5: Authentik SSO

### Paso 9: Desplegar Authentik

```bash
helm install authentik authentik/authentik \
  --namespace auth \
  --create-namespace \
  --set authentik.secret_key=$(openssl rand -base64 36) \
  --set authentik.error_reporting.enabled=false
```

### Paso 10: Configurar OIDC para tus Aplicaciones

En la UI de Authentik:

1. Crea un **Provider** de tipo OAuth2/OIDC
2. Crea una **Application** vinculada al provider
3. Configura el redirect URI de tu aplicación
4. Copia el Client ID y Client Secret

---

## Verificación Final

```bash
# Verificar que todas las capas están activas
kubectl get pods -n security
kubectl get pods -n auth
cilium policy get
istioctl authn tls-check

# Probar bloqueo de IP
cscli decisions list  # Deberías ver IPs bloqueadas
```

---

## ¿Qué sigue?

- :fontawesome-solid-arrow-right: Leer la explicación del [modelo Zero Trust](../explanation/zero-trust-model.md)
- :fontawesome-solid-arrow-right: Configurar [backup y disaster recovery](../how-to/backup-velero.md)
- :fontawesome-solid-arrow-right: Ver el [proyecto de seguridad](../projects/security.md)

---

## Referencias

- [Cloudflare Documentation](https://developers.cloudflare.com/)
- [CrowdSec Documentation](https://docs.crowdsec.net/)
- [Cilium Security Policies](https://docs.cilium.io/en/stable/security/policy/)
- [Istio Security](https://istio.io/latest/docs/concepts/security/)
- [Authentik Documentation](https://goauthentik.io/docs/)
