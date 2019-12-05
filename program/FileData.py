import os
from zipfile import ZipFile
import shutil

from Messages import *


#########################################################
#### Methods for reading/writing files
#########################################################
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


#########################################################
#### Methods for zip
#########################################################

def unzip_file(file_name):
    with ZipFile(get_current_path() + Messages.slash + "temp" + Messages.slash + file_name, 'r') as zipObj:
        zipObj.extractall('temp')


def zip_file():
    with ZipFile('files.zip', 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(os.getcwd() + Messages.slash + 'files_to_zip'):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath)


#########################################################
#### Methods for handling files
#########################################################
def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))


def get_file_list():
    files = []
    for r, d, f in os.walk(get_current_path()):
        for file in f:
            if '.zip' in file:
                files.append(os.path.join(file))
    return files


def create_directory(folder_name):
    path = os.getcwd()
    try:
        os.mkdir(path)
    except OSError:
        print ("Directory %s already existed or creation of the directory %s failed" % (path, path))
    else:
        print ("Successfully created the directory %s " % path)


def remove_directory(folder_name):
    if check_if_directory_existing(folder_name):
        shutil.rmtree(os.getcwd() + Messages.slash + folder_name)


def check_if_directory_existing(directory):
    return os.path.isdir(os.getcwd() + Messages.slash + directory)


def check_file_existing(file_name):
    file_list = get_file_list()
    if get_current_path() + Messages.slash + file_name in file_list:
        return True


def prepare_directory():
    create_directory("temp")
    create_directory("final data")


def move_file_to_directory(destination_folder_name, file_to_move):
    source_file_path = get_current_path() + Messages.slash + file_to_move
    destination_file_path = get_current_path() + Messages.slash + destination_folder_name + Messages.slash + file_to_move
    shutil.move(source_file_path, destination_file_path)


def file_manager():
    prepare_directory()
    if check_file_existing("file.zip"):
        move_file_to_directory('temp', 'file.zip')
        unzip_file("file.zip")


#########################################################
#### Methods for Certs
#########################################################
#
remove_directory('temp')
remove_directory('final data')
file_manager()