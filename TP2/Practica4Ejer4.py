from functools import partial
import tkinter as tk
from tkinter import ttk

#UI object for day/temperature
class UI_day_temperature:
    def __init__(self, day, column_num, row_num):
        self.label = ttk.Label(mainframe, text=day + ":").grid(column=column_num, row=row_num, sticky=tk.W)
        self.entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
        self.entry.grid(column=column_num+1, row=row_num, sticky=(tk.E))
    def get_temp(self):
        return self.entry.get()
    
#functions for max and min temperature
def temperature_max(temps):
    try:
        max = temps.sort()
        return max[0]
    except:
        return "-"
def temperature_min(temps):
    try:
        max = temps.sort()
        return max[-1]
    except:
        return "-"
        

#UI Construction
root = tk.Tk()
root.title("Temperaturas")
mainframe = ttk.Frame(root, padding="3 3 15 15")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=3)
#Variables:
days = {"Lunes": 0, "Martes": 0, "Miercoles": 0, "Viernes": 0, "Sabado": 0, "Domingo": 0}
ttk.Label(mainframe, text="Dias:").grid(column=0, row=0, sticky=tk.W)
ttk.Label(mainframe, text="Temperaturas:").grid(column=1, row=0, sticky=tk.W)
column_num, row_num = 0, 1
for key in days:
    ui_row = UI_day_temperature(key, column_num, row_num)
    days[key] = ui_row.get_temp()
    row_num  += 1
ttk.Label(mainframe, text="Temperatura maxima:" + temperature_max(list(days.values()))).grid(column=0, row=8, sticky=tk.W)
ttk.Label(mainframe, text="Temperatura minima:" + temperature_min(list(days.values()))).grid(column=0, row=9, sticky=tk.W)
root.mainloop()