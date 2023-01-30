---
title: "Creating custom meta-leda based SDV images"
date: 2023-01-03T17:24:56+05:30
weight: 10
---


The main objective of the Leda project is to provide a bitbake meta-layer that would allow anyone to build a custom image in the context of SDV. While the Leda quickstart image is great for experimentation
and as a developer "playground", it is in fact not-production ready (and neither it is meant to be). That is why the meta-leda focuses on providing reusable compontents for custom SDV images. 

This documentation section is aimed at anyone who wishes to build such a custom image.

## Kas and meta-layers

We recommend (and use for the quickstart image) the [kas tool](https://github.com/siemens/kas) developed by Siemens as way to help with reproducible builds. It is however, not required and you would still need to 
define your own distro meta-layer on top of meta-leda. The Leda quickstart image kas-files can be found here: [leda-distro/kas](https://github.com/eclipse-leda/leda-distro/tree/main/kas). Most of the distro-congfiguration can be found
in the `common-kirkstone.ymal` file.

Other than meta-leda you might need the following external meta-layers:

- [Poky](https://git.yoctoproject.org/git/poky) - The base poky distro
- [meta-openembedded](https://git.openembedded.org/meta-openembedded) - Busybox, systemd and other core packages
- [meta-rauc](https://github.com/rauc/meta-rauc) - RAUC integration
- [meta-kanto](https://github.com/eclipse-kanto/meta-kanto) - Kanto container management
- [meta-virtualization](https://git.yoctoproject.org/meta-virtualization) - Containerd

## General distro configuration

The place you should probably start at is with configuring your custom distribution. The BitBake mechanism for doing so can be found in the official BitBake documentation: [22 Creating Your Own Distribution](https://docs.yoctoproject.org/dev/dev-manual/custom-distribution.html#creating-your-own-distribution).

As a working example you can use the Leda-distro config file: [meta-leda/meta-leda-distro/conf/distro/leda.conf](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-distro/conf/distro/leda.conf). We will now go through some of the require (include) lines in the *leda.conf*:

```bash
require conf/distro/include/buildinfo.inc # -> Defines entries for /etc/build
require conf/distro/include/leda-distro-features.inc # -> Defines the quickstart image features. Use as a guide for your own distro.
require conf/distro/include/leda-package-blacklist.inc # -> Defines blacklisted packages (e.g. alsa)

include conf/machine/${MACHINE}-extra.conf # -> Defines ${MACHINE}-specific configuration files fstab, wks, etc. Would be elaborated on further down.
```

```bash
QB_KERNEL_CMDLINE_APPEND = "net.ifnames=0 panic=5 ip=dhcp ip=192.168.7.2::192.168.7.1:255.255.255.0::eth0:off rootwait" # -> QEMU-specific kernel command line with which all images/partitions are booted
```

### Machine-specific configs

The "extra" machine specific-cofigs the meta-leda-bsp layer provides can be found here: [meta-leda-bsp/conf/machine](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/conf/machine). These files here provide examples on how to configure machine specific options such as the Linux Kernel image type, bootloader configuration, etc. E.g. if you need a working example how to setup U-Boot for your machine, you might reference `common-qemu-arm.inc` since the Leda quickstart QEMUARM (64bit and 32bit) images use U-Boot as a bootloader.


## Partitioning your storage

The Leda quickstart image uses RAUC as a way to do A/B partition type updates. We also use add a third "rescue" partition and a persistent "data" partition. Generally the Leda quickstart image partitions its storage as so:

```text
 ----------------------------------------------------------------------------------
|            |             |             |             |             |             |
|            |             |             |             |             |             |
|    VFAT    |    NO-FS    |    EXT4     |    EXT4     |    EXT4     |    EXT4     |
|   (BOOT)   |  (GRUVENV)  |   (RESCUE)  |   (SDV_A)   |   (SDV_B)   |   (DATA)    |
|            |             |             |             |             |             |
|            |             |             |             |             |             |
 ----------------------------------------------------------------------------------
````

Where the partitions **SDV_A** and **SDV_B** are managed/updated by RAUC. They are read-only (**SDV_A** has the *sdv-image-full* image installed, **SDV_B** - *sdv-image-minimal* and **RESCUE** contains *sdv-image-rescue*). All container/user data is in the last **DATA** partition (grows dynamically to fill-out the storage). The boot partition contains the uboot/grub bootloaders and their environment.

This partition scheme is has to be seen, as of course, a suggestion (you are free to use any RAUC-compatible one) but is important for understanding the later sections in this page.

## WIC/WKS

More details on OpenEmbedded Kickstart files can be found in the official documention for Yocto: [OpenEmbedded Kickstart (.wks) Reference](https://docs.yoctoproject.org/ref-manual/kickstart.html). In short, **.wks**-files provide a reproducible way to partition your storage.

*IMPORTANT: the path to your **.wks**-file should be provided via the **WKS_FILES=** BitBake variable. For example, in the quickstart image for QEMUARM64 this variable is set in `qemuarm64-extra.conf`.*

Again, example **.wks/.wks.in** files are provided in [meta-leda/meta-leda-distro/wic](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-distro/wic). We will now take a look at the qemuarm64 .wks-file:


```text
bootloader --ptable gpt

part --source bootimg-partition --ondisk vda --fstype=vfat --label BOOT --active --align 4096 --size 100 --use-uuid
# Second Bootloader Partition (empty, for future updates)
part --fixed-size 10M --ondisk vda --align 4096 --no-table
# Empty partition (on x86, this is grubenv - we store RAUC Status here as well)
part --fixed-size 10M --ondisk vda --align 4096
part --source rootfs --rootfs-dir=sdv-image-rescue --ondisk vda --fstype=ext4 --label rescue --align 1024
part --source rootfs --rootfs-dir=sdv-image-full --ondisk vda --fstype=ext4 --label root_a --align 4096
part --source rootfs --rootfs-dir=sdv-image-minimal  --ondisk vda --fstype=ext4 --label root_b --align 4096
part --fixed-size 2048M --source rootfs --rootfs-dir=sdv-image-data --ondisk vda --fstype=ext4 --label data --align 4096
```

As you can see it directly implements the partition scheme described above. The partition table is defined with the `bootloader --ptable gpt` line and every line after that corresponds to a partition from the diagaram above.
Please note, that the order in which the `part` lines in the **wks**-file appear would be the order of the partitions.

Here it is important to note that for the the VFAT boot partition the label should be uppercase and you should add the `--use-uuid` option. Otherwise it might not be mounted properly in the final Linux distro.

## FSTAB

**.wks**-files partition your storage, but do nothing about actually mounting said partitions in the Linux userspace. This is the job of the FSTAB file. More information about writing an fstab file can be found in the [Linux fstab manpage](https://man7.org/linux/man-pages/man5/fstab.5.html).

FSTAB files are installed through the OE-core recipe `based-files_<version>.bb`. To install a custom FSTAB in your image create a `recipes-core/base-files` directory in your meta-layer and create a `base-file_%.bbappend` inside.
Use this *.bbappend* to add the directory containing your custom FSTAB to the `FILESEXTRAPATHS` list for the recipe. 

An example can be found in `meta-leda/meta-leda-distro/recipes-core/base-files/` where you would find the needed `.bbappend` file and the `meta-leda/meta-leda-distro/recipes-core/base-files/base-files/<machine>` directory containing the actual FSTAB files.

Let's investigate the Leda qemuarm64 FSTAB as an example:


```text
# Eclipse Leda - fstab for qemuarm64 RAUC redundant boot setup

/dev/root            /                    auto       defaults,noatime              1  1
proc                 /proc                proc       defaults              0  0
devpts               /dev/pts             devpts     mode=0620,ptmxmode=0666,gid=5      0  0
tmpfs                /run                 tmpfs      mode=0755,nodev,nosuid,strictatime 0  0
tmpfs                /var/volatile        tmpfs      defaults              0  0

# Add mount for boot, grubenv and data partition
LABEL=BOOT           /boot                vfat       defaults,nofail,noatime  0  0
LABEL=grubenv        /grubenv             auto       defaults,nofail,noatime  0  0
LABEL=data           /data                auto       defaults,nofail,noatime  0  2
```

Here only the BOOT, grubenv and data partitions are mounted by label.

The root partition depends on the image (sdv-image-full/minimal/rescue) that has been currently booted. Here /dev/root is a "special variable" that is set from the `root=` option in the kernel command line. This is important to be able
to boot from the different partitions via a custom bootloader script (and as a consequence these partitions to be managed by RAUC).