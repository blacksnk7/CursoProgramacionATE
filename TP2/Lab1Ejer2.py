from functools import partial
from UI_constructors import UI_root
from tkinter import ttk
import tkinter as tk
import random
import string

def password_generator(size_digits, size_pass):
    total_digits = int(size_digits.get())
    total_passwords = int(size_pass.get())
    if (total_digits > 0) and (total_passwords > 0):
        digits = string.digits + string.ascii_letters + string.punctuation
        ttk.Label(ui.mainframe, text="Contraseñas generadas:").grid(column=1, row=4, sticky=tk.W)
        #The variable 'r' counts the total ammount of rows in the program so that each password can be shown in a new row
        r = 4
        for times in range(total_passwords):
            password = ''
            for i in range(total_digits):
                password += random.choice(digits)
            ttk.Label(ui.mainframe, text=str(times+1) + ")  " + password + "\t").grid(column=2, row=r)
            r += 1
        
#UI Building        
ui = UI_root("Generador de contraseñas")
size_digits = tk.StringVar()
digits_entry = ttk.Entry(ui.mainframe, width=7, textvariable=size_digits)
digits_entry.grid(column=3, row=1, sticky=(tk.W, tk.E))
size_pass = tk.StringVar()
pass_entry = ttk.Entry(ui.mainframe, width=7, textvariable=size_pass)
pass_entry.grid(column=3, row=2, sticky=(tk.W, tk.E))
ttk.Label(ui.mainframe, text="Ingrese la cantidad de digitos").grid(column=1, row=1, sticky=tk.W)
ttk.Label(ui.mainframe, text="Ingrese la cantidad de contraseñas").grid(column=1, row=2, sticky=tk.W)
ttk.Button(ui.mainframe, text="Generar", command=partial(password_generator, size_digits, size_pass)).grid(column=3, row=3, sticky=tk.W)
ui.root.bind("<Return>", password_generator)
ui.root.mainloop()