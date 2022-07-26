---
title: "Provisioning Raspberry Pi"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

As your Raspberry Pi device might not be reachable via network, you can configure the initial credentials by specifying them as a Kubernetes resource file, copy the files to the FAT32 Boot Partition and then apply them on the offine device.

## Pre-Requisites

- Online connection to device or physical access to the device
- Device clock needs to be in sync - Verify with `timedatectl` or `systemctl status systemd-timesyncd`
- Installed `kubectl` on your workstation - See [Installing kubectl](https://kubernetes.io/docs/tasks/tools/)
  
  *Note:* If you do not have kubectl at hand, an alternative way is to [deploy secrets using Kubernetes Configuration files](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/).

## Secret for Cloud Connector

- Put the SD-Card into your card reader
  - Windows: Look for a new drive in Windows Explorer `F: [boot]`
  - Linux: Mount the SD Card
- Create a new secret file for the Cloud Connection:
```
$ kubectl create secret generic cloudagent \
 --dry-run=client \
 --from-literal=PrimaryConnectionString="{{Connection String}}" \
 -o yaml > cloudagent-secret.yaml
```
- For each private Container Registry, create an an additional yaml file to specify the credentials:
```
$ kubectl create secret docker-registry ghcr-io \
--dry-run=client \
--docker-server=ghcr.io \
--docker-username="<USERNAME>" \
--docker-password="<PASSWORD>" \
-o yaml > ghcr-io-secret.yaml
```
- Copy the secret files to the boot partition of the SD Card
- Boot the SD-Card on the Raspberry Pi
- Login as `root` without password on login prompt
- Apply the Kubernetes configuration specifications:
```
root@raspberrypi4-64:~# kubectl apply -f /boot/cloudagent-secret.yaml
root@raspberrypi4-64:~# kubectl apply -f /boot/ghcr-io-secret.yaml
```
- You may need to restart the pods for the changes to take effect:
```
root@raspberrypi4-64:~# kubectl delete pod cloud-connector
root@raspberrypi4-64:~# kubectl apply -f /var/lib/rancher/k3s/server/manifests/cloud-connector.podspec.yaml
```
- Verify and wait until k3s is started: `systemctl status k3s`
- *Optional:* Check the system health: `sdv-health`

  *Note: The status of some pods and the cloud connector are expected to
  stay in _**FAILED**_ status as long as the **Device Provisioning** steps are not completed.*

- Continue with [Deploying a Vehicle App](/leda/docs/app-deployment/)
