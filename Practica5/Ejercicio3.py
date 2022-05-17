#Ignora si el caracter ingresado esta en mayuscula o minuscula
def number_of_chars(word, char):
    word = word.lower()
    char = char.lower()
    return word.count(char)

word = input("Ingrese una cadena de caracteres: ")
char = input("Ingrese un caracter a buscar en la cadena: ")
print(f"El caracter '{char}' aparece {number_of_chars(word, char)} veces dentro de la cadena")