---
title: "Container Update Agent"
date: 2023-08-28T12:09:24+0300
weight: 2
---

## About the Container Update Agent (CUA)

The container update agent is a component of kanto container management, that can be enabled in the [Container Management's config.json](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-kanto/files/container-management/config.json).
When it receives a desired state message on the `containersupdate/desiredstate` topic it compares the containers (with their current versions and configuration)
that are managed by Kanto Container Management and those described in the desired state messages. When it has identified the differences between the two,
it resolves them by deleting, downloading, or re-creating containers.

## The desired state message

A basic desired state message has a similar structure to all update messages. To deploy the `hello-world` docker container (removing all other containers
currently deployed on the device), you can publish the following desired state message:

```json
{
   "activityId":"test-correlation-activity-uuid",
   "payload":{
      "domains":[
         {
            "id":"containers",
            "config":[],
            "components":[
               {
                  "id":"hello-world",
                  "version":"latest",
                  "config":[
                     {
                        "key":"image",
                        "value":"docker.io/library/hello-world:latest"
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

You can configure port mappings, environment variables, device mapping, logging, and more, by adding additional key-value pairs
to the "config" array of the given container. For example, if you want to set the environment variable `FOO="BAR"` inside the container, you can
specify:

```json
{
   "activityId":"test-correlation-activity-uuid",
   "payload":{
      "domains":[
         {
            "id":"containers",
            "config":[],
            "components":[
               {
                  "id":"hello-world",
                  "version":"latest",
                  "config":[
                     {
                        "key":"image",
                        "value":"docker.io/library/hello-world:latest"
                     },
                     {
                        "key": "env",
                        "value" "FOO=BAR"
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```
<!-- FIXME:  Link to an official page on the Kanto website when it gets released-->
A full list of all key-value pairs with their defaults can be found in [this doc for CUA](https://github.com/SoftwareDefinedVehicle/kanto-container-management-fork/blob/d3602e5e87e3690ed7b3e48f7b97ed0b45421656/docs/updateagent/container-component-config.md).

## System containers

If a container is not specified in the desired state message, it would be **deleted by CUA** when the message is received. This might be undesirable for containers
that are supposed to run as **system services** from the first boot of the device through its operation. Such a container might be the Self Update Agent container
on the Leda Distro image, which we do not want to specify in every desired state message and deleting/recreating-it during an update might lead to unexpected behaviour.
That's why in [Container Management's config.json](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-kanto/files/container-management/config.json)
in the CUA section, you can specify in the "**system_containers**" array the names of those containers that would like to be treated as such.

## MQTT Topics

Since the MQTT interface of the update agent is abstract, the following message flows are similar to those for the self-update agent mentioned in its [tutorial](../../self-update/self-update-tutorial.md#example-message-flows)

### Getting the current state

On initialization, CUA will publish the current state of all containers on the `containersupdate/currentstate` topic,
the activityId for such a message would be `initial-current-state-<TIMESTAMP>`. This message can be understood as the "current container inventory".
An example inventory from a running Leda image is [currentstate-leda.json](../currentstate-leda.json).

You can request an update of the current state at any point by publishing an empty message on the: `containersupdate/currentstate/get`:

```json
{
   "activityId": "<UUID>",
   "timestamp": 123456789,
   "payload": {}
}
```

The updated inventory will, again, be published on the `containersupdate/currentstate` topic with correlation ID of `<UUID>`.

### Deploying a desired state message

A desired state message describing the containers and their environments of a typical Leda Distro deployment is [leda-desired-state.json](../leda-desired-state.json).
To trigger a desired state deployment directly from CUA, publish the message above on `containersupdate/desiredstate`, e.g. by running:

```shell
   mosquitto_pub -t containersupdate/desiredstate -f leda-desired-state.json
```

You can monitor the update feedback from CUA, by listening on the topic `containersupdate/desiredstatefeedback`.

> Note: Since the desired state feedback can be quite verbose and happens in real time during the update it could be hard to understand manually.
> However it's structured json, so it could be easily machine-parsed and monitored for specific key-value pairs.
