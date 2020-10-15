#! /usr/bin/env python

import nmap
import time
import socket
import json
import sys
import os
import requests
from collections import OrderedDict

def scan():
    # Get subnet/network mask
    subnet = str(get_my_ip()) + "/24"

    # Scan subnet with "-sn" arg
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments="-sn")

    hosts = []
    for ip in scanner.all_hosts():
        host = {"ip": ip}
        hosts.append(host)

        print(host)
        # if "hostname" in scanner[ip]:
        #     host["hostname"] = scanner[ip]["hostname"]

    return hosts

def get_my_ip():
    # Returns user host IP
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    # print(ip_address)

    try:
        # 8.8.8.8 DNS server for Google DNS
        return ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    except socket.error as e:
        sys.stderr.write(str(e) + "\n") # probably offline / no internet connection
        sys.exit(e.errno)


if __name__ == "__main__":
    foundHosts = [host["mac"] for host in scan() if "mac" in host]

    # Check in some type of file if host found before
    # set() knownHosts
    # set() newHosts
