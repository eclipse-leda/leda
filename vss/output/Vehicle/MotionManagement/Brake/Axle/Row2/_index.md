---
title: Row2

date: 2026-03-08T08:02:59.061996
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.Brake.Axle.Row2` |
| Description: | MotionManagement for brake actuation for a specific electric axle. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->Brake

    Brake-->Axle

    Axle-->Row2

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.Brake.Axle.Row2](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.Brake.Axle.Row2/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.Brake.Axle.Row2` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.Brake.Axle.Row2` is `b38be1e7c1465622841b40c20a14312b`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.Brake.Axle.Row2.TorqueDistributionFrictionRightMaximum](torquedistributionfrictionrightmaximum/) (Maximum distribution range of the friction brake request on the axle to the right wheel. 0% = Complete friction torque shall be shifted to the left wheel. 50% = At most 50% friction torque may be shifted to the right wheel. 100% = Complete friction torque may be shifted to the right wheel.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.TorqueDistributionFrictionRightMinimum](torquedistributionfrictionrightminimum/) (Minimum distribution range of the friction brake request on the axle to the right wheel. 0% = Complete friction torque may be shifted to the left wheel. 50% = At least 50% friction torque shall be shifted to the right wheel. 100% = Complete friction torque shall be shifted to the right wheel.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.TorqueElectricMinimum](torqueelectricminimum/) (Limit for regenerative brake torque at given axle. Brake Torque < 0Nm.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.TorqueFrictionDifferenceMaximum](torquefrictiondifferencemaximum/) (Maximum absolute wheel torque difference between left and right wheel for friction brake.)
- [Vehicle.MotionManagement.Brake.Axle.Row2.Wheel](wheel/) (MotionManagement signals for a specific wheel.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.Brake.Axle.Row2) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

