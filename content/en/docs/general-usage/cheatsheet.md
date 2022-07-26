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
| Kubernetes | Check k3s status | `systemctl status k3s` |
| | k9s | `k9s` |
| | k3s service logs | `journalctl -f -l -t k3s` |
| | Show all Pods | `kubectl get pods -A` |
| | Pod details | `kubectl describe pod <podname>` |
| | Pod logs | `kubectl logs <podname> <containername>` |
| | Auto deployments | See `/var/lib/rancher/k3s/server/manifests/` |
| | Delete a Pod | `kubectl delete pod <podname>` |
| | Redeplod a Pod | `kubectl apply -f <podspec.yaml>` |
| | Shell in a Pod | `kubectl exec --stdin --tty <podname> -- /bin/sh` |
| | Cluster IP | `kubectl get svc clusterip` |
| ContainerdD | Show images | `ctr --address /run/k3s/containerd/containerd.sock --namespace=k8s.io i ls`
| | Import local archive | `ctr --address /run/k3s/containerd/containerd.sock --namespace=k8s.io i import <docker.tar>`
| DAPR | Reinstall | `dapr-init.sh` |
| Mosquitto | Show all messages | `mosquitto_sub -v -t '#' -h <MosquittoClusterIP>'` |
| | Send message | `mosquitto_pub -t '<target/topic>' -h <MosquittoClusterIP> -m '{"foo":"bar"}'` |
| | Mosquitto Cluster IP | `kubectl get svc mosquitto` |
| Cloud Connectivity | Cloud agent logs | `kubectl get logs sdv-core-cloud-agent` |
| | Connectivity status | `mosquitto_rr --quiet -h <MosquittoClusterIP> -t 'edge/thing/request' -e 'edge/thing/response' -m ''`
| RAUC Self Update | Current boot status | `rauc status` |
| | Switch to other boot slot | `rauc status mark-active other` |
