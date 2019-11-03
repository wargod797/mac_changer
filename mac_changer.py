#!/usr/bin/env python
#@author:Sridhar
#Importing the Libraries
import subprocess
import optparse
#Creating the function to get arguments
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help = "Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help = "New mac addresss")

    (options , arguments) = parser.parse_args()

    #Error Handeling
    if not options.interface:
        parser.error("[-] Please Specify an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new_mac, use --help for more info")
    return options
#Creating a function to perform mac_change operation
def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig"])
options = get_arguments()
change_mac(options.interface,options.new_mac) #Calling change_mac