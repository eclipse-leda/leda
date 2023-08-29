---
title: "Container Registries"
date: 2022-05-09T14:24:56+05:30
weight: 5
---

When deploying containerized applications, the container runtime will pull container images from a (remote) container registry.

The pulled container images and their layers are then stored in a local storage.

## Private Container Registries

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

Please see the [Eclipse Kanto Container Manager Configuration reference](https://eclipse.dev/kanto/docs/references/containers/container-manager-config/)
for details.
