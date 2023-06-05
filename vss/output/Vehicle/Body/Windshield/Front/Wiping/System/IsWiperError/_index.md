---
title: IsWiperError

date: 2023-06-05T12:38:42.472806
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError` |
| Description: | Indicates system failure. True if wiping is disabled due to system failure. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Body

    Body-->Windshield

    Windshield-->Front

    Front-->Wiping

    Wiping-->System

    System-->IsWiperError

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError
[get]  OK
Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError false
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `boolean` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |









**Note:** The `boolean` datatype is a *boolean value* which technically allows values of either 0 and false; or 1 and true.





## Signal Information





The vehicle signal `Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError` is a **Sensor**.

The vehicle signal `Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError` is a **Signal**.



## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError` is `5276055d973f57998e1b8d6e536de735`


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Body.Windshield.Front.Wiping.System.IsWiperError) |
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
