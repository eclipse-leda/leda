## /********************************************************************************
## * Copyright (c) 2023 Contributors to the Eclipse Foundation
## *
## * See the NOTICE file(s) distributed with this work for additional
## * information regarding copyright ownership.
## *
## * This program and the accompanying materials are made available under the
## * terms of the Apache License 2.0 which is available at
## * https://www.apache.org/licenses/LICENSE-2.0
## *
## * SPDX-License-Identifier: Apache-2.0
## ********************************************************************************/
---
title: ${node.name}
<%
from datetime import datetime
today = datetime.now()
iso_date = today.isoformat()
%>
date: ${iso_date}
no_list: true
---

${'#'} Description

> ${node.description}

% if node.comment != "":
_Comment: ${node.comment}_
% endif

${'##'} Navigation

```mermaid
flowchart LR
<%
alist = node.qualified_name().split(".")
%>
% if len(alist)==1:
    ${alist[0]}
% endif
% if len(alist)>1:
<%
    curr = alist[0]
    nxt = alist[1]
%>
% for nxt in alist[0:]:
% if curr != nxt:
    ${curr}-->${nxt}
% endif
<%
curr = nxt
%>
% endfor
% endif
```

% if node.is_attribute():
${'##'} Eclipse Leda: Usage Example

In [Eclipse Kuksa.VAL Databroker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) CLI:

<%
example_value="0"
if node.data_type_str=="boolean":
    example_value="false"
if node.data_type_str=="string":
    example_value="Foo"
if node.default != "":
    example_value=node.default
%>

```bash
$ databroker-cli
sdv.databroker.v1 > connect
[connect] OK
sdv.databroker.v1 > get ${node.qualified_name()}
[get]  OK
${node.qualified_name()}: ( NotAvailable )
sdv.databroker.v1 > set ${node.qualified_name()} ${example_value}
[set]  OK
```
% endif

${'##'} Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [${node.qualified_name()}](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/${node.qualified_name()}/) |

% if node.data_type_str != "":
${'##'} Data Type & Unit

| | | |
|---|---|---|
| Path | `${node.qualified_name()}` | [VSS: Addressing nodes](https://covesa.github.io/vehicle_signal_specification/rule_set/basics/) |
| Data type | `${node.data_type_str}` | [VSS: Datatypes](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_types/) |
% if node.has_unit():
| Unit | `${node.get_unit()}` | [VSS: Units](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
| Label | ${unit.label} | |
| Description | ${unit.description} | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
| Domain | ${unit.domain} | [](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/data_unit_types/) |
% endif
% if node.min != "":
| Minimum value | `${node.min}` | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
% endif
% if node.max != "":
| Maximum value | `${node.max}` | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
% endif
% if node.default != "":
| Default value | `${node.default}` | [VSS: Sensors & Actuators](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/sensor_actuator/) |
% endif
% if node.allowed != "":
| Allowed values | `${node.allowed}` | [VSS: Specifying allowed values](https://covesa.github.io/vehicle_signal_specification/rule_set/data_entry/allowed/) |
% endif

% if node.data_type_str == "uint8":
**Note:** The `uint8` datatype is an *unsigned 8-bit integer* which technically allows values between 0 and 255 (inclusive).
% endif

% if node.data_type_str == "int8":
**Note:** The `int8` datatype is a *signed 8-bit integer* which technically allows values between -128 and 127 (inclusive).
% endif

% if node.data_type_str == "uint16":
**Note:** The `uint16` datatype is an *unsigned 16-bit integer* which technically allows values between 0 and 65535 (inclusive).
% endif

% if node.data_type_str == "int16":
**Note:** The `int16` datatype is a *signed 16-bit integer* which technically allows values between -32768 and 32767 (inclusive).
% endif

% if node.data_type_str == "uint32":
**Note:** The `uint32` datatype is an *unsigned 32-bit integer* which technically allows values between 0 and 4294967295 (inclusive).
% endif

% if node.data_type_str == "int32":
**Note:** The `int32` datatype is a *signed 32-bit integer* which technically allows values between -2147483648 and 2147483647 (inclusive).
% endif

% if node.data_type_str == "uint64":
**Note:** The `uint64` datatype is an *unsigned 64-bit integer* which technically allows values between 0 and 2^64 - 1 (inclusive).
% endif

% if node.data_type_str == "int64":
**Note:** The `int64` datatype is a *signed 64-bit integer* which technically allows values between -2^63 and 2^63 - 1 (inclusive).
% endif

% if node.data_type_str == "boolean":
**Note:** The `boolean` datatype is a *boolean value* which technically allows values of either 0 and false; or 1 and true.
% endif

% if node.data_type_str == "float":
**Note:** The `float` datatype is a *floating point number* which technically allows values between -3.4e ^ -38 and 3.4e ^ 38
% endif

% if node.data_type_str == "double":
**Note:** The `double` datatype is a *double precision floating point number* which technically allows values between -1.7e ^ -300 and 1.7e ^ 300
% endif

% if node.data_type_str == "string":
**Note:** The `string` datatype is a *character string*.
% endif

% endif

${'##'} Signal Information

% if node.deprecation != "":
> Deprecation Warning: ${node.deprecation}
% endif

% if node.is_actuator():
The vehicle signal `${node.qualified_name()}` is an **Actuator**.
% endif

% if node.is_property():
The vehicle signal `${node.qualified_name()}` is a **Property**.
% endif

% if node.is_attribute():
The vehicle signal `${node.qualified_name()}` is an **Attribute**.
% endif

% if node.is_branch():
The vehicle signal `${node.qualified_name()}` is a **Branch**.
% endif

% if node.is_sensor():
The vehicle signal `${node.qualified_name()}` is a **Sensor**.
% endif

% if node.is_signal():
The vehicle signal `${node.qualified_name()}` is a **Signal**.
% endif

% if node.is_struct():
The vehicle signal `${node.qualified_name()}` is a **Struct**.
% endif

% if node.is_orphan():
The vehicle signal `${node.qualified_name()}` is an **Orphan**.
% endif

% if node.uuid != "":
${'##'} UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `${node.qualified_name()}` is `${node.uuid}`
% endif

% if node.is_branch() or node.is_struct():
${'##'} Children

This vehicle signal is a branch or structure and thus has sub-pages:

% for child in sorted(node.children,key=lambda t:t.qualified_name()):
- [${child.qualified_name()}](${child.name.lower()}/) (${child.description})
% endfor

% endif

${'##'} About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

% if node.data_type_str != "":
${'##'} VSS: Supported datatypes

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
%endif
