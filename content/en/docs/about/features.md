---
title: "Features"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

- **Publish/Subscribe messaging infrastructure for cloud connectivity** by [Eclipse Kanto](https://github.com/eclipse-kanto/)
  - local messaging for applications and SDV system components via an MQTT message broker
  - connection to a backend messaging hub, such as Azure IoT Hub or the IoT Suite
  - device identification and authentication for cloud connectivity by using TLS device certificates
- **Container runtime**
  - An OCI-compliant container orchestration for vehicle applications and services by [Eclipse Kanto](https://github.com/eclipse-kanto/)
  - [containerd.io](https://containerd.io/) as the default container runtime. Both layers of container runtimes can be exchanged with other implementations
- A **Vehicle Update Manager** to orchestrate deployments of Vehicle Applications, configurations and base operating system updates
- An example Vehicle Seat Service implementation to showcase
  - the [Eclipse Velocitas](https://projects.eclipse.org/projects/automotive.velocitas) programming model,
  - the [Eclipse Kuksa.VAL](https://github.com/eclipse/kuksa.val) vehicle databroker and
  - the [Covesa Vehicle Signal Specification](https://github.com/COVESA/vehicle_signal_specification)
  - the communication with basic vehicle communication networks such as CAN-Bus (CAN Feeder)
- A **Self Update Agent** for firmware-over-the-air (FOTA) updates, using an A/B deployment strategy
  - Integration with [RAUC](https://www.rauc.io/)
- An [OpenTelemetry collector](https://github.com/open-telemetry/) and example configurations to collect and publish logs and metrics of containerized Vehicle Applications to the cloud backend for further processing

The features of the reusable build recipes implemented as an [OpenEmbedded](https://www.openembedded.org) metalayer `meta-leda` are:

- Build recipes for a [Yocto](https://www.yoctoproject.org/)-based distribution to build SDV-related software components
- Build recipes for customizations of the target device's storage structure to enable A/B system updates
- Build recipes for pre-packaging container images into the device during the manufacturing process to minimize initial online provisioning time
- A customized minimal setup for use on constrained devices and a full setup with convenient developer tools
- Ready images for virtual devices, for automated testing and evaluation purposes, eg QEMU ARM-64
- Ready images for physical devices, for evaluation and demo purposes, eg Raspberry Pi 4
