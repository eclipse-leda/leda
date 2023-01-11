---
title: "Security Policy"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

This project implements the Eclipse Foundation Security Policy

* [https://www.eclipse.org/security](https://www.eclipse.org/security)

## Reporting a Vulnerability

Please report vulnerabilities to the Eclipse Foundation Security Team at
security@eclipse.org

## Supported Yocto Versions

| Version                 | Supported          |
| ----------------------- | ------------------ |
| Yocto 4.x (Kirkstone)   | Yes                |
| Yocto 3.4 (Honister)    | EOL                |
| Yocto 3.3               | Untested           |
| Yocto < 3.3             | No                 |

**Important: When you use the quickstart images for non-volatile setups, it is essential to reconfigure the system and harden it.**

## Configuration Items

* Disable system user (root) password and login
* Disable SSH login with password
* Adding a new Linux user with restricted permissions
* Adding SSH key based authentication
* Container Secrets
  * Device identity certificates for cloud connection
  * Access credentials for private container registries

### Device Identity for Cloud Connector

| Method         | Implementation | Intended use                 |
| -------------- | -------------- | ---------------------------- |
| Pre-Shared Symmetric Key | Azure IoT Hub Connection String | Development |
| Certificates | X.509 Certificates | Production |
