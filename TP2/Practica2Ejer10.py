import random
#https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
#Using partial to pass parameters through a button
from functools import partial
import tkinter as tk
from tkinter import ttk

def rock_paper_scissors(player, scores):
    #1 = rock, 2 = paper, 3 = scissors
    computer = random.randint(1, 3)
    match player, computer:
        case (1, 1) | (2, 2) | (3, 3):
            scores[0] += 1
        case (1, 2) | (2, 3) | (3, 1):
            scores[1] += 1
        case (1, 3) | (2, 1) | (3, 2):
            scores[2] += 1
    ttk.Label(mainframe, text="Ganadas: " + str(scores[2])).grid(column=1, row=3, sticky=tk.W)
    ttk.Label(mainframe, text="Perdidas: " + str(scores[1])).grid(column=2, row=3, sticky=tk.W)
    ttk.Label(mainframe, text="Empates: " + str(scores[0])).grid(column=3, row=3, sticky=tk.W)


scores = [0, 0, 0]
root = tk.Tk()
root.title("Piedra papel o tijeras")
mainframe = ttk.Frame(root, padding="3 3 15 15")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=3)
ttk.Button(mainframe, text="Piedra", command=partial(rock_paper_scissors, 1, scores)).grid(column=1, row=1, sticky=tk.W)
ttk.Button(mainframe, text="Papel", command=partial(rock_paper_scissors, 2, scores)).grid(column=2, row=1, sticky=tk.W)
ttk.Button(mainframe, text="Tijeras", command=partial(rock_paper_scissors, 3, scores)).grid(column=3, row=1, sticky=tk.W)
ttk.Label(mainframe, text="Ganadas: " + str(scores[2])).grid(column=1, row=3, sticky=tk.W)
ttk.Label(mainframe, text="Perdidas: " + str(scores[1])).grid(column=2, row=3, sticky=tk.W)
ttk.Label(mainframe, text="Empates: " + str(scores[0])).grid(column=3, row=3, sticky=tk.W)
root.mainloop()