# coding=utf-8
from PyOBEX.client import Client
from bluetooth import *

from Helpers import *
from Messages import *

#
# service_matches = find_service(name=b'OBEX Object Push')
# if len(service_matches) == 0:
#     print Messages.can_not_find_service
#     sys.exit(0)
# else:
#     print Messages.service_is_found
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
#
# look_for_all_nearby_devices()

# create_MAC_and_RSSI_dictionary(str(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33")))

# mystring = "18:F0:E4:3A:5A:31"


dictionary = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))

for key, val in dictionary.iteritems():
    print key
    print val
