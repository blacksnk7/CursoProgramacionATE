money = {'Dolar':119.40, 'Euro':128.07, 'Yen':0.94, 'Peso argentino':1}
ammount = float(input("Ingrese el monto en pesos a convertir: "))
key = input("Ingrese la divisa a convertir: ").capitalize()
if (key in money):
    conversion = ammount / money[key]
    print(f"{ammount} pesos equivalen a: {round(conversion, 2)} {key}")
else:
    print(f"La divisa '{key}' no se encuentra dentro de nuestro diccionario.")
