---
title: "Connecting to Wi-Fi networks"
date: 2023-01-03T17:24:56+05:30
---

Here we will describe the basic steps on how to identify and connect to a WiFi network in interactive or headless mode.

## Initial steps (identifying wlan interfaces)
Start by running:

```shell
$ ip a
 ...
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether <MAC> brd ff:ff:ff:ff:ff:ff
...
```

__Note:__ Usually the name of the interface would be `wlan0`. It might however follow the newer "predictable interface names" standart.
Then the interface name would start with `wl*` with the remaining characters identifying a physical bus/chip/number/etc
corresponding to the interface. For simplicity we will `wlan0` in all examples below.

Most likely your wlan interface would be in the state `DOWN`. To bring it up:

```shell
$ ip link set wlan0 up
```

## Scanning for wireless networks
You can scan for wireless networks using either `iw` or `wpa_cli`.

```shell
$ iw wlan0 scan
```

__Note:__ The output of this command can be quite verbose. You can grep for `SSID` to find the SSIDs of the networks around you.

```shell
$ wpa_cli scan && wpa_cli scan_results
```

The output of `wpa_cli` is cleaner and more readable so it is recommended to use that.

## Connecting to a network
Once you have identified the SSID of your network you can connect to it by ussing the following commands:

```shell
$ wpa_passphrase <SSID> <Passphrase> >> /etc/wpa_supplicant.conf
$ systemctl restart wpa
```

You should now be connected to the wireless network. To confirm that, you can once again use `ip a` to check that `wlan0` has been configured with an IP.

This configuration shall be remembered from now on and your interface will try to connect automaticatically to that network whenever it is available.

## Headless Wi-Fi configuration
Similarly to the Raspbian, meta-leda provides a mechanism for headless configuration of Wi-Fi credentials for your device ([Headless Raspberry Pi Setup](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/wifi-with-dhcp)).

To use this feature you have to prepapre your `wpa_supplicant.conf` ahead of time (check the reference above):

```text
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1

network={
        key_mgmt=NONE
}
network={
    ssid="<YOUR NETWORK NAME>"
    psk="<YOUR NETWORK PASSWORD>"
    key_mgmt=WPA-PSK
}
```

__IMPORTANT:__ It is recommended that if you are creating this configuration file on Windows to use an editor such as Notepad++ that can save files using the
"Unix Line endings" ([DOS vs. Unix Line Endings](https://www.cs.toronto.edu/~krueger/csc209h/tut/line-endings.html)), or run it through a tool such as `dos2unix`
that can convert between the two file formats. Otherwise `wpa_supplicant.conf` might not be read properly in the Linux image.

Once you have your `wpa_supplicant.conf` put your SD-card in your Desktop machine and place the configuration file in the root of the `BOOT` partion.

When you boot your device it should now automatically connect to your Wi-Fi network.