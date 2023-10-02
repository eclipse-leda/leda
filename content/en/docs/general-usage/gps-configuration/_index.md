---
title: "GPS Connectivity"
date: 2023-10-02T11:50:03+00:00
weight: 30
---

## GPSD

Leda Quickstart Images provide (within meta-leda) recipes for the integration and setup of GPSD.
GPSD is a service daemon that monitors one or more GPSes or AIS receivers attached to a host computer through serial or USB ports,
making all data on the location/course/velocity of the sensors available to be queried on TCP port 2947
of the host computer. To find out more about GPSD, check out its [official documentation](https://gpsd.gitlab.io/gpsd/gpsd.html).

For easier interaction and debugging gpsd client utilities such as installed [gpsfake](https://www.mankier.com/1/gpsfake),
[gpspipe](https://www.mankier.com/1/gpspipe), etc. are installed.

## Service

GPSD is installed on Leda Quickstart Images as a service. To check its status and/or logs you can use the following two commands:

```shell
root@leda-525400123502:~# systemctl status gpsd.service
* gpsd.service - GPS (Global Positioning System) Daemon
     Loaded: loaded (/lib/systemd/system/gpsd.service; disabled; vendor preset: disabled)
     Active: active (running) since Mon 2023-10-02 11:19:54 UTC; 41min ago
     ...
```

and the socket:

```shell
root@leda-525400123502:~# systemctl status gpsd.socket
* gpsd.socket - GPS (Global Positioning System) Daemon Sockets
     Loaded: loaded (/lib/systemd/system/gpsd.socket; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2023-10-02 11:19:30 UTC; 42min ago
    ...
```

With the location of the default config file being:

```text
/etc/default/gpsd.default
```

By default, the GPSD service on Leda is configured to automatically discover USB devices (plug-and-play). In some cases, a system reboot might be required
after plugging the USB GPS device.

## Kuksa.val FeederGPS

The Kuksa GPS Feeder consumes gpsd as a data source and pushes location data to the kuksa.val server (databroker). It is installed as a pre-configured container on Leda Images
through the [feedergps.json container manifest](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers/example/feedergps.json).
The container has an internal gpsd server (on port 2948) that connects to the host's gpsd instance (on port 2947). With the provided container manifest
feedergps should be plug-and-play.

## Using pre-recorder GPS traces with gpsfake

### Recording NMEA traces

It sometimes might be useful to mock gps services when testing, especially on QEMU virtual machines where emulated USB GPS hardware is not available.
Pre-recorded traces should be in the NMEA-format.

To record a GPS trace in the NMEA format, on a device with physical GPS hardware, gpsd, and gpsd-client utilities installed, run:

```shell
gpspipe -R > gps_log.nmea
```

A sample NEMA file that can be used for testing is provided in the kuksa.val.feeders repository - [simplelog_example.nmea](https://raw.githubusercontent.com/eclipse/kuksa.val.feeders/main/gps2val/simplelog_example.nmea).

### Feeding NMEA traces to feedergps

Since the running gpsd service will interfere with the following steps, make sure to stop it first by running:

```shell
systemctl stop gpsd.service
systemctl stop gpsd.socket
```

To start gpsfake on port *2946* with `gps_log.nmea` as an input,
either in the background (by adding `&` at the end of the shell line) or in a separate shell session run:

```shell
root@leda-525400123502:~# gpsfake -P 2946 gps_log.nmea
/usr/bin/gpsfake:21: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import spawn
Processing gps_log.nmea
gpsfake: log cycle of gps_log.nmea begins.
```

> Note:  you can safely ignore the distutils warning.

Then, run a foreground instance of gpsd that reads from gpsfake on port *2946* on the loopback interface **only** and forwards
the traffic on port *2947* for **all** interfaces:

```shell
gpsd -GNS 2947 gpsd://127.0.0.1:2946
```

> These extra steps are needed as feedergps requires the gpsd server on port 2947 to be available on the kanto-cm0 bridge, as it's running as a
container and gpsfake cannot be configured to listen on an interface different from the loopback.

Restart feedergps:

```shell
kanto-cm stop -n feedergps
kanto-cm start -n feedergps
```

## Known issues

Sometimes the feedergps container is started before the databroker and/or gpsd which leads to the container not being able to connect to either
of those services. In such cases, after you've made sure the databroker and gpsd are up and running, restart feedergps with:

```shell
kanto-cm stop -n feedergps
kanto-cm start -n feedergps
```
