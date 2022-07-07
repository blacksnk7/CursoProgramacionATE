import os
import string as st

def read_text():
    text = ''
    line = input('Ingrese lineas de texto. Para terminar, ingrese la linea "@fin"\n').lower()
    while ('@fin' not in line):
        text += line + '\n'
        line = input('Ingrese lineas de texto. Para terminar, ingrese la linea "@fin"\n').lower()
    line = line.replace('@fin', '')
    if (len(line) != 0):
        text += line
    return text

def in_spanish_no_duplicates(text):
    '''
    This function shows all words in the text that are not found inside the "spanish.lst" file.
    '''
    path = os.path.join(os.getcwd(), 'spanish.lst')
    try:
        file = open(path, mode="r", encoding="utf-8")
    except FileNotFoundError:
        return print(f'El archivo "{path}" no existe')
    except:
        return print('Error inesperado.')
    spanish = file.read()
    non_spanish = []
    word_list = list(dict.fromkeys(text.split()))
    for elem in word_list:
        if (elem not in spanish):
            non_spanish.append(elem)
    for elem in non_spanish:
        print(f'La palabra "{elem}" no se encuentra dentro del archivo de palabras.')
    print(f'En total, {len(non_spanish)} palabras no se encontraron dentro del archivo.')

def remove_tilde(text):
    tilde = 'áéíóú'
    no_tilde = 'aeiou'
    for elem in range(len(tilde)):
        text = text.replace(tilde[elem], no_tilde[elem])
    return text

def remove_punctuation(text):
    punct = st.punctuation
    for elem in punct:
        text = text.replace(elem, '')
    return text
