---
title: ChargeCurrent

date: 2023-06-05T12:38:40.594448
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent` |
| Description: | Current charging current. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Charging

    Charging-->ChargeCurrent

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent` is `94739cf563735b438878ac0f85601f27`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent.DC](dc/) (Current DC charging current at inlet. Negative if returning energy to grid.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent.Phase1](phase1/) (Current AC charging current (rms) at inlet for Phase 1. Negative if returning energy to grid.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent.Phase2](phase2/) (Current AC charging current (rms) at inlet for Phase 2. Negative if returning energy to grid.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent.Phase3](phase3/) (Current AC charging current (rms) at inlet for Phase 3. Negative if returning energy to grid.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

