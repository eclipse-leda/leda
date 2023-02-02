---
title: "Self Update Tutorial"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

This chapter describes the steps necessary to perform a local (without cloud) self update of the operating system.

![Self Update Architecture](../self-update-arch.png)

## Self-Update using RAUC Update Bundles

- On host: Update bundle `sdv-rauc-bundle-qemux86-64.raucb` is in current folder

  *Note: In the development environment, the update RAUC Update Bundle is located in the BitBake machine-specific output folder
  Example location is `tmp/deploy/images/qemux86-64`*

- On host: Start a dummy web server for serving the update file

  ```shell
  python3 -m http.server --bind 192.168.7.1
  ```

- On host: open two new terminals - one for monitoring and one for triggering the self-update

  - Terminal 1: To view the progress, watch the MQTT topics `selfupdate/desiredstate` and `selfupdate/desiredstatefeedback`:

      ```shell
      mosquitto_sub -h 192.168.7.2 -p 1883 -t "selfupdate/#"
      ```

  - Terminal 2: Trigger the actual self update process by publishing an MQTT message to `selfupdate/desiredstate`:

      ```shell
      mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate" -f start-update-example.json
      ```

- Switch to a terminal in the guest
- On guest: After the self update process completed, check the status:

  ```shell
  rauc status --detailed
  ```

## Self-Update Trigger Message

`start-update-example.json` file:

{{<readfile file="start-update-example.json" code="true" lang="json">}}

## Example Message Flows

### Current State

1. Initial response message on startup from self update agent in topic `selfupdate/currentstate`, or upon request by sending message to `selfupdate/currentstate/get`

      Request:

      ```json
      {
            "activityId": "<uuid>",
            "timestamp": 1676332092
      }
      ```

      Response:

      ```json
      {
            "activityId": "<uuid>",
            "timestamp": 1675345910,
            "payload": {
                  "domains": [
                        {
                              "id": "self-update",
                              "components": [
                              {
                                    "id": "os-image",
                                    "version": "bundle_version_not_available"
                              }
                              ]
                        }
                  ]
            }
      }
      ```

### Desired State

1. External trigger to update via desired state on topic `selfupdate/desiredstate`:

      ```json
      {
            "activityId": "random-uuid-as-string",
            "timestamp": 123456789,
            "payload": {
                  "domains": [
                        {
                        "id": "self-update",
                        "components": [
                              {
                                    "id": "os-image",
                                    "version": "${VERSION_ID}",
                                    "config": [
                                    {
                                          "key": "image",
                                          "value": "http://leda-bundle-server/sdv-rauc-bundle-qemux86-64.raucb"
                                    }
                                    ]
                              }
                        ]
                        }
                  ]
            }
      }
      ```

2. Initialization response by Self Update Agent on topic `selfupdate/desiredstatefeedback`

      ```json
      {
            "activityId": "<<uuid>>",
            "timestamp": 1675347152,
            "payload": {
                  "status": "IDENTIFIED",
                  "message": "Self-update agent is about to perform an OS image update.",
                  "actions": []
            }
      }
      ```

3. Responses while downloading by Self Update Agent on topic `selfupdate/desiredstatefeedback`

      ```json
       {
            "activityId": "<uuid>",
            "timestamp": 1675347152,
            "payload": {
                  "status": "RUNNING",
                  "message": "Self-update agent is performing an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "${VERSION_ID}"
                        },
                        "status": "DOWNLOADING",
                        "progress": 0,
                        "message": "Downloading 0.0 MiB..."
                  }
                  ]
            }
       }
      ```

4. Response by Self Update Agent on topic `selfupdate/desiredstatefeedback` when download successfully finished:

      ```json
      {
                "activityId": "<uuid>",
                "timestamp": 1675347154,
                "payload": {
                    "status": "RUNNING",
                    "message": "Self-update agent is performing an OS image update.",
                    "actions": [
                        {
                            "component": {
                                "id": "self-update:os-image",
                                "version": "${VERSION_ID}"
                            },
                            "status": "DOWNLOAD_SUCCESS",
                            "progress": 100,
                            "message": "Downloaded 108.9 MiB..."
                        }
                    ]
                }
      }
      ```

5. Response by Self Update Agent on topic `selfupdate/desiredstatefeedback` while performing the installation:

      ```json
      {
            "activityId": "random-uuid-as-string",
            "timestamp": 1675347159,
            "payload": {
                  "status": "RUNNING",
                  "message": "Self-update agent is performing an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "${VERSION_ID}"
                        },
                        "status": "UPDATING",
                        "progress": 20,
                        "message": "RAUC install..."
                  }
                  ]
            }
      }
      ```

6. Response by Self Update Agent on topic `selfupdate/desiredstatefeedback` when installation completed successfully:

      ```json
      {
            "activityId": "<uid>",
            "timestamp": 1675347186,
            "payload": {
                  "status": "COMPLETED",
                  "message": "Self-update completed, reboot required.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "${VERSION_ID}"
                        },
                        "status": "UPDATE_SUCCESS",
                        "progress": 100,
                        "message": "Writing partition completed, reboot required."
                  }
                  ]
            }
      }
      ```
