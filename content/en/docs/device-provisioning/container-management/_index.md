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

### Example Message Flow

1. Container Management starts and subscribes to `edge/thing/response`
2. Cloud Connector starts and publishes the following message to `edge/thing/response` as soon as the connection is online:

    ```json
    {
        "deviceId":"<namespace>:<gatewayId>:<deviceId>",
        "tenantId":"<tenantId>"
    }
    ```

    - `namespace` is `azure.edge` for Kanto's Azure Cloud Connector
    - `gatewayId` indicates the hostname of the Azure IoT Hub
    - `deviceId` is the identifier for the device, this can either be part of the Azure Connection String or part of the device authentication certificate (CN)
    - `<tenantId>` is a configuration setting in the cloud connector

    > **Note:** You can simulate the cloud connector trigger by issueing the MQTT message manually on command line:
    
        mosquitto_pub -t 'edge/thing/response' -m '{"deviceId":"dummy-namespace:dummy-gateway:dummy-device-id","tenantId":"dummy-tenant-id"}'

3. Container Management responds with a list of containers in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

    ```json
    {
        "topic": "foo/bar:baz:edge:containers/things/twin/commands/modify",
        "headers": {
            "response-required": false
        },
        "path": "/features/SoftwareUpdatable",
        "value": {
            "definition": [
                "org.eclipse.hawkbit.swupdatable:SoftwareUpdatable:2.0.0"
            ],
            "properties": {
                "status": {
                    "softwareModuleType": "oci:container",
                    "installedDependencies": {
                        "ghcr.io%2Feclipse%2Fkuksa.val%2Fdatabroker.<uuid>:0.2.5": {
                            "group": "ghcr.io/eclipse/kuksa.val/databroker",
                            "name": "<uuid>",
                            "version": "0.2.5"
                        },
                        "ghcr.io%2Feclipse%2Fkuksa.val.services%2Fseat_service.<uuid>:v0.1.0": {
                            "group": "ghcr.io/eclipse/kuksa.val.services/seat_service",
                            "name": "<uuid>",
                            "version": "v0.1.0"
                        },
                        "ghcr.io%2Feclipse-leda%2Fleda-contrib-cloud-connector%2Fcloudconnector.<uuid>:latest": {
                            "group": "ghcr.io/eclipse-leda/leda-contrib-cloud-connector/cloudconnector",
                            "name": "<uuid>",
                            "version": "latest"
                        },
                        "ghcr.io%2Feclipse-leda%2Fleda-contrib-self-update-agent%2Fself-update-agent.<uuid>:build-20": {
                            "group": "ghcr.io/eclipse-leda/leda-contrib-self-update-agent/self-update-agent",
                            "name": "<uuid>",
                            "version": "build-20"
                        },
                        "ghcr.io%2Feclipse-leda%2Fleda-contrib-vehicle-update-manager%2Fvehicleupdatemanager.<uuid>:latest": {
                            "group": "ghcr.io/eclipse-leda/leda-contrib-vehicle-update-manager/vehicleupdatemanager",
                            "name": "<uuid>",
                            "version": "latest"
                        }
                    }
                }
            }
        }
    }
    ```
4. Container Management answers with an additional message for each container in the topic `e/<tenantId>/<gatewayId>:<deviceId>:edge:containers`

    ```json
    {
        "topic": "<tenantId>/<gatewayId>:<deviceId>:edge:containers/things/twin/commands/modify",
        "headers": {
            "response-required": false
        },
        "path": "/features/Container:<uuid>",
        "value": {
            "definition": [
                "com.bosch.iot.suite.edge.containers:Container:1.5.0"
            ],
            "properties": {
                "status": {
                    "name": "seatservice-example",
                    "imageRef": "ghcr.io/eclipse/kuksa.val.services/seat_service:v0.1.0",
                    "config": {
                        "domainName": "seatservice-example-domain",
                        "hostName": "seatservice-example-host",
                        "env": [
                            "VEHICLEDATABROKER_DAPR_APP_ID=databroker",
                            "BROKER_ADDR=databroker-host:30555",
                            "RUST_LOG=info",
                            "vehicle_data_broker=info"
                        ],
                        "restartPolicy": {
                            "type": "UNLESS_STOPPED"
                        },
                        "extraHosts": [
                            "databroker-host:host_ip"
                        ],
                        "portMappings": [
                            {
                                "proto": "tcp",
                                "hostPort": 30051,
                                "hostPortEnd": 30051,
                                "containerPort": 50051,
                                "hostIP": "localhost"
                            }
                        ],
                        "networkMode": "BRIDGE",
                        "log": {
                            "type": "JSON_FILE",
                            "maxFiles": 2,
                            "maxSize": "1M",
                            "mode": "BLOCKING"
                        }
                    },
                    "createdAt": "2023-02-02T08:46:33.792687313Z",
                    "state": {
                        "status": "RUNNING",
                        "pid": 13627,
                        "startedAt": "2023-02-02T09:51:08.049572297Z",
                        "finishedAt": "2023-02-02T09:50:51.752255799Z"
                    }
                }
            }
        }
    }    
    ```
