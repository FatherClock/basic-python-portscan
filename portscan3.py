#!/usr/bin/python

import socket
from termcolor import colored
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)


host = raw_input("[*] Enter The Host To Scan: ")


def portscanner(port):
    if sock.connect_ex((host,port)):
        print (colored("[!!] Port %d is closed" % (port), 'red'))
    else:
        print (colored("[+] Port %d is open" % (port), 'green'))

for port in range(137,140):
    portscanner(port)
    time.sleep(5)
