def cuadrado(num): #Esta funcion recibe un numero, lo multiplica por si mismo y devuelve el resultado.
    return (num * num) #Aca podemos devolver el resultado directamente. Otra forma de hacer esto seria declarar una variable e igualarla a la multiplicacion (ejemplo: resultado = num * num)

num = int(input("Ingrese un numero entero: "))
print(f"El cuadrado {num} es: {cuadrado(num)}")