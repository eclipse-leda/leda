---
title: "Utilities"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# SDV Core Utils
The quickstart image contains the following toolings:
- SDV Device Info
- SDV Health
- CAN Forwarder
- SDV MOTD

For details, please see [leda-utils](https://github.com/eclipse-leda/leda-utils/)

# Connecting to Mosquitto
If you want to use your favourite MQTT tool with the quickstart image, you can
connect to the MQTT broker running on the device by using exposed port 31883:
```
$# mosquitto_sub -h 192.168.7.2 -p 31883 -t '#'
```
