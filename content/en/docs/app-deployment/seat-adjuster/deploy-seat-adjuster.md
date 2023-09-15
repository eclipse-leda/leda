---
title: "Deploy Seat Adjuster"
date: 2022-05-09T14:24:56+05:30
weight: 4
---

We now want to deploy the application to a target device.
You may follow the remainder of this guide on a separate device like a RaspberryPi, but you can emulate such a device on your development machine too.
Either way, we use Eclipse Leda as the target system, which is a Linux-based distribution with pre-installed SDV components like the KUKSA Databroker
or Eclipse Kanto for container management. For more details on how to download and run Eclipse Leda, follow the respective guides:

- [QEMU]({{< ref "/docs/general-usage/running-qemu" >}})
- [Docker]({{< ref "/docs/general-usage/docker-setup" >}})
- [RaspberryPi]({{< ref "/docs/general-usage/raspberry-pi" >}})
- [Linux]({{< ref "/docs/general-usage/linux-setup" >}})

In any case, we now need to configure Eclipse Kanto to execute our application.
For this, it helps to get an overview of which containers are currently running in Eclipse Kanto. You can get this either through the command

```bash
kantui
```

or

```bash
kanto-cm list
```

From this list, ensure that at least the KUKSA Databroker and the seatservice are already running, which should be the case since both are pre-configured
with the Eclipse Leda release.

In Eclipse Kanto, you can manage a container with the command line application `kanto-cm` or container manifest files.
The advantage of using the container manifests is that the configuration is persisted across a reboot of the system and is easier to use
to describe a desired software state for the overall vehicle.

## Starting of container

### Use `kanto-cm`

```bash
kanto-cm create \
    --name seatadjuster-app \
    --e="SDV_SEATSERVICE_ADDRESS=grpc://seatservice-example:50051" \
    --e="SDV_MQTT_ADDRESS=mqtt://mosquitto:1883" \
    --e="SDV_VEHICLEDATABROKER_ADDRESS=grpc://databroker:55555" \
    --e="SDV_MIDDLEWARE_TYPE=native" \
    --hosts="databroker:container_databroker-host, mosquitto:host_ip, seatservice-example:container_seatservice-example-host" \
    ghcr.io/<YOUR_ORG>/seat-adjuster-app:latest

kanto-cm start --name seatadjuster-app
kanto-cm logs --name seatadjuster-app
```

### Add manifest file

As an alternative to using `kanto-cm`, Eclipse Kanto comes with an auto-deploy feature where it watches a folder in the file system and applies any changes
to the container manifests in that location.

By default, the container manifests in Eclipse Leda are in `data/var/containers/manifests`.

To add the container manifest, create a new file inside this folder.

```bash
nano seat-adjuster.json
```

and copy the [manifest from below](#seat-applicationjson). You can save the file with `strg+s` and close the window with `strg+q`.
Alternatively, one can create the file on the development machine and copy it via scp (`scp -P 2222 myapp.json root@localhost:/data/var/containers/manifests/`)

The example deployment descriptor below is available in
[meta-leda-components](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example/seatadjuster-app.json.disabled)
too.
An interesting aspect of the snippet is the `config.env` section at the bottom of the container manifest.
There, we define a number of environment variables for the container
which configures the Eclipse Velocitas SDK to use the native middleware and where to find the MQTT-broker and the Kuksa.Val Databroker to use.
We did the same in `kanto-cm` call behind the parameter `--e=`.

More details on the general deployment approach can be found in [Leda Vehicle Applications](/leda/docs/app-deployment/velocitas/)

> If the GitHub packages in which you stored the container image are private, Eclipse Kanto needs a valid access token to download the container image.
You can create a personal access token in the `Developer Settings` of your GitHub account. Select `Personal access token` -> `Tokens (classic)`
and `generate a new token` that at least has the `read:packages` permission. Copy the generated token to a secure location or to Eclipse Kanto
because GitHub will not show it again.
You can now configure Eclipse Kanto in Eclipse Leda to use the token by executing:
`sdv-kanto-ctl add-registry -h <registryhostname> -u <your_username> -p <your_password>`. In the case of GitHub, the `registryhostname` is ghcr.io
, the username your GitHub handle, and the password is the generated token.
See [Container Registries]({{< ref "/docs/device-provisioning/container-management" >}}) for more details.

To make sure that Eclipse Kanto detects the changes in the `manifests` folder, you can restart the respective system services:

```bash
systemctl restart kanto-auto-deployer
```

## Disable other containers

The default Eclipse Leda release already comes with a number of container manifests and, therefore, containers pre-installed.
One of these containers is the `feedercan` that feeds changing values from a recording for signals such as `Vehicle.Speed` to the KUKSA Databroker.
These values interfere with the seat adjuster application, which only moves the seat if the vehicle speed is zero. Therefore, we need to stop the `feedercan` container.
Again, we can either use the `kanto-cm` application:

```bash
kanto-cm stop -n feedercan
```

or rename the container manifest in the `manifest` folder

```bash
mv feedercan.json feedercan.json.disabled
```

If the feedercan container still runs, the seat adjuster application app will later respond with the following error message:

```json
seatadjuster/setPosition/response
 {"requestId": "12345", "result": {"status": 1, "message": "Not allowed to move seat because vehicle speed is 9.0 and not 0"}}
```

## Seat Service

Another pre-installed container is the `seat service` acting as the connection between the KUKSA Databroker and the underlying hardware.
The `seat service` thus acts as a provider for the KUKSA Databroker.
More specifically, it subscribes to the target value of the `Vehicle.Cabin.Seat.Row1.Pos1.Position` signal and updates the current value of the signal
in small steps until it is equal to the target value.
For more details, visit the [Kuksa.val.services](https://github.com/eclipse/kuksa.val.services/tree/main/seat_service) repository,
which hosts the code for the `seat service`. In a real world scenario the seat service would interact with the seat ECU to move the seat
but for simplicity we abstract this part in this guide. You can check the [CAN setup for seat adjuster](../can-seat-adjuster) on how to add a CAN connection.

After all required components should run now, the next step is to [interact with the seat adjuster](../interact-seat-adjuster).

## seat-application.json

This is the Eclipse Kanto container manifest for the seat adjuster application.

```json
{
    "container_id": "seatadjuster-app",
    "container_name": "seatadjuster-app",
    "image": {
        "name": "ghcr.io/<identifier-for-container>:<tag-for-container>"
    },
    "host_config": {
        "devices": [],
        "network_mode": "bridge",
        "privileged": false,
        "restart_policy": {
            "maximum_retry_count": 0,
            "retry_timeout": 0,
            "type": "unless-stopped"
        },
        "runtime": "io.containerd.runc.v2",
        "extra_hosts": [        
                "mosquitto:host_ip",
                "databroker:container_databroker-host",
                "seatservice-example:container_seatservice-example-host"
        ],
        "port_mappings": [
            {
              "protocol": "tcp",
              "container_port": 30151,
              "host_ip": "localhost",
              "host_port": 50151,
              "host_port_end": 50151
            }
        ],
        "log_config": {
            "driver_config": {
                "type": "json-file",
                "max_files": 2,
                "max_size": "1M",
                "root_dir": ""
            },
            "mode_config": {
                "mode": "blocking",
                "max_buffer_size": ""
            }
        },
        "resources": null
    },
    "config": {
        "env": [
           "SDV_SEATSERVICE_ADDRESS=grpc://seatservice-example:50051",
           "SDV_VEHICLEDATABROKER_ADDRESS=grpc://databroker:55555",
           "SDV_MQTT_ADDRESS=mqtt://mosquitto:1883",
           "SDV_MIDDLEWARE_TYPE=native",
           "RUST_LOG=info",
           "vehicle_data_broker=info"
        ],
        "cmd": []
    }
}
```
