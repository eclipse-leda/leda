---
title: Light

date: 2026-03-08T08:02:50.198845
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Light` |
| Description: | Light that is part of the Cabin. |
| Comment: | V4.0 branch renamed from "Lights" to "Light" to comply with singular naming of entities. Use SingleConfigurableLight.vspec to describe interior lights that can be configured. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Light

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Light](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Light/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Light` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Light` is `2fc2ad48d5315cc4aa1e4638a6985585`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Light.AmbientLight](ambientlight/) (Decorative coloured light inside the cabin, usually mounted on the door, ceiling, etc.)
- [Vehicle.Cabin.Light.InteractiveLightBar](interactivelightbar/) (Decorative coloured light bar that supports effects, usually mounted on the dashboard (e.g. BMW i7 Interactive bar).)
- [Vehicle.Cabin.Light.IsDomeOn](isdomeon/) (Is central dome light on)
- [Vehicle.Cabin.Light.IsGloveBoxOn](isgloveboxon/) (Is glove box light on)
- [Vehicle.Cabin.Light.PerceivedAmbientLight](perceivedambientlight/) (The percentage of ambient light that is measured (e.g., by a sensor) inside the cabin. 0 = No ambient light. 100 = Full brightness.)
- [Vehicle.Cabin.Light.Spotlight](spotlight/) (Spotlight for a specific area in the vehicle.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Light) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

