palabras = []
taboo = ["pascal", "smalltalk", "java"]
total = int(input("Ingrese el total de palabras para agregar a la lista: "))
i = 1
while (i <= total):
    pal = input(f"Ingrese la palabra numero {i}: ")
    if (pal not in taboo):
        palabras.append(pal)
    else:
        print(f"La palabra {pal} es taboo. Vuelva a intentarlo")
        i -= 1
    i += 1
palabras.sort()
print(palabras)