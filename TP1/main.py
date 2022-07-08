import os
import sys
import functions as func

if (len(sys.argv) == 1):
    option = input('Elija 1 o 2 segun prefiera: \n1 - Ingresar el texto por pantalla. \n2 - Ingresar el nombre de un archivo de texto (el archivo se debe encontrar dentro de la carpeta "main" o se producira una excepcion). \n')
    while (option != '1') and (option != '2'):
        print('Opcion no valida. Seleccione nuevamente.')
        option = input('Elija 1 o 2 segun prefiera: \n1 - Ingresar el texto por pantalla. \n2 - Ingresar el nombre de un archivo de texto (el archivo se debe encontrar dentro de la carpeta "main" o se producira una excepcion). \n')
    if (option == '1'):
        text = func.read_text()
        text = func.remove_tilde(text)
        text = func.remove_punctuation(text)
        wrong_words = func.in_spanish_no_duplicates(text)
    else:
        file_name = input('Ingrese el nombre del archivo con la extension (ej: texto.txt): ')
        wrong_words = func.read_file(file_name)
else:
    file_name = sys.argv[1]
    wrong_words = func.read_file(file_name)
if (len(wrong_words) > 0):
    dict_name = 'spanish.lst'
    for elem in wrong_words:
        choice = input(f'Elija una opcion: \n1 - Agregar la palabra "{elem}" al archivo {dict_name}.\n2 - Corregir la palabra "{elem}".\n3 - Ignorar.\n4 - Salir.\n')
        while (choice not in ['1', '2', '3', '4']):
            print('Error. Opcion no permitiva. Ingrese nuevamente.')
            choice = input(f'Elija una opcion: \n1 - Agregar la palabra "{elem}" al archivo {dict_name}.\n2 - Corregir la palabra "{elem}".\n3 - Ignorar.\n4 - Salir.\n')
        match choice:
            case '1':
                func.add_to_dict(dict_name, elem)
            case '2':
                new_word = input(f'Ingrese una palabra para reemplazar "{elem}": ')
                while (not func.in_dictionary(dict_name, new_word)):
                    new_word = input(f'La palabra {new_word} no se encuentra dentro del diccionario. Ingrese otra palabra: ')
                if ((len(sys.argv) > 1) or (option == '2')):
                    func.replace_in_textfile(file_name, elem, new_word)
            case '4':
                break