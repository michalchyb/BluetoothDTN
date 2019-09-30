# coding=utf-8
from PyOBEX.client import Client
from bluetooth import *

from Helpers import *
from Messages import *

# lookForAllNearbyDevices()
#
# service_matches = find_service(name=b'OBEX Object Push')
# if len(service_matches) == 0:
#     print Messages.canNotFindService
#     sys.exit(0)
# else:
#     print Messages.serviceIsFound
#
# for x in range(len(service_matches)):
#     port = service_matches[x]["port"]
#     name = service_matches[x]["name"]
#     host = service_matches[x]["host"]
#     print"--------------------------------------"
#     print (service_matches[x])
#     print "name: " + name
#     print "port: " + str(port)
#     print "host: " + host
#     print"--------------------------------------"
#
# first_match = service_matches[0]
# port = first_match["port"]
# name = first_match["name"]
# host = first_match["host"]
# print port
# print name
# print host
# print("Connecting to \"%s\" on %s" % (name, host))
# client = Client(host, port)
# client.connect()
# client.put("test.txt", "Hello world\n")
# client.disconnect()
#
# first_match = service_matches[1]
# port = first_match["port"]
# name = first_match["name"]
# host = first_match["host"]
# print port
# print name
# print host
# print("Connecting to \"%s\" on %s" % (name, host))
# client = Client(host, port)
# client.connect()
# client.put("test.txt", "Hello world\n")
# client.disconnect()
# print "End of transmission"

replace = str(cmdLine("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))\
    .replace("\n", "")\
    .replace("hci0 dev_found: ","")\
    .replace("type","")\
    .replace("flags", "")\
    .replace("rssi", "")\
    .replace("BR/EDR", "")\
    .replace("0x0000", "")\
    .replace("LE Random", "")\
    .replace("LE Public", "")\
    .replace("0x0004", "")
print replace
