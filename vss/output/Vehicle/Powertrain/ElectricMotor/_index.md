---
title: ElectricMotor

date: 2026-10-12T19:51:21.759849
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.ElectricMotor` |
| Description: | Electric Motor specific data. |
| Comment: | Instance Front to be used if the vehicle has a motor located at the front of the vehicle, serving front and possibly also rear axle. Instance Rear to be used if the vehicle has a motor located at the rear of the vehicle, serving rear and possiblsy also front axle. Instances with Left/Right intended to be used if vehicle has separate motors for left and right side. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->ElectricMotor

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.ElectricMotor](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.ElectricMotor/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.ElectricMotor` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.ElectricMotor.Front](front/) (Electric Motor specific data.)
- [Vehicle.Powertrain.ElectricMotor.FrontLeft](frontleft/) (Electric Motor specific data.)
- [Vehicle.Powertrain.ElectricMotor.FrontRight](frontright/) (Electric Motor specific data.)
- [Vehicle.Powertrain.ElectricMotor.Rear](rear/) (Electric Motor specific data.)
- [Vehicle.Powertrain.ElectricMotor.RearLeft](rearleft/) (Electric Motor specific data.)
- [Vehicle.Powertrain.ElectricMotor.RearRight](rearright/) (Electric Motor specific data.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.ElectricMotor) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

