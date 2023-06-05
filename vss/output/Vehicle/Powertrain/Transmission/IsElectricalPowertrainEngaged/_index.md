---
title: IsElectricalPowertrainEngaged

date: 2023-06-05T12:38:38.490177
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged` |
| Description: | Is electrical powertrain mechanically connected/engaged to the drivetrain or not. False = Disconnected/Disengaged. True = Connected/Engaged. |
| Comment: | In some hybrid solutions it is possible to disconnect/disengage the electrical powertrain mechanically to avoid induced voltage reaching a too high level when driving at high speed. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->Transmission

    Transmission-->IsElectricalPowertrainEngaged

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged
[get]  OK
Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged false
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `boolean` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |









**Note:** The `boolean` datatype is a *boolean value* which technically allows values of either 0 and false; or 1 and true.





## Signal Information

The vehicle signal `Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged` is an **Actuator**.





The vehicle signal `Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged` is `6660cf1d88d15430b1e7c8908a7b769b`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.Transmission.IsElectricalPowertrainEngaged) |
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
