def read_file():
    with open('fileToSend.txt', 'r') as file:
        data = file.read().replace('\n', '')
        return data


def write_file(data):
    with open("receivedFile.txt", "w") as text_file:
        text_file.write(data)
