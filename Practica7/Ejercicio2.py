import os

def print_lines(file_path, n):
    file_name = os.path.join(file_path, 'archivo.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        for i in range(n):
            line = data.readline()
            if (line != ""):
                print(line)