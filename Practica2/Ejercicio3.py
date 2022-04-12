nombre = input("Ingrese su nombre: ")
contador = 1 #Esta variable va a contar cuanta gente llego hasta que llego Juan. Como a Juan tambien hay que contarlo la inicializamos en 1 en lugar de 0.
while (nombre != "Juan"): #Esto pregunta si el nombre ingresado es distinto de "Juan". De no ser asi, ejecuta el codigo indentado. Ojo, que "juan" con minusculas no es igual a "Juan" con mayuscula.
    nombre = input("Ingrese su nombre: ")
    contador += 1 #Incrementamos el valor del contador en +1.
print(f"Llegaron {contador} personas") #Esto se llama formateo de texto. Lo que hacemos es poner una "f" antes de las comillas, y una vez adentro de las comillas ponemos las variables que queremos mostrar entre llaves {}. Esto es para que quede mas lindo el texto y de paso no tenemos que andar complicandonos con comas o "+" ni nada de eso.