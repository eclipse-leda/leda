---
title: "Message Flow"
date: 2023-08-28T09:23:11+0300
weight: 2
---

> Note: This part of the Leda OSS stack is still in active development and there might be diffrences between the documented and the current version.

As described in [Vehicle Update Manager](../) takes a full update message for all domains, identifies the domains affected, current component verison,
actions to be taken, etc. and delegates those actions to the correct update agent (e.g. self-update/container update).

The update manager (UM) in Leda-distro is configured as specified in [UM's config.json](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-kanto/files/update-manager/config.json),
which on the final image is usually located in `/etc/update-manager/config.json`. The stantard two domains supported are _containers_ and _self-update_,
with the latter requiring a reboot on succesful update.

> Note: UM allows a custom prefix for all of its topics to be defined ("domain") in its `config.json` On the Leda Distro image the default prefix is "**vehicle**".
> If you decide to change it, replace "**vehicle**" in all MQTT topics mentioned below with your custom prefix.

A full specification of UM's API and the relevant MQTT topics can be found [in its documentation](https://github.com/eclipse-kanto/update-manager/blob/main/docs/update-agent-api.md).

## Update message

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

Where multiple domains and components per domain (each with multiple configuration key-value pairs) are allowed. To trigger a desired-state based update, publish
your full update message on the `vehicleupdate/desiredstate` MQTT topic. When UM receives your message, it would split it accross the required domains and
publish messages to the topics that the [domain-specific agents are monitoring](../).

Similarly, update progress can be monitored on the `vehicleupdate/desiredstatefeedback` topic.

## Self-update

The messages for triggering a self-update (image update) are the same as in [The Self Update Tutorial](../../self-update/self-update-tutorial).
The only difference here is that when you publish a self-update message on the `vehicleupdate/desiredstate` topic,
UM will automatically take care to forward your message to the self-update agent, including
forwarding back the update feedback on the `vehicleupdate/`-namespaced topics.

## Container-update (desired state)
