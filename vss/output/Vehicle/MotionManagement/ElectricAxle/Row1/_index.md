---
title: Row1

date: 2026-03-08T08:02:58.563241
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.ElectricAxle.Row1` |
| Description: | MotionManagement for a specific electric axle. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->ElectricAxle

    ElectricAxle-->Row1

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.ElectricAxle.Row1](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.ElectricAxle.Row1/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.ElectricAxle.Row1` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.ElectricAxle.Row1` is `5b7d73d2bc485eabbce3a93d9704a982`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.ElectricAxle.Row1.RotationalSpeed](rotationalspeed/) (Rotational speed for the specified axle, positive sign for rotation in forward direction, negative sign for rotation in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.RotationalSpeedMaximumLimit](rotationalspeedmaximumlimit/) (Maximum allowed axle rotational speed in torque control mode, positive sign for rotation in forward direction, negative sign for rotation in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.RotationalSpeedMinimumLimit](rotationalspeedminimumlimit/) (Minimum allowed axle rotational speed in torque control mode, positive sign for rotation in forward direction, negative sign for rotation in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.RotationalSpeedTarget](rotationalspeedtarget/) (Target axle rotational speed in rotation speed control mode, positive sign for rotation in forward direction, negative sign for rotation in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.Torque](torque/) (Axle torque, positive sign for torque in forward direction, negative sign for torque in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.TorqueMaximum](torquemaximum/) (Maximum momentarily available eAxle torque, positive sign for torque in forward direction, negative sign for torque in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.TorqueMaximumLimit](torquemaximumlimit/) (Maximum allowed eAxle torque in rotation speed control mode, positive sign for torque in forward direction, negative sign unused.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.TorqueMinimum](torqueminimum/) (Minimum momentarily available eAxle torque, positive sign for torque in forward direction, negative sign for torque in backward direction.)
- [Vehicle.MotionManagement.ElectricAxle.Row1.TorqueMinimumLimit](torqueminimumlimit/) (Minimum allowed axle torque in rotation speed control mode, positive sign unused, negative sign for torque in backward direction (ISO8855).)
- [Vehicle.MotionManagement.ElectricAxle.Row1.TorqueTarget](torquetarget/) (Target axle torque in torque control mode, positive sign for torque in forward direction, negative sign for torque in backward direction (ISO8855).)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.ElectricAxle.Row1) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

