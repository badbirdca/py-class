#!/usr/bin/env python
'''
3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.

'''



import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

ios1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**ios1)
# print(net_connect.find_prompt())
output = net_connect.send_command("sh ver")

with open("show_version.txt","w") as f:
    f.write(output)

net_connect.disconnect()

