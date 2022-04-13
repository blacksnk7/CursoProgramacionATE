def mayor(num1, num2): #Esta funcion recibe dos numeros, pregunta si el primero es mayor que el segundo y de cer cierto lo devulve, sino, devuelve el segundo.
    if (num1 > num2): #Como preguntamos si el 1er numero es MAYOR que el segundo, en caso de que ambos sean iguales la funcion devolvera el segundo valor (por mas que tecnicamente no sea mayor que el primero.)
        return num1
    else:
        return num2
    
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
print(f"Entre el {num1} y el {num2} el {mayor(num1, num2)} es igual o mas grande")