---
title: Rear

date: 2026-10-12T19:51:21.915711
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.ElectricMotor.Rear` |
| Description: | Electric Motor specific data. |
| Comment: | Instance Front to be used if the vehicle has a motor located at the front of the vehicle, serving front and possibly also rear axle. Instance Rear to be used if the vehicle has a motor located at the rear of the vehicle, serving rear and possiblsy also front axle. Instances with Left/Right intended to be used if vehicle has separate motors for left and right side. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->ElectricMotor

    ElectricMotor-->Rear

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.ElectricMotor.Rear](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.ElectricMotor.Rear/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.ElectricMotor.Rear` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.ElectricMotor.Rear.EngineCode](enginecode/) (Engine code designation, as specified by vehicle manufacturer.)
- [Vehicle.Powertrain.ElectricMotor.Rear.EngineCoolant](enginecoolant/) (Signals related to the engine coolant (if applicable).)
- [Vehicle.Powertrain.ElectricMotor.Rear.MaxPower](maxpower/) (Peak power, in kilowatts, that motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.Rear.MaxRegenPower](maxregenpower/) (Peak regen/brake power, in kilowatts, that motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.Rear.MaxRegenTorque](maxregentorque/) (Peak regen/brake torque, in newton meter, that the motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.Rear.MaxTorque](maxtorque/) (Peak power, in newton meter, that the motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.Rear.Power](power/) (Current motor power output. Negative values indicate regen mode.)
- [Vehicle.Powertrain.ElectricMotor.Rear.Speed](speed/) (Motor rotational speed measured as rotations per minute. Negative values indicate reverse driving mode.)
- [Vehicle.Powertrain.ElectricMotor.Rear.Temperature](temperature/) (Motor temperature.)
- [Vehicle.Powertrain.ElectricMotor.Rear.TimeInUse](timeinuse/) (Accumulated time during engine lifetime when the vehicule state's is 'READY'.)
- [Vehicle.Powertrain.ElectricMotor.Rear.Torque](torque/) (Current motor torque. Negative values indicate regen mode.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.ElectricMotor.Rear) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

