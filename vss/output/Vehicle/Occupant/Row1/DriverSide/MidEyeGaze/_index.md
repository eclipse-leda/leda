---
title: MidEyeGaze

date: 2026-03-08T08:02:57.644462
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Occupant.Row1.DriverSide.MidEyeGaze` |
| Description: | Direction from mid eye position to object driver is looking at. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Occupant

    Occupant-->Row1

    Row1-->DriverSide

    DriverSide-->MidEyeGaze

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Occupant.Row1.DriverSide.MidEyeGaze](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Occupant.Row1.DriverSide.MidEyeGaze/) |


## Signal Information




The vehicle signal `Vehicle.Occupant.Row1.DriverSide.MidEyeGaze` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Occupant.Row1.DriverSide.MidEyeGaze` is `4e6869d72ecf51f2a63b744118db723e`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Occupant.Row1.DriverSide.MidEyeGaze.Azimuth](azimuth/) (Mid eye azimuth gaze (right-hand rule) on vehicle sprung mass Z-axis as defined by ISO 23150:2023 0 = Driver looking forward. Positive values = Driver looking at something on the left side of driver. Negative values = Driver looking at something on the right side of driver.)
- [Vehicle.Occupant.Row1.DriverSide.MidEyeGaze.Elevation](elevation/) (Elevation to observed object measured as angle between vehicle sprung mass XY-plane as defined by ISO 23150:2023 at driver mid eye position and object. 0 = Driver looking at something at same height as mid eye position. Positive values = Driver looking at something above mid eye position. Negative values = Driver looking at something below mid eye position.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Occupant.Row1.DriverSide.MidEyeGaze) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

