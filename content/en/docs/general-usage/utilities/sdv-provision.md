---
title: "SDV Provision"
date: 2022-05-09T14:24:56+05:30
weight: 4
---

The provisioning helper script can be used to manually perform a device provisioning with a cloud backend.

It is meant as a convenient tool for developers, who wish to connect their device to a selfmanaged cloud backend directly.
In a production environment, the device provisioning functionality is implemented either by the *Cloud Connector* component.

The provisioning script currently supports the following backend and authentication options:

- Azure IoT Hub
  - Connection String
  - Device Certificates
- Azure IoT Device Provisioning Service
  - Device Certificates

## Usage

The *sdv-provision* script is interactive and asks for the type of backend and authentication option:

```shell
root@qemux86-64:~# sdv-provision 
Checking Eclipse Leda Device Provisioning configuration...
- Certificates directory exists
Checking Device ID
- Based on network device: eth0
- Device ID: 52-54-21-4c-f9-5a
Checking whether either IdScope or ConnectionString is configured
 - Neither Id Scope file nor ConnectionString found, needs manual configuration
Do you want to use the global Azure IoT Device Provisioning Service (DPS) by using an Id Scope, or do you want to use a direct connection to a specific Azure IoT Hub using a Connection String?
d) Azure IoT Device Provisioning Service (DPS) with Id Scope
h) Azure IoT Hub with Connection String
Choose:d
Please enter your Id Scope of the Azure IoT Device Provisioning Service:example
Recreating the Cloud Connector container...
Checking device certificates
- All device certificates are present
- Primary device certificate: /data/var/certificates/device.crt
- Primary device private key: /data/var/certificates/device.key
- Secondary device certificate: /data/var/certificates/device2.crt
- Secondary device private key: /data/var/certificates/device2.key
Fingerprints (add these to the Azure IoT Hub Device)
- Primary thumbprint: 1B172ED3D06F4E25AFFEF675ADCE519457FFFFFF
- Secondary thumbprint: B6CD5EACE96E9D0448BCB0BAED2DEE87AFFFFFFF
```

Once a configuration has been selected, the script will:

- Generate a random Device Id (based on physical network address)
- Store the Device Id in `/etc/deviceid`
- Generate a primary self-signed device certificate pair
- Generate a secondary self-signed device certificate pair
- Store the certificates in `/data/var/certificates/`
- Reconfigure the container descriptor in `/data/var/containers/manifests_dev/cloudconnector.json`
- Restarting the Cloud Connector container
- Print the key fingerprints, used for onboarding the device in Azure IoT Device Provisioning Service

## Reconfiguration

> Note: Re-running the script will only print the existing configuration.

To reconfigure the device and use different options, perform the following steps:

1. Delete the generated files

   ```shell
   rm /data/var/certificates/azure.idscope
   rm /data/var/certificates/azure.connectionstring
   rm /data/var/certificates/device*.crt
   rm /data/var/certificates/device*.key
   ```

2. Rerun the script

   ```shell
   sdv-provision
   ```
