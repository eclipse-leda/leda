---
title: CruiseControl

date: 2023-06-05T12:39:01.428842
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ADAS.CruiseControl` |
| Description: | Signals from Cruise Control system. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ADAS

    ADAS-->CruiseControl

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ADAS.CruiseControl](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ADAS.CruiseControl/) |


## Signal Information




The vehicle signal `Vehicle.ADAS.CruiseControl` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ADAS.CruiseControl` is `c4d751cf74f9576dbba3cc820991c1fb`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ADAS.CruiseControl.IsActive](isactive/) (Indicates if cruise control system is active (i.e. actively controls speed). True = Active. False = Inactive.)
- [Vehicle.ADAS.CruiseControl.IsEnabled](isenabled/) (Indicates if cruise control system is enabled (e.g. ready to receive configurations and settings) True = Enabled. False = Disabled.)
- [Vehicle.ADAS.CruiseControl.IsError](iserror/) (Indicates if cruise control system incurred an error condition. True = Error. False = No Error.)
- [Vehicle.ADAS.CruiseControl.SpeedSet](speedset/) (Set cruise control speed in kilometers per hour.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ADAS.CruiseControl) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

