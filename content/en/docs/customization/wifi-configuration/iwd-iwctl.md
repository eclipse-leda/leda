---
title: "Notes on using iwd/iwctl"
date: 2023-01-03T17:24:56+05:30
---

Here we will describe the basic steps on how to connect to a WiFi network using iwctl.

## Initial steps (identifying wlan interfaces)

Start by opening the `iwctl` shell

```shell
$ iwctl
```

If you are unsure of the name of the name of your wireless device, you can list all Wi-Fi devices and network adapters:

```shell
[iwd]# adapter list
                                    Adapters                                  *
--------------------------------------------------------------------------------
  Name               Powered   Vendor              Model               
--------------------------------------------------------------------------------
  phy0               on        Broadcom Corp.BCM43438 combo WLAN 

```

```shell
[iwd]# device list
                                    Devices                                    
--------------------------------------------------------------------------------
  Name                Address             Powered   Adapter   Mode      
--------------------------------------------------------------------------------
  <device>               <MAC>              on        phy0      station   

```
If the device or its corresponding adapter is turned off (the `Powered` property), turn it on by running:

```shell
[iwd]# device <device> set-property Powered on
[iwd]# adapter <adapter> set-property Powered on
```

Check the device/adapter list again to ensure they are now powered on.

## Connecting to a network

Initiate a network scan by running (_Note:_ this command has no output):

```shell
[iwd]# station <device> scan
```

List all available networks:

```shell
[iwd]# station <device> get-networks 
                               Available networks                              
--------------------------------------------------------------------------------
    Network name                    Security          Signal
--------------------------------------------------------------------------------
    <SSID>                           psk               ****  
```

Finally, after identifying your network's SSID, connect to it:

```shell
[iwd]# station <device> connect <SSID>
```
If a passphrase is required, you will be prompted to enter it.

You can now exit the `iwctl` shell:
```shell
[iwd]# exit
```

### Connecting with a single command

Alternatively, if you know you network's SSID and your wireless device's name you can connect to the network with a single command:

```shell
$ iwctl --passphrase <passphrase> station <device> connect <SSID>
```
To check current status of device (for example wlan0):
```shell
$ iw dev wlan0 link
```

From now on this WiFi network will be remembered for future connections.


#### References

This readme is based on the guidelines documented in the [ArchLinux Documentation](https://wiki.archlinux.org/title/Iwd#Connect_to_a_network)