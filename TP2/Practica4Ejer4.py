import random
from functools import partial
import tkinter as tk
from tkinter import ttk

#UI Construction
root = tk.Tk()
root.title("Temperaturas")
mainframe = ttk.Frame(root, padding="3 3 15 15")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=3)
#Variables:
days = {"Lunes": 0, "Martes": 0, "Miercoles": 0, "Viernes": 0, "Sabado": 0, "Domingo": 0}
for key in days:
    ttk.Label(mainframe, text="Lunes: " + str(scores[2])).grid(column=1, row=3, sticky=tk.W)
