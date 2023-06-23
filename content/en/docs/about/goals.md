---
title: "Goals"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

The project aims to provide **an integration point for Open Source components for the Software Defined Vehicle ecosystem**.

In a complex architecture, there are many different ways of implementations and alternative solutions possible.

For embedded vehicle computer systems and their software stack, there are a lot of requirements to consider, depending on the actual use cases:

- Integration and High-Level Testing (System Integrators, Suppliers)
- Proof-of-Concept projects (Integrators, OEMs, ISVs)
- Experiments and Hackathons (Developers, Research)
- Development phase (Developers, OEMs)
- Open Source Collaboration (Developers, OEMs, ISVs, Open Source Organizations, Standardization Organizations)

Some of the requirements derived from the above are taken into account for Leda's quickstart setups.
Thereas some other requirements can only be met once the project is in a nearer production environment and by customizing the target device image.
The following document will list some of these requirements and give an explanation on why they are set as goals in the Leda quickstart distribution.

## Overview

- **Provide an example operating system build and configuration for constrained in-vehicle devices:**
  Suppliers and system integrators want a way to cusomize and optimize the base operating system as much as possible.
  This is to achieve a high efficiency, high level of reuse and cost benefits of the planned hardware.
  The build system for the operating system, and the selection of the underlying distribution is key to the convenience for new users,
  but also commercially a business decision with an impact on the future maintainability of the platform.
  The Yocto Project has been chosen as an established de-facto standard for customized Linux distributions for embedded systems.
  Leda provides an OpenEmbedded Meta-Layer, which can be used with many existing SDKs of SoC manufacturers.
  Additionally, Leda will strive for being easy to install on low-cost "evaluation boards" such as the Raspberry Pi,
  or development environments such as a virtual machine in the cloud.
- **Integrate software-defined-vehicle Open Source components to showcase the available features and their state of maturity:**
  The SDV ecosystem will grow and a lot of new software projects will be needed to solve the current problems and challenges.
  The Eclipse SDV ecosystem already contains many software packages, which independently make sense for their set goals.
  With Leda, we want to increase the integrational aspect, helping project leads, developers, contributors, users and architects
  to evaluate the SDV portfolio, how it can be integrated with each other and how a possible reference architecture implementation might be loooking like.
- **Demonstrate the use and interaction of open protocols and specifications:**
  - Vehicle Signal Specifications from the [The Connected Vehicle Systems Alliance (COVESA)](https://www.covesa.global/) 
    to establish a semantically useful  abstraction model for vehicle signals.
  - OpenTelemetry specs and components, to show the possibilities of applying DevOps methodologies and technologies
    to operate, monitor and maintain fleets of vehicles and their distributed software applications
  - Eclipse IoT related specifications for software rollouts and digital twin representations
