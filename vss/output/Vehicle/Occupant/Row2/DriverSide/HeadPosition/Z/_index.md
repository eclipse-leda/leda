---
title: Z

date: 2026-03-08T08:02:58.042954
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z` |
| Description: | Height position of head center measured as mid eye position on X-axis of the vehicle rear-axle coordinate system as defined by ISO 23150:2023 section 3.7.12 Mid eye position refers to the center of a line drawn between the center of the drivers eyes. Positive values = above center of rear-axle reference point. Negative values = below center of rear-axle reference point. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Occupant

    Occupant-->Row2

    Row2-->DriverSide

    DriverSide-->HeadPosition

    HeadPosition-->Z

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z
[get]  OK
Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `int16` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `mm` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | millimeter | |
| Description | Length measured in millimeters | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | length | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |




**Note:** The `int16` datatype is a *signed 16-bit integer* which technically allows values between -32768 and 32767 (inclusive).










## Signal Information





The vehicle signal `Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z` is a **Sensor**.

The vehicle signal `Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z` is `c403eb440e085247b7210930eaca7745`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Occupant.Row2.DriverSide.HeadPosition.Z) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

## Supported datatypes

The following is a list of VSS supported built-in datatypes:

Name       | Type                       | Min  | Max
:----------|:---------------------------|:-----|:---
uint8      | unsigned 8-bit integer     | 0    | 255
int8       | signed 8-bit integer       | -128 | 127
uint16     | unsigned 16-bit integer    |  0   | 65535
int16      | signed 16-bit integer      | -32768 | 32767
uint32     | unsigned 32-bit integer    | 0 | 4294967295
int32      | signed 32-bit integer      | -2147483648 | 2147483647
uint64     | unsigned 64-bit integer    | 0    | 2^64 - 1
int64      | signed 64-bit integer      | -2^63 | 2^63 - 1
boolean    | boolean value              | 0/false | 1/true
float      | floating point number      | -3.4e -38 | 3.4e 38
double     | double precision floating point number | -1.7e -300 | 1.7e 300
string     | character string           | n/a  | n/a

> Min, max and default values defined in a Vehicle Signal Specification must be in the supported range of the data type.
