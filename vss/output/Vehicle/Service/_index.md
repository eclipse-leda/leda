---
title: Service

date: 2023-06-05T12:39:09.309077
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Service` |
| Description: | Service data. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Service

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Service](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Service/) |


## Signal Information




The vehicle signal `Vehicle.Service` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Service` is `b6463772705b56a7a993e23601bd3d47`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Service.DistanceToService](distancetoservice/) (Remaining distance to service (of any kind). Negative values indicate service overdue.)
- [Vehicle.Service.IsServiceDue](isservicedue/) (Indicates if vehicle needs service (of any kind). True = Service needed now or in the near future. False = No known need for service.)
- [Vehicle.Service.TimeToService](timetoservice/) (Remaining time to service (of any kind). Negative values indicate service overdue.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Service) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

