---
title: Brake

date: 2026-03-08T08:02:58.786297
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.Brake` |
| Description: | MotionManagement related to braking (both frictions brakes and contribution from electric axles). |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->Brake

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.Brake](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.Brake/) |


## Signal Information




The vehicle signal `Vehicle.MotionManagement.Brake` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.Brake` is `c589f6eeff005455b7012314913bdfd2`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.MotionManagement.Brake.Axle](axle/) (MotionManagement for brake actuation for a specific electric axle.)
- [Vehicle.MotionManagement.Brake.VehicleForceDistributionFrontMaximum](vehicleforcedistributionfrontmaximum/) (Maximum distribution range request of FxWhlSum to front axle. 0% = Complete longitudinal brake force shall be shifted to rear axle. 50% = At most 50% shall be shifted to front axle. 100%  = Complete longitudinal brake force may be shifted to front axle.)
- [Vehicle.MotionManagement.Brake.VehicleForceDistributionFrontMinimum](vehicleforcedistributionfrontminimum/) (Minimum distribution range request of FxWhlSum to front axle. 0% = Complete longitudinal brake force may be shifted to rear axle. 50% = At least 50% shall be shifted to front axle. 100% = Complete longitudinal brake force shall be shifted to front axle.)
- [Vehicle.MotionManagement.Brake.VehicleForceElectric](vehicleforceelectric/) (Regenerative brake force request (FxWhlSum). Sum of all tyre longitudinal forces. Brake Force < 0N.)
- [Vehicle.MotionManagement.Brake.VehicleForceElectricMinimumArbitrated](vehicleforceelectricminimumarbitrated/) (Brake system internally calculated regenerative force limit at vehicle level for eAxle actuation. Brake Force < 0N.)
- [Vehicle.MotionManagement.Brake.VehicleForceMaximum](vehicleforcemaximum/) (Maximum longitudinal brake force request (FxWhlSum). Sum of all tyre longitudinal forces. Brake Force < 0N.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.Brake) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

