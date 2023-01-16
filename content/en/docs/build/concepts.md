---
title: "Concepts"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

The example build configurations in this repository are based on the official [BitBake Quickstart tutorial](https://docs.yoctoproject.org/brief-yoctoprojectqs/index.html) and have been extended to include Leda SDV components.

## Build Setup

To set up your own BitBake build configuration, follow the BitBake documentation and include `meta-leda` in your `bblayers.conf` and add the SDV packages into your `local.conf`.

The Leda build is mainly using the kas tool for a simplified maintenance of the BitBake Configuration files. The kas configuration files are located in `kas/`

```yaml
header:
  version: 12
distro: leda
machine: qemux86-64
target: sdv-image-all
repos:
  ...
 meta-leda:
    url: "https://github.com/eclipse-leda/meta-leda"
    refspec: main
    layers:
      meta-leda-bsp:
      meta-leda-components:
      meta-leda-distro:
```

## Leda Metalayer

The `meta-leda` layer conatins the BitBake Classes and Recipes to integrate SDV Components into a BitBake based build setup.

Please see [https://github.com/eclipse-leda/meta-leda](https://github.com/eclipse-leda/meta-leda) for more information.

## Recipes for containerized components

The SDV.EDGE stack is based on a containerized architecture and the intention is to have as much components containerized as possible, to ensure a high degree of isolation and updateability. To ensure some degree of flexibility and control, certain core components may also be installed as native services.

To automatically deploy the containers of the SDV reference implementation and example applications and services, the build configurations will deploy a couple of deployment specifiction files into the auto-deployment folder `/data/var/containers/manifests`.

At start time, these containers will be automatically deployed:

- Cloud Connector
- Self Update Agent
- Vehicle Update Manager
- Vehicle API / Vehicle Abstraction Layer
  - Data Broker (Eclipse Kuksa)
  - Example Seat Service (CAN-bus implementation)

For a full list of containers, see `meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers`

## Recipes for containerized applications

OpenEmbedded's [meta-virtualization](https://layers.openembedded.org/layerindex/branch/master/layer/meta-virtualization/) already contains some recipes and reusabled classes for building virtualization and containerized applications.

`meta-leda` extends that functionality by using `skopeo` to package container images. To minimize the runtime requirements (dependencies, disk usage), an approach to pre-load container images and its layers directly into the content storage of the container runtime is followed.

## Building containers with Yocto

For components which can either be installed natively or as container, it can be beneficial to build these containers using Yocto as well. An example is in `meta-leda-distro-container/recipes-sdv/sdv-containers/cyclonedds-example-container_0.1.bb`.
