# coding=utf-8
from bluetooth import *
from PyOBEX.client import Client
import os


def lookForNearbyDevices():
    print "performing inquiry..."
    nearby_devices = discover_devices(lookup_names=True)
    print "found %d devices" % len(nearby_devices)
    for name, addr in nearby_devices:
        print " %s - %s" % (addr, name)


lookForNearbyDevices()

service_matches = find_service(name=b'OBEX Object Push')
if len(service_matches) == 0:
    print "nie moge znaleźć serwisu"
    sys.exit(0)
else:
    print "serwis znaleziony"

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]
print port
print name
print host
print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put("test.txt", "Hello world\n")
client.disconnect()

first_match = service_matches[1]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]
print port
print name
print host
print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put("test.txt", "Hello world\n")
client.disconnect()
print "End of transmission"

os.system("sudo btmgmt find |grep rssi |sort -n |uniq -w 33")
