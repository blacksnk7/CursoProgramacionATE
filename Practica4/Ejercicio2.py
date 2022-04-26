import random
lista = []
for i in range(100):
    num = random.randint(-1000, 1000)
    lista.append(num)
total = 0
for elem in lista:
    total += elem
promedio = total / 100
print(f"La suma total de los numeros dentro de la lista es de: {total}.\nEl promedio de los numeros dentro de la lista es de: {promedio}")