---
title: "SDV Device Info"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

Displays the current device configuration, such as Device ID.

> Note: **Requires** the *Cloud Connector* component to be configured and running.

Usage:

```shell
sdv-device-info
```

![Eclipse Leda Device Info Example Output](../sdv-device-info-example-output1.png)

## Usage

Synposis: `./sdv-device-info [options] [command]`

Full help:

```shell
root@qemux86-64:~# sdv-device-info --help
sdv-device-info v0.2
Usage: /usr/bin/sdv-device-info [options] [command]
Show SDV device configuration information
Example: /usr/bin/sdv-device-info show

Commands:
 show                 : Display configuration (default command)
 help                 : This message
 env                  : Format output for use in scripts

Options:
 --ansi | -a      : Don't use colored output.
 --norestart | -n : Do not automatically restart services
 --verbose | -v   : Enable verbose mode.
 --help | -h      : This message.
```

## Use in scripts

To use device information on other scripts, it may be useful to source the device information variables into the current environment variable context:

Synposis: `source ./sdv-device-info env`

Example:

```shell
$ source ./sdv-device-info env
$ echo $DEVICE_ID
exampledevice1
```
