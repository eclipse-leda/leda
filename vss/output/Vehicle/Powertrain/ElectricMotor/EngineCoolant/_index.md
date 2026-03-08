---
title: EngineCoolant

date: 2026-03-08T08:02:46.207138
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.ElectricMotor.EngineCoolant` |
| Description: | Signals related to the engine coolant (if applicable). |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->ElectricMotor

    ElectricMotor-->EngineCoolant

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.ElectricMotor.EngineCoolant](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.ElectricMotor.EngineCoolant/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.ElectricMotor.EngineCoolant` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.ElectricMotor.EngineCoolant` is `898ca20307545537929a13522eea4844`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.ElectricMotor.EngineCoolant.Capacity](capacity/) (Engine coolant capacity in liters.)
- [Vehicle.Powertrain.ElectricMotor.EngineCoolant.Level](level/) (Engine coolant level.)
- [Vehicle.Powertrain.ElectricMotor.EngineCoolant.LifeRemaining](liferemaining/) (Remaining engine coolant life in seconds. Negative values can be used to indicate that lifetime has been exceeded.)
- [Vehicle.Powertrain.ElectricMotor.EngineCoolant.Temperature](temperature/) (Engine coolant temperature.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.ElectricMotor.EngineCoolant) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

