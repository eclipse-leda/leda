---
title: "Resource Consumptions"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Baseline (no apps installed)

Baseline: 400 MB

Installed components:

- Container Management: runc, containerd, container-management
- System Services: systemd, openssh, mosquitto, mosquitto-clients
- No cloud connector or edgecontainerd yet.
- No self update agent
- No containers, no vehicle apps etc.

```bash
root@qemux86-64:/bin# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       2.5G  506M  1.8G  22% /
```

- Memory Usage: 200MB

```bash
root@qemux86-64:/# free
            total        used        free      shared  buff/cache   available
Mem:           1.9G      329.6M        1.4G       16.6M      222.2M        1.6G
Swap:    
```

## Component Details

Dependencies

- cni (container networking): 51 MB
- containerd-ctr: 26 MB
- containerd: 46 MB
- dapr cli: 38 MB
- helm cli: 43 MB
- runc: 10 MB

SDV Components

- vehicle-data-cli: 2.3 MB (dynamic)

Medium:

- Linux Kernel (Poky minimal / Leda distro kernel): 8 MB / 21 MB
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
