---
title: Row2

date: 2026-03-08T08:02:59.467117
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.Steering.Axle.Row2` |
| Description: | MotionManagement related to rear axle. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->Steering

    Steering-->Axle

    Axle-->Row2

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.Steering.Axle.Row2](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.Steering.Axle.Row2/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.Steering.Axle.Row2` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.Steering.Axle.Row2` is `0382036275a0528f806d0c511be3cb3b`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.Steering.Axle.Row2.SteerAngle](steerangle/) (Represents the current actuated steering angle of the steered wheels on rear axle. Signal orientation according ISO8855, single track model.)
- [Vehicle.MotionManagement.Steering.Axle.Row2.SteerAngleTarget](steerangletarget/) (Steer angle request to the rear axle steering actuator (external set-point). Signal orientation according ISO8855, single track model.)
- [Vehicle.MotionManagement.Steering.Axle.Row2.SteerAngleVelocityTarget](steeranglevelocitytarget/) (Requested velocity for steer angle change. Signal orientation according ISO8855. Optional signal to adapt rear wheel steering closed loop control gain.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.Steering.Axle.Row2) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

