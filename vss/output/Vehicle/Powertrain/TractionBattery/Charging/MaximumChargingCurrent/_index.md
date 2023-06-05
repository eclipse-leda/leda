---
title: MaximumChargingCurrent

date: 2023-06-05T12:38:40.122394
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent` |
| Description: | Maximum charging current that can be accepted by the system, as measured at the charging inlet. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Charging

    Charging-->MaximumChargingCurrent

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent` is `e3f2e57e7a395d9ca9931d429e540a34`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent.DC](dc/) (Maximum DC charging current at inlet that can be accepted by the system.)
- [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent.Phase1](phase1/) (Maximum AC charging current (rms) at inlet for Phase 1 that can be accepted by the system.)
- [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent.Phase2](phase2/) (Maximum AC charging current (rms) at inlet for Phase 2 that can be accepted by the system.)
- [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent.Phase3](phase3/) (Maximum AC charging current (rms) at inlet for Phase 3 that can be accepted by the system.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

