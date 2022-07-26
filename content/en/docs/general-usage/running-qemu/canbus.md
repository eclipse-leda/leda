---
title: "CAN Bus"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

*Note: The configuration mentioned in this chapter is already enabled in the `run-leda.sh` script.*

## QEMU

General documentation about using CAN-Bus in Qemu: https://www.qemu.org/docs/master/system/devices/can.html

### Enabling Virtual CAN Bus interfaces (vcan)

No special parameters are necessary for qemu, as vcan is virtual:
```
runqemu qemux86-64 nographic slirp qemuparams="-m 2048"
```

Bring interface up:
```
ip link add dev vcan0 type vcan
ip link set vcan0 up
```

### Enabling CAN Bus interfaces (can)

#### Standalone CAN within Qemu

To run a standalone CAN setup, qemu must be instructed to emulate a specific CAN hardware device. We will be using the `kvaser_pci` device in this example:
```
runqemu qemux86-64 nographic slirp qemuparams="-m 2048 -object can-bus,id=canbus0 -device kvaser_pci,canbus=canbus0"
```

After the image has booted, load the Linux Kernel Module `kvaser_pci` device driver and configure the CAN-Bus device (eg bitrate) before bringing the interface up:
```
root@qemux86-64:~# modprobe kvaser_pci

root@qemux86-64:~# dmesg | grep kvaser
[    9.565149] kvaser_pci 0000:00:04.0: initializing device 10e8:8406
[    9.569308] kvaser_pci 0000:00:04.0: reg_base=00000000d5a68095 conf_addr=000000002b3c7ef6 irq=20
[    9.596942] kvaser_pci 0000:00:04.0: xilinx version=13 number of channels=0

root@qemux86-64:~# ip link show type can
4: can0: <NOARP,ECHO> mtu 16 qdisc noop state DOWN mode DEFAULT group default qlen 10
    link/can
```

Configure the interface:
```
root@qemux86-64:~# ip link set can0 type can bitrate 1000000
[  165.519919] kvaser_pci 0000:00:04.0 can0: setting BTR0=0x00 BTR1=0x14

root@qemux86-64:~# ip link set can0 up
[  186.906065] IPv6: ADDRCONF(NETDEV_CHANGE): can0: link becomes ready

root@qemux86-64:~# ip link show type can
4: can0: <NOARP,UP,LOWER_UP,ECHO> mtu 16 qdisc pfifo_fast state UP mode DEFAULT group default qlen 10
    link/can 

```

#### Tunneling a CAN Interface from the Host
```
runqemu qemux86-64 nographic slirp qemuparams="-m 2048 -object can-bus,id=canbus0 -object can-host-socketcan,id=canhost0,if=can0,canbus=canbus0 -device kvaser_pci,canbus=canbus0"
```

Bring interface up:
```
ip link add dev can0 type can
ip link set can0 type can bitrate 1000000
ip link set can0 up
ip link show type can
```

# Raspberry Pi CAN HAT Extensions

Supported boards:
- Boards with a Microchip MCP251x based CAN chip, such as Waveshare CAN HAT or PiCAN 2

Verify driver is loaded:
```
# dmesg | grep mcp
[    8.23543] mcp251x spi0.0 can0: MCP2515 successfully initialized
```

Verify SocketCAN network interface shows up:
```
# ip link show type can
3: can0: <NOARP,ECHO> mtu 16 qdisc noop state DOWN mode DEFAULT roup default qlen 10
```

Continue with configuring the CAN chip and bring up the SocketCAN network interface:

```
# ip link set can0 type can bitrate 1000000
# ip link set can0 up
# ip link show type can
```

# Linux Kernel Modules

The following Linux Kernel modules are available on the quickstart images:

*Note: For QEMU, only *kvaser_pci* is used*

## Leda main Kernel

- peak_pciefd - Socket-CAN driver for PEAK PCAN PCIe/M.2 FD family cards
- m_can - CAN bus driver for Bosch M_CAN controller
- m_can_pci - CAN bus driver for Bosch M_CAN controller on PCI bus
- m_can_platform - M_CAN driver for IO Mapped Bosch controllers
- softing - Softing DPRAM CAN driver
- cc770_platform - Socket-CAN driver for CC770 on the platform bus
- cc770_isa - Socket-CAN driver for CC770 on the ISA bus
- cc770 - cc770CAN netdevice driver
- ifi_canfd - CAN bus driver for IFI CANFD controller
- kvaser_usb - CAN driver for Kvaser CAN/USB devices
- etas_es58x - Socket CAN driver for ETAS ES58X USB adapters
- ucan - Driver for Theobroma Systems UCAN devices
- peak_usb - CAN driver for PEAK-System USB adapters
- kvaser_pciefd - CAN driver for Kvaser CAN/PCIe devices
- kvaser_pci - Socket-CAN driver for KVASER PCAN PCI cards
- f81601 - Fintek F81601 PCIE to 2 CANBUS adaptor driver
- sja1000_isa - Socket-CAN driver for SJA1000 on the ISA bus
- plx_pci - Socket-CAN driver for PLX90xx PCI-bridge cards with the SJA1000 chips
- sja1000 - sja1000CAN netdevice driver
- ems_pci - Socket-CAN driver for EMS CPC-PCI/PCIe/104P CAN cards
- peak_pci - Socket-CAN driver for PEAK PCAN PCI family cards
- sja1000_platform - Socket-CAN driver for SJA1000 on the platform bus
- vxcan - Virtual CAN Tunnel
- c_can_platform - Platform CAN bus driver for Bosch C_CAN controller
- c_can - CAN bus driver for Bosch C_CAN controller
- c_can_pci - PCI CAN bus driver for Bosch C_CAN/D_CAN controller
- slcan - serial line CAN interface
- can_dev - CAN device driver interface
- vcan - virtual CAN interface
- can-isotop - PF_CAN isotp 15765-2:2016 protocol
- can-gw - PF_CAN netlink gateway
- can-j1939 - PF_CAN SAE J1939
- can-raw - PF_CAN raw protocol
- can-bcm - PF_CAN broadcast manager protocol
- can - Controller Area Network PF_CAN core

## Raspberry Pi

The following Linux Kernel modules are available on the quickstart image for Raspberry Pi:

- can - Controller Area Network PF_CAN core
- vxcan - Virtual CAN Tunnel
- can-dev - CAN device driver interface
- can-bcm - PF_CAN broadcast manager protocol
- can-gw - PF_CAN netlink gateway
- can-raw - PF_CAN raw protocol
- can-isotop - PF_CAN isotp 15765-2:2016 protocol
- can-j1939 - PF_CAN SAE J1939
- vcan - virtual CAN interface
- slcan - serial line CAN interface
- mcp251x - Microchip 251x/25625 CAN driver
- mcp251xfd - Microchip 251xFD Family CAN controller driver
- ems_usb - CAN driver for EMS Dr. Thomas Wuensche CAN/USB interfaces
- gs_usb - Socket CAN device driver for Geschwister Schneider UG
- peak_usb - CAN driver for PEAK-System USB adapters

