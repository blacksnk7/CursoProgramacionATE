import tkinter as tk
from tkinter import ttk

def generate_salute(*args):
    ttk.Label(mainframe, text="¡Hola " + salute.get() + "!").grid(column=1, row=3, sticky=tk.W)
        

root = tk.Tk()
root.title("Saludo")
mainframe = ttk.Frame(root, padding="3 3 15 15")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=3)
ttk.Label(mainframe, text="Ingrese su nombre: ").grid(column=1, row=1, sticky=tk.W)
salute = tk.StringVar()
salute_entry = ttk.Entry(mainframe, width=7, textvariable=salute)
salute_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Saludar", command=generate_salute).grid(column=1, row=2, sticky=tk.W)
root.bind("<Return>", generate_salute)
root.mainloop()