---
title: Cabin

date: 2023-06-05T12:38:45.309376
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin` |
| Description: | All in-cabin components, including doors. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin/) |


## Signal Information




The vehicle signal `Vehicle.Cabin` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin` is `1a94457b237f5e8eb3c77c0532ac88d7`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Convertible](convertible/) (Convertible roof.)
- [Vehicle.Cabin.Door](door/) (All doors, including windows and switches.)
- [Vehicle.Cabin.DoorCount](doorcount/) (Number of doors in vehicle.)
- [Vehicle.Cabin.DriverPosition](driverposition/) (The position of the driver seat in row 1.)
- [Vehicle.Cabin.HVAC](hvac/) (Climate control)
- [Vehicle.Cabin.Infotainment](infotainment/) (Infotainment system.)
- [Vehicle.Cabin.Lights](lights/) (Interior lights signals and sensors.)
- [Vehicle.Cabin.PowerOptimizeLevel](poweroptimizelevel/) (Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.)
- [Vehicle.Cabin.RearShade](rearshade/) (Rear window shade.)
- [Vehicle.Cabin.RearviewMirror](rearviewmirror/) (Rearview mirror.)
- [Vehicle.Cabin.Seat](seat/) (All seats.)
- [Vehicle.Cabin.SeatPosCount](seatposcount/) (Number of seats across each row from the front to the rear.)
- [Vehicle.Cabin.SeatRowCount](seatrowcount/) (Number of seat rows in vehicle.)
- [Vehicle.Cabin.Sunroof](sunroof/) (Sun roof status.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

