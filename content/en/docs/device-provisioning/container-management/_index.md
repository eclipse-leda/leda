---
title: "Container Management"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

Leda is using Kanto Container Management as the upper-layer container runtime and container orchestration engine.

Besides the command line tool `kanto-cm`, Kanto also has remote interfaces to manage containers.

## Remote Interface

Kanto's container-management service offers a remote interface via local messaging (MQTT) to interact with a digital twin on the cloud side.
This feature can be easily enabled by setting `"things": { "enabled": true }` in `/etc/container-management/config.toml`.

When one of the cloud connector components, such as leda-contrib-cloud-connector or Kanto's azure-connector, is connected to a cloud backend, the container-management will publish its own information using Eclipse Ditto and Eclipse Hono messages. For this, container-management only needs the device Id, gateway Id and tenant Id.


