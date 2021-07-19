#!/usr/bin/env python

#this file is mostly for testing out modules defined in
#config_modueles.py

from netmiko import ConnectHandler
from config_modules import create_vlans, config_general
import getpass




#read places the whole text file as one string into the variable
#splitlines splits the text file into list items based on line breaks


#probably only need 1 devices file
with open('devices.txt') as f:
    devices = f.read().splitlines()

for host in devices:

    #creating a list of lists, which each item is a deivce
    switchX = host.split(', ')

    device = {
        'device_type': 'cisco_ios',
        'host': switchX[0],
        'username': switchX[1],
        'password': switchX[2]
    }


    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    iosl2 = ConnectHandler(**device)
    output = iosl2.send_command('show ip int brief')

    #creating vlans
    create_vlans(iosl2, 1, 11)

    #takes a general config file and configures it for
    #the list of devices in devices.txt
    config_general(iosl2, 'ospf', 'config_ospf.cfg')


