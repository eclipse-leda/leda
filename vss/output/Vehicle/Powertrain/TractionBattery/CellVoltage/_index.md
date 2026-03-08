---
title: CellVoltage

date: 2026-03-08T08:02:46.390499
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.CellVoltage` |
| Description: | Voltage information for cells in the battery pack. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->CellVoltage

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.CellVoltage](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.CellVoltage/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.CellVoltage` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.CellVoltage` is `0070210b80125f1a8e9473f8875fe3d1`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.CellVoltage.CellVoltages](cellvoltages/) (Array of cell voltages. Length or array shall correspond to number of cells in vehicle.)
- [Vehicle.Powertrain.TractionBattery.CellVoltage.IdMax](idmax/) (Identifier of the battery cell with highest voltage.)
- [Vehicle.Powertrain.TractionBattery.CellVoltage.IdMin](idmin/) (Identifier of the battery cell with lowest voltage.)
- [Vehicle.Powertrain.TractionBattery.CellVoltage.Max](max/) (Current voltage of the battery cell with highest voltage.)
- [Vehicle.Powertrain.TractionBattery.CellVoltage.Min](min/) (Current voltage of the battery cell with lowest voltage.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.CellVoltage) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

