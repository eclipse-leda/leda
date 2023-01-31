---
title: "Partition Layout"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

The bootable Leda Quickstart images are disk image with multiple partitions:

- Two bootloader partitions, to enable A/B update process
- A separate partition to hold bootloader status information
- An optional rescue partition with basic operating system and tooling
- Two rootfs partitions with a full installation of the operating system, to enable A/B update process
- A data partition for storing container runtime data

## Partition Layout for QEMU x86-64

The x86_64 image uses GRUB as a bootloader and the partition layout is as follows:

![Leda Disk Layout for QEMU x86-64](leda-disk-layout-qemux86-64.png)

## Partition Layout for QEMU ARM-64

The partition layout for QEMU ARM-based images are comparable, except:

- Bootloader is replaced with U-Boot

## Partition Layout for Raspberry Pi

The partition layout for Raspberry Pi images are comparable, except:

- Bootloader is replaced with U-Boot
- The last partition (the data partition) is marked as growable, to allow the use of the larger SD-Card capacities for container runtime data