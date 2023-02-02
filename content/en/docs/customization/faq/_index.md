---
title: "FAQ"
date: 2023-01-03T17:24:56+05:30
weight: 30
---

## Frequently Asked Questions

**Q: Why is the performance very slow?**

**A:** That depends on the setup: On QEMU, try to enable KVM. This only works for x86 based setup. The ARM-based images are emulated by QEMU and software emulation is much slower. For network performance issues, try to use TAP networking instead of SLIRP networking for QEMU. That requires more setup on the host though. On Raspberry Pi, it should be fast. If the system startup takes very long, you may have an outdated image, please update to the latest version.

**Q: Why is my Bluetooth/Wifi driver missing?**

**A:** Please check the latest release, as we're continously adding features. If your driver is still missing, please open a GitHub Issue. We can add Kernel Modules for supported hardware. If you hardware is not supported out of the box by the Eclipse Leda project, you need to build your own image and customize the Linux Kernel configuration. Please see the [Yocto Project](https://www.yoctoproject.org/) documentation on how to do that.

**Q: How can a container access CAN-Bus interfaces?**

**A:** As using a CAN-Bus requires access to the host network interface, the container needs to run in privileged mode and it needs access to the host network interface. For a Kanto-CM container, simply add `privileged: true` to the [container configuration](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-config/). A more sophisticated setup involves using virtual CAN interfaces for each container and using a CAN gateway to route the traffic accordingly. However, using CAN-Bus is not in the focus of SDV-style applications, as we assume that *Vehicle Services* would be running on dedicated ECUs, offering higher-level interfaces to *Vehicle Applications* on other protocols, such as Some/IP.

```json
"host_config": {
...
"network_mode": "host",
"privileged": true,
...
}
```

**Q: Why does booting from SD-Card sometimes fail and enters maintenance mode?**

**A:** This may depend on the quality or age of the SD-Card as well. Also, consumer-grade hardware like a Raspberry Pi may fail at times. Please try another SD-Card. Another reason may be high write operations to the SD-Card due to excessive data transfer (logging, container deployment etc.).

**Q: How can I install additional software in Leda?**

**A:** As we're using Yocto, there is no central repository for software packages. Thus, we did not include any kind of package manager. If you feel that the software you want to install is valuable for other Leda users as well, please open a GitHub Issue and request the installation of the software. If the software is specific to your use case, you need to build your own image using Yocto. Alternatively, you may build a container for your software and deploy the container into the container runtime. Using `kanto-cm` or `ctr` you would be able to execute your software as a container.
