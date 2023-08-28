---
title: "Container Metrics"
date: 2022-05-09T14:24:56+05:30
weight: 4
---

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
