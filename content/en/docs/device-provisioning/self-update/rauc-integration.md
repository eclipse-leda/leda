---
title: "RAUC Integration"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

Leda integrates [RAUC](https://rauc.io/) as a reference implementation and example configuration. It allows the evaluation of the concepts, mechanisms and involved software components in an emulated, virtual environment or on physical devices.

## Checking the RAUC Status

Get the current RAUC boot status:

    rauc status


Example output:
```
root@qemux86-64:~# rauc status
=== System Info ===
Compatible:  Eclipse Leda qemu86-64
Variant:     
Booted from: rootfs.1 (SDV_B)

=== Bootloader ===
Activated: rootfs.1 (SDV_B)

=== Slot States ===

o [rootfs.1] (/dev/sda5, ext4, inactive)
        bootname: SDV_B
        mounted: /
        boot status: good

x [rootfs.0] (/dev/sda4, ext4, booted)
        bootname: SDV_A
        boot status: good
```

## Forcing to boot the other slot

To manually force the device to boot into another slot, mark the current booted slot as *bad*, mark the other partitions as *active* and perform a reboot:

```
rauc status mark-bad booted
rauc status mark-active other
reboot now
```

## Testing the rescue system

By marking both root slots as bad, the bootloader is supposed to boot the rescue system:

```
rauc status mark-bad rootfs.0
rauc status mark-bad rootfs.1
reboot now
```

Example output of rauc:
```
o [rootfs.1] (/dev/sda5, ext4, inactive)
        bootname: B
        boot status: bad

o [rootfs.0] (/dev/sda4, ext4, booted)
        bootname: A
        mounted: /
        boot status: bad
```

## Customizations

The configurations can be customized by applying or patching the following files:

- RAUC Configuration file: `meta-leda/recipes-bsp/rauc/files/qemux86-64/system.conf`
- Bootloader Configuration file: `meta-leda/recipes-bsp/grub/files/grub.cfg`
- The physical disk partition configuration: `meta-leda/recipes-sdv/wic/qemux86-grub-efi.wks`

## RAUC System Configuration

The [RAUC System Configuration ](https://rauc.readthedocs.io/en/latest/integration.html#rauc-system-configuration) is the central configuration of the RAUC Update system.

Example:
```
[system]
compatible=Eclipse Leda qemu86-64
bootloader=grub
grubenv=/grubenv/grubenv
statusfile=/data/rauc.status

[keyring]
path=ca.cert.pem

[slot.efi.0]
device=/dev/sda
type=boot-gpt-switch
region-start=4M
region-size=100M

[slot.rescue.0]
device=/dev/sda3
type=ext4
readonly=true

[slot.rootfs.0]
device=/dev/sda4
type=ext4
bootname=SDV_A

[slot.rootfs.1]
device=/dev/sda5
type=ext4
bootname=SDV_B
```

## GRUB Bootloader Configuration

The GRUB bootloader has a configuration file which describes which partitions are bootable, which partition they are located at and a reference to RAUC's slot name.

The configuration also contains **RAUC specific logic and variables required for a proper integration**. Please see the full `grub.cfg` in the source repository and [RAUC Documentation - Integration - GRUB](https://rauc.readthedocs.io/en/latest/integration.html#grub) for details.

Excerpt:
```
...

menuentry "SDV Slot A (OK=$SDV_A_OK TRY=$SDV_A_TRY)" {
    linux (hd0,4)/boot/bzImage root=/dev/vda4 $CMDLINE rauc.slot=SDV_A
}

menuentry "SDV Slot B (OK=$SDV_B_OK TRY=$SDV_B_TRY)" {
    linux (hd0,5)/boot/bzImage root=/dev/vda5 $CMDLINE rauc.slot=SDV_B
}
```

## U-Boot Bootloader Configuration

Similarly to GRUB, integration of RAUC with U-Boot requires custom boot scripting. A highly detailed explaination can, again, be found in the official [RAUC Documentation - Integration - U-Boot](https://rauc.readthedocs.io/en/latest/integration.html#id5).

Meta-Leda provides such integration recipes and scripts for all U-boot based targets, for which a Leda Quickstart image is available (qemuarm64, qemuarm and rpi4-64). For example:

- [Main uboot_%.bbappend](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/u-boot_%25.bbappend)
- [Qemuarm custom script integration recipe](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/uboot-targets/qemuarm.inc)
- [Qemuarm custom boot.scr](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/files/qemuarm/boot.cmd.in)

*Note: A custom U-Boot device defconfig might be required for some devices to be integrated with RAUC. Leda Quickstart images patch the default defconfigs for qemuarm64 and qemuarm to save the U-Boot environment in a VFAT BOOT partition.*

## Disk Partitioning with OpenEmbedded Image Creator (WIC)

The [OpenEmbedded Image Creator](https://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#creating-partitioned-images-using-wic) is used in BitBake to actually create full disk images with multiple partitions.

These disk images are machine specific and the structure of the partitions are configured in [OpenEmbedded Kickstart](https://www.yoctoproject.org/docs/current/ref-manual/ref-manual.html#ref-kickstart) files (`*.wks`).

### Excerpt `qemux86-grub-efi.wks`

*Note: The excerpt is exemplary, please see the sources for a full representation and documentation.* 
```
bootloader --ptable gpt

part --fixed-size 50M --source rawcopy --sourceparams="file=efi-boot.vfat" --fstype=vfat --label boot --active

part --fixed-size 10M --source rawcopy --sourceparams="file=grubenv.vfat" --fstype=vfat --label grubenv

part /rescue --source rootfs --fstype=ext4 --label rescue

part / --source rootfs --fstype=ext4 --label root_a

part / --source rootfs --fstype=ext4 --label root_b

part /data --fixed-size 4G --fstype=ext4 --label data
```
