# coding=utf-8
from subprocess import PIPE, Popen

from bluetooth import *

from Messages import *


def find_obex_services_devices():
    service_matches = find_service(name=b'OBEX Object Push')
    number_of_obex_devices = len(service_matches)
    if number_of_obex_devices == 0:
        print Messages.can_not_find_service
        sys.exit(0)
    else:
        print str(number_of_obex_devices) + " " + Messages.service_is_found


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


def filtering(list_of_trusted_devices, dictionary):
    flag = False
    for key, val in dictionary.iteritems():
        for i in list_of_trusted_devices:
            checking_key_and_rssi(i, key, val)


def checking_key_and_rssi(i, key, val):
    if key == i and int(val) > 50:
        flag = True
        sendFile()
    else:
        flag = False
