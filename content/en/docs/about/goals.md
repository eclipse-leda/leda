---
title: "Goals"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

The project aims to provide **an integration point for Open Source components for the Software Defined Vehicle**. For vehicle software systems, there are a lot of requirements to consider. Some of these requirements are taken into account for Leda's quickstart setups, thereas some other requirements can only be met once in a production environment and by customizing the target device image.

The following document will list some of these requirements and give an explanation on why they are met in the Leda quickstart distribution.

# Overview

- Provide an example operating system and configuration for constrained in-vehicle devices
- Integrate software-defined-vehicle Open Source components to showcase the available features and their state of maturity
- Demonstrate the use and interaction of open protocols and specifications, such as
  - the Kubernetes specifications
  - OpenTelemetry specs and components
  - Eclipse IoT related specifications for software rollouts and digital twin representations
  - open specifications from the [The Connected Vehicle Systems Alliance (COVESA)](https://www.covesa.global/)

## Background Information

| Requirement | Met | Context information |
| ---- | ---- | ---- |
| Footprint Constraints | Yes | Embedded in-vehicle devices have constrained resources such as CPU power, disk space, memory etc. Desktop operating systems use as much space as possible, thereas in-vehicle operating systems are as small as possible, omitting a lot of unnecessary tooling such as package managers or convenience tools for administrators, documenation (man pages) etc. Leda provides two different types of operating system images: one for quickstart and demo cases with some tooling, and a another minimal image which only contains the necessary software components for remote usage. <p></p>SDV Rescue Image is about 130MB<br>SDV Minimal Image is about 300MB <br>SDV Full Image (with convenience tools and pre-cached containers) is about 900MB<p></p>*Note: Future roadmap includes more footprint optimizations*|
| Hardened system | Partly | A vehicle device and its operating system are vulnerable targets in the same way as any other computer, especially once they are connected to the internet. Classically, such in-vehicle devices were hardened down once with additional audit logging for any kind of network traffic. In a connected world, these devices now become mostly always-on devices and behave like any other Internet of Things devices. Special care is to be taken to guard them against vulnerabilities by keeping these devices up-to-date, establish continuous automated monitoring and other methodologies known from DevSecOps.<p></p>As Leda is supposed to be used for quickly starting and evaluating SDV software, we balance these type of requirements. For example, installing system updates in Leda is only possible with signed update bundles, but the demo uses a self-signed certificate. For production use, these self-signed certificates would of course be replaced by the manufacturer's real certificates. |
| 
