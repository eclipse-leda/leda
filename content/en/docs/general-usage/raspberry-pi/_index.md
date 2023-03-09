---
title: "Running on Raspberry Pi"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

What you need:

- A Raspberry Pi 4B (64 Bit) with 2 GiB of RAM or more, recommended is 8 GiB
- Network connection (Ethernet or Wifi) with transparent internet access
- Optional keyboard and display (makes it easier to troubleshoot)

Steps:

- Download the [latest released SD-Card Image](/leda/docs/general-usage/download-releases/): `eclipse-leda-raspberrypi.tar.xz`
- Uncompress the SD Card image:

      apt-get install -y xz-utils
      tar xf eclipse-leda-raspberrypi.tar.xz
      bzip2 -d -f sdv-image-all-raspberrypi4-64.wic.bz2

- Flash the `sdv-image-all-raspberrypi4.wic` file to an SD-Card
  - On Linux:
    - Install bmap tools: `sudo apt-get install -y bmap-tools`
    - Insert SD Card and check which device is mounted: `sudo fdisk -l`
    - Unmount the device: `sudo umount /dev/mmcblk[X]`
    - `sudo bmaptool copy --bmap sdv-image-all-raspberrypi4-64.wic.bmap sdv-image-all-raspberrypi4-64.wic /dev/mmcblk[X]`
    - *Note:  Using `bmap` is **much** faster but works the same as with plain `dd if=<wic-file> of=dev/mmcblk[x]`.*
  - On Windows:
    - [Raspberry Pi Imager](https://www.raspberrypi.org/documentation/installation/installing-images/)
    - [Balena Etcher](https://www.balena.io/etcher/)
- *Optional: If you need to adapt the network configuration eg Wifi credentials, edit the configuration files on the `boot` partition.*
- Shutdown the Raspberry and insert the SD-Card into the Raspberry Pi SD-Card slot at the bottom
- Power on your Raspberry to boot the image
- Login with `root`
- Check disk space:
  - The `raspberry-growdisk` system service will do this automatically on first boot.
  - To manually enlarge the available disk space on the SD-Card, resize the disk partition: `parted /dev/mmcblk0 resizepart 6 100% && resize2fs /dev/mmcblk0p6`.

    *Note: Due to changes in the disk partition, the partition number (`6` in the example) may have changed.*
  - Verify with `df -h`.
  
- Verify and wait until container runtime is started: `systemctl status container-management`
- *Optional:* Check the system health: `sdv-health`
- Continue with [Device Provisioning](/leda/docs/device-provisioning/)
