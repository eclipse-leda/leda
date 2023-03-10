---
title: "CAN Forward"
date: 2022-05-09T14:24:56+05:30
weight: 6
---

The `can-forward` help script can be used to forward an existing CAN-Bus interface on the host system to a container process.

> Note: Warning! The script does not yet support Kanto (or containerd) as a container runtime. It has been implemented for k3s.

## Usage

```shell
root@qemux86-64:~# can-forward --help

Usage:  /usr/bin/can-forward {-h} {-p PID} {-c container} <hw_can>

  hw_can          Host CAN hw interface to forward. Default: can0
  -c container    Attemmpt to get netns PID from a running container: (docker, ctr). Default: seat_service
  -p PID          Use provided PID for transferring vxcan interface (e.g.: docker inspect -f '{{ .State.Pid }}' container)
  -h              Prints this message
```

The script performs the following steps:

- Find the process ID of the target container process
- Check and modprobe `vxcan`
- Check and modprobe `can-gw`
- Create a new virtual CAN interface (`vxcanX`)
- Create a new virtual CAN interface (`vxcanX+1`)
- Link both interfaces together
- Move the second interface (`vxcanX+1`) into the namespace of the target container
- Set up a bi-directional CAN-Bus packet forwarding between both interfaces using `cangw`
