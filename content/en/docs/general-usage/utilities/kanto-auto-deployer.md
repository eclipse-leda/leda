---
title: "Kanto Auto Deployer"
date: 2022-05-09T14:24:56+05:30
weight: 7
---

Automatically deploys containers to the Kanto Container Management based on deployment descriptors from a given path.
All deployment descriptors in the manifests folder will be deployed (created and started) on startup of the service.

> Note: The Kanto-CM and Kanto-Auto-Deployer container manifest descriptors (json) formats are incompatible and differ slightly in their structure!

## Usage

Usage:

```shell
root@qemux86-64:~# kanto-auto-deployer --help
USAGE:
  kanto-auto-deployer [PATH TO MANIFESTS FOLDER]
```

Example:

```shell
# Use container manifests from current working directory
/var/containers/manifests_dev/ $ kanto-auto-deployer
Reading manifests from [.]
Already exists [cloudconnector]
Already exists [otelcollector]
Already exists [seatservice-example]

# Use container manifests from specified directory
~ $ kanto-auto-deployer /var/containers/manifests_dev/
Reading manifests from [/data/var/containers/manifests_dev/]
Already exists [cloudconnector]
Already exists [otelcollector]
Already exists [seatservice-example]
```

## Usage as systemd service

In the Leda quickstart images, kanto-auto-deployer is installed as a systemd service.
The service unit configuration file is located in `/lib/systemd/system/kanto-auto-deployer.service`:

```shell
[Unit]
Description=Kanto Auto Deployer
After=network-online.target container-management.service
Wants=network-online.target container-management.service
Requires=container-management.service

[Install]
WantedBy=multi-user.target

[Service]
Restart=on-failure
RestartSec=5s
ExecStart=/usr/bin/kanto-auto-deployer /data/var/containers/manifests_dev
```

Example output:

```shell
root@qemux86-64:/lib/systemd/system# systemctl status kanto-auto-deployer.service 
* kanto-auto-deployer.service - Kanto Auto Deployer
     Loaded: loaded (/lib/systemd/system/kanto-auto-deployer.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Fri 2022-12-09 09:41:42 UTC; 7min ago
    Process: 472 ExecStart=/usr/bin/kanto-auto-deployer /var/containers/manifests (code=exited, status=0/SUCCESS)
   Main PID: 472 (code=exited, status=0/SUCCESS)

Dec 09 09:41:33 qemux86-64 systemd[1]: Started Kanto Auto Deployer.
Dec 09 09:41:33 qemux86-64 kanto-auto-deployer[472]: Creating [databroker]
Dec 09 09:41:41 qemux86-64 kanto-auto-deployer[472]: Created [databroker]
Dec 09 09:41:41 qemux86-64 kanto-auto-deployer[472]: Starting [databroker]
Dec 09 09:41:42 qemux86-64 kanto-auto-deployer[472]: Started [databroker]
Dec 09 09:41:42 qemux86-64 systemd[1]: kanto-auto-deployer.service: Deactivated successfully.
```