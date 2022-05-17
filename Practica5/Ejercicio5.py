def proper_names(names):
    print("Las personas son: ")
    for elem in names:
        elem = elem.lower()
        elem = elem.capitalize()
        print(elem)
    
names = []
name = input("Ingrese un nombre: ")
while (name != ""):
    names.append(name)
    name = input("Ingrese un nombre: ")
proper_names(names)