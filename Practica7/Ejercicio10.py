import os

#No me gusta esta solucion. Estoy abriendo el archivo dos veces. Pero no pude hacerlo andar de otra forma.
def capitalize_file(file_path):
    file_name = os.path.join(file_path, 'mf1.txt')
    new_text = ""
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            new_text += line.capitalize()
    with open(file_name, 'w', encoding='utf-8') as new_data:
        new_data.write(new_text)