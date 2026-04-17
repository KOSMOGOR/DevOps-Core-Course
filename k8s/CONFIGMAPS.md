# Lab 12

## 1. Application Changes

Visits stored in file `/data/visits`. This file is read and written after every root endpoint access. Concurrent accesses handled with use of Lock.

Evidence:

```bash
$ curl http://localhost:8000/visits
{"visits":1}
```

## 2. ConfigMap Implementation

ConfigMap implementation includes:

- `devops-info-chart/files/config.json` file with config
- `devops-info-chart/templates/configmap.yaml` file with `ConfigMap`s for config and env
- `devops-info-chart/templates/pvc.yaml` file with `PersistentVolumeClaim`

`config.json` contains app name, enviroment, featureflags and some settings.

Config `ConfigMap` is mounted in `devops-info-chart/templates/deployment.yaml` file, in volume section. Volume for container is mounted in the same file, in `volumeMounts` section.

Evidence:

```bash
$ kubectl get configmap -n myapp
NAME                                   DATA   AGE
configmap/myapp-devops-info-config     1      21s
configmap/myapp-devops-info-env        5      21s
```

## 3. Persistent Volume

Persistent Volume configuration includes name, access mode, storage size. As access mode was chosen `ReadWriteOnce`, since we need both reading and writing to volume.

Volume mount configuration includes only mount path, since we also need to write to it.

Evidence:

```bash
$ kubectl exec <pod> -- cat /data/visits
2

$ kubectl delete pod <pod>
pod "<pod>" deleted from <namespace> namespace

$ kubectl exec <pod> -- cat /data/visits
2
```

## 4. ConfigMap vs Secret

ConfigMap (as stated in name) is better for configs, since data is not secured in it by default.

Secret (as stated in name) is better for secrets, since data is secured in it by default.
