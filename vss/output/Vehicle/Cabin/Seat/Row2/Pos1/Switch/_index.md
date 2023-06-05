---
title: Switch

date: 2023-06-05T12:38:56.816319
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Seat.Row2.Pos1.Switch` |
| Description: | Seat switch signals |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Seat

    Seat-->Row2

    Row2-->Pos1

    Pos1-->Switch

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Seat.Row2.Pos1.Switch](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Seat.Row2.Pos1.Switch/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Seat.Row2.Pos1.Switch` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Seat.Row2.Pos1.Switch` is `1c4b708222de55aabddb3697308253ee`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.Backrest](backrest/) (Describes switches related to the backrest of the seat.)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.Headrest](headrest/) (Switches for SingleSeat.Headrest.)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsBackwardEngaged](isbackwardengaged/) (Seat backward switch engaged (SingleSeat.Position).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsCoolerEngaged](iscoolerengaged/) (Cooler switch for Seat heater (SingleSeat.Heating).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsDownEngaged](isdownengaged/) (Seat down switch engaged (SingleSeat.Height).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsForwardEngaged](isforwardengaged/) (Seat forward switch engaged (SingleSeat.Position).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsTiltBackwardEngaged](istiltbackwardengaged/) (Tilt backward switch engaged (SingleSeat.Tilt).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsTiltForwardEngaged](istiltforwardengaged/) (Tilt forward switch engaged (SingleSeat.Tilt).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsUpEngaged](isupengaged/) (Seat up switch engaged (SingleSeat.Height).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.IsWarmerEngaged](iswarmerengaged/) (Warmer switch for Seat heater (SingleSeat.Heating).)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.Massage](massage/) (Switches for SingleSeat.Massage.)
- [Vehicle.Cabin.Seat.Row2.Pos1.Switch.Seating](seating/) (Describes switches related to the seating of the seat.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Seat.Row2.Pos1.Switch) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

