import datetime
import difflib
import os
import re
import shutil
import time
from zipfile import ZipFile

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
        for folderName, subfolders, filenames in os.walk(get_project_directory() + 'files_to_zip'):
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
        os.mkdir(path + Messages.slash + folder_name)
    except OSError:
        print ("Directory %s already existed or creation of the directory %s failed" % (path, path))
    else:
        print ("Successfully created the directory %s " % path)


def remove_directory(folder_name):
    if check_if_directory_existing(folder_name):
        shutil.rmtree(get_project_directory() + folder_name)


def check_if_directory_existing(directory):
    return os.path.isdir(get_project_directory() + directory)


def check_file_existing(file_name):
    file_list = get_file_list()
    if get_current_path() + Messages.slash + file_name in file_list:
        return True


def prepare_directory():
    create_directory("temp")
    create_directory("repository")


def move_file_to_directory(destination_folder_name, file_to_move):
    source_file_path = get_current_path() + Messages.slash + file_to_move
    destination_file_path = get_current_path() + Messages.slash + destination_folder_name + Messages.slash + file_to_move
    shutil.move(source_file_path, destination_file_path)


#########################################################
#### Methods for Certs
#########################################################
def checking_metadata_file_present():
    counter = 0
    for file in os.listdir(get_project_directory() + 'temp'):
        if file.endswith('metadata.txt'):
            counter = counter + 1

    return counter


def get_file_list_in_directory(path):
    return os.listdir(get_project_directory() + path)


def changed_file_name():
    if checking_metadata_file_present() != 0:
        for file in os.listdir(get_project_directory() + 'temp'):
            if file.endswith('metadata.txt'):
                new_name = time.strftime("%Y%m%d-%H%M%S") + "_metadata.txt"
                path = get_project_directory() + 'temp' + Messages.slash
                os.rename(path + str(file), path + new_name)


def check_correctness_of_metadate_name():
    if checking_metadata_file_present() != 0:
        for file in os.listdir(get_project_directory() + 'temp'):
            if re.match('\d{8}-\d{6}.*', file):
                return file


def get_files_creation_date():
    temp_list = []
    for file in os.listdir(get_project_directory() + 'temp'):
        if re.match('\d{8}-\d{6}.*', file):
            data = substring_date(file)
            temp_list.append(data)
    return temp_list


def substring_date(file):
    data = datetime.datetime(int(file[0:4]), int(file[5:6]), int(file[7:8]), int(file[10:11]), int(file[12:13]),
                             int(file[14:15]))
    return data


def comparing_dates(date_list):
    if date_list[0] > date_list[1]:
        print "second file is older"
    else:
        print "first is older"


#########################################################
#### Main method
#########################################################


def file_manager():
    prepare_directory()
    if check_file_existing("file.zip"):
        move_file_to_directory('temp', 'file.zip')
        unzip_file("file.zip")


def check_if_data_existing():
    return check_file_existing("data.txt")


def get_difference_between_files():
    text1 = ""
    text2 = ""
    all_files_list = get_file_list_in_directory('temp' + Messages.slash)
    temp_list = []
    for file in all_files_list:
        if re.match('\d{8}-\d{6}.*', file):
            temp_list.append(file)

    for file in temp_list:
        text1 = open(get_project_directory() + 'temp' + Messages.slash + temp_list[0]).readlines()
        text2 = open(get_project_directory() + 'temp' + Messages.slash + temp_list[1]).readlines()

    for line in difflib.unified_diff(text1, text2):
        print line,


def get_project_directory():
    return os.getcwd() + Messages.slash


get_difference_between_files()

# remove_directory('temp')
# remove_directory('repository')
# file_manager()
