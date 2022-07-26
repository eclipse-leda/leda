---
title: "Releasing"
date: 2022-05-09T14:24:56+05:30
weight: 20
---

# Versioning and Codenames

- Distribution Versioning is following the `x.y.z` syntax for the distribution, e.g. `Leda 0.0.1`
- Build Versioning is following the git describe syntax: `v0.0.1-blank-168-g7e14c4c`
  - Latest tag name: `v0.0.1`
  - Branch name: `blank`
  - Number of commits behind: `168`
  - Short Commit ID: `g7e14c4c`
- Codenames are taken from [Wikipedia List of Motor Racing Tracks](https://en.wikipedia.org/wiki/List_of_motor_racing_tracks)
- Initial codename is `Hockenheim`
- Current distribution version can be taken from `/etc/issue`:
```
root@qemux86-64:~# cat /etc/issue
Eclipse Leda v0.0.8
```

# How to Release

A new release is triggered manually from its GitHub web page `Releases` section. By
clicking on the `Draft new release` button, the release process starts:
- Select a branch to use as code base for the release
- Create a tag using the standard pattern `vX.Y.Z`
- Write a title `Release X.Y.Z` and release notes
- Optionally select if this is a pre-release
- Publish the release
- [Validate the release](validation.md)

With `Publish the release` action the release workflow located in `.github/workflows/release.yml` will be triggered. This
will start building the distro image files for the supported platforms, running the test cases and generating reports as
junit xml and license scanning. If the image generation and the test runs are successful the artifacts: images, test
binaries and qa reports will be attached as assets to the release.

The build (`build.yml`) and release (`release.yml`) workflows share a common reusable workflow (`base.yml`). In this way the
release workflow repeats the build actions without duplicating the code.

# Detailed build information on device

## Eclipse Leda Version
```
root@qemux86-64:~# cat /etc/issue
Eclipse Leda v0.0.8
```

## Exact Build Timestamp
```
root@qemux86-64:~# cat /etc/version
20220408135014
root@qemux86-64:~# cat /etc/timestamp
20220408135230
```

## Details of Build Information
```
root@qemux86-64:~# cat /etc/build 
-----------------------
Build Configuration:  |
-----------------------
DISTRO = leda
DISTRO_VERSION = 2022
DATETIME = 20220408135014
DISTRO_NAME = Eclipse Leda
IMAGE_BASENAME = core-image-minimal
MACHINE = qemux86-64
TUNE_PKGARCH = core2-64
MACHINE_FEATURES = alsa bluetooth usbgadget screen vfat x86 pci rtc qemu-usermode
DISTRO_FEATURES = acl alsa argp  debuginfod  ipv4 ipv6 largefile pcmcia usbgadget usbhost wifi xattr  zeroconf pci    vfat seccomp largefile  ptest multiarch  vulkan virtualization k8s seccomp raucg
COMMON_FEATURES = 
IMAGE_FEATURES = debug-tweaks
TUNE_FEATURES = m64 core2
TARGET_FPU = 
APP_URI_PREFIX = 
APP_URI_BRANCH = 
-----------------------
Layer Revisions:      |
-----------------------
meta              = honister:ee68ae307fd951b9de6b31dc6713ea29186b7749 
meta-poky         = honister:ee68ae307fd951b9de6b31dc6713ea29186b7749 
meta-yocto-bsp    = honister:ee68ae307fd951b9de6b31dc6713ea29186b7749 
meta-leda          = main:30a5ff0a7e04dfa2c9b43175a49ac7a2ae0c64a9 -- modified
meta-rauc         = honister:3faf4cc4fcf558e99dad5aa8532fef2ecd566653 
meta-filesystems  = honister:061b7fc74f887454251307ef119b808a90654d3f 
meta-networking   = honister:061b7fc74f887454251307ef119b808a90654d3f 
meta-oe           = honister:061b7fc74f887454251307ef119b808a90654d3f 
meta-python       = honister:061b7fc74f887454251307ef119b808a90654d3f 
meta-perl         = honister:061b7fc74f887454251307ef119b808a90654d3f 
meta-virtualization = honister:bd7511c53b921c9ce4ba2fdb42778ca194ebc3e8 
meta-security     = honister:fb77606aef461910db4836bad94d75758cc2688c 
patch             = main:a041dad5be9444d55491b57cb6a669a44196566d -- modified
```
