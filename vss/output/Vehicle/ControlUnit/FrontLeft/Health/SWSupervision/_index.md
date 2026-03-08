---
title: SWSupervision

date: 2026-03-08T08:03:00.190740
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.ControlUnit.FrontLeft.Health.SWSupervision` |
| Description: | SW supervision attributes and signals |

## Navigation

```mermaid
flowchart LR



    Vehicle-->ControlUnit

    ControlUnit-->FrontLeft

    FrontLeft-->Health

    Health-->SWSupervision

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.ControlUnit.FrontLeft.Health.SWSupervision](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.ControlUnit.FrontLeft.Health.SWSupervision/) |


## Signal Information




The vehicle signal `Vehicle.ControlUnit.FrontLeft.Health.SWSupervision` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.ControlUnit.FrontLeft.Health.SWSupervision` is `37e2f04eef7255deb8e6d748142942a5`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.ControlUnit.FrontLeft.Health.SWSupervision.IsAliveTriggered](isalivetriggered/) (Whether the alive supervision was triggered)
- [Vehicle.ControlUnit.FrontLeft.Health.SWSupervision.IsDeadlineTriggered](isdeadlinetriggered/) (Whether the deadline supervision was triggered)
- [Vehicle.ControlUnit.FrontLeft.Health.SWSupervision.IsLogicalTriggered](islogicaltriggered/) (Whether the logical supervision was triggered)
- [Vehicle.ControlUnit.FrontLeft.Health.SWSupervision.IsWatchdogTriggered](iswatchdogtriggered/) (Whether the watchdog deadline was triggered)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.ControlUnit.FrontLeft.Health.SWSupervision) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

