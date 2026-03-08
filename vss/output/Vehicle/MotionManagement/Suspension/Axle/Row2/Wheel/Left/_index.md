---
title: Left

date: 2026-03-08T08:02:59.742097
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left` |
| Description: | MotionManagement signals for a specific wheel. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->Suspension

    Suspension-->Axle

    Axle-->Row2

    Row2-->Wheel

    Wheel-->Left

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left` is `17c664e19d3554f8bd5ef454f73f6e13`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left.DampingForce](dampingforce/) (Actuated damping force at given wheel. Signal orientation according ISO8855, meaning positive force is pointing upwards.)
- [Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left.DampingForceTarget](dampingforcetarget/) (Damping force request at given wheel. Signal orientation according ISO8855, meaning positive force is pointing upwards.)
- [Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left.DampingRate](dampingrate/) (Actuated damping rate at given wheel. 0% = lowest possible damping rate 100% = highest possible damping rate)
- [Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left.DampingRateTarget](dampingratetarget/) (Damping rate request at given wheel. 0% = lowest possible damping rate 100% = highest possible damping rate)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.Suspension.Axle.Row2.Wheel.Left) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

