---
title: LaneDepartureDetection

date: 2023-06-05T12:39:01.661908
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.LaneDepartureDetection` |
| Description: | Signals from Lane Departure Detection System. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->LaneDepartureDetection

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.LaneDepartureDetection](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.LaneDepartureDetection/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.LaneDepartureDetection` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.LaneDepartureDetection` is `e45f33fdcf245f11981b2f201ee8281a`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.LaneDepartureDetection.IsEnabled](isenabled/) (Indicates if lane departure detection system is enabled. True = Enabled. False = Disabled.)
- [Vehicle.ADAS.LaneDepartureDetection.IsError](iserror/) (Indicates if lane departure system incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.LaneDepartureDetection.IsWarning](iswarning/) (Indicates if lane departure detection registered a lane departure.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.LaneDepartureDetection) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

