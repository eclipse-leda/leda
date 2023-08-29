---
title: "Message Flow"
date: 2023-08-28T09:23:11+0300
weight: 2
---

> Note: This part of the Leda OSS stack is still in active development and there might be differences between the documented and the current version.

As described in [Vehicle Update Manager](../) takes a full update message for all domains, identifies the domains affected, the current component versions,
actions to be taken, etc., and delegates those actions to the correct update agent (e.g. self-update/container update).

The update manager (UM) in Leda-distro is configured as specified in [UM's config.json](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-kanto/files/update-manager/config.json),
which on the final image is usually located in `/etc/update-manager/config.json`. The standard two domains supported are _containers_ and _self-update_,
with the latter requiring a reboot on a successful update.

> Note: UM allows a custom prefix for all of its topics to be defined ("domain") in its `config.json` On the Leda Distro image the default prefix is "**vehicle**".
> If you decide to change it, replace "**vehicle**" in all MQTT topics mentioned below with your custom prefix.

A full specification of UM's API and the relevant MQTT topics can be found [in its documentation](https://github.com/eclipse-kanto/update-manager/blob/main/docs/update-agent-api.md).

## Update Message

The general structure of the update message is as follows:

```json
{
  "activityId": "correlation-activity-uuid",
  "timestamp": 123456789,
  "payload": {
    "domains": [
      {
        "id": "domain",
        "config": [],
        "components": [
            {
                "id": "component1",
                "version": "component1-version",
                "config": [
                    {
                        "key": "component1-config-key-1",
                        "value": "component1-config-value-1"
                    }
                ]
            }
        ]
      }
    ]
  }
}
```

Where multiple domains and components per domain (each with multiple configuration key-value pairs) are allowed. To trigger an update, publish
your full update message on the `vehicleupdate/desiredstate` MQTT topic. When UM receives your message, it splits it across the required domains and
publishes messages to the topics that the [domain-specific agents are monitoring](../).

Similarly, update progress can be monitored on the `vehicleupdate/desiredstatefeedback` topic.

## Self-update

The messages for triggering a self-update (image update) are the same as in [The Self Update Tutorial](../../self-update/self-update-tutorial).
The only difference here is that when you publish a self-update message on the `vehicleupdate/desiredstate` topic,
UM will automatically take care to forward your message to the self-update agent, including
forwarding back the update feedback on the `vehicleupdate/`-namespaced topics.

## Containers update (desired state)

Similarly to the self-update, you should start by understanding the operation of the [Container Update Agent](../../container-management/container-update-agent).
After constructing the desired state message you can publish it on the `vehicleupdate/desiredstate` and UM will, again, forward it to CUA automatically,
based on the domain specified in the update message.

## Combined update messages

The real strength of UM is deploying updates accross multiple domains with a single update message. For example, if you'd like to deploy an image update bundle
(self-update) and a single `hello-world` container image with the environment variable `FOO=BAR` set, you can construct the following message:

```json
{
   "activityId":"random-uuid-as-string",
   "timestamp":123456789,
   "payload":{
      "domains":[
         {
            "id":"self-update",
            "components":[
               {
                  "id":"os-image",
                  "version":"${VERSION_ID}",
                  "config":[
                     {
                        "key":"image",
                        "value":"https://leda-bundle-server/sdv-rauc-bundle-minimal-qemux86-64.raucb"
                     }
                  ]
               }
            ]
         },
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
                        "key":"env",
                        "value":"FOO=BAR"
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

And publish the message on the MQTT topic `vehicleupdate/desiredstate`. UM will take actions to identify the affected update domains and publish the correct
messages on the respective topics. All feedback from the specific update agents will be forwarded back to the UM and published on the `vehicleupdate/desiredstatefeedback`
topic. All these messages will use the same activityId so they can be correlated with each other.
