#!/usr/bin/env python
#@author:Sridhar


#Importing the Libraries
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help = "Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help = "New mac addresss")

    (options , arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new_mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    #subprocess.call(["ifconfig"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    #print(ifconfig_result)

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could'nt able to change MAC Address.")

options = get_arguments()
change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
print("Current MAC = "+ str(current_mac))

change_mac(options.interface,options.new_mac)
if current_mac == options.new_mac:
    print("[+] MAC address Sucessfuly Changed to = " + current_mac)
else:
    print("[-] MAC address didn't get Changed.")
