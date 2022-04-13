#Recuerden siempre que las funciones se deberian declarar al principio del programa. Lo unico que deberia venir antes es "import" en caso de que estemos importando alguna libreria.
def saludo(nom): #Esta funcion recibe un nombre y simplemente lo saluda.
    print(f"¡Hola {nom}!")
    
nombre = input("Ingrese su nombre: ")
saludo(nombre) #Aca llamamos a la funcion. Como la funcion no devuelve nada (no tiene "return") no tenemos que igualar ninguna variable a la funcion, con simplemente llamarla esta se va a ejecutar.