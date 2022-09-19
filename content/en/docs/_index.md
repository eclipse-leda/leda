---
title: "Documentation"
date: 2022-05-09T14:24:56+05:30
no_list: true
---

![Eclipse Leda](/leda/assets/eclipse-leda.png)

The Eclipse Leda project provides system image "recipes" to deliver a functional and always-available Linux-based image/distribution in the context of SDV (Software Defined Vehicle), by pulling together individual contributor pieces from [Eclipse SDV](https://sdv.eclipse.org/) and the larger OSS community.

The quickstart images help to learn how the SDV development, test and deployment lifecycle works from an E2E perspective, including the deployment of applications into the container runtimes on constrained embedded devices.

The ready images are also useful for quickly setting up showcases with virtual or real hardware devices.

Eclipse Leda provides a Poky-based reference build pipeline and an OpenEmbedded Metalayer [meta-leda](https://github.com/eclipse-leda/meta-leda) for integration into existing Yocto-based projects.

# Usage

{{% readfile "/docs/__shared/usage-overview.md" %}}

Supported Machines / Build Configurations
- Emulated Qemu: x86-64, ARM64, ARM
- Raspberry Pi 4

# Overview

![Eclipse Leda Component Overview](/leda/assets/eclipse-leda-arch-overview.png)

## Features

- Publish/Subscribe infrastructure for **local messaging and cloud connectivity**
- Linux **lightweight container runtime** and Kubernetes control plane
- **Vehicle Update Manager** to orchestrate deployments of Vehicle Applications over the air (SOTA)
- **Self Update Agent** for firmware-over-the-air (FOTA) updates
- **Example Vehicle Seat Service** implementation
- **Metrics and logs collector** for Vehicle Apps

See [About - Features](/leda/docs/about/features/) for more details about current implementation and [About - Roadmap](/leda/docs/about/roadmap/) for our future work.

# License and Copyright

This program and the accompanying materials are made available under the
terms of the Apache License 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

For details, please see our license [NOTICE](https://github.com/eclipse-leda/leda/blob/main/NOTICE.md)

