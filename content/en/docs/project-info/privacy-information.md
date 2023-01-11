---
title: "Privacy Information"
date: 2022-05-09T14:24:56+05:30
weight: 9
---

Your privacy is important to us. The following Information is to provide you with all information relevant to data protection in order to be able to use the software, in a data protection compliant manner. It is provided as an information source for your solution-specific data protection and data privacy topics. This is not intended to provide and should not be relied on for legal advice.

### Your Role

First things first: when you choose and use our software, you are most likely acting in the role of data controller, if personal related data is being processed. Therefore, you must ensure that the processing of personal data complies with the respective local legal requirements, e.g. when processing data within the scope of General Data Protection Regulation (GDPR) the legal requirements for a controller from the GDPR.

### Where may the processing of personal related data be relevant?

When using our software in combination with other software components, personal data or data categories may be collected for the purpose of developing, testing and running in-vehicle applications (Vehicle Apps). Possible examples are the vehicle identification number (VIN), the number plate, GPS data, video data, audio data, or other measurement data. You can determine which data or data categories are collected when configuring the software. These data are stored in volatile memory and are deleted by shutting down the system. You are responsible for the compliant handling of the data in accordance with the applicable local law.

### What have we done to make the software data protection friendly?

This section describes the measures taken to integrate the requirements of the data protection directly into the software development. The technical measures described below follow a "privacy by design" approach.

- **Local data:** The software may save data permanently in local virtual storage (eg when run in QEMU Emulator) or on local physical storage (SD-Card on Raspberry PI). All collected or processed data can be deleted by either deleting the virtual storage file (*.qcow2), or by erasing the SD-Card.

- **Cloud storage:** The software may send data to cloud endpoints controlled by you or your organization. Examples include connectivity data, device identification, device health, device telemetry, application metrics and application logs. Collection and processing of example data on the device is enabled by default. Sending of device data to cloud endpoints must be explicitly enabled by performing the device provisioning process. The actual cloud endpoints are determined and configured during the device provisioning process. All collected or processed data can be deleted on the cloud side in the respective cloud endpoints.

- **Vulnerabilities:** The release process for this software is set up to always update to the newest package updates. The project will continously release new versions of the software. To protect personal data, it is advisable to always use the latest version of the software.

- **Important:** When you use the Eclipse Leda quickstart images for non-volatile setups, it is essential to reconfigure the system and harden it, this includes but is not limited to the following configuration items:

  * Disable system user (root) password and login
  * Disable SSH login with password
  * Adding a new Linux user with restricted permissions
  * Adding SSH key based authentication
  * Container Resources and Configurations: Secrets, such as Device Identity Certificates for Cloud Connection and Access credentials for private Container Registries
