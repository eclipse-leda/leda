---
title: Body

date: 2023-06-05T12:38:41.688156
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body` |
| Description: | All body components. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body/) |


## Signal Information




The vehicle signal `Vehicle.Body` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body` is `bd2854e6a9165c5698ce8dd9f0438ecc`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Body.BodyType](bodytype/) (Body type code as defined by ISO 3779.)
- [Vehicle.Body.Hood](hood/) (Hood status.)
- [Vehicle.Body.Horn](horn/) (Horn signals.)
- [Vehicle.Body.Lights](lights/) (Exterior lights.)
- [Vehicle.Body.Mirrors](mirrors/) (All mirrors.)
- [Vehicle.Body.PowerOptimizeLevel](poweroptimizelevel/) (Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.)
- [Vehicle.Body.Raindetection](raindetection/) (Rainsensor signals.)
- [Vehicle.Body.RearMainSpoilerPosition](rearmainspoilerposition/) (Rear spoiler position, 0% = Spoiler fully stowed. 100% = Spoiler fully exposed.)
- [Vehicle.Body.RefuelPosition](refuelposition/) (Location of the fuel cap or charge port.)
- [Vehicle.Body.Trunk](trunk/) (Trunk status.)
- [Vehicle.Body.Windshield](windshield/) (Windshield signals.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

