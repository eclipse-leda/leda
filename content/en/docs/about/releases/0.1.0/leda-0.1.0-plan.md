---
title: "Release Plan 0.1.0"
date: 2023-04-12T14:24:56+05:30
weight: 100
---

The release plan is available at [https://projects.eclipse.org/projects/automotive.leda/releases/0.1.0](https://projects.eclipse.org/projects/automotive.leda/releases/0.1.0)

## Release Date

-Thursday, June 1, 2023- - We didn't meet the planned release date. Work is in progress on IT build infrastructure and OSS IP and license compliance.

New: Tuesday, August 1, 2023

## Deliverables

The team plans to deliver the following features:

- Leda Quickstart Images for Qemu (x86_64, arm64), Raspberry Pi and Docker
- Yocto / OpenEmbedded meta-layer for better reusability of the Eclipse SDV Vehicle.Edge stack in customized distributions for constrained devices
- User documentation (Reference, Example Use Cases)
- Automated system tests using Robot Framework
- IP scanning with Eclipse Oniro Compliance Toolchain
- Pre-Integrated Eclipse SDV Vehicle.Edge stack

The core SDV.EDGE stack in Leda would contain the following components for the first release (based upon availability):

- Eclipse Kuksa.VAL: Data Broker
- Eclipse Kanto: Container Management, Vehicle Update Manager
- Eclipse Leda Incubator: Cloud Connector (Azure), Self Update Agent, Utilities (e.g kantui)

The following components are not yet released in public or did not yet finished the project review, and may only be added to the release on shorter notice:

- (Eclipse Backend-Function-Bindings)
- (Eclipse SommR)
- (OTA Client)

## Compatibility

Compatibility to previous versions is not considered for this first release.

## Internationalization

No efforts towards i18n are done in this release.

## Target Environments

- Linux (virtual, qemu)
- Raspberry Pi 4 (consumer grade)