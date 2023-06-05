---
title: ElectricMotor

date: 2023-06-05T12:38:38.826638
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.ElectricMotor` |
| Description: | Electric Motor specific data. |

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





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.ElectricMotor` is `1ade64f6b0d05f6c9340e7a667555ae2`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.ElectricMotor.CoolantTemperature](coolanttemperature/) (Motor coolant temperature (if applicable).)
- [Vehicle.Powertrain.ElectricMotor.EngineCode](enginecode/) (Engine code designation, as specified by vehicle manufacturer.)
- [Vehicle.Powertrain.ElectricMotor.MaxPower](maxpower/) (Peak power, in kilowatts, that motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.MaxRegenPower](maxregenpower/) (Peak regen/brake power, in kilowatts, that motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.MaxRegenTorque](maxregentorque/) (Peak regen/brake torque, in newton meter, that the motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.MaxTorque](maxtorque/) (Peak power, in newton meter, that the motor(s) can generate.)
- [Vehicle.Powertrain.ElectricMotor.Power](power/) (Current motor power output. Negative values indicate regen mode.)
- [Vehicle.Powertrain.ElectricMotor.Speed](speed/) (Motor rotational speed measured as rotations per minute. Negative values indicate reverse driving mode.)
- [Vehicle.Powertrain.ElectricMotor.Temperature](temperature/) (Motor temperature.)
- [Vehicle.Powertrain.ElectricMotor.Torque](torque/) (Current motor torque. Negative values indicate regen mode.)


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

