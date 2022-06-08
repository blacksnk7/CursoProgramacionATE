import os

def count_upper(file_path):
    counter = 0
    file_name = os.path.join(file_path, 'mf1.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        words = data.read()
        for letter in words:
            if (letter == letter.upper()):
                counter += 1
    print(f'La cantidad de letras mayusculas dentro del archivo es de: {counter} letras')