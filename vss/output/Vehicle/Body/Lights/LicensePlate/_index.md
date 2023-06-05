---
title: LicensePlate

date: 2023-06-05T12:38:44.549428
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Lights.LicensePlate` |
| Description: | License plate lights. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Lights

    Lights-->LicensePlate

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Lights.LicensePlate](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Lights.LicensePlate/) |


## Signal Information




The vehicle signal `Vehicle.Body.Lights.LicensePlate` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Lights.LicensePlate` is `7bb12e42a8c45c198f83bf41b19131fa`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.Lights.LicensePlate.IsDefect](isdefect/) (Indicates if light is defect. True = Light is defect. False = Light has no defect.)
- [Vehicle.Body.Lights.LicensePlate.IsOn](ison/) (Indicates if light is on or off. True = On. False = Off.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Lights.LicensePlate) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

