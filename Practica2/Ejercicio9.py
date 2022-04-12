import random #Primero importamos la libreria para poder generar un numero aleatorio.

dado = random.randint(1, 6) #Aca usamos dicha libreria para generar un numero aleatorio entre el 1 y el 6 y lo guardamos en la variable "dado"
jugador = int(input("Ingrese un numero entero entre el 1 y el 6: "))
while (dado != jugador): #Esta estructura pregunta si el numero guardado en "dado" es igual al numero guardado en "jugador". Si son distintos, ejecuta el codigo indentado.
    dado = random.randint(1, 6) #Cramos un nuevo valor aleatorio entre el 1 y el 6
    jugador = int(input("Ingrese un numero entero entre el 1 y el 6: "))
print("Acertaste!")