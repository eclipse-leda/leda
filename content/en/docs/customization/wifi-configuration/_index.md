---
title: "Wifi Configuration"
date: 2023-01-03T17:24:56+05:30
weight: 3
---

BSP packages for emulated WiFi devices (QEMU) and hardware device drivers are provided in `meta-leda` for [supported hardware](../custom-images#hardware).
They usually do not require extra configuration. Images built with our meta-layer provide iwd/iwctl as a high-level daemon/interface for managing wireless
connectivity.

For a guide on how to connect to a wireless network with iwctl check the [_Notes on using iwctl_](iwd) page.

## Raspberry Pi 4B 64

The required kernel modules and binary blobs are provided with the `sdv-wifi-kernel-config.inc` config file and the `packagegroup-sdv-rpi4wifi` packagegroup. These
are included in `sdv-image-full.bb` and `sdv-image-minimal.bb` by default. 

If you, however, decide to define your own custom image based on [_Custom Distros_](../custom-images),
you would have to make sure the packagegroup is installed to enable WiFi connectivity.

## QEMU

QEMU images provide a virtual `wlan` interface for easier automated testing of images.