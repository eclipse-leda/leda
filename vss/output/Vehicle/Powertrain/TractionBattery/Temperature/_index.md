---
title: Temperature

date: 2023-06-05T12:38:39.321942
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Temperature` |
| Description: | Temperature Information for the battery pack. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Temperature

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Temperature](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Temperature/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Temperature` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Temperature` is `1cfbcf8c152959dcb3eb2c54fc42e623`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Temperature.Average](average/) (Current average temperature of the battery cells.)
- [Vehicle.Powertrain.TractionBattery.Temperature.Max](max/) (Current maximum temperature of the battery cells, i.e. temperature of the hottest cell.)
- [Vehicle.Powertrain.TractionBattery.Temperature.Min](min/) (Current minimum temperature of the battery cells, i.e. temperature of the coldest cell.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Temperature) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

