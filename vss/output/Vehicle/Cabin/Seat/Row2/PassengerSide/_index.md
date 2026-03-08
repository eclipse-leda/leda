---
title: PassengerSide

date: 2026-03-08T08:02:54.800095
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Seat.Row2.PassengerSide` |
| Description: | All seats. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Seat

    Seat-->Row2

    Row2-->PassengerSide

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Seat.Row2.PassengerSide](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Seat.Row2.PassengerSide/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Seat.Row2.PassengerSide` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Seat.Row2.PassengerSide` is `8cd32cb3e2d157b39af57d9cfe2e128c`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Seat.Row2.PassengerSide.Airbag](airbag/) (Airbag signals.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Backrest](backrest/) (Describes signals related to the backrest of the seat.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Headrest](headrest/) (Headrest settings.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.HeatingCooling](heatingcooling/) (Heating or Cooling requsted for the Item. -100 = Maximum cooling, 0 = Heating/cooling deactivated, 100 = Maximum heating.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Height](height/) (Seat position on vehicle z-axis. Position is relative within available movable range of the seating. 0 = Lowermost position supported.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsBackwardSwitchEngaged](isbackwardswitchengaged/) (Seat backward switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsBelted](isbelted/) (Is the belt engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsCoolerSwitchEngaged](iscoolerswitchengaged/) (Cooler switch for Seat heater.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsDecreaseMassageLevelSwitchEngaged](isdecreasemassagelevelswitchengaged/) (Decrease massage level switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsDownSwitchEngaged](isdownswitchengaged/) (Seat down switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsForwardSwitchEngaged](isforwardswitchengaged/) (Seat forward switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsIncreaseMassageLevelSwitchEngaged](isincreasemassagelevelswitchengaged/) (Increase massage level switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsTiltBackwardSwitchEngaged](istiltbackwardswitchengaged/) (Tilt backward switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsTiltForwardSwitchEngaged](istiltforwardswitchengaged/) (Tilt forward switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsUpSwitchEngaged](isupswitchengaged/) (Seat up switch engaged.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.IsWarmerSwitchEngaged](iswarmerswitchengaged/) (Warmer switch for Seat heater.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Massage](massage/) (Massage related information for the seat.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.NeckScarf](neckscarf/) (NeckScarf settings.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.OccupancyStatus](occupancystatus/) (Occupancy status of the seat.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Position](position/) (Seat position on vehicle x-axis. Position is relative to the frontmost position supported by the seat. 0 = Frontmost position supported.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.SeatBeltHeight](seatbeltheight/) (Seat belt position on vehicle z-axis. Position is relative within available movable range of the seat belt. 0 = Lowermost position supported.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Seating](seating/) (Describes signals related to the seat bottom of the seat.)
- [Vehicle.Cabin.Seat.Row2.PassengerSide.Tilt](tilt/) (Tilting of seat (seating and backrest) relative to vehicle x-axis. 0 = seat bottom is flat, seat bottom and vehicle x-axis are parallel. Positive degrees = seat tilted backwards, seat x-axis tilted upward, seat z-axis is tilted backward.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Seat.Row2.PassengerSide) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

