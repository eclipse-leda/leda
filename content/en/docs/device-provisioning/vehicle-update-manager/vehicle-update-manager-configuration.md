---
title: "Configuration"
date: 2022-072109T14:24:56+05:30
weight: 1
---

**Note: This part of the Leda meta-layer and quickstart image is currently under active development and this documentation page may not represent the actual state of VUM**

The vehicle update manager container requires the following configuration:
- Container needs to run in **privileged mode** to enable automatic reboot.

  *Note: This is enabled by default on the Leda Quickstart images to simplify automated testing.*

- **Connection to MQTT broker**, defaults to `THINGS_CONN_BROKER=tcp://mosquitto:1883`
- **Enable container orchestration** feature: `THINGS_FEATURES=ContainerOrchestrator`

Optional configuration options are:

`SELF_UPDATE_ENABLE_REBOOT=true`
: Enable automatic reboot after a successfull application of the update bundle.

`SELF_UPDATE_TIMEOUT=30m`
: Timeout for downloading and installing an update bundle.


# Example Deployment Specification

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vehicle-update-manager
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vehicle-update-manager
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vehicle-update-manager
subjects:
- kind: ServiceAccount
  name: vehicle-update-manager
  namespace: default
roleRef:
  kind: ClusterRole
  name: vehicle-update-manager
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vehicle-update-manager
spec:
  selector:
    matchLabels:
      component: vehicle-update-manager
  template:
    metadata:
      labels:
        component: vehicle-update-manager
    spec:
      serviceAccountName: vehicle-update-manager
      containers:
        - name: vehicle-update-manager
          image: <repository>/vehicleupdatemanager:<tag>
          imagePullPolicy: IfNotPresent
          securityContext:
            privileged: true
          env:
            - name: SELF_UPDATE_TIMEOUT
              value: 30m
            - name: SELF_UPDATE_ENABLE_REBOOT
              value: "true"
            - name: THINGS_CONN_BROKER
              value: tcp://mosquitto:1883
            - name: THINGS_FEATURES
              value: ContainerOrchestrator
          volumeMounts:
          - mountPath: /proc
            name: proc
      volumes:
      - hostPath:
          path: /proc
        name: proc
      imagePullSecrets:
        - name: ghcr-io
```