---
title: Massage

date: 2026-03-08T08:02:54.851289
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Seat.Row2.PassengerSide.Massage` |
| Description: | Massage related information for the seat. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Seat

    Seat-->Row2

    Row2-->PassengerSide

    PassengerSide-->Massage

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Seat.Row2.PassengerSide.Massage/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Seat.Row2.PassengerSide.Massage` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Seat.Row2.PassengerSide.Massage` is `bd9ec382d92e52ae826cb532ba13e11f`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage.IsAvailable](isavailable/) (True if the seat have the massage capability)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage.Level](level/) (Seat massage level. 0 = off. 100 = max massage.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage.Status](status/) (Massage status.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage.SupportedTypes](supportedtypes/) (Type of massage.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage.TypeActive](typeactive/) (Type of massage active.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Seat.Row2.PassengerSide.Massage) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

