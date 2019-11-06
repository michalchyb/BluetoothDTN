from bluetooth import *

# Create the client socket
client_socket = BluetoothSocket(RFCOMM)

client_socket.connect(("64:27:37:b7:91:55", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
