---
title: "Cheatsheet"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

This cheat sheet gives you an overview of common command line commands to interact with the tools available on the quickstart image.

## General Commands

| Category | Task | Command |
| --- | --- | --- |
| General | Overall info | `sdv-health` |
| | Show device info | `sdv-device-info` |
| | Device provisioning | `sdv-provision` |
| | Switch Keyboard layout | `loadkeys de` |
| System | System load | `htop` |
| | Disk free | `df -h -t ext4` |
| | Memory free | `free -h` |
| Network | Interfaces summary | `networkctl` |
| | Ethernet status | `networkctl status enp0s2` |
| | Routing table | `route` |
| | Active listeners | `netstat -l -n -t` |
| Kanto-CM | Show all containers| `kanto-cm list` |
| | User interface | `kantui` |
| | Service logs | `journalctl -f -l -t container-management` |
| | Auto deployments | See `/data/var/containers/manifests/` |
| | Development deployments | See `/data/var/containers/manifests_dev/` |
| | Restart a container | `kanto-cm restart -n <containername>` |
| ContainerdD | Show images | `ctr --address /data/run/containerd/containerd/containerd.sock --namespace=kanto-cm i ls`
| | Import local archive | `ctr --address /data/run/containerd/containerd.sock --namespace=kanto-cm i import <docker.tar>`
| | Prune containers | `nerdctl system prune --all`
| Mosquitto | Show all messages | `mosquitto_sub -v -t '#' -h localhost` |
| | Send message | `mosquitto_pub -t '<target/topic>' -h localhost -m '{"foo":"bar"}'` |
| | Connectivity status | `mosquitto_rr --quiet -h localhost -t 'edge/thing/request' -e 'edge/thing/response' -m ''`
| RAUC Self Update | Current boot status | `rauc status` |
| | Switch to other boot slot | `rauc status mark-active other` |
| CAN-Bus | CAN Dump | `candump -l any,0:0,#FFFFFFFF` |

## Configuring NTP

A failed download of container images may be caused by out-of-sync clock, thus failing the TLS certificate validation.
A hardware device without hardware clock (such as the Raspberry Pi) relies on network time.
In some (corporate) networks, there might be rogue NTP servers and it might be necessary to override the NTP sources.

To reset NTP server to a public server, follow these steps:

```shell
# Check NTP clock sync
timedatectl timesync-status
# Add your NTP server
vi /etc/systemd/timesyncd.conf
# Restart container management
systemctl restart container-management
systemctl restart kanto-auto-deployer
```

## Reset container deployment

When things go really wrong and the container runtime is unable deploy containers properly, it may be necessary to reset the internal state.
This is achieved by stopping the container runtime(s) and deleting the `/var/lib/container-management` folder:

```shell
# Stop all container runtimes
systemctl stop container-management 
systemctl stop containerd

# Delete the persistence of container management
# Attention! Here be dragons
rm -rf /var/lib/container-management

# Restart the container runtimes
systemctl start containerd
systemctl start container-management

# Redeploy the containers
systemctl restart kanto-auto-deployer
```

## Running custom ad-hoc containers

To install arbitrary containers, create the container using the `kanto-cm` command line tool.
If it's not a background service, but a cli tool, adding the `--t --i` options allows console access.

```shell
root@qemux86-64:~# kanto-cm remove --name python
root@qemux86-64:~# kanto-cm create --name python --t --i --privileged docker.io/library/python:3.8.16-slim-bullseye
bf9deca4-dbf1-4132-9ba7-e0f378bd34a7
root@qemux86-64:~# kanto-cm start --name python --a --i
Python 3.8.16 (default, Jan 24 2023, 00:19:05) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```
