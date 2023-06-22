---
title: "Running on Linux"
date: 2023-05-09T14:24:56+05:30
weight: 5
---

To run the main components of the SDV EDGE stack on an existing Linux distribution (e.g. Debian, Ubuntu, Raspberry Pi OS),
you need to install the following packages.

Please note that since this is not a full-system installation, but an additional installation, there are some differences
compared to the usual Leda installation on Docker/QEMU/Devices using our Quickstart image:

- The Self-Update use case is not used, as the distribution-specific channels apply.
  E.g. it does not make sense to use the Leda infrastructure to flash a full system image.
- The configuration differs slightly and you need to put some more work into getting the examples to work out of the box.
  This may include different port numbers, different paths of volume mounts for containers etc.

## Debian-based Linux distributions

Tested on x86_64 via Docker:

- Debian 11
- Debian 12
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 23.10

> *Note:* Ubuntu 18.04 is not supported, as the glibc is outdated.

### Pre-Requisuites

The SDV stack requires the following packages to be present on the target system:

- Mosquitto (adapt configuration, see below)
- Data folders

  - Storage for Self Update Bundles: `mkdir -p /data/selfupdates`
  - Device Certificates Folder:

    ```shell
    # Required by Cloud Connector
    mkdir -p /data/var/certificates/
    touch /data/var/certificates/device.crt
    touch /data/var/certificates/device.key
    ```

- systemd *(Optional: You can also manually start the services)*
- D-Bus *(Optional: This is for Self Update Agent to RAUC integration)*
- RAUC *(Optional: Only for Self-Update Use Case or testing purposes)*

### Installation Steps

*Note: The steps below are examples for x86 platform. If you deploy on ARM64 platform, adapt the filenames accordingly.*

1. Update repository and install dependencies:

    ```shell
    apt-get update
    apt-get -y install ca-certificates mosquitto wget
    
    # Optional:
    apt-get -y install dbus rauc
    ```

1. Download the Debian package from the [Eclipse Kanto](https://github.com/eclipse-kanto/kanto/releases) release page

    ```shell
    wget "https://github.com/eclipse-kanto/kanto/releases/download/v0.1.0-M3/kanto_0.1.0-M3_linux_x86_64.deb"
    apt-get install -y ./kanto_0.1.0-M3_linux_x86_64.deb

    # Check if Kanto has been installed
    command -v container-management
    command -v kanto-cm
    systemctl status container-management
    ```

    > *Note:* This will also install `containerd`.

1. Download the Debian packages from the [Eclipse Leda Utilities](https://github.com/eclipse-leda/leda-utils/releases/) release page:

    ```shell
    wget "https://github.com/eclipse-leda/leda-utils/releases/download/v0.0.2/eclipse-leda-utils_0.0.2.0.00680_all.deb"
    apt-get install -y ./eclipse-leda-utils_0.0.2.0.00680_all.deb
    command -v sdv-health

    wget "https://github.com/eclipse-leda/leda-utils/releases/download/v0.0.2/eclipse-leda-kantui_0.0.2.0.00680_amd64.deb"
    apt-get install -y ./eclipse-leda-kantui_0.0.2.0.00680_amd64.deb
    command -v kantui

    wget "https://github.com/eclipse-leda/leda-utils/releases/download/v0.0.2/eclipse-leda-kanto-auto-deployer_0.0.2.0.00680_amd64.deb"
    apt-get install -y ./eclipse-leda-kanto-auto-deployer_0.0.2.0.00680_amd64.deb
    command -v kanto-auto-deployer
    ```

1. Download the Debian package `eclipse-leda-container-*.deb` from the [Eclipse Meta-Leda](https://github.com/eclipse-leda/meta-leda/releases) release page:

    ```shell
    wget "https://github.com/eclipse-leda/meta-leda/releases/download/0.1.0-M2/eclipse-leda-containers_0.1.0.2.0.422_all.deb"
    apt-get install -y ./eclipse-leda-containers_0.1.0.2.0.422_all.deb
    ```

1. Run the `kanto-auto-deployer` to deploy the core components:

    ```shell
    kanto-auto-deployer /var/containers/manifests
    ```

    To install the example containers, run the following:

    ```shell
    kanto-auto-deployer /var/containers/manifests/examples
    ```

### Configuration Hacks

- Mosquitto must be configured to allow anonymous access and listen on the network interface available to the containers. The easiest (and least secure!) configuration would be:

    `/etc/mosquitto/conf.d/public.conf`:

    ```plain
    listener 1883 0.0.0.0
    allow_anonymous true
    ```

    > **Attention:** Only apply this configuration on a device in a secured network, or adapt the configuration accordingly (e.g. specify internal IP address)
