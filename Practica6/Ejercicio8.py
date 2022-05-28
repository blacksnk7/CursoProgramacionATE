def tupla(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return tuple(lista)

n = int(input("Ingrese la cantidad de elementos para la tupla: "))
print(tupla(n))