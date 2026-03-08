---
title: PassengerSide

date: 2026-03-08T08:02:48.979689
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Mirrors.PassengerSide` |
| Description: | All mirrors. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Mirrors

    Mirrors-->PassengerSide

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Mirrors.PassengerSide](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Mirrors.PassengerSide/) |


## Signal Information




The vehicle signal `Vehicle.Body.Mirrors.PassengerSide` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Mirrors.PassengerSide` is `8025a1e06e9d5ddb96405cce1f1f38cb`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.Mirrors.PassengerSide.IsFolded](isfolded/) (Is mirror folded? True = Fully or partially folded. False = Fully unfolded.)
- [Vehicle.Body.Mirrors.PassengerSide.IsHeatingOn](isheatingon/) (Mirror Heater on or off. True = Heater On. False = Heater Off.)
- [Vehicle.Body.Mirrors.PassengerSide.IsLocked](islocked/) (Is mirror movement locked? True = Locked, mirror will not react to Tilt/Pan change. False = Unlocked.)
- [Vehicle.Body.Mirrors.PassengerSide.Pan](pan/) (Mirror pan as a percent. 0 = Center Position. 100 = Fully Left Position. -100 = Fully Right Position.)
- [Vehicle.Body.Mirrors.PassengerSide.Tilt](tilt/) (Mirror tilt as a percent. 0 = Center Position. 100 = Fully Upward Position. -100 = Fully Downward Position.)
- [Vehicle.Body.Mirrors.PassengerSide.Yaw](yaw/) (Relative mirror yaw angle, measured from the vehicle sprung mass X-axis as defined by ISO 23150:2023 to the mirror X-axis, around the vehicle Z-axis (right-hand rule). 0 = Mirror in default position. Exact position (yaw relative to vehicle X-axis) is vehicle dependent. 100 = Maximum yaw. Mirror rotated clockwise as much as possible around Z-axis. -100 = Minimum yaw. Mirror rotated counter-clockwise as much as possible around Z-axis.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Mirrors.PassengerSide) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

