---
title: ChargeVoltage

date: 2023-06-05T12:38:40.739040
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage` |
| Description: | Current charging voltage, as measured at the charging inlet. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Charging

    Charging-->ChargeVoltage

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage` is `7170151d653b52c6bb5e75cb0a14d1c5`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage.DC](dc/) (Current DC charging voltage at charging inlet.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage.Phase1](phase1/) (Current AC charging voltage (rms) at inlet for Phase 1.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage.Phase2](phase2/) (Current AC charging voltage (rms) at inlet for Phase 2.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage.Phase3](phase3/) (Current AC charging voltage (rms) at inlet for Phase 3.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

