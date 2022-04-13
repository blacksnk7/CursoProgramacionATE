import random #Importamos la libreria para hacer numeros aleatorios.

computadora = random.randint(1, 3) #Generamos un numero aleatorio para simular la piedra, papel o tijera.
jugador = int(input("Elija una opcion: \n1)Piedra \n2)Papel \n3Tijeras \n4)Salir \n"))
victorias, derrotas, empates = 0, 0, 0 #Aca contabilizamos las victorias, derrotas y empates
while (jugador != 4):
    if (computadora != jugador): #Primero preguntamos si ambos elegimos lo mismo. Si no fue asi, ejecutamos el codigo indentado.
        match jugador: #Esto va a preguntar en base a jugador, que valor tiene la variable.
            case 1: #Si la variable jugador es igual a 1 entonces ejecuta el codigo indentado
                if (computadora == 2): #Si el jugador eligio 1 y la computadora 2 significa que fue Piedra contra Papel, por lo que gano la computadora.
                    print("Perdiste! Yo eleji papel")
                    derrotas += 1 #Como gano la computadora sumamos un +1 al contador de derrotas
                else: #Si el jugador eligio 1 y la computadora NO eligio 2 entonces significa que eligio 3 (porque lo primero que preguntamos era si el jugador y la computadora eran iguales, es decir, si ambos eligieron 1 en este caso). Por lo tanto es una victoria para el jugador
                    print("Ganaste! Yo eleji tijeras")
                    victorias += 1 #Como gano el jugador sumamos un +1 al contador de victorias.
            case 2: #Si la variable jugador es igual a 2 entonces ejecuta el codigo indentado
                if (computadora == 3): #Si el jugador eligio 2 y la computadora 3 significa que fue Papel contra Tijeras, por lo que gano la computadora.
                    print("Perdiste! Yo eleji tijeras")
                    derrotas += 1 #Gano la computadora, asi que sumamos un +1 a las derrotas.
                else: #Al igual que en el caso uno, si el jugador eligio 2, y la computadora no eligio lo mismo ni tampoco eligio 3, entonces por descarte eligio 1. Esto seria Papel contra Piedra por lo que gana el jugador.
                    print("Ganaste! Yo eleji piedra")
                    victorias += 1 #Gano el jugador, asi que sumamos un +1 a las victorias
            case 3: #Si la variable jugador es igual a 3 entonces ejecuta el codigo indentado
                if (computadora == 1): #Si el jugador eligio 3 y la computadora eligio 1 entonces es Tijeras contra Piedra, por lo que gana la computadora.
                    print("Perdiste! Yo eleji piedra")
                    derrotas += 1 #Sumamos un +1 a las derrotas porque gano la computadora
                else: #Al igual que el caso 1 y 2, si llegamos hasta este punto significa que el jugador es 3 y la computadora no es ni igual al jugador ni 1, asi que por descarte la computadora es 2, es decir Tijeras contra Papel. Victoria para el jugador.
                    print("Ganaste! Yo eleji papel")
                    victorias += 1 #Sumamos un +1 a las victorias.
            case __: #Si la variable tiene cualquier otro valor que no sea 1, 2 o 3 (osea que el jugador no eligio ninguna de las opciones permitidas) entonces ejecuta el codigo indentado
                print("No ingresaste un valor permitido :(")
    else: #Si entramos aca significa que tanto el jugador como la computadora eligieron lo mismo.
        print("Empate 0.0")
        empates += 1 #Si ambos eligieron lo mismo entonces es un empate y sumamos un +1 a los empates.
    computadora = random.randint(1, 3) #Generamos un numero aleatorio para simular la piedra, papel o tijera.
    jugador = int(input("Elija una opcion: \n1)Piedra \n2)Papel \n3Tijeras \n4)Salir \n"))
print(f"Usted tuvo {victorias} victorias, {derrotas} derrotas y {empates} empates") #Cuando termina de jugar mostramos las victorias, derrotas y empates. Nuevamente volvemos a usar formateo de texto.