---
title: "Velocitas VApps"
date: 2022-05-09T14:24:56+05:30
---

For local deployment without a cloud backend, deployment specifications for [Eclipse Velocitas](https://projects.eclipse.org/projects/automotive.velocitas) Vehicle Apps may be put directly onto the device.

- Create a Kubernetes deployment specification for your vehicle app
- Copy the specification file to the device, e.g. `scp -P 2222 myapp.yaml root@localhost`
- Apply the specification: `ssh -p 2222 root@localhost /usr/local/bin/kubectl apply -f myapp.yaml`

## Example Pod Specification
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-example-app
  annotations:
    dapr.io/enabled: "true"
    dapr.io/app-id: "my-example-app"
    dapr.io/app-port: "50008"
    dapr.io/log-level: "info"
    dapr.io/app-protocol: "grpc"
spec:
  restartPolicy: Always
  hostAliases:
  - ip: "10.0.2.15"
    hostnames:
    - "edgehost"
  containers:
    - name: my-example-app
      image: my-private-container-registry.azurecr.io/my-example-app:latest
      imagePullPolicy: IfNotPresent
      ports:
        - containerPort: 50008
      env:
        - name: SEAT_SERVICE_ADDRESS
          value: "edgehost:50051"
  imagePullSecrets:
  - name: my-private-container-registry-secret
```
