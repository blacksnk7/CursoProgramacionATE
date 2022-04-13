#Finalmente estamos usando funciones y librerias (es decir, importando cosas). Fijense que incluso antes que las funciones viene el import.
import random #Esto siempre primero de todo en el programa

def dado6(): #Ahora si viene la funcion. Esta funcion lo unico que hace es devolveer un numero aleatorio entre el 1 y el 6. Fijense que no recibe nada, solo devuelve un numero.
    return random.randint(1, 6)

jugador = int(input("Ingrese un numero entero entre el 1 y el 6: "))
#Este "while" tambien podria ser una funcion que no devuelva nada y simplemente imprima "acertaste" cuando el dado y el jugador tienen el mismo valor. Por que no lo hice asi? Porque el chiste de las funciones es re-utilizar codigo que se va a usar varias veces a lo largo del programa. En este ejemplo, la funcion "dado6()" se llama cada vez que tengamos que comparar si el numero ingresado en "jugador" es igual o distinto al del dado. Tener una funcion que solo se ejecuta una vez no suele ser demasiado util en un programa tan cortito. Cuando tengamos programas con cientos o miles de lineas de codigo, ahi va a tener mas sentido tener funciones que se llamen una unica vez para que el codigo sea mas facil de leer.
while (dado6() != jugador): #Aca en lugar de guardar el valor que nos devuelve la funcion "dado6()" en una variable y despues preguntar si esa variable es igual a "jugador", directamente preguntamos si el valor que nos devuelve la funcion "dado6()" es igual al valor guardado en la variable "jugador". Mientras no sean iguales, se ejecuta el codigo indentado.
    jugador = int(input("Ingrese un numero entero entre el 1 y el 6: "))
print("Acertaste!")