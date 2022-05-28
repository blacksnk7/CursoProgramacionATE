money = {'Dolar':'$', 'Euro':'€', 'Yen':'¥', 'Peso argentino':'$'}
option = input("Ingrese el nombre de una divisa para saber su simbolo: ").capitalize()
try:
    print(f"El simbolo de la divisa {option} es: {money[option]}")
except KeyError:
    print(f"La divisa '{option}' no se encuentra dentro de nuestro diccionario.")
except:
    print("Error inesperado")