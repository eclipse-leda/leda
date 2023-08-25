---
title: "Configuration"
date: 2023-08-25T17:03:19+0300
weight: 1
---

## Config file

The default location for the VUM service on the Leda Distro image can be found at `/etc/update-manager/config.json`.
The location of the config file is specified with the `--cfg-file [PATH]` flag when starting the binary.

## Minimal configuration

A minimal configuration (that is used by the Leda Distro) is the following:

```json
{
    "log": {
      "logFile": "/var/log/update-manager/update-manager.log"
    },
    "domain": "vehicle",
    "agents": {
        "containers": {
            "name": "containers",
            "rebootRequired": false,
            "readTimeout": "30s"
        },
        "self-update": {
            "name": "self-update",
            "rebootRequired": true,
            "readTimeout": "30s"
        }
    },
    "thingsEnabled": false
}
```

Where:

- "domain": specifies the prefix for the MQTT topic, e.g. in this case it's set to `vehicle`, so all VUM related topic are prefixed with `vehicleupdate/[TOPIC]`
- "agents": configures the update agents that would be available to VUM. Here the "readTimeout" key specifies how long should VUM wait for a response from the configured agent.
- "thingsEnabled": whether VUM should use the Kanto Things API for communication or not.

## Full configuration

An example configuration file for VUM with all available options is the following one:

```json
{
  "log": {
    "logFile": "log/update-manager.log",
    "logLevel": "ERROR",
    "logFileSize": 3,
    "logFileCount": 6,
    "logFileMaxAge": 29
  },
  "connection": {
    "broker":"www",
    "keepAlive": 500,
    "disconnectTimeout": 500,
    "username":"username",
    "password":"pass",
    "connectTimeout": 500,
    "acknowledgeTimeout": 500,
    "subscribeTimeout": 500,
    "unsubscribeTimeout": 500
  },
  "domain": "vehicle",
  "thingsEnabled": false,
  "rebootEnabled": true,
  "rebootAfter": "1m",
  "reportFeedbackInterval": "2m",
  "currentStateDelay": "1m",
  "phaseTimeout": "2m",
  "agents": {
    "self-update": {
      "rebootRequired": false,
      "readTimeout": "20s"
    },
    "containers": {
      "rebootRequired": true,
      "readTimeout": "30s"
    }
  }
}
```

Here keys (other the ones above) are self-explanatory. The "connection" section object specifies configuration options for the MQTT connection.
Allowed log leves (in order of increasing verbosity)are: ERROR, WARN, INFO, DEBUG, TRACE.
