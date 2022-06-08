import os

def count_words(file_path):
    counter = 0
    file_name = os.path.join(file_path, 'mf1.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        words = data.read().split()
        print(f'La cantidad de palabras en el archivo es de: {len(words)} palabras.')