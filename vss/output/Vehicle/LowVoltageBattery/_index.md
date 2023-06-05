---
title: LowVoltageBattery

date: 2023-06-05T12:38:35.001286
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.LowVoltageBattery` |
| Description: | Signals related to low voltage battery. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->LowVoltageBattery

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.LowVoltageBattery](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.LowVoltageBattery/) |


## Signal Information




The vehicle signal `Vehicle.LowVoltageBattery` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.LowVoltageBattery` is `ab8c5816d44f55b68f6e1d6d9e5acb0b`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.LowVoltageBattery.CurrentCurrent](currentcurrent/) (Current current flowing in/out of the low voltage battery. Positive = Current flowing in to battery, e.g. during charging or driving. Negative = Current flowing out of battery, e.g. when using the battery to start a combustion engine.)
- [Vehicle.LowVoltageBattery.CurrentVoltage](currentvoltage/) (Current Voltage of the low voltage battery.)
- [Vehicle.LowVoltageBattery.NominalCapacity](nominalcapacity/) (Nominal capacity of the low voltage battery.)
- [Vehicle.LowVoltageBattery.NominalVoltage](nominalvoltage/) (Nominal Voltage of the battery.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.LowVoltageBattery) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

