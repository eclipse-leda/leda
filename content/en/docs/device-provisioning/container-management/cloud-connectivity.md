---
title: "Cloud Connectivity"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Simulation of cloud connectivity

1. Container Management starts and subscribes to `edge/thing/response`
2. Cloud Connector starts and publishes the following message to `edge/thing/response` as soon as the connection is online:

{{<readfile file="simulate-connectivity.json" code="true" lang="json">}}

- `namespace` is `azure.edge` for Kanto's Azure Cloud Connector
- `gatewayId` indicates the hostname of the Azure IoT Hub
- `deviceId` is the identifier for the device, this can either be part of the Azure Connection String or part of the device authentication certificate (CN)
- `tenantId` is a configuration setting in the cloud connector

> **Note:** You can simulate the cloud connector trigger by issueing the MQTT message manually on command line:

```shell
mosquitto_pub -t 'edge/thing/response' -m '{"deviceId":"dummy-namespace:dummy-gateway:dummy-device-id","tenantId":"dummy-tenant-id"}'
```
