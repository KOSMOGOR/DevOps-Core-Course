# Lab 11

## 1. Kubernetes Secrets

Creating:

```bash
$ kubectl create secret generic app-credentials --from-literal=username=user --from-literal=password=pass
secret/app-credentials created
```

Viewing:

```bash
$ kubectl get secret app-credentials -o yaml
apiVersion: v1
data:
  password: cGFzcw==
  username: dXNlcg==
kind: Secret
metadata:
  creationTimestamp: "2026-04-05T11:01:47Z"
  name: app-credentials
  namespace: default
  resourceVersion: "2352"
  uid: 5123ab4a-3552-4648-bb9e-6b87d88f76f6
type: Opaque
```

Decoding:

```bash
$ echo dXNlcg== | base64 -d
user
```

base64 encoding can't secure your data, since anyone can just decode it. But encryption often requires key to decrypt, so it can be even safe to commit.

## 2. Helm Secret Integration

`devops-info-chart/templates` now includes `secrets.yml` and `serviceaccount.yml`.

During deployment secrets consumed in `devops-info-chart/templates/deployment.yml` file using `envFrom` form with `secretRef` argument.

Enviroment secrets are hidden:

```bash
$ kubectl describe <pod>
...
    Environment Variables from:
      myapp-devops-info-secret  Secret  Optional: false
    Environment:
      DEBUG:  false
...
```

## 3. Resource Management

Resources in `values.yaml` were increased since last lab to test new variables.

Requests vs limits for resources is like minimum allowed and maximum allowed.

Appropritate values can be chosen using tests (for example with `locust`).

## 4. Vault Integration

Vault installation:

```bash
$ kubectl get pods -l app.kubernetes.io/name=vault
NAME                                    READY   STATUS    RESTARTS   AGE
vault-0                                 1/1     Running   0          ...
vault-agent-injector-...                1/1     Running   0          ...
```

Policy:

```hcl
path "secret/data/devops-info/*" {
  capabilities = ["read"]
}
```

Role:

```bash
vault write auth/kubernetes/role/devops-info \
  bound_service_account_names=devops-info \
  bound_service_account_namespaces=default \
  policies=devops-info \
  ttl=24h
```

Enable the KV v2 engine and store the application secret:

```bash
vault secrets enable --path=secret kv-v2
vault kv put secret/myapp/config username="user" password="pass"
```

Secrets injected at `/vault/secrets/config`:

```bash
$ kubectl exec <pod> -- cat /vault/secrets/config
username=<sensitive>
password=<sensitive>
```

Sidecar pattern adds container, that authenticates to Vault and writes secret to the pod. Application read this file directly, without using the Vault.

## 5. Security Analysis

Vault is more secure, than K8s secrets, but requires more time to config.

Vault is better in situations when security is needed or this is big production deplot, K8s secrets are better for configs or in small deploys without security violations.

Never commit secrets to Git (production reccomendation).

## 6. Bonus Task - Vault Agent Templates

Template for file rendering is located inside `devops-info-chart/values.yaml` and then imported to `devops-info-chart/templates/deployment.yml`. Rendered file with contain `username` and `password`.

Agent allow dynamic secret rotation - changes secrets in runtime.
