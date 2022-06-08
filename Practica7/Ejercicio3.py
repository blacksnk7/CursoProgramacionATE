import os

def count_M(file_path):
    counter = 0
    file_name = os.path.join(file_path, 'mf1.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            if (line[0].lower() == 'm'):
                counter += 1
    print(f'La cantidad de lineas que comienzan con la letra "M" dentro del texto fue de: {counter} lineas')
        