---
title: "DAPR Installation"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# Initial configuration
- To initialize DAPR, run:
```
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
/dapr init -k
```
- For accessing private container registries, create `/etc/rancher/k3s/registries.yml`:
Example for accessing GitHub Packages container registry at ghcr.io:
```
configs:
  "ghcr.io":
    auth:
      username: <<github-username>>
      password: <<github-personal-access-token>>
```
*Note:* Ensure the Personal Access Token has the permission to access GitHub packages
- Get your Azure IoT Hub Connection String and base64 it:
```
echo "<<AzureIoTHubConnectionString>>" | base64 -w 0
```
  Put the encoded result into `/var/lib/rancher/k3s/server/manifest/cloud-connector.secret.yaml` (rename from template)
- Verify that credentials have been crated: `kubectl get secrets cloudagent`
- Restart k3s: `systemctl restart k3s`
- Manually start the k3s agent:
```
k3s agent -s https://10.0.2.15:6443 -lb-server-port 6445 -t $(cat /var/lib/rancher/k3s/server/node-token)
```