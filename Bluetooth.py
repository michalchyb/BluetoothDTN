# coding=utf-8
import time
from Helpers import *
from Messages import *

# dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(cmd_line("sudo btmgmt find |grep rssi |sort -n |uniq -w 33"))

# string = "hci0 dev_found: 18:F0:E4:3A:5A:31 type BR/EDR rssi -44 flags 0x0000" + "\r\n" + "hci0 dev_found: 53:BC:CB:CA:65:81 type LE Random rssi -97 flags 0x0004" + "\r\n" + "hci0 dev_found: 64:27:37:B7:91:56 type BR/EDR rssi -68 flags 0x0000" + "\r\n" + "hci0 dev_found: 74:40:BB:98:88:A4 type BR/EDR rssi -93 flags 0x0000"
# dictionary_MAC_and_rssi = create_MAC_and_RSSI_dictionary(string)

# filtering(list_of_trusted_devices, dictionary_MAC_and_rssi)
list_of_trusted_devices = ["18:F0:E4:3A:5A:31"]

timeout = 60  # [seconds]

time_start = time.time()

WAIT_SECONDS_FOR_THREAD = 15

print "start of program"
while time.time() < time_start + timeout:
    temp = create_MAC_and_RSSI_dictionary(cmd_line(Messages.linux_command_for_searching_devices))
    filtering_to_what_devices_send_file(list_of_trusted_devices, temp)
    time.sleep(WAIT_SECONDS_FOR_THREAD)

print "end of program"
