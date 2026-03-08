---
title: FuelEconomy

date: 2026-03-08T08:02:47.743738
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy` |
| Description: | Current fuel economy during Charge Sustaining mode operation. |
| Comment: | This value represents the fuel efficiency when the engine is operating as a generator to maintain battery charge. It differs from conventional vehicle fuel economy because the engine is optimized to run at efficient generator speeds rather than varying speeds for direct wheel propulsion. The actual fuel economy in CS mode may be different from the vehicle's rated CS mode fuel economy depending on driving conditions and power demands. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->RangeExtender

    RangeExtender-->ChargeSustaining

    ChargeSustaining-->FuelEconomy

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy
[get]  OK
Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `float` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
| Unit | `km/l` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | kilometers per liter | |
| Description | Distance per volume measured in kilometers per liter | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | distance-per-volume | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |










**Note:** The `float` datatype is a *floating point number* which technically allows values between -3.4e ^ -38 and 3.4e ^ 38




## Signal Information





The vehicle signal `Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy` is a **Sensor**.

The vehicle signal `Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy` is `b1cca487316a507faf2dbc371ca295ff`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.RangeExtender.ChargeSustaining.FuelEconomy) |
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
