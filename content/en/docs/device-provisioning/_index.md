---
title: "Device Provisioning"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

The device needs to be configured before it can make a connection to the cloud.

The following initial configuration steps are required:

- Create a device in Azure IoT Hub
- Configure authentication on device
- Configure credentials for accessing private container registries

## Create a device in Azure IoT Hub

For the device to be connectable, it needs to be known to the cloud service first. In these steps, we will create a new device identity by using Azure IoT Hub.

**Pre-Requisites**:

- Virtual device must already be started with `runqemu ...` or `leda`
  
  *Note: For Raspberry Pi, please follow the manual steps below and adapt the SSH connection options to the IP of your Raspbery Pi.*
- The virtual device needs to be remotely accessible via ssh port `2222` on the host's `localhost` (Qemu port forwarding in userspace)
  or via ssh port `22` on the IP address `192.168.7.2` (Qemu virtual networking using TAP network interface)
- The k3s service needs to have started successfully, check with `systemctl status k3s`
- A Device has been created in Azure IoT Hub

  *Note: Do **not** create an*edge*device.*

## Script on host system

*Note: For Linux hosts only. Alternatively, you can perform the steps [manually on command line](/leda/docs/device-provisioning/manual-provisioning/).*

Pre-Requisite:

- Install `jq` and `dialog` on your host:

      apt-get install jq dialog

- Run the provisioning script on your host system

      ./provision-device.sh

The script will:

- Remotely connect to the QEMU instance via `root@192.168.7.2`
- Install Azure CLI
- Ask you to login to Azure using the Device Code Flow
- Ask which Azure Subscription to use
- Ask which Azure IoT Hub the device shall connect to
- Ask which existing device to use or to create a new device
- Generate and retrieve the connection string secret
- Deploy the connection string to device as Kubernetes secret

*Note: Kubernetes will take some time before reconsidering a redeployment of failed pods. If you want to force a redeployment, use k9s to delete the failed pods. The Deployments will then ensure to recreate the pods with the new configurations.*

When finished, continue with

- [Deploying a Vehicle App](/leda/docs/app-deployment/)
- [Performing a Self Update](/leda/docs/device-provisioning/self-update/self-update-tutorial/)

## Script on guest system

*Note: When running the device provisioning from the guest, you need to manually retrieve the device secrets first.*

- Run the provisioning script on the guest system

      sdv-provision

The script will:

- Ask for an Azure IoT device *Connection String*
- Ask for credentials to access private container registries ('imagePullSecret')
- Deploy the connection string as Kubernetes secret
- Deploy the imagePullSecret as Kubernetes secret

*Note: Kubernetes will take some time before reconsidering a redeployment of failed pods. If you want to force a redeployment, use k9s to delete the failed pods. The Deployments will then ensure to recreate the pods with the new configurations.*

When finished, continue with

- [Deploying a Vehicle App](/leda/docs/app-deployment/)
- [Performing a Self Update](/leda/docs/device-provisioning/self-update/self-update-tutorial/)
