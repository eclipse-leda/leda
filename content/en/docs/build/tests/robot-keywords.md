---
title: "Robot Keywords"
date: 2022-05-09T14:24:56+05:30
weight: 4
---

In the Leda Robot Tests, keywords are used for reusable functionality. Common keywords are defined in `resources/docker-snapshot/dockerfiles/leda-tests/leda_keywords.resource`

The goal is to treat the Leda Quickstart image as a black box, utilizing as much as possible with public APIs.

## Interaction with Self Update Agent

- `Trigger to start update`: Send a "Desired State Request" to the target, to install a RAUC Update Bundle
- `Connect and Subscribe to Listen`: Wait for the asynchronous messages which indicate a successful installation of an update

## Arbitrary Commands

Nevertheless, during implementation of test cases, it may be necessary to execute lower level processes for system level tests. For that, a fallback is possible to execute arbitrary test commands via remote SSH connection. These commands are executed through another docker container running in the same Docker network (`leda-network`) and allow access to the target QEMU instances:

- `Leda Execute`: Execute an arbitrary shell command via SSH on the test target
