---
title: "Cheatsheet"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

This cheat sheet gives you an overview of common command line commands to interact with the tools available on the quickstart image.

| Category | Task | Command |
| --- | --- | --- |
| General | Overall info | `sdv-health` |
| | Show device info | `sdv-device-info` |
| | Device provisioning | `sdv-provision` |
| | Switch Keyboard layout | `loadkeys de` |
| Kanto-CM | Show all containers| `kanto-cm list` |
| | User interface | `kantui` |
| | Service logs | `journalctl -f -l -t container-management` |
| | Auto deployments | See `/data/containers/manifests/` |
| | Restart a container | `kanto-cm restart -n <containername>` |
| ContainerdD | Show images | `ctr --address /run/k3s/containerd/containerd.sock --namespace=kanto-cm i ls`
| | Import local archive | `ctr --address /run/k3s/containerd/containerd.sock --namespace=kanto-cm i import <docker.tar>`
| Mosquitto | Show all messages | `mosquitto_sub -v -t '#' -h localhost` |
| | Send message | `mosquitto_pub -t '<target/topic>' -h localhost -m '{"foo":"bar"}'` |
| | Connectivity status | `mosquitto_rr --quiet -h localhost -t 'edge/thing/request' -e 'edge/thing/response' -m ''`
| RAUC Self Update | Current boot status | `rauc status` |
| | Switch to other boot slot | `rauc status mark-active other` |
