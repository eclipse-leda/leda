---
title: ABS

date: 2023-06-05T12:39:01.868024
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.ABS` |
| Description: | Antilock Braking System signals. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->ABS

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.ABS](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.ABS/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.ABS` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.ABS` is `219270ef27c4531f874bbda63743b330`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.ABS.IsEnabled](isenabled/) (Indicates if ABS is enabled. True = Enabled. False = Disabled.)
- [Vehicle.ADAS.ABS.IsEngaged](isengaged/) (Indicates if ABS is currently regulating brake pressure. True = Engaged. False = Not Engaged.)
- [Vehicle.ADAS.ABS.IsError](iserror/) (Indicates if ABS incurred an error condition. True = Error. False = No Error.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.ABS) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

