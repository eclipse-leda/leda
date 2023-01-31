---
title: "Creating custom meta-leda based SDV images"
date: 2023-01-03T17:24:56+05:30
weight: 10
---



The Leda project aims to provide a BitBake meta-layer for building custom images within the SDV context. The Leda quickstart image serves as an experimentation and development platform but is not production-ready. The focus of the meta-leda meta-layer is to offer reusable components for custom SDV images.

This documentation section is aimed at anyone who wishes to build such a custom image.

## kas and meta-layers

We recommend (and use for the quickstart image) the [kas tool](https://github.com/siemens/kas) developed by Siemens as a way to help with reproducible builds. It is, however, not required and you would still need to
define your own distro meta-layer on top of meta-leda. The Leda quickstart image kas-files can be found here: [leda-distro/kas](https://github.com/eclipse-leda/leda-distro/tree/main/kas). Most of the distro-configuration can be found
in the `common-kirkstone.yaml` file.

Other than meta-leda you might need the following external meta-layers:

- [Poky](https://git.yoctoproject.org/git/poky) - The base poky distro
- [meta-openembedded](https://git.openembedded.org/meta-openembedded) - Busybox, systemd, and other core packages
- [meta-rauc](https://github.com/rauc/meta-rauc) - RAUC integration
- [meta-kanto](https://github.com/eclipse-kanto/meta-kanto) - Kanto container management
- [meta-virtualization](https://git.yoctoproject.org/meta-virtualization) - containerd

## General distro configuration

The place you should probably start is by configuring your custom distribution. The BitBake mechanism for doing so can be found in the official BitBake documentation: [22 Creating Your Own Distribution](https://docs.yoctoproject.org/dev/dev-manual/custom-distribution.html#creating-your-own-distribution).

As a working example, you can use the Leda-distro config file: [meta-leda/meta-leda-distro/conf/distro/leda.conf](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-distro/conf/distro/leda.conf). We will now go through some of the require (include) lines in the *leda.conf*:

```bash
require conf/distro/include/buildinfo.inc # -> Defines entries for /etc/build
require conf/distro/include/leda-distro-features.inc # -> Defines the quickstart image features. Use it as a guide for your distro.
require conf/distro/include/leda-package-blacklist.inc # -> Defines blacklisted packages (e.g. alsa)

include conf/machine/${MACHINE}-extra.conf # -> Defines ${MACHINE}-specific configuration files fstab, wks, etc. Would be elaborated on further down.
```

```bash
QB_KERNEL_CMDLINE_APPEND = "net.ifnames=0 panic=5 ip=dhcp ip=192.168.7.2::192.168.7.1:255.255.255.0::eth0:off rootwait" # -> QEMU-specific kernel command line with which all images/partitions are booted
```

### Machine-specific configs

The "extra" machine specific-configs the meta-leda-bsp layer provides can be found here: [meta-leda-bsp/conf/machine](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/conf/machine). These files here provide examples on how to configure machine specific options such as the Linux Kernel image type, bootloader configuration, etc. E.g. if you need a working example of how to setup U-Boot for your machine, you might reference `common-qemu-arm.inc` since the Leda quickstart QEMUARM (64bit and 32bit) images use U-Boot as a bootloader.

## Partitioning your storage

The Leda quickstart image uses RAUC as a way to do A/B partition type updates. We also use add a third "rescue" partition and a persistent "data" partition. Generally, the Leda quickstart image partitions its storage as so:

```text
 ----------------------------------------------------------------------------------
|            |             |             |             |             |             |
|            |             |             |             |             |             |
|    VFAT    |    NO-FS    |    EXT4     |    EXT4     |    EXT4     |    EXT4     |
|   (BOOT)   |  (GRUBENV)  |   (RESCUE)  |   (SDV_A)   |   (SDV_B)   |   (DATA)    |
|            |             |             |             |             |             |
|            |             |             |             |             |             |
 ----------------------------------------------------------------------------------
````

Where the partitions **SDV_A** and **SDV_B** are managed/updated by RAUC. They are read-only (**SDV_A** has the *sdv-image-full* image installed, **SDV_B** - *sdv-image-minimal* and **RESCUE** contains *sdv-image-rescue*). All container/user data is in the last **DATA** partition (grows dynamically to fill out the storage). The boot partition contains the U-Boot/Grub bootloaders and their environment.

This partition scheme has to be seen, as of course, a suggestion (you are free to use any RAUC-compatible one) but is important for understanding the later sections on this page.

## WIC/WKS

More details on OpenEmbedded Kickstart files can be found in the official documentation for Yocto: [OpenEmbedded Kickstart (.wks) Reference](https://docs.yoctoproject.org/ref-manual/kickstart.html). In short, **.wks**-files provide a reproducible way to partition your storage.

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

As you can see it directly implements the partition scheme described above. The partition table is defined with the `bootloader --ptable gpt` line and every line after that corresponds to a partition from the diagram above.
Please note, that the order in which the `part` lines in the **wks**-file appear would be the order of the partitions.

Here it is important to note that for the VFAT boot partition the label should be uppercase and you should add the `--use-uuid` option. Otherwise, it might not be mounted properly in the final Linux distro.

## FSTAB

**.wks**-files partition your storage, but do nothing about actually mounting said partitions in the Linux userspace. This is the job of the FSTAB file. More information about writing a fstab file can be found in the [Linux fstab manpage](https://man7.org/linux/man-pages/man5/fstab.5.html).

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

Here only the BOOT, grubenv, and data partitions are mounted by label.

The root partition depends on the image (sdv-image-full/minimal/rescue) that has been currently booted. Here /dev/root is a "special variable" that is set from the `root=` option in the kernel command line. This is important to be able
to boot from the different partitions via a custom bootloader script (and as a consequence these partitions are to be managed by RAUC).

## Integrating RAUC

Whether you are using GRUB or U-Boot integrating RAUC requires custom bootloader scripting. The official documentation for integrating RAUC can be found here: [6. Integration](https://rauc.readthedocs.io/en/latest/integration.html).

This documentation can, however, be quite complicated. Concise, self-contained examples for proper integration of the most popular targets can be found in the [meta-rauc-community](https://github.com/rauc/meta-rauc-community/tree/master/meta-rauc-qemux86) repository.

### The RAUC system config file

Irrespective of your bootloader, you need to provide a RAUC system.conf file describing the slots, the bootloader, certificates, etc. This is best explained via an example: [meta-leda/meta-leda-bsp/recipes-bsp/rauc/files/qemuarm64/system.conf](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/rauc/files/qemuarm64/system.conf)

### GRUB

The only Leda quickstart image that uses GRUB as a bootloader is for qemux86_64. It directly uses [meta-rauc-community/meta-rauc-qemux86/](https://github.com/rauc/meta-rauc-community/tree/master/meta-rauc-qemux86) meta-layer.

### U-Boot

The rpi4-64 target, similar to qemux86_64, directly uses [meta-rauc-community/meta-rauc-raspberrypi](https://github.com/rauc/meta-rauc-community/tree/master/meta-rauc-raspberrypi) which also has a great README, explaining the details of the integration. This meta-layer includes quite a lot of rpi4-64 specific recipes and depends on the fact that the meta-raspberrypi layer provides a recipe for custom boot scripts. Such a recipe, in general, for U-Boot-based targets is not available and has to be manually created. That is why, [meta-rauc-community/meta-rauc-sunxi](https://github.com/rauc/meta-rauc-community/tree/master/meta-rauc-sunxi) might provide a better example in a more general case.

The Leda quickstart images that use U-boot as a bootloader are based on the ideas in `meta-rauc-sunxi`. We will now go into more detail on how to integrate such a U-Boot target that requires a more "from-scratch" integration.

#### The U-Boot environment and "slot-counting"

RAUC "talks" to the bootloader and tracks how many times you have tried to boot a slot via the **bootloader** environment variables "BOOT_ORDER" and "BOOT_<SLOT_NAME>_LEFT". Thus, U-Boot should be able to save its environment in a file
(`uboot.env`) somewhere that can be read by RAUC from userspace (the booted Linux image). This can be the VFAT BOOT partition, a flash chip, EEPROM, etc. which can be mounted in userspace and read by RAUC.

Note that while most of the steps for each of these options are the same, they might need some specific configuration. For example, the build for the Leda Quickstart QEMUARM64 patches the U-Boot defconfig file to point U-Boot to save its environment in the VFAT BOOT partition [env_in_fat_qemuarm.patch](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/files/qemuarm64/env_in_fat_qemuarm.patch). You can instead directly provide a custom defconfig in your machine-specific config (ref: [qemuarm64-extra.conf](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/conf/machine/qemuarm64-extra.conf#L8)).

#### uboot_%.bbappend

After ensuring that the device containing the U-Boot environment is correctly mounted in userspace (e.g. the BOOT partition as /boot). Create a custom `uboot_%.bbappend` file and as an example, you can use [meta-leda/meta-leda-bsp/recipes-bsp/uboot/uboot-targets/qemuarm64.inc](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/uboot-targets/qemuarm64.inc). This .bbappend should, generally do two things:

- Take your custom `boot.cmd.in` script and compile it to a boot.scr  (or boot.scr.uimg) file with mkimage.

- Install the `fw_env.config` file in /etc/fw_env.config.

- Optional: Apply any patches, custom settings, etc.

*Note: if you are building for more than one U-Boot-based target extensive use of machine-specific overrides is recommended*

#### Custom boot.scr

If a custom boot.scr that was compiled with the *mkimage* tool is in the same partition as the U-Boot binary, U-Boot will run that on boot. This is the point of integration of RAUC and U-Boot. All concepts behind setting up such a script are explained in the [rauc documentation](https://github.com/rauc/rauc/blob/8216e0df6c716a87406df676295af94b77814e5e/docs/integration.rst#id27).

Generally, as a starting point, you can use one of the custom scripts in meta-rauc-community or those in meta-leda: [meta-leda/meta-leda-bsp/recipes-bsp/uboot/files/qemuarm64/boot.cmd.in](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-bsp/recipes-bsp/uboot/files/qemuarm64/boot.cmd.in).

**IMPORTANT: Be consistent with your slot names!**

As it can be seen in the examples, after the "slot retries counting" part of the script is done, the `root=` and `rauc.slot=` kernel command line arguments are set, the U-Boot environment is saved in the VFAT boot partition as uboot.env and the selected image is booted.

Then, from userspace RAUC reads the kernel command line (/proc/cmdline) and the uboot.env (through the fw_printenv/fw_setenv utilities) and decides (based on that) whether a slot is "Good" or "Bad".

#### fw_env.config

For RAUC to be able to read and modify the U-Boot environment from userspace, it needs the fw_printenv/fw_setenv utilities to be installed in the distro. This can be done by installing the packages: `"u-boot-fw-utils u-boot-env libubootenv"` through IMAGE_INSTALL or RDEPENDS in a recipe.

This, however, is not enough since these utilities, in turn, have to be configured to know where U-Boot stores its environment. This is done through the /etc/fw_env.config file. An example of such a file with all of its different variations can be seen here [fw_env.config](https://github.com/ARM-software/u-boot/blob/master/tools/env/fw_env.config).

The one for Leda quickstart contains a single line:

```
/boot/uboot.env 0x0000  0x4000
```

If you are unsure of the environment size and the device offset, check the defconfig file for your machine, where these two values should be specified as U-Boot compile-time configuration parameters.

#### Conclusion (U-Boot <-> RAUC integration checklist)

Given the following:

1. You have setup U-Boot to save its environment in a known place (device, partition, etc)

2. This device is mounted in userspace

3. You have provided a custom boot-script that does the RAUC slot-counting

4. You have installed fw_printenv/fw_setenv and properly setup the /etc/fw_env.config file

The RAUC mark-good-service should successfully go through and mark both RAUC slots as "GOOD".
