import os

def count_times(file_path, word):
    file_name = os.path.join(file_path, 'mf1.txt')
    with open(file_name, 'r', encoding='utf-8') as data:
        words = data.read().split()
        print(f'La cantidad veces que aparece la palabra "{word}" es de: {words.count(word)} veces.')