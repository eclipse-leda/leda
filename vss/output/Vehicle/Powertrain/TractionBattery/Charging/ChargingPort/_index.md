---
title: ChargingPort

date: 2026-03-08T08:02:46.653806
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Charging.ChargingPort` |
| Description: | Properties related to a particular charging port available in the vehicle. |
| Comment: | If a vehicle has a single charging port, then use the instance AnyPosition. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Charging

    Charging-->ChargingPort

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Charging.ChargingPort/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Charging.ChargingPort` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Charging.ChargingPort` is `a13011fe556b5e3388fec7d183022917`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.AnyPosition](anyposition/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.FrontLeft](frontleft/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.FrontMiddle](frontmiddle/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.FrontRight](frontright/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.RearLeft](rearleft/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.RearMiddle](rearmiddle/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort.RearRight](rearright/) (Properties related to a particular charging port available in the vehicle.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Charging.ChargingPort) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

