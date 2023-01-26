---
title: "Self Update Tutorial"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

This chapter describes the steps necessary to perform a local (without cloud) self update of the operating system.

![](../self-update-arch.png)

## Self-Update using RAUC Update Bundles

- On host: Update bundle `sdv-rauc-bundle-qemux86-64.raucb` is in current folder

  *Note: In the development environment, the update RAUC Update Bundle is located in the BitBake machine-specific output folder, for example `tmp/deploy/images/qemux86-64`*
- On host: Start a dummy web server for serving the update file

      python3 -m http.server --bind 192.168.7.1

- On host: open two new terminals - one for monitoring and one for triggering the self-update

   - Terminal 1: To view the progress, watch the MQTT topics `selfupdate/desiredstate` and `selfupdate/desiredstatefeedback`:

         mosquitto_sub -h 192.168.7.2 -p 1883 -t "selfupdate/#"

   - Terminal 2: Trigger the actual self update process by publishing an MQTT message to `selfupdate/desiredstate`:

         mosquitto_pub -h 192.168.7.2 -p 1883 -t "selfupdate/desiredstate" -f start-update-example.yaml

- Switch to a terminal in the guest
- On guest: After the self update process completed, check the status:

      rauc status --detailed

## Self-Update Trigger Message

`start-update-example.yaml` file:

{{<readfile file="start-update-example.yaml" code="true" lang="yaml">}}
