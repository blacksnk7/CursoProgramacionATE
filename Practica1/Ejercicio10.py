saldo = 5000 #Esta variable puede valer lo que quieran, es para representar el cajero nomas.
retirar = int(input("Ingrese una cantidad a extraer de su saldo: "))
if (retirar <= saldo): #Aca el if pregunta si el monto a retirar es MENOR O IGUAL al saldo de la cuenta. De ser asi ejecuta el codigo indentado
    saldo -= retirar
    print("Ha extraido: " + str(retirar) + "$") #Aca usamos el mas en lugar de la coma porque sino nos quedaria un espacio vacio entre el numero y el simbolo de "$". Pero para usar el "+" nuestra variable tiene que ser un texto, no puede ser un numero. Ahi es donde entra el "str()". Lo que hace basicamente es transformar la variable que tenga adentro de los parentesis y convertirla a un string (una cadena de texto) 
    print("Le quedan: " + str(saldo) + "$") #Aca hacemos lo mismo que arriba
else:
    print("Error. Usted no tiene el saldo suficiente para retirar", retirar, "$. Su saldo es de:", saldo, "$") #Y aca pueden ver lo que pasa si tratan de usar comas en lugar del "+".