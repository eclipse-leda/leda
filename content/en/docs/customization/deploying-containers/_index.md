---
title: "Deploying Containers"
date: 2023-01-03T17:24:56+05:30
weight: 2
---


## Kanto-auto-deployer (KAD)

This service has been implemented as a stopgap solution by the Leda team since as of now the Kanto CM-native mechanism
for initial container deployment does not suit the needs of the Leda Quickstart image well.

In-depth documentation on its operation and development can be found in [Kanto Auto deployer](../../build/dev-and-maintenance/rust/kanto-auto-deployer).

In the Leda Distro KAD runs as a service that continuously monitors the directory defined with the BitBake variable `KANTO_MANIFESTS_DEV_DIR` in the distro config recipes.
By default, the Leda quickstart images use `KANTO_MANIFESTS_DEV_DIR=/data/var/containers/manifests"`.
So, these manifests are again stored in the persistent **data**-partition and can be modified after the image has been deployed.

**Important: KAD supports the [Kanto Container Management Manifest Template](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-config/#template) 
AND the [Container Internal State Representation](../../build/dev-and-maintenance/rust/kanto-auto-deployer//#internal-state-representation). For future compatiblity reasons it is recommended that you choose [Kanto Container Management Manifest Template](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-config/#template).** 

A standard set of containers is deployed through meta-leda, the manifests for which can be found in `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/core` and `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example`.  

The advantage of this service is that it can be restarted very quickly (`systemctl restart kanto-auto-deployer`), without having to restart the _whole_ container-management service. The implemented filewatcher (the `--daemon` flag) allows you to quickly create/edit  (or even `touch` them) container manifests on the device that would be on-the-fly deployed after saving. This allows for rapid testing when creating new container manifests.

## Kanto Container Management init-dir

This feature of Kanto Container Managament by the Kanto Teams is currently under development and hence unstable. That is why it is not used as of the test-0.0.6 release of Leda Distro and 0.1.0-M1 release of meta-leda.