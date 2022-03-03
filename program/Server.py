from bluetooth import *

from FileData import *


def run_server():
    print('Server started')
    server_socket = BluetoothSocket(RFCOMM)
    server_socket.bind(("", 2))
    server_socket.listen(2)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    write_zip_file(data)
    print("received file successfully")
    client_socket.close()
    server_socket.close()
    print('Server finished')

# run_server()
