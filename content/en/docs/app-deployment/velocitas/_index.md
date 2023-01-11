---
title: "Velocitas VApps"
date: 2022-05-09T14:24:56+05:30
---

For local deployment without a cloud backend, deployment specifications for [Eclipse Velocitas](https://projects.eclipse.org/projects/automotive.velocitas) Vehicle Apps may be put directly onto the device.

- Create a Kanto deployment specification for your vehicle app. You may copy one of the existing JSON files in `/data/containers/manifests` as a template
- Copy the specification file to the device, e.g. `scp -P 2222 myapp.json root@localhost:/data/containers/manifests/`
- Apply the specification: `systemctl restart kanto-auto-deployer`

## Example Deployment Specification
```json
...
```
