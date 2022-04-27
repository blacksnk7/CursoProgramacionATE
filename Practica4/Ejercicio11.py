import random

def llenar_mazo():
    cartas = []
    numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    for i in range(4):
        for num in numeros:
         cartas.append(num)
    return cartas

def jugar(total):
    jugadores = []
    for i in range(total):
        jugadores.append(0.0)
    actual = 0
    ant = actual
    while (len(cartas) != 0) and (actual < total):
        if (ant == actual):
            ant += 1
            print(f"------------\nTurno del jugador {actual+1}")
        pos = random.randint(0, (len(cartas)-1))
        carta = cartas.pop(pos)
        if (carta >= 10):
            valor = 0.5
        else:
            valor = carta
        jugadores[actual] += valor
        if (jugadores[actual] <= 7.5):
            basta = input(f"Usted acaba de agarrar un {carta}. Su puntuacion actual es de: {jugadores[actual]}.\nDesea agarrar otra carta? Y/N ")
        else:
            print(f"Te pasaste! Tu puntuacion es: {jugadores[actual]}")
            actual += 1
        if (basta.lower() == "n"):
            actual += 1
            basta = "y"
    return jugadores

cartas = llenar_mazo()
total = int(input("Ingrese el numero de jugadores (minimo 2): "))
if (total >= 2):
    jugadores = jugar(total)
    max = -1
    ganador = -1
    for i in range(total):
        act = jugadores[i]
        if (act <= 7.5) and (act >= max):
            ganador = i
    print(f"------------\nGano el jugador numero {ganador+1} con un puntaje de {jugadores[ganador]}")
else:
    print("Deben haber un minimo de 2 jugadores...")
