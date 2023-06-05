---
title: MountingPosition

date: 2023-06-05T12:38:36.440827
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.CurrentLocation.GNSSReceiver.MountingPosition` |
| Description: | Mounting position of GNSS receiver antenna relative to vehicle coordinate system. Axis definitions according to ISO 8855. Origin at center of (first) rear axle. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->CurrentLocation

    CurrentLocation-->GNSSReceiver

    GNSSReceiver-->MountingPosition

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.CurrentLocation.GNSSReceiver.MountingPosition](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.CurrentLocation.GNSSReceiver.MountingPosition/) |


## Signal Information




The vehicle signal `Vehicle.CurrentLocation.GNSSReceiver.MountingPosition` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.CurrentLocation.GNSSReceiver.MountingPosition` is `5c0887bce6fb5eb79402baaccb203e61`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.CurrentLocation.GNSSReceiver.MountingPosition.X](x/) (Mounting position of GNSS receiver antenna relative to vehicle coordinate system. Axis definitions according to ISO 8855. Origin at center of (first) rear axle. Positive values = forward of rear axle. Negative values = backward of rear axle.)
- [Vehicle.CurrentLocation.GNSSReceiver.MountingPosition.Y](y/) (Mounting position of GNSS receiver antenna relative to vehicle coordinate system. Axis definitions according to ISO 8855. Origin at center of (first) rear axle. Positive values = left of origin. Negative values = right of origin. Left/Right is as seen from driver perspective, i.e. by a person looking forward.)
- [Vehicle.CurrentLocation.GNSSReceiver.MountingPosition.Z](z/) (Mounting position of GNSS receiver on Z-axis. Axis definitions according to ISO 8855. Origin at center of (first) rear axle. Positive values = above center of rear axle. Negative values = below center of rear axle.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.CurrentLocation.GNSSReceiver.MountingPosition) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

