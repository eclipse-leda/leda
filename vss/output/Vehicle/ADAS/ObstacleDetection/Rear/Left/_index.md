---
title: Left

date: 2026-03-08T08:02:55.922320
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.ObstacleDetection.Rear.Left` |
| Description: | Signals form Obstacle Sensor System. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->ObstacleDetection

    ObstacleDetection-->Rear

    Rear-->Left

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.ObstacleDetection.Rear.Left](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.ObstacleDetection.Rear.Left/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.ObstacleDetection.Rear.Left` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.ObstacleDetection.Rear.Left` is `2f6bd6744d5d5b52a01e10aab86d6c72`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.ObstacleDetection.Rear.Left.Distance](distance/) (Distance in meters to detected object)
- [Vehicle.ADAS.ObstacleDetection.Rear.Left.IsEnabled](isenabled/) (Indicates if obstacle sensor system is enabled (i.e. monitoring for obstacles). True = Enabled. False = Disabled.)
- [Vehicle.ADAS.ObstacleDetection.Rear.Left.IsError](iserror/) (Indicates if obstacle sensor system incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.ObstacleDetection.Rear.Left.IsWarning](iswarning/) (Indicates if obstacle sensor system registered an obstacle.)
- [Vehicle.ADAS.ObstacleDetection.Rear.Left.TimeGap](timegap/) (Time in milliseconds before potential impact object)
- [Vehicle.ADAS.ObstacleDetection.Rear.Left.WarningType](warningtype/) (Indicates the type of obstacle warning detected as some track not only the presence of an obstacle but potential intercepting trajectory or other characteristics.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.ObstacleDetection.Rear.Left) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

