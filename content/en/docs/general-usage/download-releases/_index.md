---
title: "Download latest release"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

Go to the [Eclipse Leda Releases](https://github.com/eclipse-leda/leda-distro/releases) page and download the disk image for the respective machine and the respective Linux kernel:

# Latest Release Artifacts

**Note: There is no binary release yet. A first milestone binary release is planned for Q3/2022.**

| Machine | Filename | Description |
| ------- | -------- | ----------- |
| QEMU x86_64 | eclipse-leda-qemu-x86_64.tar.xz | For running QEMU x86 64-Bit |
| QEMU ARM 64 | eclipse-leda-qemu-arm64.tar.xz | For running QEMU ARM 64-Bit |
| Raspberry Pi 4 | eclipse-leda-raspberrypi.tar.xz | For running on Raspberry Pi 4 (SD-Card Image) |
| Misc | qa-reports.tar | Test and other QA reports |
| | sdv-os-test-x86_64 | Smoke Tests executable x86_64 |

# Using GitHub CLI tool

To download all files of the latest release using the GitHub CLI:
- Install [GitHub CLI](https://github.com/cli/cli), e.g. for Ubuntu:
```
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```
- Authenticate to GitHub:
```
gh auth login
```
- Download Leda latest release:

On Linux:
```
mkdir leda && cd leda

gh release download \
  --pattern '*.zip' \
  --pattern 'eclipse-leda-*' \
  --repo eclipse-leda/leda-distro
```

On Windows:
```
gh release download --pattern "*.zip" --pattern "eclipse-leda-*" --repo eclipse-leda/leda-distro
```

- Continue with [Running Eclipse Leda on QEMU](/leda/docs/general-usage/running-qemu/) or [Running Eclipse Leda on Raspberry Pi 4](/leda/docs/general-usage/raspberry-pi/)
