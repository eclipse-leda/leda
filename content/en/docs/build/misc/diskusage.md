---
title: "Resource Consumptions"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# Baseline (no apps installed)

Baseline: 400 MB
Baseline after k3s started: 535 MB disk

Installed components:
- Container Management: runc, containerd, k3s
- System Services: systemd, openssh, mosquitto, mosquitto-clients
- No dapr
- No cloud connector or edgecontainerd yet.
- No self update agent
- No containers, no vehicle apps etc.

```
root@qemux86-64:/bin# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       2.5G  506M  1.8G  22% /
```

- Memory Usage: 200MB
```
root@qemux86-64:/var/lib/rancher/k3s/server# free
              total        used        free      shared  buff/cache   available
Mem:           1.9G      329.6M        1.4G       16.6M      222.2M        1.6G
Swap:    
```

# With dapr and pods

# With DAPR preinstalled, no pods yet
```
root@qemux86-64:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       2.5G  1.3G 1005M  57% /
```

```
root@qemux86-64:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           1.9G      812.7M       19.4M       18.1M        1.1G        1.1G
Swap:             0           0           0
```

# With DAPR, with cloud connector and vehicle update manager
```
root@qemux86-64:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       2.5G  2.2G   90M  97% /
```

```
root@qemux86-64:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           1.9G      849.5M      100.8M       26.6M        1.0G        1.1G
Swap:             0           0           0
```

# Details

Dependencies

- k3s (binary executable only): 140 MB
- cni (container networking): 51 MB
- containerd-ctr: 26 MB
- containerd: 46 MB
- dapr cli: 38 MB
- helm cli: 43 MB
- runc: 10 MB

SDV Components
- vehicle-data-cli: 2.3 MB (dynamic)


Medium:

- Linux Kernel (Poky minimal): 8 MB
- oci-image-tool: 9 MB
- oci-runtime-tool: 7 MB
- sshd: 1 MB
- libstdc++: 2 MB
- lic: 2 MB
- libcrypto: 3 MB
- containerd-shim: 7 MB
- containerd-shim-runc-v1: 9 MB
- containred-shim-runc-v2: 9 MB
- libsystemd: 1 MB
- busybox: 1 MB


