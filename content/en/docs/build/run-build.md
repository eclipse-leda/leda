---
title: "Run the build"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

## Run the full build

To setup the environment and build the Leda image, please refer to: [Setup development environment](/leda/docs/build/devenv/).


## Running QEMU from existing build

- Switch to the build directory: `cd poky && source oe-init-build-env ../build-sdv-xxx`
- Use `runqemu qemux86-64 nographic slirp qemuparams="-m 2048"` to execute the image. Replace `qemux86-64` with one of the machines listed above.
  - `slirp` enables user-networking which does not require root privileges on the host. `tun` is default but requires setup on the host.
  - `nographic` disables graphical user interface
  - `qemuparams` are additional command line parameters for qemu
  - `-m 2048` gives 2GB of memory to the qemu instance, required for k3s
- Using `tap` networking
  - Login as `root` without password on login prompt, or use `ssh root@192.168.7.2` to login remotely to qemu instance
- Using `slirp` networking
  - Login as `root` without password on login prompt, or use `ssh -p 2222 root@localhost` to login remotely to qemu instance
- Continue with [Device Provisioning](/leda/docs/device-provisioning/)

### Variations of runqemu command line

- Use `runqemu ovmf`
  - `ovmf` will enable the UEFI support for IA32 (x86) and X64 (x86-64) guests, for testing the dual-boot capabilities and SDV Self-Update mechanisms
- All other options are now part of the default Leda distribution configuration (see *leda-qemu-settings.inc*)
- Continue with [Device Provisioning](/leda/docs/device-provisioning/)

## Running QEMU in the background

To start QEMU in the background enter, use `nohup` and bring the process into the background.

```bash
nohup runqemu qemux86-64 nographic qemuparams="-m 2048 -pidfile qemu.pid" &
```

The image is then reachable via `ssh root@192.168.72`
This will write a file qemu.pid in the current directory including the process ID of QEMU. Once done, ``kill -9 <qemu.pid>`` kills the process.

## Running with kas-shell

If you've chosen to build the Leda image with kas, you can use the kas-shell to run QEMU, with kas setting up the environment for you. To do that change to the main working directory and run:

```bash
kas shell -c 'runqemu slirp nographic ovmf sdv-image-full'
```