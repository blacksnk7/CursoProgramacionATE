from functools import partial
from UI_constructors import UI_root
from tkinter import ttk
import tkinter as tk
import os
import csv

def clean_name(name):
    #banned_chars = "áéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ"
    name = name.casefold()
    name = name.replace("á", "a")
    name = name.replace("é", "e")
    name = name.replace("í", "i")
    name = name.replace("ó", "o")
    name = name.replace("ú", "u")
    name = name.replace("à", "a")
    name = name.replace("è", "e")
    name = name.replace("ì", "i")
    name = name.replace("ò", "o")
    name = name.replace("ù", "u")
    return name
    

def repeated_names(name_value, column_num, row_num, label):
    path = os.path.join(os.getcwd(), 'csv', 'nombres-2015.csv')
    name = name_value.get()
    with open(path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        categories = reader.__next__()
        names = []
        for row in reader:
            names.append(row)
        counter = 0
        found = False
        for elem in names:
            counter += 1
            if (clean_name(name) == clean_name(elem[0])):
                found = True
                break
        if (found):
            label.config(text=f"Su nombre '{name}' es el numero: {counter} mas registrado en el año 2015 con: {elem[1]} personas registradas")
        else:
            label.config(text=f"El nombre '{name}' jamas fue registrado en el 2015")
    label.grid(column=column_num+1, row=row_num, sticky=tk.W)
            
def UI_init(ui):
    '''
    This function creates the window which contains all of the UI elements. When something 
    needs to be updated, this function can be called again to "refresh" the window by re-constructing
    it from scratch
    '''
    column_num, row_num = 0, 0
    label_name = ttk.Label(ui.mainframe, text="Ingrese su nombre: ")
    label_name.grid(column=column_num, row=row_num, sticky=tk.W)
    name = tk.StringVar()
    entry_name = ttk.Entry(ui.mainframe, width=35, textvariable=name)
    entry_name.grid(column=column_num+1, row=row_num, sticky=(tk.W))
    row_num += 1
    label_namesRepeated = ttk.Label(ui.mainframe)
    button_check = ttk.Button(ui.mainframe, text="Buscar nombre:", command=partial(repeated_names, name, column_num, row_num, label_namesRepeated))
    button_check.grid(column=column_num, row=row_num, sticky=tk.W)
    ui.root.bind("<Return>", lambda event: repeated_names(name, column_num, row_num, label_namesRepeated))
    ui.root.mainloop()

ui = UI_root("Nombres Repetidos")
UI_init(ui)