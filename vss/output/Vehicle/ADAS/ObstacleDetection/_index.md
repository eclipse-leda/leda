---
title: ObstacleDetection

date: 2023-06-05T12:39:01.751236
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.ObstacleDetection` |
| Description: | Signals form Obstacle Sensor System. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->ObstacleDetection

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.ObstacleDetection](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.ObstacleDetection/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.ObstacleDetection` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.ObstacleDetection` is `e7b6d81631cc5ac584d027d4c1a66cb5`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.ObstacleDetection.IsEnabled](isenabled/) (Indicates if obstacle sensor system is enabled (i.e. monitoring for obstacles). True = Enabled. False = Disabled.)
- [Vehicle.ADAS.ObstacleDetection.IsError](iserror/) (Indicates if obstacle sensor system incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.ObstacleDetection.IsWarning](iswarning/) (Indicates if obstacle sensor system registered an obstacle.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.ObstacleDetection) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

