# coding=utf-8
from subprocess import PIPE, Popen

from bluetooth import *
from Client import *
from Server import *
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
        # temp_list = []
        # for i in service_matches:
        #     # host = i["host"]
        #     temp_list.append(get_host_data(i))
        # return temp_list


def look_for_all_nearby_devices():
    print "performing inquiry..."
    nearby_devices = discover_devices(lookup_names=True)
    print "found %d devices" % len(nearby_devices)
    for name, mac_address, port in nearby_devices:
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


def sendFile(name):
    print("Connecting to \"%s\"" % name)
    run_client(name)


def get_host_data(device):
    host = device["host"]
    port = device["port"]
    name = device["name"]
    protocol = device["protocol"]
    return host, name, port, protocol


def get_mac_addresses(obex_devices):
    lists_mac_addresses_in_obex_devices = []
    for service in obex_devices:
        lists_mac_addresses_in_obex_devices.append(service['host'])
    return lists_mac_addresses_in_obex_devices


def check_conditions_for_sending_and_send_file(host, key, port, rssi_value, val):
    # if key == host and val > rssi_value:
    if val > rssi_value:
        sendFile(host)
    else:
        print "rssi conditions check :  FALSE"


def main(list_of_trusted_devices, dictionary, obex_devices, rssi_value):
    for key, val in dictionary.iteritems():
        mac_list_obex_devices = get_mac_addresses(obex_devices)
        if key in list_of_trusted_devices and key in mac_list_obex_devices:
            for device in obex_devices:
                if key == device['host']:
                    host, name, port, protocol = get_host_data(device)
                    check_conditions_for_sending_and_send_file(host, key, port, rssi_value, val)
