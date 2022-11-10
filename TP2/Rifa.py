from functools import partial
from UI_constructors import UI_root
from tkinter import ttk
import tkinter as tk

class Contest:
    def __init__(self, numbers=10):
        self.contestants = {}
        for i in range(numbers):
            self.contestants.update({str(i): ""})
    def get_contestants(self):
        return self.contestants
    def get_name_number_pairs(self):
        pairs = []
        contestants = self.get_contestants()
        for key in contestants:
            pairs.append(f"{key} - {contestants[key]}")
        return pairs
    def set_contestant(self, key, value):
        self.contestants.update({key: value})
    def free_numbers(self):
        free_numbers = []
        contestants = self.get_contestants()
        for key in contestants:
            if (contestants[key] == ""):
                free_numbers.append(key)
        print(free_numbers)
        return free_numbers

def take_number(contestants, name, number, ui):
    name_value = name.get()
    free_numbers = contestants.free_numbers()
    number_value = number.get()
    if (number_value in free_numbers):
        contestants.set_contestant(number_value, name_value)
    else:
        print("ERROR. That number is taken!")
    print(contestants.get_contestants())
    UI_init(ui)

def UI_init(ui):
    '''
    This function creates the window which contains all of the UI elements. When something 
    needs to be updated, this function can be called again to "refresh" the window by re-constructing
    it from scratch
    '''
    column_num, row_num = 0, 0
    label_name = ttk.Label(ui.mainframe, text="Enter your name: ")
    label_name.grid(column=column_num, row=row_num, sticky=tk.W)
    name = tk.StringVar()
    entry_name = ttk.Entry(ui.mainframe, width=35, textvariable=name)
    entry_name.grid(column=column_num+1, row=row_num, sticky=(tk.E))
    row_num += 1
    label_number = ttk.Label(ui.mainframe, text="Choose your number: ")
    label_number.grid(column=column_num, row=row_num, sticky=tk.W)
    number = tk.StringVar()
    combobox_number = ttk.Combobox(ui.mainframe, height=5, textvariable=number, values=c.free_numbers(), width=8)
    combobox_number.grid(column=column_num+1, row=row_num, sticky=tk.W)
    row_num += 1
    button_buy_number = ttk.Button(ui.mainframe, text="Buy number", command=partial(take_number, c, name, number, ui))
    button_buy_number.grid(column=column_num, row=row_num, sticky=tk.W)
    label_contestants = ttk.Label(ui.mainframe, text="Contestants:")
    label_contestants.grid(column=2, row=0, sticky=tk.W)
    listbox_choices = tk.StringVar(value=c.get_name_number_pairs())
    listbox_contestants = tk.Listbox(ui.mainframe, listvariable=listbox_choices)
    listbox_contestants.grid(column=column_num+2, row=1, sticky=tk.W)


c = Contest(10)
#UI Initialization
ui = UI_root("Contest")
UI_init(ui)
ui.root.mainloop()
