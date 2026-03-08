---
title: RotationalSpeed

date: 2026-03-08T08:02:58.745688
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed` |
| Description: | Rotational speed for the specified axle, positive sign for rotation in forward direction, negative sign for rotation in backward direction. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->MotionManagement

    MotionManagement-->ElectricAxle

    ElectricAxle-->Row2

    Row2-->RotationalSpeed

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed
[get]  OK
Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `int16` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `rpm` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | revolutions per minute | |
| Description | Rotational speed measured in revolutions per minute | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | rotational-speed | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |




**Note:** The `int16` datatype is a *signed 16-bit integer* which technically allows values between -32768 and 32767 (inclusive).










## Signal Information





The vehicle signal `Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed` is a **Sensor**.

The vehicle signal `Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed` is `8814e9975dc65f9882752f39cc86260b`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.MotionManagement.ElectricAxle.Row2.RotationalSpeed) |
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
