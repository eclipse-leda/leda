---
title: Row3

date: 2023-06-05T12:38:45.866838
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.HVAC.Station.Row3` |
| Description: | HVAC for single station in the vehicle |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->HVAC

    HVAC-->Station

    Station-->Row3

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.HVAC.Station.Row3](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.HVAC.Station.Row3/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.HVAC.Station.Row3` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.HVAC.Station.Row3` is `6eb8d63b66c859d5b36ef52d264aed2b`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.HVAC.Station.Row3.Left](left/) (HVAC for single station in the vehicle)
- [Vehicle.Cabin.HVAC.Station.Row3.Right](right/) (HVAC for single station in the vehicle)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.HVAC.Station.Row3) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).
