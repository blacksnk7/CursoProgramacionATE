import random
total = int(input("Ingrese el numero de jugadores: "))
jugadores = []
for i in range(total):
    nom = input("Ingrese su nombre: ")
    apuesta = int(input("Ingrse un numero de apuesta (entre el 0 y el 99): "))
    if (apuesta not in jugadores):
        nombres = [nom]
        jugadores.append(apuesta)
        jugadores.append(nombres)
    else:
        pos = jugadores.index(apuesta)
        jugadores[pos+1].append(nom)
ganador = random.randint(0, 99)
print(f"El numero ganador fue el: {ganador}")
if (ganador in jugadores):
    pos = jugadores.index(ganador) + 1
    print(f"Los ganadores fueron: {jugadores[pos]}")
else:
    print("No hubieron ganadores esta vuelta.")
