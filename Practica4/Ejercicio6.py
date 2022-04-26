palabras = []
total = int(input("Ingrese el total de palabras para agregar a la lista: "))
for i in range(total):
    pal = input(f"Ingrese la palabra numero {i+1}: ")
    palabras.append(pal)
palabras.sort()
print(palabras)