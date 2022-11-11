---
title: "Building with kas/manually"
date: 2022-05-09T14:24:56+05:30
weight: 3
---


After setting up your [VSCode DevContainer](/leda/docs/build/devenv/vscode-devcontainer/) or [GitHub Codespace](/leda/docs/build/devenv/github-codespaces/) you can proceed with the actual build process. Here you have two choices - either using the kas-build system or setting up the build manually.

## Building with kas

This is the easiest way to build leda semi-automatically
- `cd /workspaces/meta-leda-fork/`
- Open the VSCode terminal and run `kas build`
-   __Note: you can alter the build options by modifying the .config.yaml file in the trunk of the repository__

## Building manually

You can also build Leda manually if more customization of the build process is required.
- `export LEDA_WORKDIR=/workspaces/meta-leda-fork/`
- `cd ${LEDA_WORKDIR}`
- Clone the Poky repository with the required release, e.g. `kirkstone` and pull updates if necessary:

   ```bash
   git clone git://git.yoctoproject.org/poky
   cd poky
   git checkout -t origin/kirkstone -b kirkstone
   git config pull.rebase false
   git pull
   ```

- Prepare the build environment: 
      
   ```bash
   source oe-init-build-env
   ```

- Dry-run a build of the Linux Kernel recipe using BitBake:

   ```bash
   bitbake --dry-run linux-yocto
   ```

- Checkout the meta-layer dependencies for Leda:
   ```bash
   cd $LEDA_WORKDIR
   git clone -b kirkstone https://github.com/rauc/meta-rauc.git meta-rauc
   git clone -b kirkstone https://github.com/rauc/meta-rauc-community.git meta-rauc-community
   git clone -b kirkstone https://git.yoctoproject.org/meta-virtualization meta-virtualization
   git clone -b kirkstone https://git.openembedded.org/meta-openembedded meta-openembedded
   ```

- Change to the `poky/build` directory (generated from the `oe-init-build-env` script automatically)
- Add all the necessary meta-layers:
   ```bash
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-rauc
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-rauc-community/meta-rauc-qemux86
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-openembedded/meta-oe
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-openembedded/meta-filesystems
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-openembedded/meta-python
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-openembedded/meta-networking
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-virtualization
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-leda-components
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-leda-bsp
   bitbake-layers add-layer ${LEDA_WORKDIR}/meta-leda-distro
   ```

- Dry run:
   ```bash
   DISTRO=leda bitbake --dry-run sdv-image-all
   ```

- Real build:
   ```bash
   DISTRO=leda bitbake sdv-image-all
   ```
- You can also build one of the target recipies this way:
   ```bash
   DISTRO=leda bitbake kanto-container-management
   ```
-   __Note: in this case you can set the target architecture and other build options in the build/local.conf file__

