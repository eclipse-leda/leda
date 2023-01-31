---
title: "Deploying Containers"
date: 2023-01-03T17:24:56+05:30
weight: 1
---

## Kanto Container Management (kanto-cm) init-dir

Kanto-cm provides a mechanism to automatically deploy containers based on json-manifests stored in a so-called `init_dir` on boot. The template can be found in the kanto-cm documentation: [Template](https://websites.eclipseprojects.io/kanto/docs/references/containers/container-manager-config/#template).

A "filled in" template can be found in meta-leda (e.g. meta [meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/core/databroker.json](https://github.com/eclipse-leda/meta-leda/blob/2cb683a9606c01a73fc4f4d01df92a23a2cd2b9c/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/core/databroker.json)).

The directory for these manifests is set during image build time through the BitBake variable `KANTO_MANIFESTS_DIR`. By default, the Leda Quickstart image sets this directory to `/data/var/containers/manifests`. Since this is a directory mounted on the persistent **data**-partition you can add custom manifests/customize the default ones after an image has been built. These changes **will not be affected** by a RAUC update.

A standard set of containers is deployed with meta-leda, the manifests for which can be found in `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/core` and `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example/`.

**Important: The manifests in the kanto-cm init-dir are checked only _ONCE_  - on service start-up. If you add/change a manifest you would need to restart the whole "container-management" service for your changes to take effect.**

## Kanto-auto-deployer

This service has been implemented as a stopgap solution by the Leda team before the kanto-cm init-dir mechanism was implemented by the Kanto team. In-depth documentation on its operation and development can be found in the [Kanto Auto deployer](../../build/dev-and-maintenance/rust/kanto-auto-deployer). This runs as a one-shot service on boot and checks the directory defined in the BitBake variable `KANTO_MANIFESTS_DEV_DIR` in the distro config recipes. By default, the Leda quickstart images use `KANTO_MANIFESTS_DEV_DIR=/data/var/containers/manifests_dev"`. So, these manifest are again stored in the persistent **data**-partition and can be modified after the image has been deployed.

**Important: the [manifest template](../../build/dev-and-maintenance/rust/kanto-auto-deployer#manifest-structure) used for this service is similar to the one for the kanto-cm native mechanism, but is, in fact, different. Kanto-auto-deployer uses the kanto-cm internal state representation.**

A standard set of _dev_-containers is deployed with meta-leda, the manifests for which can be found in `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/core_dev` and `meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example_dev/`.

The advantage of this service is that it can be restarted very quickly (`systemctl restart kanto-auto-deployer`), without having to restart the _whole_ container-management service. This allows for rapid testing when deploying a new container. Due to the similarity of both manifests, the kanto-auto-deployer-style manifest can later be easily migrated to the kanto ini-dir style-one.
