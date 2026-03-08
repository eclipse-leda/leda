---
title: RearShade

date: 2026-03-08T08:02:49.091297
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.RearShade` |
| Description: | Rear window shade. Open = Retracted, Closed = Deployed. Start position for RearShade is Open/Retracted. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->RearShade

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.RearShade](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.RearShade/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.RearShade` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.RearShade` is `8a0c86f4fc6f5ea8ac8cf8f327969dcc`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.RearShade.IsOpen](isopen/) (Is item open or closed? True = Fully or partially open. False = Fully closed.)
- [Vehicle.Cabin.RearShade.Position](position/) (Item position. 0 = Start position 100 = End position.)
- [Vehicle.Cabin.RearShade.Switch](switch/) (Switch controlling sliding action such as window, sunroof, or blind.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.RearShade) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

