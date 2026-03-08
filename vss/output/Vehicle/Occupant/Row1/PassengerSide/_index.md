---
title: PassengerSide

date: 2026-03-08T08:02:57.818183
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Occupant.Row1.PassengerSide` |
| Description: | Occupant (Driver or Passenger) data. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Occupant

    Occupant-->Row1

    Row1-->PassengerSide

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Occupant.Row1.PassengerSide](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Occupant.Row1.PassengerSide/) |


## Signal Information




The vehicle signal `Vehicle.Occupant.Row1.PassengerSide` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Occupant.Row1.PassengerSide` is `f8e6e66800f65da1adce3bbcb4757bff`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Occupant.Row1.PassengerSide.HeadPosition](headposition/) (The current position of the driver head on vehicle axis according to ISO 23150:2023.)
- [Vehicle.Occupant.Row1.PassengerSide.Identifier](identifier/) (Identifier attributes based on OAuth 2.0.)
- [Vehicle.Occupant.Row1.PassengerSide.MidEyeGaze](mideyegaze/) (Direction from mid eye position to object driver is looking at.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Occupant.Row1.PassengerSide) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

