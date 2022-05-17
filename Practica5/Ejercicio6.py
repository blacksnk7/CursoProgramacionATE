#La funcion ignora mayusculas y minusculas
def in_word(word1, word2):
    word2 = word2.lower()
    if (word2.count(word1.lower()) > 0):
        return True
    else:
        return False

word1 = input("Ingrese una cadena de caracteres: ")
word2 = input("Ingrese una sub-cadena de caracteres: ")
if (in_word(word2, word1)):
    print(f"La subcadena '{word2}' se encuentra dentro de la cadena '{word1}'")
else:
    print(f"La subcadena '{word2}' NO se encuentra dentro de la cadena '{word1}'")