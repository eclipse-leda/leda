---
title: "Orchestration"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

# Container Management

The container management will respond to the cloud connectivity status message by initially sending a list of containers:

1. Container Management responds with a list of containers in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

{{<readfile file="container-management-list.json" code="true" lang="json">}}

2. Container Management answers with an additional message for each container in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

{{<readfile file="container-management-detail.json" code="true" lang="json">}}
