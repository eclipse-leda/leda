---
title: StateOfCharge

date: 2023-06-05T12:38:39.608880
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.StateOfCharge` |
| Description: | Information on the state of charge of the vehicle's high voltage battery. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->StateOfCharge

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.StateOfCharge](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.StateOfCharge/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.StateOfCharge` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.StateOfCharge` is `26bae2ce7c4d5e2a951915ef2f5d8b7d`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.StateOfCharge.Current](current/) (Physical state of charge of the high voltage battery, relative to net capacity. This is not necessarily the state of charge being displayed to the customer.)
- [Vehicle.Powertrain.TractionBattery.StateOfCharge.Displayed](displayed/) (State of charge displayed to the customer.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.StateOfCharge) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

