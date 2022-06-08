import os

def print_file(file_path):
    file_name = os.path.join(file_path, 'archivo.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(line)