---
title: OilLifeRemaining

date: 2023-06-05T12:38:37.300375
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.CombustionEngine.OilLifeRemaining` |
| Description: | Remaining engine oil life in seconds. Negative values can be used to indicate that lifetime has been exceeded. |
| Comment: | In addition to this a signal a vehicle can report remaining time to service (including e.g. oil change) by Vehicle.Service.TimeToService. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->CombustionEngine

    CombustionEngine-->OilLifeRemaining

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Powertrain.CombustionEngine.OilLifeRemaining
[get]  OK
Vehicle.Powertrain.CombustionEngine.OilLifeRemaining: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Powertrain.CombustionEngine.OilLifeRemaining 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.CombustionEngine.OilLifeRemaining](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.CombustionEngine.OilLifeRemaining/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Powertrain.CombustionEngine.OilLifeRemaining` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `int32` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `s` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | second | |
| Description | Time measured in seconds | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | time | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |






**Note:** The `int32` datatype is a *signed 32-bit integer* which technically allows values between -2147483648 and 2147483647 (inclusive).








## Signal Information





The vehicle signal `Vehicle.Powertrain.CombustionEngine.OilLifeRemaining` is a **Sensor**.

The vehicle signal `Vehicle.Powertrain.CombustionEngine.OilLifeRemaining` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.CombustionEngine.OilLifeRemaining` is `94303734c68c5353a02625f652103918`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.CombustionEngine.OilLifeRemaining) |
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
