num1 = int(input("Ingrese el primer numero: ")) #El "int" que esta antes del input transforma el texto que ingresemos nosotros en un "integer", es decir, un numero entero.
num2 = int(input("Ingrese el segundo numero: "))
if (num1 > num2): #Esta estructura pregunta si la primera variable es mayor que la segunda. Si es asi, entra y lee el codigo que esta identado.
    print("El primer numero es mayor que el segundo")
else: #Si la pregunta da un falso (es decir, el primer numero no es mayor que el segundo), entonces la estructura entra a y lee el codigo a continuacion.
    print("El segundo numero es mayor que el perimero")
#La estructura solo va a entrar a UNO de los dos casos. Si el primer numero es mayor ejecuta el primer codigo identado e ignora el segundo codigo identado. En caso contrario, ignora el primer codigo identado y ejecuta el segundo.    
#Un pequeño error que tiene este programa es que si ambos numeros son iguales va a decir que el segundo numero es mayor que el primero. Por que? Porque la estructura "if" esta preguntando si el numero 1 es MAYOR que el numero 2, si son iguales, el "if" va a devolver falso (ya que el primer numero no es mayor) por lo que el programa ejecuta el segundo codigo identado.