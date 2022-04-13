def esCero(num): #Esta funcion recibe un numero. Si el numero es igual a 0 entonces la funcion devuelve un booleano (un dato que solo tiene 2 valores: Verdadero o Falso).
    if (num == 0):
        return True  #Si el numero es igual a 0 la funcion devuelve "True" es decir "Verdadero"
    else:
        return False #Si el numero NO es igual a 0 la funcion devuelve "False" es decir "Falso"
    
num = int(input("Ingrese un numero: "))
if (esCero(num)): #Como nuestra funcion nos devuelve un dato, podemos simplemente llamarla adentro del "if". Esta linea de codigo lo que hace primero que nada es llamar a la funcion "esCero()", la funcion devuelve un valor booleano que el codigo luego utiliza para el if. En lugar de preguntar si algo es igual, distinto, etc. de otra cosa lo que hacemos es preguntar "if booleano", o en casellano "si verdadero/falso". En caso de ser verdadero se va a ejecutar el codigo indentado, caso contrario se ejecuta el codigo indentado dentro del "else".
    print(f"El numero ingresado {num} es igual cero")
else:
    print(f"El numero ingresado {num} no es igual a cero")