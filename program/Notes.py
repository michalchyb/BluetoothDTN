# zmiana czasu  z unixa do normalnej godziny
import time
import datetime

# time_start = datetime.time.time()
from PyOBEX.client import Client

print str(datetime.timedelta(seconds=3.69548797607e-05))

________________________________


# list_of_trusted_devices = ["18:F0:E4:3A:5A:31"]
#
# # dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))
#
# # string = "hci0 dev_found: 18:F0:E4:3A:5A:31 type BR/EDR rssi -44 flags 0x0000" + "\r\n" + "hci0 dev_found: 53:BC:CB:CA:65:81 type LE Random rssi -97 flags 0x0004" + "\r\n" + "hci0 dev_found: 64:27:37:B7:91:56 type BR/EDR rssi -68 flags 0x0000" + "\r\n" + "hci0 dev_found: 74:40:BB:98:88:A4 type BR/EDR rssi -93 flags 0x0000"
# # dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(string)
#
# # filtering(list_of_trusted_devices, dictionary_MAC_and_rssi)
#
#
# timeout = 60  # [seconds]
#
# time_start = time.time()
#
#
# WAIT_SECONDS_FOR_THREAD = 20
#
# while time.time() < time_start + timeout:
#     temp = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))
#     filtering(list_of_trusted_devices, temp)
#     time.sleep(WAIT_SECONDS_FOR_THREAD)
#
# print "end"


#########################################################
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


def read_file():
    f = open("fileToSend.txt", "r")
    file_string = str(f.read())
    return file_string


def sendFile(name, host, port):
    print("Connecting to \"%s\" on %s" % (name, host))
    client = Client(host, port)
    client.connect()
    file_to_send = read_file()
    client.put("fileToSend.txt", file_to_send)
    client.disconnect()

def run_client(name, host, port):
        # Create the client socket
        client_socket = BluetoothSocket(RFCOMM)
        client_socket.connect(("5C:F3:70:6C:72:02", 3))
        client_socket.send("Hello World")
        print ("Finished")
        client_socket.close()


----------------------------------------------------------------------------------------------------------------------

# coding=utf-8
import time
from Helpers import *
from Messages import *
from Server import *
from Client import *

# temporary_string_with_tests_values = "hci0 dev_found: 18:F0:E4:3A:5A:31 type BR/EDR rssi -44 flags 0x0000" + "\r\n" + "hci0 dev_found: 53:BC:CB:CA:65:81 type LE Random rssi -97 flags 0x0004" + "\r\n" + "hci0 dev_found: 64:27:37:B7:91:56 type BR/EDR rssi -68 flags 0x0000" + "\r\n" + "hci0 dev_found: 74:40:BB:98:88:A4 type BR/EDR rssi -93 flags 0x0000"

dictionary = {'FC:03:9F:41:0C:49': '-92', '64:27:37:B7:91:56': '-65', '18:F0:E4:3A:5A:31': '-45',
              '74:40:BB:98:88:A4': '-96', '59:AF:54:17:09:22': '-93', '5C:F3:70:6C:72:02': '-90'}
list_of_trusted_devices = ["18:F0:E4:3A:5A:31", "5C:F3:70:6C:72:02"]

PROGRAM_WILL_WORK_FOR_THIS_TIME = 60  # [seconds]
PROGRAM_TIME_START = time.time()
WAIT_SECONDS_FOR_THREAD = 15
rssi_value = -50

print ("start of program")
while time.time() < PROGRAM_TIME_START + PROGRAM_WILL_WORK_FOR_THIS_TIME:
    # temp = create_MAC_and_RSSI_dictionary(cmd_line(Messages.linux_command_for_searching_devices))
    # temp = create_MAC_and_RSSI_dictionary(cmd_line(temporary_string_with_tests_values))

    # list of all devices around and getting rssi
    temp = dictionary

    # list of all devices around with OBEX protocol
    obex_devices_which_can_send_and_receive_messages = find_obex_services_devices()

    main(list_of_trusted_devices, temp, obex_devices_which_can_send_and_receive_messages, rssi_value)
    time.sleep(WAIT_SECONDS_FOR_THREAD)

print ("end of program")

---------------------------------------------
f = open("test.zip", "rb")
num = f.read()
print (num)
f.close()

f = open("photo.zip", "wb")
f.write(num)
f.close()