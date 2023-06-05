---
title: Brake

date: 2023-06-05T12:39:03.946897
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake` |
| Description: | Brake signals for wheel |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Chassis

    Chassis-->Axle

    Axle-->Row2

    Row2-->Wheel

    Wheel-->Left

    Left-->Brake

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake/) |


## Signal Information




The vehicle signal `Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake` is `774d0a5771d35975872870cf71ea1487`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake.FluidLevel](fluidlevel/) (Brake fluid level as percent. 0 = Empty. 100 = Full.)
- [Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake.IsBrakesWorn](isbrakesworn/) (Brake pad wear status. True = Worn. False = Not Worn.)
- [Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake.IsFluidLevelLow](isfluidlevellow/) (Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.)
- [Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake.PadWear](padwear/) (Brake pad wear as percent. 0 = No Wear. 100 = Worn.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Chassis.Axle.Row2.Wheel.Left.Brake) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

