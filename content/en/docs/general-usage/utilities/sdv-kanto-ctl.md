---
title: "SDV Kanto-Ctl"
date: 2022-05-09T14:24:56+05:30
weight: 20
---

Manage the Kanto Container Management configuration via CLI.

> Note: **Requires** `jq` to be installed.

Features:

- Add and remove container registries (for authentication purposes)
- Set primitive values in configuration
- Restart `container-management.service` on configuration changes
- Automatically back up configuration file
- Display changes to user

![Eclipse Leda Kanto Container Manager Configuration utility](../sdv-kanto-ctl-example-output1.png)

## Usage

Synposis: `./sdv-kanto-ctl <command> [<options>]`

Full help:

```shell
$ ./sdv-kanto-ctl --help
Eclipse Kanto Container Manager Configuration Utility
See https://websites.eclipseprojects.io/kanto/docs/references/containers/container-manager-config/
Usage: ./sdv-kanto-ctl <command> {options}
Commands:
        add-registry -h <hostname> -u <username> -p <password>
                Adds or replaces a container registry authentication configuration
                -h or --hostname: Configure the hostname of the container registry (e.g. hub.docker.io, ghcr.io, ...)
                -u or --username: Configure the username
                -p or --password: Configure the password
        remove-registry -h <hostname>
                Removes the specified container registry
                -h or --hostname: The hostname of the container registry
        remove-all-registries
                Removes all configured container registries
        list-registries
                Prints all configured container registries
        show-config
                Print the container management configuration
        set <key> <value>
                Set a primitive configuration value. Key in JSON Dot-Notation
                Examples: ./sdv-kanto-ctl set containers.registry_configurations.MyRegistry.credentials.password foobar
                          ./sdv-kanto-ctl set things.enable true
Options:
        --no-reload : Do not reload the configuration and restart the container-management service automatically
        --ansi : Don't use colored output.
        --verbose | -v : Enable verbose mode.
        --help : This message.
```

### Example: Private Container Registries

To be able to pull container images, the container runtime needs access to the container registry.
Some container registries require authentication.
The Kanto Container Manager can be configured to use credentials when accessing remote container registries.

In the Leda images, the *sdv-kanto-ctl* tools allows to easily add authentication to the container manager configuration:

```shell
sdv-kanto-ctl add-registry -h <registryhostname> -u <your_username> -p <your_password>
```

For example, to access container images from GitHub Packages in a private repository, you need a GitHub Personal Access Token (PAT) with the `read: packages` scope.
Then, add the repository as shown below:

```shell
sdv-kanto-ctl add-registry -h ghcr.io -u github -p <Your_GitHub_PersonalAccessToken>
```

*sdv-kanto-ctl*  will make the necessary modifications to `/etc/container-management/config.json` and restarts the `container-management.service` systemd unit,
so that the changes take effect. You may need to recreate or restart the container if a previous pull failed.

Please see the [Eclipse Kanto Container Manager Configuration reference](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-manager-config/)
for details.

### Example: Enabling Things management

Enable the container manager digital twin representation.

```shell
sdv-kanto-ctl set things.enable true
```

### Example: Container Stop Timeout

Kanto waits for a timeout before forcefully stopping a container.
The default is 30 seconds in Kanto, and 10 seconds in the Leda quickstart image.

To change this behavior at runtime:

```shell
sdv-kanto-ctl set manager.default_ctrs_stop_timeout 2
```
