---
title: "Kanto Auto Deployer (KAD)"
date: 2022-05-09T14:24:56+05:30
weight: 7
---

Automatically deploys containers to the Kanto Container Management based on deployment descriptors from a given path.
All deployment descriptors in the manifests folder will be deployed (created and started) on startup of the service.
The directory will then be monitored for creation of/changes to manifests and those changes will be redeployed.

## Usage

Usage:

```shell
$ kanto-auto-deployer --help
kanto-auto-deployer 0.2.0
Automated deployment of Kanto Container Management Manifests

USAGE:
    kanto-auto-deployer [OPTIONS] [MANIFESTS_PATH]

ARGS:
    <MANIFESTS_PATH>    Set the path to the directory containing the manifests [default: .]

OPTIONS:
    -d, --daemon                   Run as a daemon that continuously monitors the provided path for
                                   changes
    -h, --help                     Print help information
    -s, --socket-cm <SOCKET_CM>    Set the path to the Kanto Container Management API socket
                                   [default: /run/container-management/container-management.sock]
    -V, --version                  Print version information
```

Example:

```shell
# Use container manifests from current working directory
root@qemux86-64:/data/var/containers/manifests# kanto-auto-deployer 
[2023-04-18T10:27:21Z INFO  kanto_auto_deployer] Running initial deployment of "/data/var/containers/manifests"
[2023-04-18T10:27:21Z INFO  kanto_auto_deployer] Reading manifests from [/data/var/containers/manifests]
[2023-04-18T10:27:21Z WARN  kanto_auto_deployer::manifest_parser] Failed to load manifest directly. Will attempt auto-conversion from init-dir format.
[2023-04-18T10:27:21Z INFO  kanto_auto_deployer] Already exists [cloudconnector]
[2023-04-18T10:27:21Z WARN  kanto_auto_deployer::manifest_parser] Failed to load manifest directly. Will attempt auto-conversion from init-dir format.
[2023-04-18T10:27:21Z INFO  kanto_auto_deployer] Already exists [databroker]

# Use container manifests from specified directory
root@qemux86-64:~# kanto-auto-deployer /data/var/containers/manifests/
[2023-04-18T10:27:44Z INFO  kanto_auto_deployer] Running initial deployment of "/data/var/containers/manifests"
[2023-04-18T10:27:44Z INFO  kanto_auto_deployer] Reading manifests from [/data/var/containers/manifests]
[2023-04-18T10:27:44Z WARN  kanto_auto_deployer::manifest_parser] Failed to load manifest directly. Will attempt auto-conversion from init-dir format.
[2023-04-18T10:27:44Z INFO  kanto_auto_deployer] Already exists [cloudconnector]
[2023-04-18T10:27:44Z WARN  kanto_auto_deployer::manifest_parser] Failed to load manifest directly. Will attempt auto-conversion from init-dir format.
[2023-04-18T10:27:44Z INFO  kanto_auto_deployer] Already exists [databroker]
```

> Nоte: The warnings from the manifest_parser module are normal and expected when the manifest is in the [Container Management Manifests Format](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-config/#template)

## Usage as systemd service

In the Leda quickstart images, kanto-auto-deployer is installed as a systemd service. 
> Note the service uses the `--daemon` flag that asks KAD to continously monitor the specified directory (see last line of logs).

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
ExecStart=/usr/bin/kanto-auto-deployer /data/var/containers/manifests --daemon
```

Example output:

```shell
root@qemux86-64:/lib/systemd/system# systemctl status kanto-auto-deployer.service 
* kanto-auto-deployer.service - Kanto Auto Deployer
     Loaded: loaded (/lib/systemd/system/kanto-auto-deployer.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2023-04-18 10:22:10 UTC; 3min 55s ago
   Main PID: 525 (kanto-auto-depl)
      Tasks: 10 (limit: 4708)
     Memory: 1.4M
     CGroup: /system.slice/kanto-auto-deployer.service
             `- 525 /usr/bin/kanto-auto-deployer /data/var/containers/manifests --daemon

Apr 18 10:22:48 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:22:48Z INFO  kanto_auto_deployer] Creating [sua]
Apr 18 10:23:04 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:04Z INFO  kanto_auto_deployer] Created [sua]
Apr 18 10:23:04 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:04Z INFO  kanto_auto_deployer] Starting [sua]
Apr 18 10:23:05 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:05Z INFO  kanto_auto_deployer] Started [sua]
Apr 18 10:23:05 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:05Z WARN  kanto_auto_deployer::manifest_parser] Failed to load manifest directly. Will attempt auto-conversion from init-dir format.
Apr 18 10:23:05 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:05Z INFO  kanto_auto_deployer] Creating [vum]
Apr 18 10:23:10 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:10Z INFO  kanto_auto_deployer] Created [vum]
Apr 18 10:23:10 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:10Z INFO  kanto_auto_deployer] Starting [vum]
Apr 18 10:23:11 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:11Z INFO  kanto_auto_deployer] Started [vum]
Apr 18 10:23:11 qemux86-64 kanto-auto-deployer[525]: [2023-04-18T10:23:11Z INFO  kanto_auto_deployer] Running in daemon mode. Continuously monitoring "/data/var/containers/manifests"
```