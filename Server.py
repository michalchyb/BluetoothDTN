from bluetooth import *
from FileData import *


def run_server(port):
    server_socket = BluetoothSocket(RFCOMM)
    server_socket.bind(("", 1))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    write_zip_file(data)
    print "received [%s]" % data
    client_socket.close()
    server_socket.close()
