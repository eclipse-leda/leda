---
title: WasherFluid

date: 2023-06-05T12:38:43.772328
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Windshield.Rear.WasherFluid` |
| Description: | Windshield washer fluid signals |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Windshield

    Windshield-->Rear

    Rear-->WasherFluid

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Windshield.Rear.WasherFluid](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Windshield.Rear.WasherFluid/) |


## Signal Information




The vehicle signal `Vehicle.Body.Windshield.Rear.WasherFluid` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Windshield.Rear.WasherFluid` is `1ea4ac2370e1567b9b812c1e3020ddfb`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.Windshield.Rear.WasherFluid.IsLevelLow](islevellow/) (Low level indication for washer fluid. True = Level Low. False = Level OK.)
- [Vehicle.Body.Windshield.Rear.WasherFluid.Level](level/) (Washer fluid level as a percent. 0 = Empty. 100 = Full.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Windshield.Rear.WasherFluid) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

