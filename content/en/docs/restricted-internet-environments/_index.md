---
title: "Restricted-Internet Environments"
date: 2023-01-03T17:24:56+05:30
weight: 12
---

Developers working in a corporate environment may face challenges when building Leda-based images, pulling SDV containers, etc.,
usually due to a restrictive corporate proxy. Thus the objective of this page is to collect helpful guides for mitigating such problems.

## HTTP(S) proxy

First you might need to configure your http(s) SOCKS proxy such that the BitBake shell uses it for `do_fetch` recipe tasks. By default, `http_proxy` and `https_proxy`
environment variables are part of the `BB_ENV_PASSTHROUGH` list and are directly passed from the current environment to BitBake. If you are still facing `http(s)_proxy`
issues during `do_fetch` tasks, you might want to check the [Working Behind a Network Proxy @ Yocto Project Wiki](https://wiki.yoctoproject.org/wiki/Working_Behind_a_Network_Proxy).

## GOPROXY

GOPROXY is a golang-specific mechanism for fetching dependencies during build-time. What is more, _gomod-type_ BitBake recipes pull their external dependencies during
the `do_compile` task, instead of the `do_fetch` task leading to further issues. The simplest workaround is to set-up a local (caching) goproxy container on
the build host and make BitBake use that. The following steps assume that the build host has docker installed and working, with access to the docker hub registry.

### Hosting a local goproxy server

Start by setting up the goproxy container in host networking mode.

```shell
docker run -d --env HTTP_PROXY="http://<PROXY_IP>:<PROXY_PORT>" --env HTTPS_PROXY="http://<PROXY_IP>:<PROXY_PORT>" -v cacheDir:/go --network host goproxy/goproxy
```

_NOTE:_ Don't forget to substitute `<PROXY_IP>` and `<PROXY_PORT>` with the appropriate address of your HTTP(S) proxy.

This will start a local caching goproxy on port `8081` with a volume named `cacheDir` for caching the downloaded Go packages. The goproxy container can be configured
further to provide access to private Go-package registries. For more information on its configuration take a look at [goproxyio/goproxy on GitHub](https://github.com/goproxyio/goproxy).

### Using the local goproxy server for BitBake builds

Since the main objective of BitBake/kas is to facilitate reproducible builds, only certain variables from the host environment are used for the build. Go, however,
looks at the `GOPROXY` environmental variable to decide on which proxy to use. That's why you should first start by exporting the GOPROXY variable in the terminal
from which you will later run the build:

```shell
export GOPROXY="http://127.0.0.1:8081"
```

To make BitBake use the value of the variable you just exported for the build, you should add it to its "environment passtrough" list:

```shell
export BB_ENV_PASSTHROUGH_ADDITIONS="${BB_ENV_PASSTHROUGH_ADDITIONS} GOPROXY"
```

### Kas

If you are using kas as a top-level build tool, to set the value of the GOPROXY variable for builds, all you need to do is to add it the _env_-section of your
kas-config yaml. For example:

```yaml
header:
  version: 12
machine: qemux86-64
env:
  GOPROXY: "http://127.0.0.1:8081"
```

Kas will handle the exporting of the variable and adding it to BitBake's passtrough list automatically from there.

## Airgapped container installation

Sometimes devices might not have internet access on first boot and therefore the SDV containers that are needed for provisioning and updating a SDV-image
will not be available.

### Build-Time

The meta-leda layer provides an opitional distro feature that pre-downloads and injects a minimal set of SDV container images in Kanto's local container registry
on first boot.

__IMPORTANT__: **This will lead to a significant increase of the image size since all containers are downloaded as self-contained tarballs and therefore "layer reuse"
is not possible.**

To enable this distro feature, add to your `local.conf`:

```shell
  DISTRO_FEATURES += " airgap-containers"
  PREINSTALLED_CTR_IMAGES_DIR = "/path/to/container/images"
  IMAGE_INSTALL += "packagegroup-sdv-airgap-containers"
```

If you are using the `sdv-image-data` image recipe `packagegroup-sdv-airgap-containers` will be automatically installed when the distro-feature is enabled.
Therefore all you need to add to your `local.conf` will be:

```shell
  DISTRO_FEATURES += " airgap-containers"
  PREINSTALLED_CTR_IMAGES_DIR = "/data/var/containers/images"
```

_Note_: _Here we have assumed that the partition where sdv-image-data is installed is mounted as `/data` on the rootfs_.

### Manual

If you do not wish to use the _airgap-containers_ distro-feature, you can manually download inject the container images in the kanto namespace with ctr.

1. Start on a machine with internet access and docker/ctr installed:

    Pull the container image in your machine's local registry:

    ```shell
    ctr -n kanto-cm image pull <REGISTRY>/<IMAGE>:<TAG> --platform linux/<ARCH>
    ```

    Where if you would like to download the Kuksa Databroker container for an arm64 device you would change the following:

    ```text
    <REGISTRY>/<IMAGE>:<TAG> -> ghcr.io/eclipse/kuksa.val/databroker:0.3.0 
    <ARCH> -> arm64
    ```

    After the pull was successful, export the image as a tarball:

    ```shell
    ctr -n kanto-cm images export <tarbal_name>.tar <REGISTRY>/<IMAGE>:<TAG> --platform --platform linux/<ARCH>
    ```

   `<REGISTRY>/<IMAGE>:<TAG>` and `<ARCH>` __should__ be the same as in the `pull` command, while `<tarball_name>` can be any name you would like.

2. Transfer the exported `<tarball_name>.tar` to your device to a folder of your choosing, e.g. `/data/var/containers/images`

3. Obtain a terminal connection to this device and go to the directory where you transferred the container image tarball.

4. Import the image to the kanto-cm registry by running:

    ```shell
    ctr --namespace kanto-cm image import <tarball_name>.tar
    ```

    _Note_: If you see a message from ctr that the "image might be filtered out" this means that you might have pulled an image for an architecture that 
    does not match the one of your device.
