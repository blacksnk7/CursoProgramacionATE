import os
import string as st

def read_text():
    '''
    This function reads a text from console and returns the text as a single string.
    '''
    text = ''
    line = input('Ingrese lineas de texto. Para terminar, ingrese la linea "@fin"\n').lower()
    while ('@fin' not in line):
        text += line + '\n'
        line = input('Ingrese lineas de texto. Para terminar, ingrese la linea "@fin"\n').lower()
    line = line.replace('@fin', '')
    if (len(line) != 0):
        text += line
    return text

def read_file(file_name):
    '''
    This function reads a text file and converts it into lower case, removes any tildes and any punctuation symbols.
    It then checks how many words inside the file are missing in the "spanish.lst" file and returns a list with
    all missing words.
    '''
    path = os.path.join(os.getcwd(), file_name)
    non_spanish = []
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
        text = remove_tilde(text)
        text = remove_punctuation(text)
        non_spanish = in_spanish_no_duplicates(text)
    file.close()
    return non_spanish

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
    file.close()
    return non_spanish

def remove_tilde(text):
    '''
    This function removes any tildes from all vocals inside the text.
    '''
    tilde = 'áéíóú'
    no_tilde = 'aeiou'
    for elem in range(len(tilde)):
        text = text.replace(tilde[elem], no_tilde[elem])
    return text

def remove_punctuation(text):
    '''
    This function removes any puntuation symbols from the text.
    '''
    punct = st.punctuation
    for elem in punct:
        text = text.replace(elem, '')
    return text

def add_to_dict(file_name, word):
    '''
    This function adds the string "word" into a file with the name "file_name".
    '''
    path = os.path.join(os.getcwd(), file_name)
    try:
        file = open(path, mode="a", encoding="utf-8")
    except FileNotFoundError:
        return print(f'El archivo "{path}" no existe')
    except:
        return print('Error inesperado.')
    file.write(word)
    file.close()

def in_dictionary(file_name, word):
    '''
    This functions checks if the string "word" is found inside the file "file_name"
    '''
    path = os.path.join(os.getcwd(), file_name)
    try:
        file = open(path, mode="r", encoding="utf-8")
        spanish_words = file.read()
    except FileNotFoundError:
        return print(f'El archivo "{path}" no existe')
    except Exception as exception:
        return print(exception)
    if (word in spanish_words):
        file.close()
        return True
    else:
        file.close()
        return False

def replace_in_textfile(file_name, old_word, new_word):
    '''
    This function replaces the string "old_word" for "new_word" inside the file "file_name". If the "old_word" doesnt exist then no changes are
    made.
    '''
    path = os.path.join(os.getcwd(), file_name)
    try:
        file = open(path, mode="r+", encoding="utf-8")
        old_text = file.read()
    except FileNotFoundError:
        return print(f'El archivo "{path}" no existe')
    except:
        return print('Error inesperado.')
    new_text = old_text.replace(old_word, new_word)
    file.seek(0)
    file.write(new_text)
    file.close()