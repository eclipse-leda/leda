---
title: "Develop Seat Adjuster"
date: 2022-05-09T14:24:56+05:30
weight: 3
---

The following pages show how to execute the explained setup using Eclipse Velocitas 0.9.0 and Eclipse Leda 0.1.0:

On a high level, you need to perform the following steps:

1. Use the Eclipse Velocitas template repository to develop, build and deploy your
version of the [seat adjuster example (v0.9.0)](https://github.com/eclipse-velocitas/vehicle-app-python-sdk/tree/v0.9.0/examples/seat-adjuster) following this guide.

2. Run Eclipse Leda, for example, [as container](../../../general-usage/docker-setup) or with other options like [QEMU, physical hardware, etc.](../../../general-usage).
:

```bash
docker run -it ghcr.io/eclipse-leda/leda-distro/leda-quickstart-x86
```

3. [Manage the Eclipse Kanto container runtime]({{< ref "/deploy-seat-adjuster" >}}) to deploy your seat adjuster application.

4. [Test the deployed setup]({{< ref "/interact-seat-adjuster" >}}) by interacting with the seat adjuster to change the seat position.

## Setup Eclipse Velocitas from template repository

We use Eclipse Velocitas to develop the seat application against the API of the Kuksa.val Databroker:

In the first step, you create a copy of the [Eclipse Velocitas template repository](https://github.com/eclipse-velocitas/vehicle-app-python-template/tree/main).
You can create the copy by opening the repository in GitHub and selecting:  `Use this template` -> `Create a new repository`.
In the next step, you can choose under which organization to place the created repository and whether it should be public.
If you set the repository to private, you have to perform additional configuration steps mentioned below.

The template repository [contains skeleton code for the application](https://github.com/eclipse-velocitas/vehicle-app-python-template/tree/main/app),
[test and release workflows for GitHub actions](https://github.com/eclipse-velocitas/vehicle-app-python-template/tree/main/.github/workflows),
and the configuration of a [development environment in a container](https://github.com/eclipse-velocitas/vehicle-app-python-template/tree/main/.devcontainer).

In addition to the Python template used in this guide, there is a [C++ template](https://github.com/eclipse-velocitas/vehicle-app-cpp-template) available.

## Execute Development Container in VSCode

You then checkout the repository on your development machine and open it in VSCode. From VSCode
you can execute the development container (DevContainer) configured in the repository. For this to function, you need the following tools to be installed on your computer:

- Docker (e.g. [Docker Desktop](https://www.docker.com) or [Rancher Desktop](https://rancherdesktop.io))
- [VSCode](https://code.visualstudio.com) with the
[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) plugin installed.

In the best case, VSCode may detect that the repository contains a DevContainer configuration and ask you whether to execute it.
Alternatively, you can press `F1` in VSCode and then enter `DevContainers: Reopen in container` to start the DevContainer.
In either case, VSCode should reopen and then connect to the DevContainer.
Because of the DevContainer, we do not need to make further modifications to the developer machine.

## Develop the application

In the next step, we develop the actual application. You find the skeleton code in `/app/src/main.py`. Eclipse Velocitas provides you with [the code
to realize the described seat adjuster application](https://github.com/eclipse-velocitas/vehicle-app-python-sdk/blob/v0.11.0/examples/seat-adjuster/src).
For reference we put the code for which this tutorial has been tested [in the end of this page](#the-example-application).

Let us walk through some lines of the code where the logic is in the `vapp.py` while the entry point is in `main.py`.

In the `onStart(self)` function we subscribe to any changes of the current value of the VSS signal `Vehicle.Cabin.Seat.Row1.Pos1.Position` in the KUKSA Databroker.

```python
async def on_start(self):
        """Run when the vehicle app starts"""
        await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.subscribe(
            self.on_seat_position_changed
        )
```

When the seat position changes, the `on_seat_position_changed` function is triggered and publishes the new seat position value as MQTT-message to the topic `seatadjuster/currentPosition`.

```python
 async def on_seat_position_changed(self, data: DataPointReply):
        response_topic = "seatadjuster/currentPosition"
        await self.publish_event(
            response_topic,
            json.dumps(
                {"position": data.get(self.Vehicle.Cabin.Seat.Row1.Pos1.Position).value}
            ),
        )
```

In addition, we have the function `on_set_position_request_received` which is triggered for every MQTT-message to the topic `seatadjuster/setPosition/request`.

```python
 @subscribe_topic("seatadjuster/setPosition/request")
    async def on_set_position_request_received(self, data_str: str) -> None:
        data = json.loads(data_str)
        (...)
        vehicle_speed = (await self.Vehicle.Speed.get()).value

        position = data["position"]
        if vehicle_speed == 0:
                try:
                    await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.set(position)
        (...)
```

If the vehicle speed is zero, meaning that the vehicle does not move, we set the target value in the KUKSA Databroker for the position signal of the seat
to the value requested in the incoming MQTT message.

The `get()` and `set()` functions are created based on a VSS model, and we assume that the KUKSA Databroker instance uses the same VSS model.
In many cases, like the default Eclipse Leda, one may rely on the upstream VSS model, but some scenarios require further signals, e.g., by applying an overlay.

At this point, you may wonder how the application actually knows to which MQTT broker to connect and where to find the correct instance of the KUKSA Databroker.
This service discovery is abstracted within the Velocitas SDK and involves the usage of so-called middleware to find and call the other components.
As of writing this page, Eclipse Velocitas supports DAPR as middleware or uses the `native` approach to configure the correct address directly.
The details of how to set and configure the used middleware are part of the [deployment](../deploy-seat-adjuster).

> *Signal Description:* The signal indicates the seat position on the vehicle x-axis, where the value 0 is the frontmost position supported by the seat.

The value is the *distance measured in millimeters*.

The example implementation supports values between `0` and `1000` millimeters.

> *Note:* This range of valid values is not reflected in the standard Vehicle Signal Specification. OEMs would overlay the VSS tree with actual Min/Max values,
depending on the seat hardware available in the vehicle model.

## Start Runtime in DevContainer to test application

> You may skip the application testing since we already provide the example code.
But it still makes sense to get a general idea of how to test and debug the code with the tooling in the DevContainer.

As mentioned before, the execution and, thus, the testing of the application requires a set of other components to be available
like the KUKSA Databroker or an MQTT-broker.
Furthermore, the deployment, the configuration, and the behavior of the application may change depending on the used (container) management solution.
Therefore, Eclipse Velocitas allows the deployment of the required components and the application with the container management approach of choice inside the DevContainer.

The different runtimes are maintained in [a separate Eclipse Velocitas repository](https://github.com/eclipse-velocitas/devenv-runtimes). To start a runtime,
we use the [Eclipse Velocitas CLI](https://github.com/eclipse-velocitas/cli):

```bash
velocitas exec runtime-kanto up
```

We use the Eclipse Kanto runtime here since we later deploy the seat adjuster application to Eclipse Leda, which uses Eclipse Kanto for container management.

Once the runtime is available, we add our application by executing:

```bash
velocitas exec deployment-kanto build-vehicleapp
velocitas exec deployment-kanto deploy-vehicleapp
```

You can now check the behavior of the application by interacting with it through the MQTT-broker in the VSMQTT plugin available
in the left side of the VSCode instance connected to the DevContainer.
We will not get into details here since we will test the application in Eclipse Leda again later in this guide.

Once you finish the application testing and development, you can shutdown the runtime with:

```bash
velocitas exec runtime-kanto down
```

## Commit and Release Application

When we are confident about the application, we want to be able to distribute it. Here, pre-configured workflows from Eclipse Velocitas for GitHub Actions are helpful.

You now commit your changes and push them to your copy of the Eclipse Velocitas template repository in GitHub.
Before you create the commit, we recommend running the pre-commit task, which performs similar checks and linting as the CI workflow from Eclipse Velocitas.
You can trigger the pre-commit as a task in VSCode:

1. Press F1
2. Write `Tasks: Run Task` and press enter
3. Write `Pre Commit Action` and press enter

The pre commit action should start in a terminal inside VSCode.

You can check the available tasks configured by Eclipse Velocitas in `.vscode/tasks.json`.

If the pre-commit was successful, you may push your changes and open the repository in the browser.
In the meantime, the push should trigger the `CI workflow` and the `Build multiarch image` workflow, which you can track in the `Actions` tab.

> If you set your copy of the template repository to private, the `CI workflow` may fail due to missing permissions to write container images to GitHub packages.
You can grant more `Workflow permissions` in the `Settings` tab of the repository under `Actions`-> `General`.

To deploy your application to a target and if the two workflows have finished successfully, you can perform a release in GitHub.
The subsequent release workflow will make the application available as a built container in the container registry of GitHub (`Code` -> `Packages`).
To do the release in GitHub, go to the `Code` tab and click `Releases` on the right side of the page.
Then you can `Draft a new release`, create a new tag and title for the release, and click `Publish Release`, which triggers the `Release workflow`.

The next step is to [deploy the seat adjuster in Eclipse Leda](../deploy-seat-adjuster)

## The example application

main.py:

```python
"""The launcher for starting a Vehicle App."""

import asyncio
import logging
import signal

from vapp import SeatAdjusterApp  # type: ignore # noqa: E402
from vehicle import vehicle  # type: ignore

from sdv.util.log import (  # type: ignore
    get_opentelemetry_log_factory,
    get_opentelemetry_log_format,
)

logging.setLogRecordFactory(get_opentelemetry_log_factory())
logging.basicConfig(format=get_opentelemetry_log_format())
logging.getLogger().setLevel("DEBUG")
logger = logging.getLogger(__name__)


async def main():
    """Main function"""
    logger.info("Starting seat adjuster app...")
    seat_adjuster_app = SeatAdjusterApp(vehicle)
    await seat_adjuster_app.run()


LOOP = asyncio.get_event_loop()
LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
LOOP.run_until_complete(main())
LOOP.close()
```

vapp.py:

```python
"""A sample Velocitas vehicle app for adjusting seat position."""

import json
import logging

from vehicle import Vehicle  # type: ignore

from sdv.util.log import (  # type: ignore
    get_opentelemetry_log_factory,
    get_opentelemetry_log_format,
)
from sdv.vdb.reply import DataPointReply
from sdv.vehicle_app import VehicleApp, subscribe_topic

logging.setLogRecordFactory(get_opentelemetry_log_factory())
logging.basicConfig(format=get_opentelemetry_log_format())
logging.getLogger().setLevel("DEBUG")
logger = logging.getLogger(__name__)


class SeatAdjusterApp(VehicleApp):
    """
    Sample Velocitas Vehicle App.
    """

    def __init__(self, vehicle_client: Vehicle):
        super().__init__()
        self.Vehicle = vehicle_client

    async def on_start(self):
        """Run when the vehicle app starts"""
        await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.subscribe(
            self.on_seat_position_changed
        )

    async def on_seat_position_changed(self, data: DataPointReply):
        response_topic = "seatadjuster/currentPosition"
        await self.publish_event(
            response_topic,
            json.dumps(
                {"position": data.get(self.Vehicle.Cabin.Seat.Row1.Pos1.Position).value}
            ),
        )

    @subscribe_topic("seatadjuster/setPosition/request")
    async def on_set_position_request_received(self, data_str: str) -> None:
        data = json.loads(data_str)
        response_topic = "seatadjuster/setPosition/response"
        response_data = {"requestId": data["requestId"], "result": {}}

        vehicle_speed = (await self.Vehicle.Speed.get()).value

        position = data["position"]
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
