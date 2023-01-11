---
title: "Cloud Connector"
date: 2022-05-09T14:24:56+05:30
weight: 5
---

The cloud connector is used in the context of [Device Provisioning](/leda/docs/device-provisioning/) and cloud backend connectivity.

## Overview

Leda Cloud Connector for Azure IoT Hub is a fork (extended and adapted) of the generic [Eclipse Kanto's Azure connector](https://github.com/eclipse-kanto/azure-connector) that is being able to process cloud-to-device and device-to-cloud messages as defined for the Software-Defined Vehicle cloud backend.

![Cloud Connector Fork Relationship](./cloud-connector-fork.png)

## Runtime

The SDV cloud connector will come up with pluggable architecture that will allow easy **transformation of the incoming cloud-to-device command messages (SDV message envelope) to a format suitable and understandable by the rest of the in-vehicle components** and vice-versa. It shall be possible to map SDV messages to and from [Eclipse Hono](https://www.eclipse.org/hono/docs/concepts/connecting-devices/) and [Eclipse Ditto](https://www.eclipse.org/ditto/) messages using simple configuration, rules written in JSON; thus allowing this component to work together with other [Eclipse Kanto](https://websites.eclipseprojects.io/kanto/) components too.

![Cloud Connector Runtime View](./cloud-connector-runtime.png)

## Source Repository

Source Repository: <https://github.com/eclipse-leda/leda-contrib-cloud-connector>

## Building and Deployment

The Cloud Connector can either be installed natively into the system image by using the respective Yocto recipe [leda-contrib-cloud-connector_git.bb](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/leda-contrib-cloud-connector_git.bb), or the cloud connector can be deployed as a [container](https://github.com/eclipse-leda/leda-contrib-cloud-connector/pkgs/container/leda-contrib-cloud-connector%2Fcloudconnector).

### Native Installation

A native installation has the advantage that no additional container runtime is required. In some vehicle system architectures, there are separate devices for connectivity and for general computation. The actual physical device for connectivity may hence have less ressources available which then requires a native installation of such core components.

- Add the recipe to the image in your Yocto configuration:

```
    IMAGE_INSTALL += "leda-contrib-cloud-connector"
```

- Override the configuration in `/etc/cloud-connector/config.json`
- Create the device certificate
- The cloud-connector can be managed (start, stop, restart) using systemd: `systemctl restart cloud-connector`

### Container Installation

When the connectivity components can be deployed on the more generic compute module, where a container runtime is available, the cloud connector can also be deployed as a container. This is the default for the Eclipse Leda quickstart images.

Initial deployment and configuration steps are:

- On first start, the auto deployment will deploy and start the cloud connector container automatically, but with invalid default values or missing device certificates.
- The user needs to adapt the device authentication to suit his needs, e.g. creating and providing a device certificate. Check the `/data/containers/cloud-connector.json` deployment descriptor for the correct location of the certificate files.
- After this configuration has been done once, the container needs to be restarted using the Kanto CLI: `kanto-cm restart -n cloud-connector`
