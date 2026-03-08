---
title: Pitch

date: 2026-03-08T08:02:57.767394
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch` |
| Description: | Head pitch angle, measured as angle from vehicle sprung mass XY-plane as defined by ISO 23150:2023 to the head X-axis. 0 = Head in normal position. Positive values = Head leaning up. Negative values = Head leaning down. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Occupant

    Occupant-->Row1

    Row1-->Middle

    Middle-->HeadPosition

    HeadPosition-->Pitch

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch
[get]  OK
Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `float` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `degrees` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | degree | |
| Description | Angle measured in degrees | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | angle | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Minimum value | `-90` | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Maximum value | `90` | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |










**Note:** The `float` datatype is a *floating point number* which technically allows values between -3.4e ^ -38 and 3.4e ^ 38




## Signal Information





The vehicle signal `Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch` is a **Sensor**.

The vehicle signal `Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch` is `0ef41c4346265a92be1e974ddf347d89`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Occupant.Row1.Middle.HeadPosition.Pitch) |
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
