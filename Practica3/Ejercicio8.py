import random #Recuerden siempre que los "import" van al comienzo del programa.

def quien_gana(jugador): #Esta funcion solo va a recibir la eleccion del jugador y se va a encargar de retornar si empato, gano o perdio contra la computadora.
    computadora = random.randint(1, 3)
    if (computadora != jugador): #Primero preguntamos si ambos elegimos lo mismo. Si no fue asi, ejecutamos el codigo indentado.
        match jugador: #Esto va a preguntar en base a jugador, que valor tiene la variable.
            case 1: #Si la variable jugador es igual a 1 entonces ejecuta el codigo indentado
                if (computadora == 2):
                    print("Perdiste! Yo eleji papel")
                    return 2 #Cuando el jugador pierde, la funcion devuelve el numero "2". Por que? Porque asi decidi resolver el problema yo. La funcion puede devolver lo que quieran, yo decidi que devolviera un 2 en caso de perder, un 1 en caso de ganar y un 0 en caso de un empate. En el programa principal yo pregunto si lo que devuelve la funcion es un 2, 1 o 0 y en base a eso sumo una derrota, victoria o empate.
                else:
                    print("Ganaste! Yo eleji tijeras")
                    return 1 #Gano el jugador, asi que devuelvo un 1
            case 2: #Si la variable jugador es igual a 2 entonces ejecuta el codigo indentado
                if (computadora == 3):
                    print("Perdiste! Yo eleji tijeras")
                    return 2 #Gano la computadora asi que devuelvo un 2
                else:
                    print("Ganaste! Yo eleji piedra")
                    return 1 #Gano el jugador, asi que devuelvo un 1
            case 3: #Si la variable jugador es igual a 3 entonces ejecuta el codigo indentado
                if (computadora == 1):
                    print("Perdiste! Yo eleji piedra")
                    return 2 #Gano la computadora asi que devuelvo un 2
                else:
                    print("Ganaste! Yo eleji papel")
                    return 1 #Gano el jugador, asi que devuelvo un 1
            case __: #Si la variable tiene cualquier otro valor que no sea 1, 2 o 3 (osea que el jugador no eligio ninguna de las opciones permitidas) entonces ejecuta el codigo indentado
                print("No ingresaste un valor permitido :(")
    else: #Si la variable "jugador" es igual a la variable "computadora" entonces se ejecuta el codigo indentado.
        print("Empate 0.0")
        return 0 #Como dije al principio, si empatan la funcion me devuelve un 0.
    
jugador = int(input("Elija una opcion: \n1)Piedra \n2)Papel \n3Tijeras \n4)Salir \n"))
victorias, derrotas, empates = 0, 0, 0 #Aca contabilizamos las victorias, derrotas y empates
while (jugador != 4): #Esto funciona igual que en el ejercicio original. Mientras el jugador no elija un 4 para salir del programa, el while seguira ejecutando el juego.
    ganador = quien_gana(jugador) #Aca llamo a la funcion "quien_gana()" que me va a devolver un numero. El numero va a ser un 2 (si el jugador perdio), un 1 (si el jugador gano) o un 0 (si fue un empate).
    if (ganador == 1): #Si la funcion me devolvio un 1 entonces le sumo un +1 al total de victorias del jugador.
        victorias += 1
    elif (ganador == 2): #Si la funcion me devolvio un 2 entonces le sumo un +1 al total de derrotas del jugador
        derrotas += 1
    else: #Si la funcion no devolvio ni un 2 ni un 1, entonces por descarte significa que el jugador empato, por lo que le sumo un +1 a los empates del jugador.
        empates += 1
    jugador = int(input("Elija una opcion: \n1)Piedra \n2)Papel \n3Tijeras \n4)Salir \n"))
print(f"Usted gano {victorias} veces, perdio {derrotas} veces y empato {empates} veces.")
    