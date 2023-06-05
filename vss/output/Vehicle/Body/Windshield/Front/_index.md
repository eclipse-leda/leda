---
title: Front

date: 2023-06-05T12:38:42.148544
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Windshield.Front` |
| Description: | Windshield signals. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Windshield

    Windshield-->Front

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Windshield.Front](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Windshield.Front/) |


## Signal Information




The vehicle signal `Vehicle.Body.Windshield.Front` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Windshield.Front` is `8f0c61e4e4f557d98729210fc3c74f72`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.Windshield.Front.IsHeatingOn](isheatingon/) (Windshield heater status. False - off, True - on.)
- [Vehicle.Body.Windshield.Front.WasherFluid](washerfluid/) (Windshield washer fluid signals)
- [Vehicle.Body.Windshield.Front.Wiping](wiping/) (Windshield wiper signals.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Windshield.Front) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

