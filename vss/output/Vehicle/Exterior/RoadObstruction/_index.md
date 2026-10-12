---
title: RoadObstruction

date: 2026-10-12T19:51:33.105693
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Exterior.RoadObstruction` |
| Description: | Type of road obstruction detected ahead of the vehicle. |
| Comment: | Reports the category of road obstruction detected by the vehicle's perception systems. UNKNOWN (0) shall be used when obstruction type cannot be classified. NONE (9) indicates no obstruction detected. SHED_LOAD (4) covers cargo fallen from another vehicle. LAND_SLIP (5) or landslide is ground material that has slid down slope into road. ANIMAL (6) covers small animals (cat, dog); ANIMAL_LARGE (7) covers large animals (deer, horse, livestock); ANIMAL_HERD (8) covers groups of animals on road. FLOODING (10) indicates standing water sufficient to obstruct passage (distinct from WET surface state in Vehicle.Exterior.RoadSurfaceCondition). Values 1-8 are aligned with SENSORIS v1.6 RoadObstructionCondition.TypeAndConfidence and TPEG-TEC road obstruction taxonomy. Determination method is implementation specific (camera, radar, lidar). Primary consumers: navigation systems (dynamic re-routing), ADAS safety systems, and emergency dispatch systems.
 |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Exterior

    Exterior-->RoadObstruction

```

## Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:



```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get Vehicle.Exterior.RoadObstruction
[get]  OK
Vehicle.Exterior.RoadObstruction: ( NotAvailable )
sdv.databroker.v1 > set Vehicle.Exterior.RoadObstruction 0
[set]  OK
```

## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Exterior.RoadObstruction](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Exterior.RoadObstruction/) |

## Data Type & Unit

| | | |
|---|---|---|
| Path | `Vehicle.Exterior.RoadObstruction` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `uint8` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |

**Note:** The `uint8` datatype is an *unsigned 8-bit integer* which technically allows values between 0 and 255 (inclusive).













## Signal Information





The vehicle signal `Vehicle.Exterior.RoadObstruction` is a **Sensor**.

The vehicle signal `Vehicle.Exterior.RoadObstruction` is a **Signal**.





## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Exterior.RoadObstruction) |
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
