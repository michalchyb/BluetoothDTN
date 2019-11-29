def read_file():
    with open('fileToSend.txt', 'r') as file:
        data = file.read().replace('\n', '')
        return data


def write_file(data):
    with open("receivedFile.txt", "w") as text_file:
        text_file.write(data)


def read_zip_file():
    f = open("file.zip", "rb")
    file = f.read()
    print (file)
    f.close()


def write_zip_file(data):
    f = open("file.zip", "wb")
    f.write(data)
    f.close()
