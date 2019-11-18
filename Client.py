from bluetooth import *


def run_client(name, host, port):
    # Create the client socket
    client_socket = BluetoothSocket(RFCOMM)
    client_socket.connect((host, port))
    print "connect to " + host
    client_socket.send("Hello World")
    print "Finished"
    client_socket.close()
