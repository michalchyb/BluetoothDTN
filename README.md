# BluetoothDTN


Installation PyObex and PyBluez
First step

To install the package alongside other packages and modules in your Python installation, unpack the contents of the archive. At the command line, enter the directory containing the setup.py script and install it by typing the following::

python setup.py install

You may need to become the root user or administrator to do this.


# Available ports

bluetooth RFCOMM ports only go up to 25. Every other is simply an 'Invalid Argument'


# String error

Traceback (most recent call last):
  File "rfcomm-client.py", line 41, in <module>
    sock.connect((host, port))
  File "<string>", line 5, in connect
bluetooth.btcommon.BluetoothError: (22, 'Invalid argument')

# Start OBEX
sudo obexpushd -B -n