from bluetooth import *

from FileData import *


def run_client(host):
    setting_port = set_port(host)
    client_socket = BluetoothSocket(RFCOMM)
    client_socket.connect((host, setting_port))
    print "connect to " + host
    data = read_zip_file()
    print data
    client_socket.send(data)
    print "Finished"
    client_socket.close()


def set_port(host):
    port = 0
    if host == "5C:F3:70:6C:72:02":
        port = 2
    return port
