---
title: ChargeSustaining

date: 2026-03-08T08:02:47.733673
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.RangeExtender.ChargeSustaining` |
| Description: | Signals related to Charge Sustaining (CS) mode operation. |
| Comment: | CS mode represents the range-extended operation where the internal combustion engine operates as a generator to maintain battery charge and provide extended driving range. During this mode, fuel consumption becomes the primary energy source metric. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->RangeExtender

    RangeExtender-->ChargeSustaining

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.RangeExtender.ChargeSustaining](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.RangeExtender.ChargeSustaining/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.RangeExtender.ChargeSustaining` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.RangeExtender.ChargeSustaining` is `b5d8945c8f8c54fbb15a1aca578ad70a`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy](fueleconomy/) (Current fuel economy during Charge Sustaining mode operation.)
- [Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range](range/) (Estimated remaining distance that can be traveled in Charge Sustaining mode using available fuel.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.RangeExtender.ChargeSustaining) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

