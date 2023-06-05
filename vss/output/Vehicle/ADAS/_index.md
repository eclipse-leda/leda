---
title: ADAS

date: 2023-06-05T12:39:01.348327
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS` |
| Description: | All Advanced Driver Assist Systems data. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS/) |


## Signal Information




The vehicle signal `Vehicle.ADAS` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS` is `14c2b2e1297b513197d320a5ce58f42e`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.ABS](abs/) (Antilock Braking System signals.)
- [Vehicle.ADAS.ActiveAutonomyLevel](activeautonomylevel/) (Indicates the currently active level of autonomy according to SAE J3016 taxonomy.)
- [Vehicle.ADAS.CruiseControl](cruisecontrol/) (Signals from Cruise Control system.)
- [Vehicle.ADAS.EBA](eba/) (Emergency Brake Assist (EBA) System signals.)
- [Vehicle.ADAS.EBD](ebd/) (Electronic Brakeforce Distribution (EBD) System signals.)
- [Vehicle.ADAS.ESC](esc/) (Electronic Stability Control System signals.)
- [Vehicle.ADAS.LaneDepartureDetection](lanedeparturedetection/) (Signals from Lane Departure Detection System.)
- [Vehicle.ADAS.ObstacleDetection](obstacledetection/) (Signals form Obstacle Sensor System.)
- [Vehicle.ADAS.PowerOptimizeLevel](poweroptimizelevel/) (Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.)
- [Vehicle.ADAS.SupportedAutonomyLevel](supportedautonomylevel/) (Indicates the highest level of autonomy according to SAE J3016 taxonomy the vehicle is capable of.)
- [Vehicle.ADAS.TCS](tcs/) (Traction Control System signals.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

