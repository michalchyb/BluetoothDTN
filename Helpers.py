# coding=utf-8
from subprocess import PIPE, Popen

from PyOBEX.client import Client
from bluetooth import *

from Messages import *


def find_obex_services_devices():
    print "start looking for obex devices..."
    service_matches = find_service(name=b'OBEX Object Push')
    number_of_obex_devices = len(service_matches)
    if number_of_obex_devices == 0:
        print Messages.can_not_find_service
        print "end looking for obex devices..."
        sys.exit(0)
    else:
        print str(number_of_obex_devices) + " " + Messages.service_is_found
        print "end looking for obex devices..."
        return service_matches


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
    print "start creating dictionary from command line..."
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
    print dictionary
    print "end creating dictionary from command line..."
    return dictionary


def sendFile(name, host, port):
    print("Connecting to \"%s\" on %s" % (name, host))
    client = Client(host, port)
    client.connect()
    file_to_send = read_file()
    client.put("file.txt", file_to_send)
    client.disconnect()


def read_file():
    f = open("file.txt", "r")
    file_string = str(f.read())
    return file_string


def get_host_data(device):
    host = device["host"]
    port = device["port"]
    name = device["name"]
    return host, name, port


def main(list_of_trusted_devices, dictionary, obex_devices, rssi_value):
    for key, val in dictionary.iteritems():
        for i in list_of_trusted_devices:
            for device in obex_devices:
                host, name, port = get_host_data(device)
                if key == host and val > rssi_value:
                    sendFile(name, host, port)
