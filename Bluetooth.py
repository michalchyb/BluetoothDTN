# coding=utf-8
import time
from Helpers import *
import threading

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

# look_for_all_nearby_devices()
#
# find_obex_services_devices()

list_of_trusted_devices = ["18:F0:E4:3A:5A:31"]

# dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))

# string = "hci0 dev_found: 18:F0:E4:3A:5A:31 type BR/EDR rssi -44 flags 0x0000" + "\r\n" + "hci0 dev_found: 53:BC:CB:CA:65:81 type LE Random rssi -97 flags 0x0004" + "\r\n" + "hci0 dev_found: 64:27:37:B7:91:56 type BR/EDR rssi -68 flags 0x0000" + "\r\n" + "hci0 dev_found: 74:40:BB:98:88:A4 type BR/EDR rssi -93 flags 0x0000"
# dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(string)

# filtering(list_of_trusted_devices, dictionary_MAC_and_rssi)


timeout = 60  # [seconds]

time_start = time.time()


WAIT_SECONDS_FOR_THREAD = 20

while time.time() < time_start + timeout:
    temp = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))
    filtering(list_of_trusted_devices, temp)
    time.sleep(WAIT_SECONDS_FOR_THREAD)

print "end"
