---
title: Safety

date: 2026-10-12T19:51:31.225857
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Safety` |
| Description: | Safety-related derived signals for crash detection and emergency response. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Safety

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Safety](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Safety/) |


## Signal Information




The vehicle signal `Vehicle.Safety` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Safety.IsFire](isfire/) (Indicates whether a fire has been detected in or on the vehicle.)
- [Vehicle.Safety.IsSubmersed](issubmersed/) (Indicates whether the vehicle is partially or fully submersed in water.)
- [Vehicle.Safety.RoadIcingState](roadicingstate/) (Indicates whether the vehicle is currently at risk of icing-related loss of control or has detected such conditions affecting traction.)
- [Vehicle.Safety.Rollover](rollover/) (Indicates whether the vehicle has rolled over or is at risk of rollover.)
- [Vehicle.Safety.VisibilityImpairment](visibilityimpairment/) (Indicates whether reduced exterior visibility is currently creating a driving-safety risk, or such a condition has been detected.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Safety) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

