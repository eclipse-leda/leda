---
title: Played

date: 2026-10-12T19:51:25.823917
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Infotainment.Media.Played` |
| Description: | Collection of signals updated in concert when a new media is played |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Infotainment

    Infotainment-->Media

    Media-->Played

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Infotainment.Media.Played](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Infotainment.Media.Played/) |


## Signal Information




The vehicle signal `Vehicle.Cabin.Infotainment.Media.Played` is a **Branch**.






## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Cabin.Infotainment.Media.Played.Album](album/) (Name of album being played)
- [Vehicle.Cabin.Infotainment.Media.Played.Artist](artist/) (Name of artist being played)
- [Vehicle.Cabin.Infotainment.Media.Played.Genre](genre/) (Name of genre being played)
- [Vehicle.Cabin.Infotainment.Media.Played.PlaybackRate](playbackrate/) (Current playback rate of media being played.)
- [Vehicle.Cabin.Infotainment.Media.Played.Source](source/) (Media selected for playback)
- [Vehicle.Cabin.Infotainment.Media.Played.Track](track/) (Name of track being played)
- [Vehicle.Cabin.Infotainment.Media.Played.URI](uri/) (User Resource associated with the media)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Infotainment.Media.Played) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

