---
title: "KantUI"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

The KantoUI tool is a text-based user interface for conveniently managing containers in the Kanto Container Management.
It supports simple navigation using keyboard and mouse to select a specific container.
Commands to start, stop, remove and re-deploy containers are available along with a functionality to retrieve the application logs of a selected container.

## Kanto User Interface

Usage:

```shell
kantui
```

Example output:

![KantoUI](../kantui-large.png)

## Command Line Options

Print command line help:

```shell
root@qemux86-64:~# kantui --help
kantui 0.2.0
A TUI for Kanto CM that allows easier management of deployed containers. Requires root.

USAGE:
    kantui [OPTIONS]

OPTIONS:
    -c, --config-file-path <CONFIG_FILE_PATH>
            Set a custom path for the kantui configuration file [default:
            /etc/kantui/kantui_conf.toml]

    -h, --help
            Print help information

    -V, --version
            Print version information

Note: All config values can be overridden through env variables prefixed with KANTUI_,
e.g. KANTUI_STOP_TIMEOUT=5 overrides the timeout before SIGKILL is sent to be 5 seconds.
```

## Keyboard commands

- Arrow keys `Up` and `Down` to select a container
- Arrow keys `Left` and `Right` to select a column
- `Enter` to change the sort ordering of the currently selected column
- `S` to **start** the selected container which is currently not running
- `P` to **stop** the selected container
- `R` to **remove** a container
- `L` to show the **log output** of a container
- `D` to redeploy an existing container (rereads deployment descriptor)
- `Q` to **quit** kantui

> Note: The mouse can be used to select ui items when holding the `Shift` key.

## Starting, Stopping, Removing containers

To use the lifecycle commands on a container:

1. Select a container by using the mouse or the arrow keys.
2. The selected container is highlighted.
3. Press one of the lifecycle commands, e.g. `s`, `p` or `r`
4. Wait for the value in the *State* column to change, before issueing the next command.

> Note: When using the lifecycle commands for containers (Start, Stop, Remove), it may take a few seconds before the UI is updated with the status changes.
  The amount of time before a container is forcefully killed is determined by the `stop_timeout` configuration option.

## Show container Logs

To view the container's log output:

1. Select a container by using the mouse or the arrow keys.
2. Press the `L` key
3. Log output will be displayed (tail, oldest messages first)
4. Use the arrow keys `Up` and `Down` or drag the scrollbar using your mouse to scroll through the log
5. Close the Log viewer by pressing `Enter` or clicking on the `OK` button

> Note: The log output is **not followed** automatically. Close the dialog and reopen to see new output.

## Redeploying containers

To redeploy a container, e.g. when a deployment descriptor has changed on disk:

1. Select a container by using the mouse or the arrow keys.
2. Press the `P` key to stop the container
3. Press the `R` key to remove the container
4. Press the `D` key to invoke the Kanto Auto Deployer, which will redeploy the missing containers

> Note: Only containers managed by Kanto Auto Deployer will be redeployed.

## Column Sorting

To sort a column:

1. Select the column using the `Left` and `Right` arrow keys
2. Press `Enter` to activate sorting
3. Press `Enter` again on a sorted column to invert sort order (Ascending -> Descending -> Ascending)

> Note: The selected sort order is not persisted and will reset to the default on restart: By `ID`, ascending

## Configuration File

The default location of the configuration file is `/etc/kantui/kantui_conf.toml`:

```shell
# General Configuration Options
socket_path = "/run/container-management/container-management.sock" # Path to kanto-cm unix socket
stop_timeout = 5 # timeout (integer) in seconds before a SIGKILL is sent after a SIGTERM

[keyconfig]
start_btn_name = "[S]tart"
start_kbd_key = "s"

stop_btn_name = "Sto[P]"
stop_kbd_key = "p"

remove_btn_name = "[R]emove"
remove_kbd_key = "r"

logs_btn_name = "[L]ogs"
logs_kbd_key = "l"

quit_btn_name = "[Q]uit"
quit_kbd_key = "q"

redeploy_btn_name = "Re[D]eploy"
redeploy_kbd_key = "d"
# Includes a shell lexer so anything that would be a valid shell command can be used
# No pipes/redirects allowed.
# N.B.: Command inherits kantui's privileges (root)
redeploy_command = "systemctl restart kanto-auto-deployer.service"
```
