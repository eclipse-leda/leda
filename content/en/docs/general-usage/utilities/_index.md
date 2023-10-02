---
title: "Utilities"
date: 2022-05-09T14:24:56+05:30
weight: 15
---

The quickstart image contains the following utilities.
These utility scripts are meant to be convenience tools for users and developers.
They help to experiment with the container deployment, device provisioning or vehicle data access.

- **sdv-health:** Show SDV software components health status
- **kantui:** A text user interface for kanto-cm to manage containers (start, stop, logs, redeploy all)
- **sdv-device-info:** Show and update device information
- **sdv-provision:** Generate device certificates and configuration of cloud connection
- **sdv-motd:** Message-of-the-Day shown after login prompt
- **can-forward:** Forwarding a CAN-bus network interface into a containerized Vehicle Application
- **kanto-auto-deployer:** Automatically deploys containers on boot. Runs as a systemd service, and can also be invoked by a user directly.
- **sdv-ctr-exec:** Execute arbitrary commands in existing containers
- **sdv-kanto-ctl:** Manage the Kanto Container Management configuration via CLI
- **blueprint-selector:** Deploy and fetch new SDV blueprints easily with an interactive CLI

> Note:
  These scripts are not meant to be reused or called from production software.
  Their behaviour or command line syntax is not a stable API and should not be trusted for automation purposes.
  For details, please see [leda-utils](https://github.com/eclipse-leda/leda-utils/)
