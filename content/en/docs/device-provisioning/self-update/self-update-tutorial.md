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
      mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate/command" -f download-command.json
      mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate/command" -f update-command.json
      mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate/command" -f activate-command.json
      mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate/command" -f cleanup-command.json
      ```

      Files:

      [start-update-example.json](../start-update-example.json)

      [download-command.json](../download-command.json)

      [update-command.json](../update-command.json)

      [activate-command.json](../activate-command.json)

      [cleanup-command.json](../cleanup-command.json)

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

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087
      }
     ```

      Response by Self Update Agent on topic `selfupdate/currentstate`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787461,
            "payload": {
                  "softwareNodes": [
                  {
                        "id": "self-update-agent",
                        "version": "build-152",
                        "name": "OTA NG Self Update Agent",
                        "type": "APPLICATION"
                  },
                  {
                        "id": "self-update:leda-deviceimage",
                        "version": "v0.0.10-194-g3d48cb8",
                        "name": "Official Leda device image",
                        "type": "IMAGE"
                  }
                  ],
                  "hardwareNodes": [],
                  "associations": [
                  {
                        "sourceId": "self-update-agent",
                        "targetId": "self-update:leda-deviceimage"
                  }
                  ]
            }
      }
     ```

### Desired State

1. External trigger to update via desired state on topic `selfupdate/desiredstate`:

     ```json
      {
            "activityId": "<uuid>",
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

      Response on topic `selfupdate/desiredstatefeedback`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687786390,
            "payload": {
                  "status": "IDENTIFYING",
                  "message": "Self-update agent has received new desired state request and is evaluating it.",
                  "actions": []
            }
      }
     ```

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687786390,
            "payload": {
                  "status": "IDENTIFIED",
                  "message": "Self-update agent is about to perform an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "IDENTIFIED",
                        "progress": 0,
                        "message": "Self-update agent is about to perform an OS image update."
                  }
                  ]
            }
      }
     ```

2. External trigger to download command on topic `selfupdate/desiredstate/command`:

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087,
            "payload": {
                  "baseline": "BASELINE NAME",
                  "command": "DOWNLOAD"
            }
      }
     ```

      Response on topic `selfupdate/desiredstatefeedback`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687786931,
            "payload": {
                  "status": "DOWNLOADING",
                  "message": "Self-update agent is performing an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "DOWNLOADING",
                        "progress": 0,
                        "message": "Downloading 0.0 MiB..."
                  }
                  ]
            }
      }     
     ```

      ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687786936,
            "payload": {
                  "status": "DOWNLOAD_SUCCESS",
                  "message": "Self-update agent is performing an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "DOWNLOAD_SUCCESS",
                        "progress": 100,
                        "message": "Downloaded 106.3 MiB..."
                  }
                  ]
            }
      }
     ```

3. External trigger to update command on topic `selfupdate/desiredstate/command`:

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087,
            "payload": {
                  "baseline": "BASELINE NAME",
                  "command": "UPDATE"
            }
      }
     ```

      Response on topic `selfupdate/desiredstatefeedback`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787145,
            "payload": {
                  "status": "UPDATING",
                  "message": "Self-update agent is performing an OS image update.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATING",
                        "progress": 0,
                        "message": "Checking bundle version and version in desired state request."
                  }
                  ]
            }
      }
     ```

      ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787228,
            "payload": {
                  "status": "UPDATE_SUCCESS",
                  "message": "Self-update completed, reboot required.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATING",
                        "progress": 100,
                        "message": "Writing partition completed, reboot required."
                  }
                  ]
            }
      }
     ```

4. External trigger to activate command on topic `selfupdate/desiredstate/command`:

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087,
            "payload": {
                  "baseline": "BASELINE NAME",
                  "command": "ACTIVATE"
            }
      }
     ```

      Response on topic `selfupdate/desiredstatefeedback`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787302,
            "payload": {
                  "status": "ACTIVATING",
                  "message": "Self-update agent is performing an OS image activation.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATING",
                        "progress": 0,
                        "message": "Self-update agent is performing an OS image activation."
                  }
                  ]
            }
      }
     ```

      ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787303,
            "payload": {
                  "status": "ACTIVATION_SUCCESS",
                  "message": "Self-update agent has activated the new OS image.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATED",
                        "progress": 0,
                        "message": "Self-update agent has activated the new OS image."
                  }
                  ]
            }
      }
      ```

5. External trigger to cleanup command on topic `selfupdate/desiredstate/command`:

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087,
            "payload": {
                  "baseline": "BASELINE NAME",
                  "command": "CLEANUP"
            }
      }
     ```

      Response on topic `selfupdate/desiredstatefeedback`

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787382,
            "payload": {
                  "status": "CLEANUP_SUCCESS",
                  "message": "Self-update agent has cleaned up after itself.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATE_SUCCESS",
                        "progress": 0,
                        "message": "Self-update agent has activated the new OS image."
                  }
                  ]
            }
      }
     ```

      ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687787382,
            "payload": {
                  "status": "COMPLETE",
                  "message": "Self-update completed.",
                  "actions": [
                  {
                        "component": {
                              "id": "self-update:os-image",
                              "version": "v0.0.10-194-g3d48cb8"
                        },
                        "status": "UPDATE_SUCCESS",
                        "progress": 0,
                        "message": "Self-update agent has activated the new OS image."
                  }
                  ]
            }
      }
      ```

### Rollback command

- External trigger to rollback command on topic `selfupdate/desiredstate/command`:

     ```json
      {
            "activityId": "1234567890",
            "timestamp": 1687510087,
            "payload": {
                  "baseline": "BASELINE NAME",
                  "command": "ROLLBACK"
            }
      }
     ```

     Self Update Agent returns in Idle state

 Can be used from

- Downloading (when it is waiting for DOWNLOAD command)
- Installing (when it is waiting for UPDATE command)
- Installed (when it is waiting for ACTIVATE command)
- Failed (when it is waiting for CLEANUP command)
