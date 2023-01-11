---
title: "Run the build"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

## Run the full build

To setup the environment and build the Leda image, please refer to: [Setup development environment](/leda/docs/build/devenv/).

## Running QEMU from existing build

- Use `kas shell -c "runqemu qemux86-64 ovmf kvm nographic" <kas-configs>` to execute the image.
- Replace `qemux86-64` with one of the other qemu machines, such as `qemuarm64`
- Use the keyword `slirp` to enable user-networking which does not require root privileges on the host. `tun` is default but requires setup on the host.
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

The image is then reachable via `ssh root@192.168.7.2`
This will write a file qemu.pid in the current directory including the process ID of QEMU. Once done, ``kill -9 <qemu.pid>`` kills the process.

## Running with kas-shell

If you've chosen to build the Leda image with kas, you can use the kas-shell to run QEMU, with kas setting up the environment for you. To do that change to the main working directory and run:

```bash
kas shell -c 'runqemu slirp nographic ovmf sdv-image-full'
```

## DHCP Configuration

As the Leda Quickstart image will try to retrieve its IP address via DHCP broadcast request, it is good to run a DHCP daemon on the host, listening on the respective TAP network interface of QEMU. This will then simulate a LAN with DHCP server and let's us control which IP address gets assigned to multiple QEMU instances.

The [run-dhcp.sh](https://github.com/eclipse-leda/leda-distro/blob/main/scripts/run-dhcp.sh) utility will run an ISC-DHCP server on the host. The default configuration has a couple of MAC addresses preconfigured.
