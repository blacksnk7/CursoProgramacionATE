import os
from datetime import datetime

def save_info(dates, start_date):
    path = os.path.join(os.getcwd(), "files", "registro-" + start_date.replace(".", "-") + ".txt")
    print(path)
    with open(path,'w',encoding = 'utf-8') as f:
        f.write(f"Período: {start_date} al {list(dates.keys())[-1]}\n")
        total = 0
        for key in dates:
            total += dates[key]
        prom = total / len(dates.keys())
        f.write(f"Total de minutos: {total}\n")
        f.write(f"Promedio en minutos: {prom:.2f} minutos por dia\n")
        f.write("-- Detalle:\n")
        for key in dates:
            f.write(f"{key}: {dates[key]}\n")

dates = {}
start_date = input("Ingrese la fecha inicial en formato dia.mes.anio: ")
start = datetime.strptime(start_date, "%d.%m.%Y")
days = int(input("Ingrese la cantidad de dias a procesar: "))
for n in range(days):
    current_date = start.replace(day=start.day+n)
    minutes = int(input(f"Tiempo para el dia {current_date.day}.{current_date.month}.{current_date.year}: "))
    dates[f"{str(current_date.day)}.{str(current_date.month)}.{str(current_date.year)}"] = minutes
save_info(dates, start_date)
