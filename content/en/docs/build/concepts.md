---
title: "Concepts"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# BitBake and Metalayers

The example build configurations in this repository are based on the official [BitBake Quickstart tutorial](https://www.yoctoproject.org/docs/current/brief-yoctoprojectqs/brief-yoctoprojectqs.html) and have been extended to include SDV components.

To set up your own BitBake build configuration, follow the BitBake documentation and include `meta-leda` in your `bblayers.conf` and add the SDV packages into your `local.conf`. You may use the the `local.conf` files in the `build-sdv-*/conf/local.conf` as a guiding reference.

# SDV Meta Layer

The `meta-leda` layer conatins the BitBake Classes and Recipes to integrate SDV Components into a BitBake based build setup.

Please see https://github.com/eclipse-leda/meta-leda for more information.

# Recipes for Kubernetes Pods

The SDV stack is based on a Kubernetes Control Plane and the intention is to have as much components containerized as possible, to ensure a high degree of isolation and updateability.

To automatically deploy the pods of the SDV reference implementation and example applications and services, the build configurations will deploy a couple of Pod specifiction files into the [auto-deployment folder of k3s](https://rancher.com/docs/k3s/latest/en/advanced/#auto-deploying-manifests).

At start time of k3s, these pods will be automatically deployed:
- Cloud Connector by [Eclipse Kanto](https://projects.eclipse.org/projects/iot.kanto)
- Log and Trace by [OpenTelemetry](https://github.com/open-telemetry/)
- Example Application: [Seat Adjuster python app](https://github.com/eclipse-velocitas/vehicle-app-python-template)
- Vehicle API
  - Data Broker
  - Example Seat Service (CAN-bus implementation)
- Vehicle Update Manager

For a full list of pods, see [`meta-leda/recipes-sdv/sdv-core/files/sdv-core-bundle-pods/`](https://github.com/eclipse-leda/meta-leda/tree/main/recipes-sdv/sdv-core/files/sdv-core-bundle-pods)

# Recipes for containerized applications

OpenEmbedded's [meta-virtualization](https://layers.openembedded.org/layerindex/branch/master/layer/meta-virtualization/) already contains some recipes and reusabled classes for building virtualization and containerized applications.

`meta-leda` extends that functionality by using `skopeo` to package container images. To minimize the runtime requirements (dependencies, disk usage), an approach to pre-load container images and its layers directly into the content storage of the container runtime is followed.




