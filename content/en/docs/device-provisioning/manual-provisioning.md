---
title: "Manual Provisioning"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

Follow these steps to do a manual device provisioning:

- Log in to Azure Portal
- Go to Azure Iot Hub
- Create a new device (Note: Do **not** create an *edge* device)
- Copy the *Primary Connection String*
- Create a Kubernetes Secret with the name `cloudagent` by using `kubectl` on the device

Alternatively, on command line:
- Install Azure CLI: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
- Allow automated installation of extensions: `az config set extension.use_dynamic_install=yes_without_prompt`
- Login to Azure: `az login`
- Select the correct subscription: `az account set --subscription <<subscription>>`
- Create device: `az iot hub device-identity create -n {iothub_name} -d {device_id}`
- Show connection string: `az iot hub device-identity connection-string show -n {iothub_name} -d {device_id} -o tsv`
- Create a Kubernetes Secret
```
ssh -p 2222 root@localhost /usr/local/bin/kubectl create secret generic cloudagent \
            --from-literal=PrimaryConnectionString='<<Connection String>>'
```

# Configure credentials for private container registries

For each private container registry, a separate Secret is needed.
For GitHub, your Personal Access Token requires the `read:packages` permission.

```
ssh -p 2222 root@localhost /usr/local/bin/kubectl create secret docker-registry ghcr-io \
    --docker-server=ghcr.io \
    --docker-username=<your github username> \
    --docker-password=<your github personal access token>
```

If you have additional project-specific container registries, you may need to add them as well:
```
ssh -p 2222 root@localhost /usr/local/bin/kubectl create secret docker-registry azurecr \
    --docker-server=<your cr>.azurecr.io \
    --docker-username=<username> \
    --docker-password=<password>
```
The Pod specifications need to reference the image pull secret:

```
apiVersion: v1
kind: Pod
metadata:
  name: ...
spec:
  containers:
    - name: ...
      image: ...
  imagePullSecrets:
  - name: azurecr
```

## Verifying correct configuration

- Check that the secret `cloudagent` has been deployed:
```
root@qemux86-64:~# kubectl get secrets
NAME                  TYPE                                  DATA   AGE
default-token-pmtd9   kubernetes.io/service-account-token   3      47m
cloudagent            Opaque                                1      10s
```
- Check that the SDV Cloud Agent pod has been deployed and started:
```
root@qemux86-64:~# kubectl describe pod cloud-connector
Name:         cloud-connector
Namespace:    default
Priority:     0
Node:         qemux86-64/10.0.2.15
...
Status:       Running
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
```
