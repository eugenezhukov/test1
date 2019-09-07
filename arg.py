#!/usr/bin/python
import sys
from sys import argv

if len(argv)<2:
    print ("No any argument passed. Exiting.")
    sys.exit()

print ('Command line',argv[0])
interface = argv[1]
vlan = argv[2]
print (interface,vlan)