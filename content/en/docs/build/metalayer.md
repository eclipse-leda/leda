---
title: "Metalayer"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

# Initializing BitBake environment

Alternatively, initialize build environment manually. This way, you can invoke multiple build processes in the same context, eg when building individual recipes.
```bash
cd poky
source oe-init-build-env ../build-sdv-<target>
bitbake sdv-image-all
leda
```

# Individual recipes

General usage:
```bash
cd poky
source oe-init-build-env ../build-sdv-<target>
bitbake <recipe>
```

## Recipes Structure

```
 meta-leda
 \-- classes                      // Reusable BitBake Classes, eg for offline container image pre-caching
 \-- conf                         // Distribution specific configurations, eg version numbers, release codename
 \-- recipes-bsp                  // Board Support Packages, eg specifics for QEMU and Raspberry Pi
 \-- recipes-devtools             // Build tools
 \-- recipes-kernel               // Kernel configuration, eg kernel modules, logging, virtio
 \-- recipes-sdv
   |-- eclipse-kanto              // Build recipes for Kanto
   |-- images                     // Definition of three disk images: full, minimal, rescue
   |-- packagegroups              // Grouping packages
   \-- sdv-base                   // SDV Base Bundle: k3s, fstab, can0.network
     |--- base-files
     |--- SDV Core Utilities
     |--- DAPR & HELM CLI
     \--- SDV Utilities
   |-- sdv-containers              // Container images recipes for pre-caching
     |--- Cloud Agent
     |--- Data Broker
     |--- Feeder CAN
     |--- OTel Collector
     |--- Self Update Agent
     |--- Vehicle Update manager
     |--- Example Seat Service
     \--- ...
   |-- sdv-core                    // SDV Core Bundle
     |--- SDV Core Bundle Pods     // Kubernetes Deployment files
     |--- DAPR Initializer         // Initialize HELM and DAPR on first boot
     \--- Cloud Connector          // Optional: Native installation of Cloud Agent
   \-- tools                       // Convenience tools for the "full" image, eg nerdctl and k9s
```

## SDV Base Bundle

Contains the recipes to build and install the minimal set of dependencies for the SDV stack on the edge device. With these minimal components, the SDV stack should be able to bootstrap itself.

Example:
`bitbake sdv-core-utils`

### CAN-Bus Kernel Configuration

To enable support for CAN bus related modules, the kernel needs to be reconfigured. This is done by the `sdv-canbus-modules.inc` include file in the `recipes-kernel/linux` folder, which patches Poky's `linux-yocto` recipe.

Verifying and displaying the current kernel configuration: `bitbake -e virtual/kernel`

To verify the recipe and the kernel configuration: `bitbake linux-yocto -c kernel_configcheck -f`

The kernel config file can be found in:
`./tmp/work/qemux86_64-poky-linux/linux-yocto/*/linux-qemux86_64-standard-build/.config`

## SDV Core Bundle

Contains the recipes to build and install additional SDV components, which are required for a proper runtime setup.

Example:
`bitbake sdv-core-bundle-pods`

## SDV Containers

Contains the recipes for pre-installing specific containers into the container management at runtime. This is mainly for pre-caching container image layers onto the device to speed up the initial deployment but can also be used to enable offline usecases.

Example:
`bitbake sdv-container-seatservice`

## Building SDV Container Seat Service container image

- With dependencies (default): `bitbake sdv-container-seatservice`
- Without dependencies: `bitbake -v -b ../meta-leda/recipes-sdv/sdv-containers/sdv-container-seatservice.bb`
- Output in `/leda-distro/build-sdv-x86_64/tmp/work/core2-64-poky-linux/sdv-container-seatservice/1.0-r0/deploy-rpms/core2_64/sdv-container-seatservice-1.0-r0.core2_64.rpm` (Example)

# Build Configuration

## Requirements
- Yocto Project 3.4 (honister) or higher - required for k3s support in meta-virtualization
- 50GB+ free disk space per build configuration
- Online connection for fetching sources and container images

## Build Scripts

- `build-aarch64-qemu.sh` - generix ARM64 for QEMU emulation
- `build-aarch64-rpi4.sh` - ARM64 with Raspberry Pi 4 board support package
- `build-arm-qemu.sh` - generix ARM for QEMU emulation
- `build-x86_64.sh` - generix x64-64 for QEMU emulation
