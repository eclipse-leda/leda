---
title: "Metalayer"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

## Initializing BitBake environment

Initialize the build environment and start the build for QEMU:

```bash
kas build kas/leda-qemux86-64.yaml
```

## Building specific recipes

General usage:

```bash
kas build kas/leda-qemux86-64.yaml --target <recipename>
```

## Metalayer Structure

```text
 meta-leda-bsp
 \-- classes                      // Reusable BitBake Classes, eg for offline container image pre-caching
 \-- conf                         // Distribution specific configurations, eg version numbers, release codename
 \-- recipes-bsp                  // Board Support Packages, eg specifics for QEMU and Raspberry Pi
 meta-leda-components
 \-- classes                      // Reusable BitBake Classes, eg for offline container image pre-caching
 \-- conf                         // Distribution specific configurations, eg version numbers, release codename
 \-- recipes-sdv
   |-- eclipse-leda               // Build recipes for Eclipse Leda Incubator components
   |-- eclipse-kuksa              // Build recipes for Eclipse Kuksa
   |-- eclipse-cyclonedds         // Build recipes for Eclipse CycloneDDS
   |-- northstar                  // Build recipes for Northstar Container Runtime
   |-- packagegroups              // Grouping packages
   \-- sdv-base                   // SDV Base Bundle: k3s, fstab, can0.network
     |--- base-files
     |--- SDV Core Utilities
     \--- SDV Utilities
   |-- sdv-containers             // Container images recipes for pre-caching / airgap installation
     |--- Cloud Agent
     |--- Data Broker
     |--- Feeder CAN
     |--- OTel Collector
     |--- Self Update Agent
     |--- Vehicle Update manager
     |--- Example Seat Service
     \--- ...
   |-- sdv-core                   // SDV Core Bundle
     |--- SDV RAUC Bundle         // RAUC Update Bundle Manifest
   \-- tools                      // Convenience tools for the "full" image, eg nerdctl and kantui
 meta-leda-distro
 \-- classes                      // Reusable BitBake Classes, eg for offline container image pre-caching
 \-- conf                         // Distribution specific configurations, eg version numbers, release codename
 \-- recipes-containers           // Container related configuration recipes (containerd, nerdctl)
 \-- recipes-core                 // Core recipes (base-files, systemd)
 \-- recipes-kernel               // Kernel configuration, eg kernel modules, logging, virtio
 \-- recipes-sdv-distro           // Image definitions
 \-- wic                          // WIC Kickstarter files - Partition layouts
meta-leda-distro-container
 \-- classes                      // Reusable BitBake Classes, eg for offline container image pre-caching
 \-- conf                         // Distribution specific configurations, eg version numbers, release codename
 \-- recipes-sdv                  // Build containers with Yocto
```

## Base Bundle

Contains the recipes to build and install the minimal set of dependencies for the SDV stack on the edge device. With these minimal components, the SDV stack should be able to bootstrap itself.

### CAN-Bus Kernel Configuration

To enable support for CAN bus related modules, the kernel needs to be reconfigured. This is done by the `sdv-canbus-modules.inc` include file in the `recipes-kernel/linux` folder, which patches Poky's `linux-yocto` recipe.

Verifying and displaying the current kernel configuration: `bitbake -e virtual/kernel`

To verify the recipe and the kernel configuration: `bitbake linux-yocto -c kernel_configcheck -f`

The kernel config file can be found in:
`./tmp/work/qemux86_64-poky-linux/linux-yocto/*/linux-qemux86_64-standard-build/.config`

## Core Bundle

Contains the recipes to build and install additional SDV components, which are required for a proper runtime setup.

## Containers

Contains the recipes for pre-installing specific containers into the container management at runtime. This is mainly for pre-caching container image layers onto the device to speed up the initial deployment but can also be used to enable offline usecases.

## Build Host System Requirements

- Yocto Project 4.0 (kirkstone) or higher
- 100GB+ free disk space per build configuration
- Online connection for fetching sources and container images
