from bluetooth import *

# Create the client socket
client_socket = BluetoothSocket(RFCOMM)

client_socket.connect(("5C:F3:70:6C:72:02", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
