---
title: Left

date: 2023-06-05T12:38:44.983746
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Mirrors.Left` |
| Description: | All mirrors. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Mirrors

    Mirrors-->Left

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Mirrors.Left](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Mirrors.Left/) |


## Signal Information




The vehicle signal `Vehicle.Body.Mirrors.Left` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Mirrors.Left` is `22609e45a09d58fc85cb77959a686abc`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.Mirrors.Left.IsHeatingOn](isheatingon/) (Mirror Heater on or off. True = Heater On. False = Heater Off.)
- [Vehicle.Body.Mirrors.Left.Pan](pan/) (Mirror pan as a percent. 0 = Center Position. 100 = Fully Left Position. -100 = Fully Right Position.)
- [Vehicle.Body.Mirrors.Left.Tilt](tilt/) (Mirror tilt as a percent. 0 = Center Position. 100 = Fully Upward Position. -100 = Fully Downward Position.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Mirrors.Left) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

