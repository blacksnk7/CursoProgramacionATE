def maximo(num1, num2): #Esta funcion recibe dos datos y devuelve el mayor entre ellos. Si se fijan es identica a la del ejercicio 3
    if (num1 > num2): #Si los numeros son iguales, entonces va a ignorar este codigo indentado y se va a mandar por el "else".
        return num1
    else:
        return num2

def minimo(num1, num2): #Esta funcion es la inversa de la anterior. Recibe dos numero y devuelve cual es el menor de entre los dos.
    if (num1 < num2): #Nuevamente, si ambos numeros son iguales este codigo indentado no se ejecuta y en su lugar ejecuta el del "else".
        return num1
    else:
        return num2
    
num = int(input("Ingrese un numero entero positivo: "))
#Hay varias vormas de resolver este ejercicio. Una de ellas es hacer que min y max tomen el primer valor ingresado. Asi nos aseguramos que si el programa se corre una unica ves (osea ingresan un numero positivo y despues uno negativo), tanto min como max van a tomar el primer valor ingresado.
min, max = num, num #Esta es una forma mas comoda para asignar varios valores. Lo que estamos diciendo aca es que min y maximo sean iguales a num. Ponemos "num" dos veces porque la asignacion de valores funciona por pares, osea, min tiene que ser igual a un valor propio y max tiene que ser igual a otro valor propio, los valores pueden ser iguales, pero tienen que ser la misma cantidad que variables fueron declaradas.
while (num >= 0): #Aca decimos "mientras num sea mayor O igual a cero, ejecuta el codigo indentado". El programa solo sale de este "while" cuando se ingrese un numero menor que cero (es decir, negativo) 
    max = maximo(num, max) #Aca finalmente llamamos a la funcion "maximo()" con dos valores: el numero ingresado y el numero maximo guradado hasta este momento. La funcion nos va a devolver cual de los dos numeros es el mayor, por lo que el resultado de la funcion lo vamos a guardar en la variable "max".
    min = minimo(num, min) #Aca hacemos exactamente lo mismo que arriba pero para calcular el numero minimo.
    num = int(input("Ingrese un numero entero positivo: "))
print(f"El menor numero ingresado fue el: {min}. Mientras que el mayor fue el: {max}")