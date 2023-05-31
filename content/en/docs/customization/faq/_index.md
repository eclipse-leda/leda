---
title: "FAQ"
date: 2023-01-03T17:24:56+05:30
weight: 30
---

## Frequently Asked Questions

### **Why is the performance very slow?**

The performance of a system heavily relies on the infrastructure and the general setup.

- On virtual setup (QEMU): Typical reasons for slow performance are software emulation, e.g. when you run an ARM-based image on an x86-based host machine. This requires QEMU to emulate the execution, which is very slow. When you run an x86-based image on an x86-based host machine, QEMU can leverage acceleration, such as KVM, which greatly improves the performance. For network performance issues, try to use TAP networking instead of SLIRP networking for QEMU. That requires more setup on the host though.
- On hardware, such as Raspberry Pi, it should be fast. If the system startup takes very long, you may have an outdated image, please update to the latest version. Another cause of performance loss can be networking issues, especially if the system does not have transparent internet access, network requests (e.g. DNS) may time out and slowing down the startup. On startup, the container runtime may download newer versions of containers and unpack them, which takes a considerable amount of time depending on the size of the container images.

### **Why is my Bluetooth/Wifi driver missing?**

Please check the latest release, as we're continously adding features. If your driver is still missing, please [open a new GitHub Issue](https://github.com/eclipse-leda/leda-distro/issues/new/choose). We can add Kernel Modules for supported hardware. If you hardware is not supported out of the box by the Eclipse Leda project, you need to build your own image and customize the Linux Kernel configuration. Please see the [Yocto Project](https://www.yoctoproject.org/) documentation on how to do that.

### **How do I connect to a WiFi network?**

We use iwd/iwctl as high-level interfaces to manage wireless devices. For a guide on how to connect to a WiFi network with iwctl, you can check: [_Notes on using iwd/iwctl_](../wifi-configuration/iwd-iwctl).

### **How can a container access CAN-Bus interfaces?**

As using a CAN-Bus requires access to the host network interface, the container needs to run in privileged mode and it needs access to the host network interface. For a Kanto-CM container, simply add `privileged: true` to the [container configuration](https://eclipse.dev/kanto/docs/references/containers/container-config/). A more sophisticated setup involves using virtual CAN interfaces for each container and using a CAN gateway to route the traffic accordingly. However, using CAN-Bus is not in the focus of SDV-style applications, as we assume that *Vehicle Services* would be running on dedicated ECUs, offering higher-level interfaces to *Vehicle Applications* on other protocols, such as Some/IP.

```json
"host_config": {
...
"network_mode": "host",
"privileged": true,
...
}
```

### **Why does booting from SD-Card sometimes fail and enters maintenance mode?**

This may depend on the quality or age of the SD-Card as well. Also, consumer-grade hardware like a Raspberry Pi may fail at times. Please try another SD-Card. Another reason may be high write operations to the SD-Card due to excessive data transfer (logging, container deployment etc.).

### **How can I install additional software in Leda?**

As we're using Yocto, there is no central repository for software packages. Thus, we did not include any kind of package manager. If you feel that the software you want to install is valuable for other Leda users as well, please [open a new GitHub Issue](https://github.com/eclipse-leda/leda-distro/issues/new/choose) and request the installation of the software. If the software is specific to your use case, you need to build your own image using Yocto. Alternatively, you may build a container for your software and deploy the container into the container runtime. Using `kanto-cm` or `ctr` you would be able to execute your software as a container. See the [Cheatsheet](/leda/docs/general-usage/cheatsheet/#running-custom-ad-hoc-containers) for an example.
