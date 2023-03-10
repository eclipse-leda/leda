---
title: "SDV Container Exec"
date: 2022-05-09T14:24:56+05:30
weight: 8
---

The `sdv-ctr-exec` wrapper allows to execute arbitrary user commands in existing containers.
Kanto Container Management cli tool (`kanto-cm`) only allows to manage the lifecycle of a container,
but does not allow to specify or override the entrypoint or command definitions of an existing container.
The `ctr` command line tool of containerd allows the execution of additional *tasks* in a running container.

## Usage

As a convenient tool, `sdv-ctr-exec` allows the simple execution of arbitrary commands inside of containers.
This is especially useful for non-service-containers, or containers which have additional binaries (e.g. cli tools) embedded.

Usage:

```shell
root@qemux86-64:~# sdv-ctr-exec 
/usr/bin/sdv-ctr-exec -h to print this message

Usage:
/usr/bin/sdv-ctr-exec <container-id> <command>
or
/usr/bin/sdv-ctr-exec -n <container-name> <command>
```

Example:

```shell
# Executing a containerized cli tool using sdv-ctr-exec
kanto-cm create --i --t --network=host --name=kuksa-client ghcr.io/eclipse/kuksa.val/kuksa-client:master
kanto-cm start --name=kuksa-client
sdv-ctr-exec -n kuksa-client /kuksa-client/bin/kuksa-client --port 30555 --protocol grpc --insecure
```

## Alternatives

### containerd: `ctr`

The above commands are equivalent to the following commands:

```shell
# Executing a containerized cli tool using ctr
ctr --namespace kanto-cm image pull ghcr.io/eclipse/kuksa.val/kuksa-client:master
ctr --namespace kanto-cm container create --net-host --tty ghcr.io/eclipse/kuksa.val/kuksa-client:master kuksa-client
ctr --namespace kanto-cm tasks start --detach kuksa-client
ctr --namespace kanto-cm tasks exec --tty --exec-id sometask kuksa-client /kuksa-client/bin/kuksa-client --port 30555 --protocol grpc --insecure
```

### containerd: `nerdctl`

> Note: `nerdctl` is currently not installed on the Leda Quickstart images.

### containerd: `ctr` and mounting

To execute a binary natively (outside of a containerized environment), the container image may be mounted to the host filesystem using the `ctr snapshots mount` commands.

This approach only works if the binary is compatible with the host environment (dependencies, libraries etc.).

```shell
$CONTAINER_IMAGE="ghcr.io/my-org/my-project/my-container"
ctr --namespace kanto-cm image pull $CONTAINER_IMAGE
ctr --namespace kanto-cm container create --net-host --tty $CONTAINER_IMAGE my-container
mkdir my-container
ctr --namespace=kanto-cm snapshots mount my-container my-container | $SHELL
cd my-container
./bin/my-application --help
```
