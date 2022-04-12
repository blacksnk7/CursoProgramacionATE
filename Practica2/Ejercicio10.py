import random #Importamos la libreria para hacer numeros aleatorios.

computadora = random.randint(1, 3) #Generamos un numero aleatorio para simular la piedra, papel o tijera.
jugador = int(input("Elija una opcion: \n1)Piedra \n2)Papel \n3Tijeras \n"))
if (computadora != jugador): #Primero preguntamos si ambos elegimos lo mismo. Si no fue asi, ejecutamos el codigo indentado.
    match jugador: #Esto va a preguntar en base a jugador, que valor tiene la variable.
        case 1: #Si la variable jugador es igual a 1 entonces ejecuta el codigo indentado
            if (computadora == 2):
                print("Perdiste! Yo eleji papel")
            else:
                print("Ganaste! Yo eleji tijeras")
        case 2: #Si la variable jugador es igual a 2 entonces ejecuta el codigo indentado
            if (computadora == 3):
                print("Perdiste! Yo eleji tijeras")
            else:
                print("Ganaste! Yo eleji piedra")
        case 3: #Si la variable jugador es igual a 3 entonces ejecuta el codigo indentado
            if (computadora == 1):
                print("Perdiste! Yo eleji piedra")
            else:
                print("Ganaste! Yo eleji papel")
        case __: #Si la variable tiene cualquier otro valor (osea que el jugador no eligio ninguna de las opciones permitidas) entonces ejecuta el codigo indentado
            print("No ingresaste un valor permitido :(")
else:
    print("Empate 0.0")