from functools import partial
from UI_constructors import UI_root
import tkinter as tk
from tkinter import ttk

#UI object for day/temperature
class UI_day_temperature:
    def __init__(self, mainframe, day, column_num, row_num):
        self.label = ttk.Label(mainframe, text=day + ":").grid(column=column_num, row=row_num, sticky=tk.W)
        self.entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
        self.entry.grid(column=column_num+1, row=row_num, sticky=(tk.E))
    def get_temp(self):
        return self.entry.get()

#Functions
#UI Initialization
def UI_initialization(mainframe):
    days = {"Lunes": 0, "Martes": 0, "Miercoles": 0, "Viernes": 0, "Sabado": 0, "Domingo": 0}
    ttk.Label(mainframe, text="Dias:").grid(column=0, row=0, sticky=tk.W)
    ttk.Label(mainframe, text="Temperaturas:").grid(column=1, row=0, sticky=tk.W)
    column_num, row_num = 0, 1
    for key in days:
        ui_row = UI_day_temperature(mainframe, key, column_num, row_num)
        days[key] = ui_row
        row_num  += 1
    max = ttk.Label(mainframe, text="")
    max.grid(column=column_num, row=row_num+1, sticky=tk.W)
    min = ttk.Label(mainframe, text="")
    min.grid(column=column_num, row=row_num+2, sticky=tk.W)   
    print(max)
    ttk.Button(mainframe, text="Calcular temperatura maxima y minima", command=partial(calculate_temp, days, max, min)).grid(column=column_num, row=row_num, sticky=tk.W)

#Calculating temperature
def calculate_temp(days, max, min):
    max.config(text="")
    min.config(text="")
    temps = []
    for elem in days.values():
        try:
            temps.append(float(elem.get_temp()))
        except:
            max.config(text="Una o mas temperaturas ingresadas no son un numero")
            return
    max.config(text=f"Temperatura maxima: {temperature_max(temps)}")
    min.config(text=f"Temperatura minima: {temperature_min(temps)}")
    
def temperature_max(temps):
    try:
        temps.sort()
        return temps[-1]
    except:
        return "-"
def temperature_min(temps):
    try:
        temps.sort()
        return temps[0]
    except:
        return "-"
        

#UI Construction
ui = UI_root("Temperaturas")
UI_initialization(ui.mainframe)
ui.root.mainloop()