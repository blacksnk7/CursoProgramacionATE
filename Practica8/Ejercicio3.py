class Persona:
    def __init__(self, nombre='None', edad=0):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f'Hola! Soy {self.nombre} y tengo {self.edad} anios.')

def cargar_persona():
    nombre = input("Ingrese su nombre: ")
    if (nombre == "fin"):
        edad = -1
    else:
        edad = int(input("Ingrese su edad: "))
    return nombre, edad

lista = []
per = cargar_persona()
while (per[0] != "fin"):
    lista.append(Persona(per[0], per[1]))
    per = cargar_persona()
for i in range(len(lista)):
    lista[i].presentarse()