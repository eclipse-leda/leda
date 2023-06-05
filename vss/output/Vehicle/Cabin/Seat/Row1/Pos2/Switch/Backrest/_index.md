---
title: Backrest

date: 2023-06-05T12:38:53.555706
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest` |
| Description: | Describes switches related to the backrest of the seat. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Seat

    Seat-->Row1

    Row1-->Pos2

    Pos2-->Switch

    Switch-->Backrest

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest` is `79b1c57ac9245a5ca426a8b5e21717a6`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest.IsReclineBackwardEngaged](isreclinebackwardengaged/) (Backrest recline backward switch engaged (SingleSeat.Backrest.Recline).)
- [Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest.IsReclineForwardEngaged](isreclineforwardengaged/) (Backrest recline forward switch engaged (SingleSeat.Backrest.Recline).)
- [Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest.Lumbar](lumbar/) (Switches for SingleSeat.Backrest.Lumbar.)
- [Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest.SideBolster](sidebolster/) (Switches for SingleSeat.Backrest.SideBolster.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Seat.Row1.Pos2.Switch.Backrest) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

