---
title: Backrest

date: 2023-06-05T12:39:00.572513
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest` |
| Description: | Describes switches related to the backrest of the seat. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Seat

    Seat-->Row2

    Row2-->Pos3

    Pos3-->Switch

    Switch-->Backrest

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest` is `583a22d4a1365db9bf386a96bcafd292`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest.IsReclineBackwardEngaged](isreclinebackwardengaged/) (Backrest recline backward switch engaged (SingleSeat.Backrest.Recline).)
- [Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest.IsReclineForwardEngaged](isreclineforwardengaged/) (Backrest recline forward switch engaged (SingleSeat.Backrest.Recline).)
- [Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest.Lumbar](lumbar/) (Switches for SingleSeat.Backrest.Lumbar.)
- [Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest.SideBolster](sidebolster/) (Switches for SingleSeat.Backrest.SideBolster.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Seat.Row2.Pos3.Switch.Backrest) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

