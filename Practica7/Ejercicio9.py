import os

def create_new_file(file_path):
    name = input('Ingrese el nombre (con la extension) de este nuevo archivo: ')
    new_file = os.path.join(file_path, name)
    with open(new_file, 'w', encoding='utf-8') as data:
        line = input('Ingrese lineas de texto. Al ingresar una linea que solo contenga la palabra "fin" el programa terminara: ')
        while (line.lower() != 'fin'):
            data.write(line)
            line = input()
        data.write(line)