---
title: "Runqemu"
date: 2022-05-09T14:24:56+05:30
weight: 5
---

QEMU's command line option can get quiet complex. Yocto is providing a convenient wrapper script called `runqemu`, which takes configurations into account which have been populated during the build process and also takes care of TAP networking setup and teardown. Unfortunately, it can only be used within an OpenEmbedded build environment.

Running without runqemu: when you need more control over qemu options

```bash
qemu-system-x86_64 -kernel .\bzImage-qemux86-64.bin -nographic -m 2G -append "console=ttyS0 root=/dev/vda1" -drive file=.../sdv-image-full-qemux86-64.ext4
```

Running with runqemu: simple and some convenient flags are supported

    runqemu ovmf sdv-image-full


Running with leda: no options, runs the default settings only

    leda

![](qemu-runner-script.png)

## Enabling KVM for better performance

The performance of qemux86_64 is much better when KVM can be used.
Try running with:

    runqemu ovmf kvm

*Note: You may need to set up KVM for your host machine first, please refer to [How to enable KVM for Poky qemu](https://wiki.yoctoproject.org/wiki/How_to_enable_KVM_for_Poky_qemu)*

```bash
/workspaces/leda-distro/build-sdv-x86_64 (imageformatcleanup ✗) $ ls -al /dev/kvm
crw-rw---- 1 root kvm 10, 232 May 16 06:46 /dev/kvm
```
