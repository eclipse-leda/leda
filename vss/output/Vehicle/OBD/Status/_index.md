---
title: Status

date: 2023-06-05T12:39:05.130675
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.OBD.Status` |
| Description: | PID 01 - OBD status |

## Navigation

```mermaid
flowchart LR



    Vehicle-->OBD

    OBD-->Status

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.OBD.Status](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.OBD.Status/) |


## Signal Information




The vehicle signal `Vehicle.OBD.Status` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.OBD.Status` is `474f58e593ee5bfebbb9c6ce4a453f96`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.OBD.Status.DTCCount](dtccount/) (Number of sensor Trouble Codes (DTC))
- [Vehicle.OBD.Status.IgnitionType](ignitiontype/) (Type of the ignition for ICE - spark = spark plug ignition, compression = self-igniting (Diesel engines))
- [Vehicle.OBD.Status.IsMILOn](ismilon/) (Malfunction Indicator Light (MIL) False = Off, True = On)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.OBD.Status) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

