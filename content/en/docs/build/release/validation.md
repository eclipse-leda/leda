---
title: "Validating"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Validating the release

Steps to validate if a release is properly working:

1. Create a new pre-release from your branch
2. Download the release artifacts onto a clean system.

   Do not use your build environment, to minimize the impact of existing environment configuration from BitBake etc.
3. Run the `run-leda` scripts to execute Qemu

   *Note: You should test each of the release archives, for each target machine.*
4. Follow the [Device Provisioning](/leda/docs/device-provisioning/) guide
5. Perform some verification tests (see below)
6. Cleanup: Delete the pre-release and the git tag:

       git push --delete origin <tagname>

## Ideas for manual verification steps

*Note: These are just for manual testing, as we intend to extend the automated tests as much as possible.*

- Operating system level
  - Run `sdv-health` on the shell
  - Verify disk partitions and RAUC status, e.g. `rauc status`
  - Verify network interface and CAN-Bus with `ip addr`
- Container runtime
  - Check status of containers with `kantui`
