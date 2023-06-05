---
title: DieselExhaustFluid

date: 2023-06-05T12:38:37.789335
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid` |
| Description: | Signals related to Diesel Exhaust Fluid (DEF). DEF is called AUS32 in ISO 22241. |
| Comment: | In retail and marketing other names are typically used for the fluid. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->CombustionEngine

    CombustionEngine-->DieselExhaustFluid

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid` is `81d8eec46d9357a3b1064bfb5d070fa2`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid.Capacity](capacity/) (Capacity in liters of the Diesel Exhaust Fluid Tank.)
- [Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid.IsLevelLow](islevellow/) (Indicates if the Diesel Exhaust Fluid level is low. True if level is low. Definition of low is vehicle dependent.)
- [Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid.Level](level/) (Level of the Diesel Exhaust Fluid tank as percent of capacity. 0 = empty. 100 = full.)
- [Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid.Range](range/) (Remaining range in meters of the Diesel Exhaust Fluid present in the vehicle.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.CombustionEngine.DieselExhaustFluid) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

