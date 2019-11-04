def read_file():
    with open('file.txt', 'r') as file:
        data = file.read().replace('\n', '')
        return data
