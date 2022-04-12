numero = int(input("Ingrese un numero entero: "))
#Version 1 con un iterador
suma = 0
for n in range(numero): #Esta estructura ejecuta el codigo indentado una cantidad de veces igual al numero ingresado.
    suma += n #Aca le sumamos "n" a la variable "suma". "n" va a tomar todos los valores entre 0 y el numero que se encuentre dentro de "range()", con el 0 inclusive. Esto significa que si numero es igual a 3, n va a ser igual a 0, despues a 1 y despues a 2.
    print(f"El valor de n es: {n}") #Esto lo puse puramente para que puedan ver los valores que va tomando "n", no es necesario para resolver el problema.
suma += numero #Una vez que terminamos de sumar todos los numeros entre 0 y el numero ingresado a la suma, le sumamos el numero ingresado. Por que? Porque el "for" suma todos los numeros HASTA el numero ingresado, pero no INCLUSIVE, por lo que se lo tenemos que sumar nosotros a la variable manualmente.
print(f"La suma de todos los numeros naturales hasta el {numero} inclusive es igual a: {suma}")
#Version 2 con formula matematica
suma2 = (numero * (numero+1)) /2 #La unica cosa para recalcar aca es que el resultado va a ser un numero real, no entero, asi que cuando lo mostremos va a mostrar sus decimales (que deberian ser 0)
print(f"La suma de todos los numeros naturales hasta el {numero} inclusive es igual a: {suma2}")