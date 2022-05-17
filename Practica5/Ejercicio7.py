#Creo una nueva lista y le copio los valores de la lista original para no cambiar el orden de la lista original. Si usamos "sort" directamente sobre la primer lista entonces esta va a quedar ordenada, cambiando su orden original.
def max_and_min(elements):
    sorted_elements = elements.copy()
    sorted_elements.sort()
    return sorted_elements[0], sorted_elements[-1]

elements = [23, 56, 11, 677, 0, 77, 44, 33]
min, max = max_and_min(elements)
print(f"El maximo de la lista {elements} es: {max}\nEl minimo de la lista {elements} es: {min}")