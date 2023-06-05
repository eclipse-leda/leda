---
title: SteeringWheel

date: 2023-06-05T12:39:04.730990
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Chassis.SteeringWheel` |
| Description: | Steering wheel signals |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Chassis

    Chassis-->SteeringWheel

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Chassis.SteeringWheel](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Chassis.SteeringWheel/) |


## Signal Information




The vehicle signal `Vehicle.Chassis.SteeringWheel` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Chassis.SteeringWheel` is `8c759072791e5986ac4efe9df0c2b751`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Chassis.SteeringWheel.Angle](angle/) (Steering wheel angle. Positive = degrees to the left. Negative = degrees to the right.)
- [Vehicle.Chassis.SteeringWheel.Extension](extension/) (Steering wheel column extension from dashboard. 0 = Closest to dashboard. 100 = Furthest from dashboard.)
- [Vehicle.Chassis.SteeringWheel.Position](position/) (Position of the steering wheel on the left or right side of the vehicle.)
- [Vehicle.Chassis.SteeringWheel.Tilt](tilt/) (Steering wheel column tilt. 0 = Lowest position. 100 = Highest position.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Chassis.SteeringWheel) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

