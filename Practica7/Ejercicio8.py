import os

def exchange_words(file_path, old, new):
    old_file = os.path.join(file_path, 'mf1.txt')
    new_file = os.path.join(file_path, 'mf1-a.txt')
    with open(old_file, 'r', encoding='utf-8') as data:
        words = data.read()
        if (old in words):
            new_words = words.replace(old, new)
            with open(new_file, 'w') as new_data:
                new_data.write(new_words)
        else:
            print(f'La palabra: {old} no existe dentro del archivo. Ningun archivo nuevo fue creado.')
    