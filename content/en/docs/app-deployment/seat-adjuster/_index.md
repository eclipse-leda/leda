---
title: "Seat Adjuster"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

The **Seat Adjuster** use case has been derived from the [Eclipse Velocitas Seat Adjuster example](https://websites.eclipseprojects.io/velocitas/docs/about/use_cases/seat_adjuster/), the [Eclipse Kuksa.VAL Seat Service example](https://github.com/eclipse/kuksa.val.services/tree/main/seat_service) and the [Digital.Playground Prototyping Library](https://digitalauto.netlify.app/model/997XF1ch2f5DjgPIzhY3/library/prototype/ZqhnonCBSSwP8ZVM7CFh)

## Description

The Seat Adjuster use cases demonstrates the idea of having a cloud-based driver profile hosted by a third-party web service, which is then used by a custom application to move the driver seat to certain positions.

Examples range from simple personalization to dynamic seat control (such as periodic back massages) based on personal health treatment plans by an health insurance organization. A driver could opt-in to such a service, which would lead to the ad-hoc installation of a seat adjuster vehicle application when the driver enters the vehicle. The seat adjuster application would then contact the health insurance webservice to retrieve the driver's personal treatment plan for back massage and start moving the motors in certain intervals, to ease or prevent back pain during long driving periods.

This example focuses on the technical aspect, namely the interface between such an assumed application with the high-level logic, and the lower-level backend service (Seat Service), which controls the communication to the underlying hardware (Seat ECU). In this case, the Vehicle Signal Specification and the simple signal for seat position is used exemplarily. Safety considerations are not in scope for this example, but would probably be handled within the Seat ECU as the lowest level component to guard against non-safe use of the seat motors.

## Architecture Overview

![Leda Seat Adjuster Use Case](seatadjuster.png)

- Cloud or mobile trigger: not part of the Leda image, but can be simulated by issueing MQTT messages
- Eclipse Velocitas - Vehicle Application: **Seat Adjuster** (to be deployed by user as part of the Velocitas tutorial)
- Eclipse Kuksa.VAL - Example Service: **Seat Service** (pre-installed)
- Eclipse Kuksa.VAL - **Data Broker** (pre-installed)
- Seat ECU and the separate Seat Motor hardware: not part of the Leda image, but can be emulated using virtual CAN-Bus. The Kuksa Seat Service container contains configuration options to use VCAN

## Getting started

1. Follow the Velocitas tutorial: build and deploy your clone of the [seat adjuster example](https://websites.eclipseprojects.io/velocitas/docs/about/use_cases/seat_adjuster/)
2. Download and run the Leda quickstart image
3. Deploy your seat adjuster application to the container runtime, either manually by using `kanto-cm create` or by providing a deployment descriptor in `/var/containers/manifests`. An example deployment descriptor can be found in [meta-leda-components](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example/seatservice.json). Details on the deployment can be found in [Leda Vehicle Applications](/leda/docs/app-deployment/velocitas/)
4. Ensure the databroker and the seat service containers are running and you know how to check their log files
5. Publish an MQTT message for the seat adjuster application, e.g. `mosquitto_pub -t seatadjuster/setPosition/request -f seat-request.json` and a possible payload like this:

        {"position": 300, "requestId": <request_id>}

## Prototyping

The pseudo-code for the Seat Adjuster application could look like the following excerpt from the [Digital.Playground example](https://digitalauto.netlify.app/model/997XF1ch2f5DjgPIzhY3/library/prototype/ZqhnonCBSSwP8ZVM7CFh/view/code):

```python
from sdv_model import Vehicle
vehicle = Vehicle()

on_user_profile_changed(Issuer):
    vehicle.Cabin.Seat.Row1.Pos1.Height.set(profile[Issuer]["VerticalHeight"])
    vehicle.Cabin.Seat.Row1.Pos1.Position.set(profile[Issuer]["HorizontalPosition"])
```

In the next step, this prototype can be taken to the next level of implementation by using the [Velocitas example](https://github.com/eclipse-velocitas/vehicle-app-python-sdk/blob/main/examples/seat-adjuster/src/main.py#L81) to express it like this, with possibly more logic:

```python
@subscribe_topic("seatadjuster/setPosition/request")
async def on_set_position_request_received(self, data_str: str) -> None:
  vehicle_speed = (await self.Vehicle.Speed.get()).value
  ...
  if vehicle_speed == 0:
    try:
        await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.set(position)
        response_data["result"] = {
            "status": 0,
            "message": f"Set Seat position to: {position}",
        }
    except ValueError as error:
        response_data["result"] = {
            "status": 1,
            "message": f"Failed to set the position {position}, error: {error}",
        }
    except Exception:
        response_data["result"] = {
            "status": 1,
            "message": "Exception on set Seat position",
        }
  else:
    error_msg = f"""Not allowed to move seat because vehicle speed
        is {vehicle_speed} and not 0"""
    response_data["result"] = {"status": 1, "message": error_msg}

  await self.publish_event(response_topic, json.dumps(response_data))
```

## CAN-Bus

The default configuration of the *Seat Service* is using simulated VCAN. If you want to switch to a physical CAN-Bus interface, the container needs to have access to the CAN-Bus hardware.

For a Raspberry Pi setup with an MCP251x-based CAN-Hat extension, you would need to reconfigure two components:

1. Make Seat Service container privileged and run on the host network interface:

    ```json
    "host_config": {
    ...
    "network_mode": "host",
    "privileged": true,
    ...
    }
    ```

2. Reconfigure the seat controller application to use the CAN interface, please see Eclipse Kuksa.VAL [seat_controller/README.md](https://github.com/eclipse/kuksa.val.services/blob/main/seat_service/src/lib/seat_adjuster/seat_controller/README.md) for details:

    ```shell
    SC_CAN=can0
    ```