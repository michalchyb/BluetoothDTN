# coding=utf-8
import time
from Helpers import *
from Messages import *

# temporary_string_with_tests_values = "hci0 dev_found: 18:F0:E4:3A:5A:31 type BR/EDR rssi -44 flags 0x0000" + "\r\n" + "hci0 dev_found: 53:BC:CB:CA:65:81 type LE Random rssi -97 flags 0x0004" + "\r\n" + "hci0 dev_found: 64:27:37:B7:91:56 type BR/EDR rssi -68 flags 0x0000" + "\r\n" + "hci0 dev_found: 74:40:BB:98:88:A4 type BR/EDR rssi -93 flags 0x0000"

dictionary = {'FC:03:9F:41:0C:49': '-92', '64:27:37:B7:91:56': '-65', '18:F0:E4:3A:5A:31': '-45', '74:40:BB:98:88:A4': '-96', '59:AF:54:17:09:22': '-93', 'AC:7A:4D:C9:F7:CF': '-90'}

list_of_trusted_devices = ["18:F0:E4:3A:5A:31"]

PROGRAM_WILL_WORK_FOR_THIS_TIME = 60  # [seconds]
PROGRAM_TIME_START = time.time()
WAIT_SECONDS_FOR_THREAD = 15
RSSI_VALUE = -50

print "start of program"
while time.time() < PROGRAM_TIME_START + PROGRAM_WILL_WORK_FOR_THIS_TIME:
    # temp = create_MAC_and_RSSI_dictionary(cmd_line(temporary_string_with_tests_values))
    obex_devices = find_obex_services_devices()
    # temp = create_MAC_and_RSSI_dictionary(cmd_line(Messages.linux_command_for_searching_devices))
    temp = dictionary
    main(list_of_trusted_devices, temp, obex_devices, RSSI_VALUE)
    time.sleep(WAIT_SECONDS_FOR_THREAD)

print "end of program"
