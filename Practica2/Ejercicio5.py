num = input("Ingrese un numero: ") 
total = 0 
contador = 0 #Esta variable es lo unico diferente. Aca vamos a ir contando cuantos numeros fueron leidos. Nuevamente, la inicializamos en 0 en caso de que el primer elemento leido sea un punto en lugar de un numero.
while (num != "."): 
    total += int(num) 
    contador += 1 #Sumamos 1 porque si estamos aca significa que leimos un nuevo numero
    num = input("Ingrese un numero: ")
promedio = total / contador #Dividimos la suma total de los numeros ingresados por la cantidad de numeros para calcular el promedio de los numero singresados y guardamos el resultado en una nueva variable llamada "promedio".
print(f"La suma de todos los numeros ingresados es de: {total}. \nEl promedio de dichos numeros es: {promedio}") #Nuevamente usamos formateo de texto (el f antes de las comillas). El "\n" Que esta antes de "El promedio" se llama salto de linea, basicamente le dice al programa que antes de escribir lo que viene (que aca seria "El promedio de dichos numeros es") cambie de linea y empiece a escribir desde el comienzo de la linea de abajo.