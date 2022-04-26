dias = ["Lunes", "Martes", "Miercoles", "Viernes", "Sabado", "Domingo"]
maxTemp = -999
maxDia = ""
minTemp = 999
minDia = ""
for elem in dias:
    temp = float(input(f"Ingrese la temperatura del dia {elem}: "))
    if (temp >= maxTemp):
        maxTemp = temp
        maxDia = elem
    if (temp <= minTemp):
        minTemp = temp
        minDia = elem
print(f"La temperatura maxima due de {maxTemp} centigrados y sucedio en el dia {maxDia}.\nLa Temperatura minima fue de {minTemp} centigrados y sucedio el dia {minDia}")