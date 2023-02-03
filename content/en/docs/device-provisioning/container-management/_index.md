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

### Simulation of cloud connectivity

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

### Container Management

The container management will respond to the cloud connectivity status message by initially sending a list of containers:

1. Container Management responds with a list of containers in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

{{<readfile file="container-management-list.json" code="true" lang="json">}}

2. Container Management answers with an additional message for each container in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

{{<readfile file="container-management-detail.json" code="true" lang="json">}}

### Container Metrics

Container-level metrics, such as CPU utilization or memory usage, can be retrieved on-demand and continuously by enabling the container metrics events.
This is done by sending a request to the topic `command//<namespaceId>:<gatewayId>:<deviceId>:edge:containers/req/<correlationId>/request`:

1. Enable Container Metrics with a frequency of `5s`:

{{<readfile file="container-metrics-request.json" code="true" lang="json">}}

Example command line:

```shell
mosquitto_pub -t command//dummy-namespace:dummy-gateway:dummy-device-id:edge:containers/req/3fdc463c-293c-4f39-ab19-24aef7944550/request -m '{"topic":"dummy-namespace/dummy-gateway:dummy-device-id:edge:containers/things/live/messages/request","headers":{"timeout":"10","response-required":true,"content-type":"application/json","correlation-id":"3fdc463c-293c-4f39-ab19-24aef7944550"},"path":"/features/Metrics/inbox/messages/request","value":{"frequency":"5s"}}'
```

2. Container Metrics answers with an additional message for each container in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

{{<readfile file="container-management-detail.json" code="true" lang="json">}}

3. To disable Container Metrics, send a request with frequency of `0s`:

    ```shell
    mosquitto_pub -t command//dummy-namespace:dummy-gateway:dummy-device-id:edge:containers/req/3fdc463c-293c-4f39-ab19-24aef7944550/request -m '{"topic":"dummy-namespace/dummy-gateway:dummy-device-id:edge:containers/things/live/messages/request","headers":{"timeout":"10","response-required":true,"content-type":"application/json","correlation-id":"3fdc463c-293c-4f39-ab19-24aef7944550"},"path":"/features/Metrics/inbox/messages/request","value":{"frequency":"0s"}}'
    ```
