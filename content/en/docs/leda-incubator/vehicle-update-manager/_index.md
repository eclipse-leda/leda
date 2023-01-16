---
title: "Vehicle Update Manager"
date: 2022-05-09T14:24:56+05:30
weight: 15
---

The vehicle update manager is used in the context of [OTA Software Updates](/leda/docs/device-provisioning/vehicle-update-manager).

## Overview

Vehicle Update Manager (VUM) is an extended version of the [Eclipse Kanto Container Manager](https://github.com/eclipse-kanto/container-management) that is being able to **handle new desired state for the software on the whole vehicle device**.

![Vehicle Update Manager Scope](./vehicle-update-manager-arch.png)

## Implementation

The desired state comes as a multi document YAML content and it includes a list of container resources:

- Container
- Configuration

VUM detects the system-level update custom resource and passes it for further processing to the [Self Update Agent](/leda/docs/leda-incubator/self-update-agent/).

VUM also monitors the self-update agent and the control plane, and compiles and report the current state of the device.

## Source Repository

Source Repository: <https://github.com/eclipse-leda/leda-contrib-vehicle-update-manager>
