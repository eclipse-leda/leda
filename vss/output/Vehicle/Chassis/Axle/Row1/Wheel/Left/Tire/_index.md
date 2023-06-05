---
title: Tire

date: 2023-06-05T12:39:03.327231
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire` |
| Description: | Tire signals for wheel. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Chassis

    Chassis-->Axle

    Axle-->Row1

    Row1-->Wheel

    Wheel-->Left

    Left-->Tire

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire/) |


## Signal Information




The vehicle signal `Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire` is `17c60ec3c02054b4951c975156375d9a`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.IsPressureLow](ispressurelow/) (Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.)
- [Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure](pressure/) (Tire pressure in kilo-Pascal.)
- [Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Temperature](temperature/) (Tire temperature in Celsius.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

