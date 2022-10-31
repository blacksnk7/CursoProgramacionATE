import tkinter as tk
from tkinter import ttk

class UI_root:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.mainframe = ttk.Frame(self.root, padding="3 3 15 15")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=3)
        self.root.rowconfigure(0, weight=3)
        