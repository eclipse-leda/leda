---
title: ESC

date: 2023-06-05T12:39:02.054773
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.ESC` |
| Description: | Electronic Stability Control System signals. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->ESC

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.ESC](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.ESC/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.ESC` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.ESC` is `636b4586ce7854b4b270a2f3b6c0af4f`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.ESC.IsEnabled](isenabled/) (Indicates if ESC is enabled. True = Enabled. False = Disabled.)
- [Vehicle.ADAS.ESC.IsEngaged](isengaged/) (Indicates if ESC is currently regulating vehicle stability. True = Engaged. False = Not Engaged.)
- [Vehicle.ADAS.ESC.IsError](iserror/) (Indicates if ESC incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.ESC.IsStrongCrossWindDetected](isstrongcrosswinddetected/) (Indicates if the ESC system is detecting strong cross winds. True = Strong cross winds detected. False = No strong cross winds detected.)
- [Vehicle.ADAS.ESC.RoadFriction](roadfriction/) (Road friction values reported by the ESC system.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.ESC) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

