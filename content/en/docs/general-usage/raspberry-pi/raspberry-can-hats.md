---
title: "CAN-Bus extensions"
date: 2022-05-09T14:24:56+05:30
weight: 2
---

The Eclipse Leda quickstart image has CAN-Bus kernel modules and some CAN hardware drivers pre-installed.
However, some hardware configuration needs to be adapted at boot time depending on the specific CAN-Extension being attached to the device.

On Raspberry Pi, there is a `/boot/config.txt` file where you can configure the `dtoverlay` options accordingly. 

> **Note:** After modification, the device **requires rebooting** for the changes to take effect.

## MCP2515 based modules

Products:

- [Waveshare RS485 CAN HAT for Raspberry Pi](https://www.waveshare.com/rs485-can-hat.htm)

```shell
dtoverlay=mcp2515-can0,oscillator=12000000,interrupt=25,spimaxfrequency=2000000
```

## MCP2518FD based modules

Products:

- [Waveshare 2-Channel Isolated CAN FD Expansion HAT for Raspberry Pi, Multi Protections](https://www.waveshare.com/product/raspberry-pi/2-ch-can-fd-hat.htm)

```shell
dtoverlay=2xMCP2517FD
#dtoverlay=2xMCP2518FD-spi0
```
