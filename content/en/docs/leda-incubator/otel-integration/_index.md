---
title: "OpenTelemetry Integration"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

The OpenTelemetry integration shall be used to connect the edge device's application log files to an existing DevOps infrastructure on the cloud side.

**Status:** Open for initial contribution

## Background

The legacy approach to logging of vehicle applications is outdated and prevents application developers from retrieving near-time information
on the application's health in a fleet. Existing log or remote diagnostic systems for vehicles may still use a "file upload on remote request" approach.

For a more streamlined and updated way of accessing applications logs, the idea is to expore the use of current Cloud DevOps methods and
technologies and apply them to remote vehicle edge system devices.

## Goals and Wishlist

- Collect logs from containerized applications (and system logs) on the edge device
- Control the edge's log manager configuration remotely and on-demand:
  - Enable and disable
  - One-shot activation schedules
  - Changing log levels
  - Apply filtering or sampling configurations
  - Trigger logging based on locally evaluated, dynamic conditions (IF condition=true THEN stream logs and metrics of app X for 15 minutes)
- Retrieve and stream log messages from the edge device to an existing cloud backend (e.g. Grafana, Loki, ELK, Prometheus).
  The point here being that the endpoints should be vendor-neutral and use open standard protocols.
- Retrieve application logs in different ways:
  - streamed near-time debug/trace logs for application developers in development and testing environments
  - streamed error logs for fleet operators for production environments
  - packaged, file-based logs for offroad (offline) vehicles
- Retrieve container metrics, such as CPU, memory, disk i/o, network usage and other I/O
  This is interesting for application developers, for system integrators and for fleet operators to optimize their products and services.
- Enable distributed tracing of application requests using span IDs, trace IDs or correlation IDs
  For future troubleshooting and support purposes, an integration of cloud-side applications and edge-side applications into commercial operation
  of distributed vehicle systems may become necessary.

## Source Repository

Source Repository: <https://github.com/eclipse-leda/leda-contrib-otel>

