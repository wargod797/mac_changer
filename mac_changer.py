#!/usr/bin/env python

@author Sridhar 


import subprocess

import optparse

def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + "to" + new_mac)

    subprocess.call("ifconfig")

    subprocess.call(["ifconfig ", interface, " down"])

    subprocess.call(["ifconfig ", interface, "hw", "ether", new_mac])

    subprocess.call(["ifconfig ", interface, " up"])

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please Specify an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new_mac, use --help for more info")
    return options


parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC Address")

parser.add_option("-m","--mac",dest="new_mac", help="New max addresss")



"""interface=Options.interface

new_mac = options.new_mac"""
options = get_arguments()
change_mac(options.interface, options.new_mac)
