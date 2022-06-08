import os

def short_words(file_path):
    counter = 0
    file_name = os.path.join(file_path, 'mf1.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        words = data.read().split()
        for word in words:
            if (len(word) < 4):
                counter += 1
    print(f'La cantidad de palabras con menos de 4 caracteres dentro del archivo es de: {counter} palabras')