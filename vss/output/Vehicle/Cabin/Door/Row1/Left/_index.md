---
title: Left

date: 2023-06-05T12:38:49.034379
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Door.Row1.Left` |
| Description: | All doors, including windows and switches. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Door

    Door-->Row1

    Row1-->Left

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Door.Row1.Left](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Door.Row1.Left/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Door.Row1.Left` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Door.Row1.Left` is `ee74ca8275485ea89f70931d3b3e4bed`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Door.Row1.Left.IsChildLockActive](ischildlockactive/) (Is door child lock engaged. True = Engaged. False = Disengaged.)
- [Vehicle.Cabin.Door.Row1.Left.IsLocked](islocked/) (Is door locked or unlocked. True = Locked. False = Unlocked.)
- [Vehicle.Cabin.Door.Row1.Left.IsOpen](isopen/) (Is door open or closed)
- [Vehicle.Cabin.Door.Row1.Left.Shade](shade/) (Side window shade)
- [Vehicle.Cabin.Door.Row1.Left.Window](window/) (Door window status)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Door.Row1.Left) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

