def total_words(word):
    words = word.split()
    return len(words)

word = input("Ingrese una cadena de caracteres: ")
print(f"La oracion '{word}' contiene {total_words(word)} palabras")