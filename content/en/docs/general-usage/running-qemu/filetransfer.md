---
title: "Transferring Files"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# Sharing a directory with the guest

When you want to copy files between the host and the guest, an easy way is to use an SFTP tunnel.
With `sshfs`, you can mount a local directory to a remote directory via SSH.

## Pre-Requisites

Installation of needed packages:

- Run `apt-get install sshfs` on your host
- Enable `CORE_IMAGE_EXTRA_INSTALL += " openssh-sftp-server"` in `local.conf` of your image
- Verify SFTP connection working with `sftp -P 2222 root@localhost`

## Transfering files from host to guest

When you want to copy files from the host to the guest, an easy way is to use an SFTP tunnel.
With `sshfs`, you can mount a local directory to a remote directory via SSH.

- Create a mount point on your host: `mkdir remote`
- Open the SSH Filesystem tunnel: `sshfs root@localhost:/ remote/ -p 2222`
- Check files: `ls -al remote/` - you should see the root filesystem of the device now
- You can now easily copy files: `cp foo.txt remote/home/root/`

## Transfering files from guest to host

_Note:_ The reverse direction, e.g. initiating an SSH tunnel from within the device to the host, is currently not supported by the installed software on the image.
