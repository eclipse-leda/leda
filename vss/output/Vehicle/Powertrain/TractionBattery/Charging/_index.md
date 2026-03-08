---
title: Charging

date: 2026-03-08T08:02:46.643733
no_list: true
---


| | |
|---|---|
| Full qualified VSS Path: | `Vehicle.Powertrain.TractionBattery.Charging` |
| Description: | Properties related to battery charging. |

## Navigation

```mermaid
flowchart LR



    Vehicle-->Powertrain

    Powertrain-->TractionBattery

    TractionBattery-->Charging

```


## Digital Auto: Playground

[playground.digital.auto](http://digital.auto) provides an in-browser, rapid prototyping environment utilizing the COVESA APIs for connected vehicles. 

| Vehicle Model | Direct link to Vehicle Signal |
|---|---|
| ACME Car (EV) v0.1 | [Vehicle.Powertrain.TractionBattery.Charging](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list/Vehicle.Powertrain.TractionBattery.Charging/) |


## Signal Information




The vehicle signal `Vehicle.Powertrain.TractionBattery.Charging` is a **Branch**.





## UUID

Each vehicle signal is identified by a [Universally Unique Identifier (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier))

The UUID for `Vehicle.Powertrain.TractionBattery.Charging` is `49b9ef0c8b145a36afdf17d0cb44131b`

## Children

This vehicle signal is a branch or structure and thus has sub-pages:

- [Vehicle.Powertrain.TractionBattery.Charging.AveragePower](averagepower/) (Average charging power of last or current charging event.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeCurrent](chargecurrent/) (Current charging current.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeLimit](chargelimit/) (Target charge limit (state of charge) for battery.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeRate](chargerate/) (Current charging rate, as in kilometers of range added per hour.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargeVoltage](chargevoltage/) (Current charging voltage, as measured at the charging inlet.)
- [Vehicle.Powertrain.TractionBattery.Charging.ChargingPort](chargingport/) (Properties related to a particular charging port available in the vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.EvseId](evseid/) (EVSE charging point ID (without separators) of last or current charging event according to ISO 15118-2 Annex H.)
- [Vehicle.Powertrain.TractionBattery.Charging.IsCharging](ischarging/) (True if charging is ongoing. Charging is considered to be ongoing if energy is flowing from charger to vehicle.)
- [Vehicle.Powertrain.TractionBattery.Charging.IsDischarging](isdischarging/) (True if discharging (vehicle to grid) is ongoing. Discharging is considered to be ongoing if energy is flowing from vehicle to charger/grid.)
- [Vehicle.Powertrain.TractionBattery.Charging.Location](location/) (Location of last or current charging event.)
- [Vehicle.Powertrain.TractionBattery.Charging.MaxPower](maxpower/) (Maximum charging power of last or current charging event.)
- [Vehicle.Powertrain.TractionBattery.Charging.MaximumChargingCurrent](maximumchargingcurrent/) (Maximum charging current that can be accepted by the system, as measured at the charging inlet.)
- [Vehicle.Powertrain.TractionBattery.Charging.PowerLoss](powerloss/) (Electrical energy lost by power dissipation to heat inside the AC/DC converter.)
- [Vehicle.Powertrain.TractionBattery.Charging.StartStopCharging](startstopcharging/) (Start or stop the charging process.)
- [Vehicle.Powertrain.TractionBattery.Charging.Temperature](temperature/) (Current temperature of AC/DC converter converting grid voltage to battery voltage.)
- [Vehicle.Powertrain.TractionBattery.Charging.TimeToComplete](timetocomplete/) (The time needed for the current charging process to reach Charging.ChargeLimit. 0 if charging is complete or no charging process is active or planned.)
- [Vehicle.Powertrain.TractionBattery.Charging.Timer](timer/) (Properties related to timing of battery charging sessions.)


## Feedback

Do you think this Vehicle Signal specification needs enhancement? Do you want to discuss with experts? Try the following ressources to get in touch with the VSS community:

| | |
|---|---|
| Enhancement request | [Create COVESA GitHub Issue](https://github.com/COVESA/vehicle_signal_specification/issues/new?body=Please+describe+your+feedback&title=Signal+feedback+Vehicle.Powertrain.TractionBattery.Charging) |
| Join COVESA | [www.covesa.global](https://www.covesa.global/join?src=sidebar) |
| Discuss VSS on Slack | [w3cauto.slack.com](http://w3cauto.slack.com/) |
| VSS Data Experts on Google Groups | [covesa.global data-expert-group](https://groups.google.com/a/covesa.global/g/data-expert-group) |

## About VSS

The [Vehicle Signal Specification](https://covesa.github.io/vehicle_signal_specification/) (VSS)
is an initiative by COVESA to define a syntax and a catalog for vehicle signals.
The source code and releases can be found in the [VSS github repository](https://github.com/COVESA/vehicle_signal_specification).

