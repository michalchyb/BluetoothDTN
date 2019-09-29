from bluetooth import *
from subprocess import PIPE, Popen


def lookForAllNearbyDevices():
    print "performing inquiry..."
    nearby_devices = discover_devices(lookup_names=True)
    print "found %d devices" % len(nearby_devices)
    for name, addr in nearby_devices:
        print " %s - %s" % (addr, name)


def cmdLine(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
