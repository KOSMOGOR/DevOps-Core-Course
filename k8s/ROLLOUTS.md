# Lab 14

## 1. Argo Rollouts Setup

Installation verification:

```bash
$ kubectl argo rollouts version
kubectl-argo-rollouts: v1.9.0+838d4e7
  BuildDate: 2026-03-20T21:15:27Z
  GitCommit: 838d4e792be666ec11bd0c80331e0c5511b5010e
  GitTreeState: clean
  GoVersion: go1.24.13
  Compiler: gc
  Platform: windows/amd64
```

Dashboard can be accessed on `http://localhost:3100` after `kubectl port-forward svc/argo-rollouts-dashboard -n argo-rollouts 3100:3100`.

Main difference between Deployment and Rollout - Rollout supports progressive delivery. But also it requires some additional fields in `strategy` section.

## 2. Canary Deployment

Canary configuration steps includes alternating `setWeight` and `pause` states for changing from old delivery to new.

Upgrading release created canary service:

```bash
$ helm upgrade --install myapp devops-info-chart -n dev -f devops-info-chart/values-dev.yaml
Release "myapp" has been upgraded. Happy Helming!
NAME: myapp
LAST DEPLOYED: Thu Apr 23 18:37:49 2026
NAMESPACE: dev
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
TEST SUITE: None

$ kubectl argo rollouts get rollout myapp-devops-info -n dev -w
Name:            myapp-devops-info
Namespace:       dev
Status:          ॥ Paused
Message:         CanaryPauseStep
Strategy:        Canary
  Step:          1/9
  SetWeight:     20
  ActualWeight:  50
Images:          kosmogor/devops:latest (canary, stable)
Replicas:
  Desired:       1
  Current:       2
  Updated:       1
  Ready:         2
  Available:     2

NAME                                           KIND        STATUS     AGE    INFO
⟳ myapp-devops-info                            Rollout     ॥ Paused   6m28s  
├──# revision:2                                                              
│  └──⧉ myapp-devops-info-5fdc684c6b           ReplicaSet  ✔ Healthy  107s   canary
│     └──□ myapp-devops-info-5fdc684c6b-z5zjk  Pod         ✔ Running  106s   ready:1/1
└──# revision:1                                                              
   └──⧉ myapp-devops-info-58fcbc4964           ReplicaSet  ✔ Healthy  6m28s  stable
      └──□ myapp-devops-info-58fcbc4964-r7br2  Pod         ✔ Running  6m28s  ready:1/1
```

Then, after release was promoted in UI:

```bash
$ kubectl argo rollouts get rollout myapp-devops-info -n dev -w
Name:            myapp-devops-info
Namespace:       dev
Status:          ✔ Healthy
Strategy:        Canary
  Step:          9/9
  SetWeight:     100
  ActualWeight:  100
Images:          kosmogor/devops:latest (stable)
Replicas:
  Desired:       1
  Current:       1
  Updated:       1
  Ready:         1
  Available:     1

NAME                                           KIND        STATUS        AGE    INFO
⟳ myapp-devops-info                            Rollout     ✔ Healthy     13m    
├──# revision:2                                                                 
│  └──⧉ myapp-devops-info-5fdc684c6b           ReplicaSet  ✔ Healthy     8m44s  stable
│     └──□ myapp-devops-info-5fdc684c6b-z5zjk  Pod         ✔ Running     8m43s  ready:1/1
└──# revision:1                                                                 
   └──⧉ myapp-devops-info-58fcbc4964           ReplicaSet  • ScaledDown  13m
```

Abortion during upgrading reverted app to state before upgrading.

## 3. Blue-Green Deployment

Blue-green configuration has `activeService`, `previewService`, `autoPromotionEnabled`, `previewReplicaCount` (for preview service size) and `scaleDownDelaySeconds` (for time after which old service will be scaled down).

Active service - is what users can access now, while preview service - new revision before deployment.

Upgrading release created preview service with new revision. It can be viewed using `kubectl port-forward svc/myapp-devops-info -n dev 8001:80` and checking `http://localhost:8001`.

Promoting app makes active service same as preview, but with different replica count.

## 4. Strategy Comparison

Canary should be good when new version is not very different from old and smooth transition is acceptable. Blue-green, in other hand, requires more resources (up to x2), but transitions instantly, also it allows to check preview.

Blue-green must be used, if viewing preview is necessary or smooth transition is not acceptable.

## 5. CLI Commands Reference

Useful commands:

- for installing/upgrading release: `helm upgrade --install myapp devops-info-chart -n dev`
- for deleting release: `helm uninstall myapp -n dev`
- for monitoring rollout status: `kubectl argo rollouts get rollout myapp-devops-info -n dev -w`
- for aborting rollout: `kubectl argo rollouts abort myapp-devops-info -n dev`
