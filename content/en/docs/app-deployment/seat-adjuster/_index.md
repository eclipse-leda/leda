---
title: "Seat Adjuster"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

The **Seat Adjuster** use case has been derived from the [Eclipse Velocitas Seat Adjuster example](https://eclipse.dev/velocitas/docs/about/use_cases/seat_adjuster/), the [Eclipse Kuksa.VAL Seat Service example](https://github.com/eclipse/kuksa.val.services/tree/main/seat_service) and the [Digital.Playground Prototyping Library](https://digitalauto.netlify.app/model/997XF1ch2f5DjgPIzhY3/library/prototype/ZqhnonCBSSwP8ZVM7CFh)

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

1. Follow the Velocitas tutorial: build and deploy your clone of the [seat adjuster example](https://eclipse.dev/velocitas/docs/about/use_cases/seat_adjuster/)
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

## Testing the seatservice-example container on the Leda Quickstart Image
    
Whether you are running the seatservice-example with a simulated CAN or a physical (emulated) CAN, the seatservice-example container included in the Leda Quickstart image provides a simple client application that can be used to test the GRPC interface.

To set the seat position to `x%`, take `x*10` and truncate it to an integer `<position>`. Then using the sdv-ctr-exec script issue the following command:

```shell
$ sdv-ctr-exec -n seatservice-example /app/bin/seat_svc_client <position>
```

You can now check the logs (either with `kanto-cm logs` or `kantui`) and you should be able to see the `seatservice-example` application responding to the command by moving the seat to the desired position.

### Specifics for physical (emulated) CAN

1. You will have to generate initial CAN frames that will emulate the car ECU responding to the service:

    ```shell
    $ cangen -v can0 -L 8 -I 712 -D r -n 5
    can0  712#4F.BF.B0.6B.5F.2D.54.09
    can0  712#13.2E.98.7E.77.11.99.5B
    can0  712#15.70.87.07.73.24.3A.7A
    can0  712#99.7F.F5.3F.FB.99.00.04
    can0  712#FE.1C.D5.55.22.86.3A.1F
    ```
2. You can now start tracing CAN frames written to the bus with `candump can0`

3. From now on when a request to change the seat position is issued you will be able to see the corresponding CAN frames in the trace.

_Note_: On QEMU you can tunnel the host CAN bus to the guest: [Tunneling a CAN Interface from the Host](../../general-usage/running-qemu/canbus/#enabling-can-bus-interfaces-can).

## Hardware CAN-Bus

The default configuration of the *Seat Service* is using simulated VCAN. If you want to switch to a physical CAN-Bus interface, the container needs to have access to the CAN-Bus hardware.

Such a CAN-Bus device might be a Raspberry Pi setup with an MCP251x-based CAN-Hat extension or a QEMU image with an emulated *kvaser_pci* device (enabled on the Leda QEMU Quickstart images by default).

This setup would require some adjustments to the container manifest in order for the container to have access to the physical CAN-Bus.

1. Make Seat Service container privileged and run on the host network interface:

    ```json
    "host_config": {
    ...
    "network_mode": "host",
    "privileged": true,
    ...
    }
    ```

2. Remove all port mappings and extra hosts (set `"extra_hosts": []` and `"port_mappings": []`) for the container as it's now running in host-networking mode (host_ip variable no longer available) and all ports are directly exposed.

3. Set the address to the databroker to `localhost:30555`: 

    ```json
        "config": {
        "env": [
           ...
            "BROKER_ADDR=127.0.0.1:30555",
           ...
        ],
        ...
        }
    ```

4. Reconfigure the seat controller application to use the physical CAN interface, please see Eclipse Kuksa.VAL [seat_controller/README.md](https://github.com/eclipse/kuksa.val.services/blob/main/seat_service/src/lib/seat_adjuster/seat_controller/README.md) for details:

    ```shell
    SC_CAN=can0
    CAN=can0
    ```

    All the necessary changes combined for clarity as a single diff can be found below:

    ```diff
    --- ../meta-leda-fork/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example_dev/seatservice.json	2023-03-06 11:32:00.771754434 +0200
    +++ seatservice-new.json	2023-03-06 11:37:12.967182044 +0200
    @@ -14,26 +14,16 @@
        "hooks": [],
        "host_config": {
            "devices": [],
    -        "network_mode": "bridge",
    -        "privileged": false,
    +        "network_mode": "host",
    +        "privileged": true,
            "restart_policy": {
                "maximum_retry_count": 0,
                "retry_timeout": 0,
                "type": "unless-stopped"
            },
            "runtime": "io.containerd.runc.v2",
    -        "extra_hosts": [
    -            "databroker-host:host_ip"
    -        ],
    -        "port_mappings": [
    -            {
    -              "protocol": "tcp",
    -              "container_port": 50051,
    -              "host_ip": "localhost",
    -              "host_port": 30051,
    -              "host_port_end": 30051
    -            }
    -        ],
    +        "extra_hosts": [],
    +        "port_mappings": [],
            "log_config": {
                "driver_config": {
                    "type": "json-file",
    @@ -58,9 +48,11 @@
        },
        "config": {
            "env": [
    -           "BROKER_ADDR=databroker-host:30555",
    -           "RUST_LOG=info",
    -           "vehicle_data_broker=info"
    +            "CAN=can0",
    +            "SC_CAN=can0",
    +            "BROKER_ADDR=127.0.0.1:30555",
    +            "RUST_LOG=info",
    +            "vehicle_data_broker=info"
            ],
            "cmd": []
        },
    ```