import os
from datetime import datetime

current = datetime.now()
date = str(current.day) + "-" + str(current.month) + "-" + str(current.year)
path = os.path.join(os.getcwd(), "files", "asistencia-" + date + ".csv")
with open(path, 'a', encoding = 'utf-8') as f:
    employee = input("Ingrese su nombre: ")
    current = datetime.now()
    tstamp = datetime.timestamp(current)
    while (employee != "$fin"):
        f.write(f"{str(tstamp)},{employee}\n")
        print(f"Se registro el ingreso de {employee} a las {current.hour}:{current.minute}:{current.second}")
        employee = input("Ingrese su nombre: ")
        current = datetime.now()
        tstamp = datetime.timestamp(current)
    print("Finalizo el fichaje.")