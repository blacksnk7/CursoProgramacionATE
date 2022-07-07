import os
import functions as func

option = input('Elija 1 o 2 segun prefiera: \n1 - Ingresar el texto por pantalla. \n2 - Ingresar el nombre de un archivo de texto (el archivo se debe encontrar dentro de la carpeta "main" o se producira una excepcion). \n')
while (option != '1') and (option != '2'):
    print('Opcion no valida. Seleccione nuevamente.')
    option = input('Elija 1 o 2 segun prefiera: \n1 - Ingresar el texto por pantalla. \n2 - Ingresar el nombre de un archivo de texto (el archivo se debe encontrar dentro de la carpeta "main" o se producira una excepcion). \n')
if (option == '1'):
    text = func.read_text()
    text = func.remove_tilde(text)
    text = func.remove_punctuation(text)
    func.in_spanish_no_duplicates(text)
else:
    file_name = input('Ingrese el nombre del archivo con la extension (ej: texto.txt): ')
    path = os.path.join(os.getcwd(), file_name)
    try:
        file = open(path, mode="r", encoding="utf-8")
        end = False
    except FileNotFoundError:
        print(f'El archivo "{file_name}" no existe')
        end = True
    except:
        print('Error inesperado')
        end = True
    if (not end):
        text = file.read().lower()
        text = func.remove_tilde(text)
        text = func.remove_punctuation(text)
        func.in_spanish_no_duplicates(text)