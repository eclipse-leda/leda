---
title: HVAC

date: 2023-06-05T12:38:45.409927
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.HVAC` |
| Description: | Climate control |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->HVAC

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.HVAC](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.HVAC/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.HVAC` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.HVAC` is `f8ff34337cdf568e91ab406a365c3249`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.HVAC.AmbientAirTemperature](ambientairtemperature/) (Ambient air temperature inside the vehicle.)
- [Vehicle.Cabin.HVAC.IsAirConditioningActive](isairconditioningactive/) (Is Air conditioning active.)
- [Vehicle.Cabin.HVAC.IsFrontDefrosterActive](isfrontdefrosteractive/) (Is front defroster active.)
- [Vehicle.Cabin.HVAC.IsRearDefrosterActive](isreardefrosteractive/) (Is rear defroster active.)
- [Vehicle.Cabin.HVAC.IsRecirculationActive](isrecirculationactive/) (Is recirculation active.)
- [Vehicle.Cabin.HVAC.PowerOptimizeLevel](poweroptimizelevel/) (Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.)
- [Vehicle.Cabin.HVAC.Station](station/) (HVAC for single station in the vehicle)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.HVAC) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

