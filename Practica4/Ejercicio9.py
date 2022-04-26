import random
personas = []
pares = []
total = int(input("Ingrese la cantidad de personas que van a jugar: "))
for i in range(total):
    nom = input(f"Ingrese la persona numero {i+1}: ")
    personas.append(nom)
mitad = total // 2
for i in range(mitad):
    nom1 = random.choice(personas)
    personas.remove(nom1)
    nom2 = random.choice(personas)
    personas.remove(nom2)
    par = (nom1, nom2)
    pares.append(par)
if ((total % 2) != 0):
    nom = personas.pop()
    par = (nom, "Cristian")
    pares.append(par)
print(pares)
