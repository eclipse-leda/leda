---
title: DMS

date: 2026-03-08T08:02:56.392581
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.DMS` |
| Description: | Driver Monitoring System signals. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->DMS

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.DMS](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.DMS/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.DMS` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.DMS` is `1cd72c7fc7fe5269a93c9954f46a4f60`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.DMS.IsEnabled](isenabled/) (Indicates if DMS is enabled. True = Enabled. False = Disabled.)
- [Vehicle.ADAS.DMS.IsError](iserror/) (Indicates if DMS incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.DMS.IsWarning](iswarning/) (Indicates if DMS has registered a driver alert condition.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.DMS) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

