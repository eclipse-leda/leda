---
title: "Manual Provisioning"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

Follow these steps to do a manual device provisioning:

- Generate the device certificate (eg using openssl) and sign it with your CA.
- Log in to Azure Portal, Go to Azure Iot Hub and create a new device
- Select the proper authentication type, e.g. X.509 Self-signed or X.509 CA Signed
- Copy the device certificate (cert file and key file) to the device to `/data/var/certificate`
- Restart cloud connector service or container.

## Create a device in Azure IoT Hub

For the device to be connectable, it needs to be known to the cloud service first. In these steps, we will create a new device identity by using Azure IoT Hub.

**Pre-Requisites**:

- Virtual device must already be started with `runqemu ...` or `leda`
  
  *Note: For Raspberry Pi, please follow the manual steps below and adapt the SSH connection options to the IP of your Raspbery Pi.*
- The virtual device needs to be remotely accessible via ssh port `2222` on the host's `localhost` (Qemu port forwarding in userspace)
  or via ssh port `22` on the IP address `192.168.7.2` (Qemu virtual networking using TAP network interface)
- The container runtime needs to have started successfully, check with `sdv-health`
- A Device has been created in Azure IoT Hub

  *Note: Do **NOT** create an "edge" device.*

## Configure authentication on device

For the proper device authentication, the device management backend authority needs to issue a device-specific certificate and sign it. This is a complex process and subject to the specific situation.

For the Leda quickstart images, the software configuration is prepared with dummy certificates which need to be replaced.

> ATTENTION: The Leda example device certificates are public and insecure, they only serve demonstration purposes. You need to replace the intermediate certificates and device certificates with your own.

- Generate a device certificate using openssl
- Sign it with your intermediate CA certificate
- Put it into `/data/var/certificate/`
- Restart the cloud connector service or container: `systemctl restart cloud-connector` or `kanto-cm restart -n cloud-connector`

When finished, continue with

- [Deploying a Vehicle App](/leda/docs/app-deployment/)
- [Performing a Self Update](/leda/docs/device-provisioning/self-update/self-update-tutorial/)

## Private container registries

Please refer to the [Kanto Container Management documentation](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-manager-config/) on how to configure private container registries.
