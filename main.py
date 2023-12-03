# my modules
from modules import hostname
from modules import ipAddress

import paramiko
import ipaddress
import socket
import sys
import os
import datetime
import time
import re

os.system('')


def main():
    # select format name
    from ui import selectFormatHostname
    selectFormatHostname.selectFormat()

    selection = str(input("Select 1/2/q : "))
    #print(selection)
    if selection == "1":
        print("you select 1")
    elif selection == "2":
        print("you select 2")
    elif selection == "q":
        print("exit")
        sys.exit(1)

    #username = 'admin'
    #password = ''        
    #ip_range_input = input("""
     #   [*] Masukkan range IP dengan format dibawah
     #        |
     #        v
     #   192.168.1.0/24
     #       atau
     #   192.168.1.1-192.168.1.100 (tanpa spasi diantara '-')


      #  : """)
      
"""
    if '-' in ip_range_input:
        start_ip, end_ip = ip_range_input.split('-')
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)

        for ip_int in range(int(start_ip), int(end_ip) + 1):
            ip = ipaddress.IPv4Address(ip_int)
            hostname.login_mikrotik(str(ip), username, password)
    else:
        ip_range = ipaddress.ip_network(ip_range_input)
        for ip in ip_range.hosts():
            hostname.login_mikrotik(str(ip), username, password)
"""
if __name__ == "__main__":
    main()
