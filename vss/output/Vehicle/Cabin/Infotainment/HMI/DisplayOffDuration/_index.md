---
title: DisplayOffDuration

date: 2026-03-08T08:02:50.004470
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration` |
| Description: | Duration in seconds before the display is turned off. Value shall be 0 if screen never shall turn off. |
| Comment: | Display shall be turned off at HMI.LastActionTime + HMI.DisplayOffDuration, unless HMI.IsScreenAlwaysOn==True. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Cabin

    Cabin-->Infotainment

    Infotainment-->HMI

    HMI-->DisplayOffDuration

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration
[get]  OK
Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `uint16` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `s` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | second | |
| Description | Duration measured in seconds | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | duration | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |



**Note:** The `uint16` datatype is an *unsigned 16-bit integer* which technically allows values between 0 and 65535 (inclusive).











## Signal Information

The vehicle signal `Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration` is an **Actuator**.





The vehicle signal `Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration` is `130114ebf81f59718cf257e198b90e01`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Cabin.Infotainment.HMI.DisplayOffDuration) |
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
