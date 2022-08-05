from datetime import datetime

act = datetime.now()
cumple = input("Por favor ingrese su fecha de nacimiento en formato dia.mes.anio: ")
fecha = datetime.strptime(cumple, "%d.%m.%Y")
edad = act - fecha
edad = edad.days
if ((act.month == fecha.month) and (act.day == fecha.day)):
    egg = True
else:
    egg = False
edad = int(edad / 365)
print(f'Usted tiene {edad} anios')
if (egg):
    print('''Art by lgbeard
       , , , , , ,
       |_|_|_|_|_|
      |~=,=,=,=,=~|         Feliz Cumpleanios!
      |~~~~~~~~~~~|
    |~=,=,=,=,=,=,=~|
    |~~~~~~~~~~~~~~~|
  |~=,=,=,=,=,=,=,=,=~|
  |~~~~~~~~~~~~~~~~~~~|
(^^^^^^^^^^^^^^^^^^^^^^^)
 `'-------------------'`    ''')