---
title: "Blueprint Selector"
date: 2023-10-02T12:43:16+00:00
weight: 30
---

A Rust application that reads all blueprint files in a directory and provides the user with an
interactive (supports filtering) menu to select the one to be deployed on the edge device via MQTT.
If no directory is provided the default one on a Leda Quickstart Image is: `/data/var/containers/blueprints`.

![Screenshot](../blueprint-selector-1.png)

The "blueprint" files are desired state messages, that have the extension ".blueprint.json" (configurable) and an additional metadata header (required):

```json
{
  "blueprintMetadata": {
    "name": "<NAME>",
    "description": "<Short Description>"
  },
  "activityId": "correlation-id",
  "timestamp": 1235466
  "payload": {} // This is the desired state message
}
```

The metadata header will be used to construct the list of options presented to the user. You can find example blueprints under the
`example_blueprints` directory in the [leda-utils repository](https://github.com/eclipse-leda/leda-utils/tree/main/src/rust/blueprint-selector/example_blueprints).

The selected blueprint is then published as an MQTT message on the `vehicleupdate/desiredstate` topic.

## CLI options

To get all available configuration options use the `--help/-h` flag:

```shell
A user-friendly tool to select and deploy SDV blueprints

Usage: blueprint-selector [OPTIONS]

Options:
  -d, --blueprints-dir <BLUEPRINTS_DIR>
          The directory containing the SDV blueprints [default: /data/var/containers/blueprints]
  -f, --fetch-blueprints
          Start in fetch mode (presents a menu to fetch new/updated blueprints) from a remote repository
  -e, --blueprints-ext <BLUEPRINT_EXTENSION>
          Extension to use when iterating over the files in the blueprints directory [default: .blueprint.json]
      --mqtt-broker-host <HOST>
          Hostname/IP to the MQTT broker where the desired state message would be posted [default: 127.0.0.1]
      --mqtt-broker-port <PORT>
          Port for the MQTT broker [default: 1883]
      --mqtt-topic <TOPIC>
          Topic on which to publish the blueprint desired state message [default: vehicleupdate/desiredstate]
  -h, --help
          Print help
  -V, --version
          Print version
```

## Normal mode

To run in normal mode use:

```shell
blueprint-selector
```

or if you'd like to provide a directory different from the default one, use:

```shell
blueprint-selector -d </path/to/dir>
```

## Fetch mode

When starting the `blueprint-selector` with the `-f/--fetch-blueprints` flag, you will be presented with a selection of different
fetchers that allow you to download/update blueprints directly in the directory specified with the `-d/--blueprints-dir` flag
(or in the default directory if not specified).
For example:

```shell
  blueprint-selector -fd </path/to/dir>
```

![Selection](https://raw.githubusercontent.com/eclipse-leda/leda-utils/main/src/rust/blueprint-selector/images/fetcher-selection-screenshot.png)

When you choose a fetcher, you will be asked for an URI and `blueprint-selector` will attempt to fetch the blueprints inside the directory specified by `-d`.

After providing a URI, pressing Enter, and a successful fetch, you will be brought back to the usual
selector menu, this time including all successfully fetched manifests.

![Success](https://raw.githubusercontent.com/eclipse-leda/leda-utils/main/src/rust/blueprint-selector/images/fetcher_success.png)