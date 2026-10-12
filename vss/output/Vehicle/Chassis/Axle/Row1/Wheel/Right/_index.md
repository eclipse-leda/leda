---
title: Right

date: 2026-10-12T19:51:31.510987
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Chassis.Axle.Row1.Wheel.Right` |
| Description: | Wheel signals for axle |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Chassis

    Chassis-->Axle

    Axle-->Row1

    Row1-->Wheel

    Wheel-->Right

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Chassis.Axle.Row1.Wheel.Right](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Chassis.Axle.Row1.Wheel.Right/) |


## Signal Information




The vehicle signal `Vehicle.Chassis.Axle.Row1.Wheel.Right` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Chassis.Axle.Row1.Wheel.Right.AngularSpeed](angularspeed/) (Angular (Rotational) speed of a vehicle's wheel.)
- [Vehicle.Chassis.Axle.Row1.Wheel.Right.Brake](brake/) (Brake signals for wheel)
- [Vehicle.Chassis.Axle.Row1.Wheel.Right.Speed](speed/) (Linear speed of a vehicle's wheel.)
- [Vehicle.Chassis.Axle.Row1.Wheel.Right.Tire](tire/) (Tire signals for wheel.)
- [Vehicle.Chassis.Axle.Row1.Wheel.Right.Torque](torque/) (Torque provided by drivetrain, excluding torque provided by friction brakes. Negative values indicate regen mode.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Chassis.Axle.Row1.Wheel.Right) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

