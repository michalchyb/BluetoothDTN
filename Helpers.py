from subprocess import PIPE, Popen

from bluetooth import *

from Messages import *


def find_OBEX_services_devices():
    service_matches = find_service(name=b'OBEX Object Push')
    if len(service_matches) == 0:
        print Messages.can_not_find_service
        sys.exit(0)
    else:
        print Messages.service_is_found


def look_for_all_nearby_devices():
    print "performing inquiry..."
    nearby_devices = discover_devices(lookup_names=True)
    print "found %d devices" % len(nearby_devices)
    for name, mac_address in nearby_devices:
        print " %s - %s" % (mac_address, name)


def cmd_line(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def create_MAC_and_RSSI_dictionary(s):
    dictionary = {}
    for line in s.split('\n'):
        line = line.strip()
        count = 0
        for i in line:
            if i == " ":
                count = count + 1
                words = line.split(' ')
                if count % 2 == 1:
                    dictionary[words[2]] = words[7]
                else:
                    dictionary[words[2]] = words[6]
    return dictionary


def sendFile():
    print "will send a file"
