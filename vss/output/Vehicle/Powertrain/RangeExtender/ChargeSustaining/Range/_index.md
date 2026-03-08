---
title: Range

date: 2026-03-08T08:02:47.754113
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range` |
| Description: | Estimated remaining distance that can be traveled in Charge Sustaining mode using available fuel. |
| Comment: | This range estimate is calculated based on the current fuel level and recent fuel consumption patterns in CS mode. It represents the extended range capability provided by the internal combustion engine. The total vehicle range is the sum of CD mode range and CS mode range. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->RangeExtender

    RangeExtender-->ChargeSustaining

    ChargeSustaining-->Range

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range
[get]  OK
Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `uint32` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `m` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | meter | |
| Description | Length measured in meters | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | length | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |





**Note:** The `uint32` datatype is an *unsigned 32-bit integer* which technically allows values between 0 and 4294967295 (inclusive).









## Signal Information





The vehicle signal `Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range` is a **Sensor**.

The vehicle signal `Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range` is `cb5d446b2cf25fc795e490be0ef4c35c`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.RangeExtender.ChargeSustaining.Range) |
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
