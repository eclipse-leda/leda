---
title: "Milestone 0.1.0-M2"
date: 2023-04-12T14:24:56+05:30
weight: 2
---

Release artifacts: [https://github.com/eclipse-leda/leda-distro/releases/tag/v0.1.0-M2](https://github.com/eclipse-leda/leda-distro/releases/tag/v0.1.0-M2)

| Artifact | Download | Size |
| --- | --- | ---: |
| Leda Raspberry Pi 4 | [eclipse-leda-raspberrypi.tar.xz](https://github.com/eclipse-leda/leda-distro/releases/download/v0.1.0-M2/eclipse-leda-raspberrypi.tar.xz) | 578 MB |
| Leda QEMU ARM64 | [eclipse-leda-qemu-arm64.tar.xz](https://github.com/eclipse-leda/leda-distro/releases/download/v0.1.0-M2/eclipse-leda-qemu-arm64.tar.xz) | 381 MB |
| Leda QEMU x86_64 | [eclipse-leda-qemu-x86_64.tar.xz](https://github.com/eclipse-leda/leda-distro/releases/download/v0.1.0-M2/eclipse-leda-qemu-x86_64.tar.xz) | 465 MB |

> Note: You need to uncompress *eclipse-leda-raspberrypi.tar.xz* multiple times until the plain *.wic* file is extracted, which can be flashed.

After download, continue with [Getting Started](/leda/docs/general-usage/)

## Release Notes

First pre-release of Eclipse Leda quickstart images, based on [Yocto LTS release](https://wiki.yoctoproject.org/wiki/Releases)
Kirkstone with Long Term Support until at least April 2024.

Minimal feature set to run software-defined-vehicle applications (such as Eclipse Velocitas apps) using COVESA Vehicle Signal Specification
and the Eclipse Kuksa.VAL Databroker on virtual devices (QEMU), in Docker,
or on physical consumer-grade devices (Raspberry Pi 4 64-Bit) for development, demonstration and prototyping purposes.

Includes example applications from Kuksa:

- Example Seat Service
- Example HVAC Service
- DBC Feeder replays a Tesla Model 3 CAN-Dump and feeds it into Kuksa.VAL Databroker

### Change log 0.1.0-M2

- Remove skopeo dependency from packagegroup-sdv-tools.bb
- Fix typo in SRCREV_FORMAT for pahocpp
- dd kernel config for RAUC stream mode to raspberrypi4-64 and qemuarm64
- Adding extra space in RPi for RAUC updates
- Backport Go 1.20 from Poky Mickledore
- Adding seatadjuster-app
- seatadjuster-app distribution

### Change log 0.1.0-M1

- Replaced k3s with [Eclipse Kanto Container Management](https://github.com/eclipse-kanto/)
- Replaced packages licensed under GPLv3 and similar licenses with alternatives
  - Replaced Grub with U-Boot
  - Replaced `nano` with `kibi`
  - Removed `readline` library
  - Removed `bash`
- RAUC Updates
  - Bundles available for each image type (Full, Minimal, Rescue)
  - Enabled verity format by default
  - Fixed the `compatible` configuration string
- Added and updated [Leda utilities](https://github.com/eclipse-leda/leda-utils)
- Build infrastructure improvements
  - Builds for Dockerized images
  - Switched to a BitBake build using [kas](https://kas.readthedocs.io/) for layer management
  - Added automated system tests using Robot framework and Dockerized environments
  - General cleanup of recipes, dependencies and structuring of the meta-leda sublayers to improve reusability
- Automatic deployment of containers based on container manifests with ad-hoc updates (filewatcher in kanto-auto-deployer)
- Preparation for AirGap installation of containers
- General improvements, such as Wifi network management

### Known Issues

The following issues were known to the development team before starting the 0.1.0-M1 build cycle.
They have been prioritized as non-critical and may be fixed for later releases.

- [RAUC can not install in stream-mode on Raspberry Pi](https://github.com/eclipse-leda/leda-distro/issues/64)
- [sdv-motd is confused by wlan interfaces](https://github.com/eclipse-leda/leda-distro/issues/71)
- [growdisk on RPi4 with sfdisk instead of parted (signaling kernel)](https://github.com/eclipse-leda/leda-distro/issues/59)
- [Partition sizes are not multiple of 4096 byte for Rauc block-hash-index](https://github.com/eclipse-leda/leda-distro/issues/63)
- [sdv-provision produces an empty Device ID](https://github.com/eclipse-leda/leda-distro/issues/56)
- [Missing/Outdated Kuksa databroker-cli](https://github.com/eclipse-leda/leda-distro/issues/34)
- [sdv-image-minimal missing SDV edge components](https://github.com/eclipse-leda/leda-distro/issues/26)
- [Home/End key navigation does not work with putty](https://github.com/eclipse-leda/leda-distro/issues/18)

### OSS IP Compliance Report

Report [scan-report-web-app_0.1.0-M1.html](../scan-report-web-app_0.1.0-M1.html)

1. Incorrectly detected license "biosl-4.0"

    - Rule: OCaaS Policy A9 License with no classification
    - Message: The license LicenseRef-scancode-biosl-4.0 found for package 'Unmanaged::leda-distro-fork:0716b55ff8f57319263d67ee16d90e64588b391d' is not categorized and / or evaluated for usage.
    - Evaluation: This license seems to be detected incorrectly by the tool being used, as it is an internal, proprietary license which is **not** used in the Eclipse Leda project.

2. Incorrectly detected license "GPL-1.0" for ORT configuration file

    - Rule: OCaaS Policy C1 Strict Copyleft
    - Message: License GPL-1.0-only found for package 'Unmanaged::leda-distro-fork:0716b55ff8f57319263d67ee16d90e64588b391d' is categorized as strict-copyleft which must not be used for BT11 Open Source Development service applications. 
    - Evaluation: The scan tool incorrectly detects its own configuration file (`.ort.original.yml`) as being licensed under GPL-v1.0

3. Incorrectly detected license "GPL-2.0-only" for standard Leda license header (which is Apache Software License)

    - Rule: OCaaS Policy C1 Strict Copyleft
    - Message: License GPL-2.0-only found for package 'Unmanaged::leda-distro-fork:0716b55ff8f57319263d67ee16d90e64588b391d' is categorized as strict-copyleft which must not be used for BT11 Open Source Development service applications. 
    - Evaluation: The scan tool incorrectly detects the Apache License header as GPL-2.0 license text

4. Incorrectly detected license "proprietary"

    - Rule: OCaaS Policy C3 Commercial
    - Message: License LicenseRef-scancode-proprietary-license found for package 'Unmanaged::leda-distro-fork:0716b55ff8f57319263d67ee16d90e64588b391d' is categorized as commercial and requires special handling.
    - Evaluation: The scan tool incorrectly detects its own configuration file (`.ort.original.yml`) as being licensed under proprietary licenses.
