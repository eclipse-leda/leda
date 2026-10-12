---
title: Network

date: 2026-10-12T19:51:35.371300
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ControlUnit.FrontLeft.Health.Network` |
| Description: | Network attributes and signals |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ControlUnit

    ControlUnit-->FrontLeft

    FrontLeft-->Health

    Health-->Network

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ControlUnit.FrontLeft.Health.Network](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ControlUnit.FrontLeft.Health.Network/) |


## Signal Information




The vehicle signal `Vehicle.ControlUnit.FrontLeft.Health.Network` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ControlUnit.FrontLeft.Health.Network.CAN](can/) (CAN network attributes and signals)
- [Vehicle.ControlUnit.FrontLeft.Health.Network.ETH](eth/) (Ethernet network attributes and signals)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ControlUnit.FrontLeft.Health.Network) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

