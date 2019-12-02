import os
from zipfile import ZipFile


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
    f.close()
    return file


def write_zip_file(data):
    f = open("file.zip", "wb")
    f.write(data)
    f.close()


def file_list():
    path = '/home/michalch/PycharmProjects'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.zip' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)


def unzip_file():
    with ZipFile('/home/michalch/PycharmProjects/tests/file.zip', 'r') as zipObj:
        zipObj.extractall('temp')
