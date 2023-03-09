---
title: "Wifi Configuration"
date: 2023-01-03T17:24:56+05:30
weight: 3
---

BSP packages for emulated WiFi devices (QEMU) and hardware device drivers are provided in `meta-leda` for [supported hardware](../../customization/custom-images#hardware).
They usually do not require extra configuration.

For a guide on how to connect to a wireless network check the [_Connecting to Wi-Fi networks_](connecting-to-wifi) page.

## Raspberry Pi 4B 64

The required kernel modules and binary blobs are provided with the `sdv-wifi-kernel-config.inc` config file and the `packagegroup-sdv-rpi4wifi` packagegroup. These
are included in `sdv-image-full.bb` and `sdv-image-minimal.bb` by default.

If you, however, decide to define your own custom image based on [_Custom Distros_](../../customization/custom-images),
you would have to make sure the packagegroup is installed to enable WiFi connectivity.

## QEMU

QEMU images provide the kernel modules necessary to set-up a virtual wlan interface and connect it to a virtual wifi network. This can be useful in various testing scenarios.

To create and link a virtual WiFi interface to eth0, boot your QEMU image and run:

```shell
$ ip link add link eth0 name wlan0 type virt_wifi
```

The SSID of the virtual network you can connect to is `VirtWifi`.

_Note:_ Leda Quickstart QEMU images set the name of the default virtual ethernet interface to `eth0` through kernel CMDLINE configurations (`net.ifnames=0 biosdevname=0`).
If you are building a custom image with a different kernel CMDLINE replace `eth0` with the name of your virtual interface (check `ifconfig`).
