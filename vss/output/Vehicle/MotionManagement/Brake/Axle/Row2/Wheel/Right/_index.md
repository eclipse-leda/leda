---
title: Right

date: 2026-03-08T08:02:59.193587
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right` |
| Description: | MotionManagement signals for a specific wheel. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->Brake

    Brake-->Axle

    Axle-->Row2

    Row2-->Wheel

    Wheel-->Right

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right` is `20621c745e7b5139a14608e814e64a6f`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.OmegaLower](omegalower/) (Lower wheel speed limit request controlled by friction brake. ISO 8855 wheel-spin velocity.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.OmegaUpper](omegaupper/) (Upper wheel speed limit request controlled by friction brake. ISO 8855 wheel-spin velocity.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.Torque](torque/) (Estimated friction brake torque. Brake Torque < 0Nm.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.TorqueArbitrated](torquearbitrated/) (Brake system internally calculated friction brake torque target. Brake Torque < 0Nm.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.TorqueFrictionMaximum](torquefrictionmaximum/) (Maximum wheel torque request for friction brake. Brake Torque < 0Nm.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right.TorqueFrictionMinimum](torquefrictionminimum/) (Minimum wheel torque request for friction brake. Brake Torque < 0Nm.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.Brake.Axle.Row2.Wheel.Right) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

