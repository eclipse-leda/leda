---
title: "SDV Health"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Health check

The sdv-health utility displays a status overview of some important dependencies and device configurations for the SDV edge stack.
The sdv health utility can be configured using the sdv.conf configuration file.

Usage:

```shell
# sdv-health
```

Example output:

![SDV Health Example Output](../sdv-health-output.png)

### Version Information

The Leda image version and build time will be displayed at the top in the first category:

- OS Release: Year and codename of the release version
- Image Version: Name of the image and more specific version information, such as the git tag or commit id
- Build timestamp in `yyyMMddHHmmss` notation

> Note: The information is read from the system base file in `/etc/os-release`:

  ```shell
  root@qemux86-64:~# cat /etc/os-release 
  BUILD_ID="20230309083051"
  DISTRO_CODENAME="Dracon"
  ID=leda
  IMAGE_VERSION="0.0.5-41-g82f2b12"
  NAME="Eclipse Leda"
  PRETTY_NAME="Eclipse Leda 2023 (Dracon)"
  VERSION="2023 (Dracon)"
  VERSION_CODENAME="Dracon"
  VERSION_ID=0.0.5-41-g82f2b12
  ```

### Bus networks

If available, vehicle bus network information, such as the status of the CAN-Bus, will be displayed iin its own category.
This helps to quickly identify if there problems with the hardware connectivity for automotive bus networks.

### Ports

The health utility checks the TCP ports of specific services.
This helps to identify if these services are up and running and potentiallyconnectable via external network interfaces.

### Services and Containers

The services category shows the status of required and optional containers.
The required containers are supposed to be up and running for the SDV.EDGE stack to be correctly up and running.
If any of these core components have a failed state, the functionality is impacted.

The optional containers are for additional features and for example applications.
These containers may not be necessary for each use case and hence will be marked as a warning if they are not up and running.
The overview still helps to identify which containers are working properly.

### Errors, Warnings, Failed states

When there are errors or warnings related to the status of SDV related components,
the health utility will print out these error states, and if available also a more detailed error message.

In the following example, the health utility helps the troubleshooting process:

- The container runtime is properly started: "Kanto CM" is OK in the "SDV Ports" section and the "container-management" service is OK in the "SDV Services" section".
- Some containers are in state "OK", which means there is no general issue with the container runtime.
- The cloud connector is in a "Stopped" state, which indicates that the user manually stopped the container by using "kanto-cm stop -n cloud-connector".
- The sua container is in a "Exited" state, which indicates the process exited with an error code.

![SDV Health Example Errors](../sdv-health-example-errors2.png)
