# coding=utf-8
from Helpers import *

from RssiDetection import *

dictionary = {'FC:03:9F:41:0C:49': '-92', '64:27:37:B7:91:56': '-65', '18:F0:E4:3A:5A:31': '-45',
              '74:40:BB:98:88:A4': '-96', '59:AF:54:17:09:22': '-93', '5C:F3:70:6C:72:02': '-90'}

list_of_available_devices_to_send_file = ["18:F0:E4:3A:5A:31", "5C:F3:70:6C:72:02", "5C:F3:70:6C:73:3B"]

PROGRAM_WILL_WORK_FOR_THIS_TIME = 60  # [seconds]
PROGRAM_TIME_START = time.time()
WAIT_SECONDS_FOR_THREAD = 15
rssi_value = -100

# simple inquiry example

print("program starting...")
while time.time() < PROGRAM_TIME_START + PROGRAM_WILL_WORK_FOR_THIS_TIME:
    # list of all devices around and getting rssi
    # wszystkie w poblizu
    devices_in_bluetooth_range = device_inquiry_with_with_rssi.__globals__.get('dictionary')
    # te które są obexem
    obex_devices_which_can_send_and_receive_messages = find_obex_services_devices()

    main(list_of_available_devices_to_send_file, {},
         obex_devices_which_can_send_and_receive_messages, rssi_value)
    time.sleep(WAIT_SECONDS_FOR_THREAD)

print("program ending...")
