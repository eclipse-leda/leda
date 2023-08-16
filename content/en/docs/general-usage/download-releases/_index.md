---
title: "Download latest release"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

- [Milestone 0.1.0-M1](/leda/docs/about/releases/0.1.0/leda-0.1.0-m1/)

## Latest Release Artifacts

**Note: There are no official releases yet.
The artifacts available on the Release page are for testing the build and release workflows.
They should be considered as unstable nightly builds from the main branch.
Releases marked `-M1`, `-M2`, `-RC1` etc. are preparations for official releases according to the Eclipse Release process.**

Go to the [Eclipse Leda Releases](https://github.com/eclipse-leda/leda-distro/releases) page and download the release archive for the respective machine.
The release archives container the disk image and the respective Linux kernel:

| Machine | Filename | Description |
| ------- | -------- | ----------- |
| QEMU x86_64 | eclipse-leda-qemu-x86_64.tar.xz | For running QEMU x86 64-Bit |
| QEMU ARM 64 | eclipse-leda-qemu-arm64.tar.xz | For running QEMU ARM 64-Bit |
| Raspberry Pi 4 | eclipse-leda-raspberrypi.tar.xz | For running on Raspberry Pi 4 (SD-Card Image) |

## Using GitHub CLI tool

To download all files of the latest release using the GitHub CLI:

- Install [GitHub CLI](https://github.com/cli/cli), e.g. for Ubuntu:

  ```shell
  curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
  sudo apt update
  sudo apt install gh
  ```

- Authenticate to GitHub:

  ```shell
  gh auth login
  ```
- Download Leda latest release:

  On Linux:

  ```shell
  mkdir leda && cd leda

  gh release download \
    --pattern '*.zip' \
    --pattern 'eclipse-leda-*' \
    --repo eclipse-leda/leda-distro
  ```

  On Windows:

  ```shell
  gh release download --pattern "*.zip" --pattern "eclipse-leda-*" --repo eclipse-leda/leda-distro
  ```

- Continue with [Running Eclipse Leda on QEMU](/leda/docs/general-usage/running-qemu/) or [Running Eclipse Leda on Raspberry Pi 4](/leda/docs/general-usage/raspberry-pi/)
