# MAC-Address-spoofer

## Prerequisites 

``python3 python3-pyinstaller``

## Building

Run ``make`` in the root folder, and it should just work. If it's not working for your platform (i.e. aarch64), see [this page](https://pyinstaller.org/en/stable/bootloader-building.html).

## Usage

```
usage: mac-spoof [-h] target

A program which performs a MITM attack by spoofing the MAC address. (INFOST 695-001 Final Project)

positional arguments:
  target      IP of the computer you want to target

options:
  -h, --help  show this help message and exit

Copyright © 2024 Hemanth Chinnappa, Kevin Agyei, Lauren Rodriguez, & Cedar Lehman.
See LICENSE file for more details.
```