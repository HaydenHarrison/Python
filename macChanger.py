#!/usr/bin/env python 

import subprocess 

interface = input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing the MAC address for " + interface + " to "  + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether" new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True) 

print("...Done")
