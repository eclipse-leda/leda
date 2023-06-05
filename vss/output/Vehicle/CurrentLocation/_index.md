---
title: CurrentLocation

date: 2023-06-05T12:38:36.107259
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.CurrentLocation` |
| Description: | The current latitude and longitude of the vehicle. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->CurrentLocation

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.CurrentLocation](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.CurrentLocation/) |


## Signal Information




The vehicle signal `Vehicle.CurrentLocation` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.CurrentLocation` is `24777bd485f15fb69550ae0520c40ad5`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.CurrentLocation.Altitude](altitude/) (Current altitude relative to WGS 84 reference ellipsoid, as measured at the position of GNSS receiver antenna.)
- [Vehicle.CurrentLocation.GNSSReceiver](gnssreceiver/) (Information on the GNSS receiver used for determining current location.)
- [Vehicle.CurrentLocation.Heading](heading/) (Current heading relative to geographic north. 0 = North, 90 = East, 180 = South, 270 = West.)
- [Vehicle.CurrentLocation.HorizontalAccuracy](horizontalaccuracy/) (Accuracy of the latitude and longitude coordinates.)
- [Vehicle.CurrentLocation.Latitude](latitude/) (Current latitude of vehicle in WGS 84 geodetic coordinates, as measured at the position of GNSS receiver antenna.)
- [Vehicle.CurrentLocation.Longitude](longitude/) (Current longitude of vehicle in WGS 84 geodetic coordinates, as measured at the position of GNSS receiver antenna.)
- [Vehicle.CurrentLocation.Timestamp](timestamp/) (Timestamp from GNSS system for current location, formatted according to ISO 8601 with UTC time zone.)
- [Vehicle.CurrentLocation.VerticalAccuracy](verticalaccuracy/) (Accuracy of altitude.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.CurrentLocation) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

