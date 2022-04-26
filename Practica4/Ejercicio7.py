palabras = []
total = int(input("Ingrese el total de palabras para agregar a la lista: "))
for i in range(total):
    pal = input(f"Ingrese la palabra numero {i+1}: ")
    palabras.append(pal)
palabras.sort()
pal = input("Ingrese una palabra a buscar en la lista: ")
total = palabras.count(pal)
print(f"La palabra '{pal}' aparece {total} veces dentro de la lista")