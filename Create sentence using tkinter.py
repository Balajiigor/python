
from tkinter import *
from tkinter.ttk import *


ui = Tk()
ui.title("Experiment")

label = Label(font=('Karumbi', 120), background='black', foreground='white')
label.pack(anchor='center')

def name():
    label.config(text=('Hi all"Enter any sentence"'))
name()
mainloop()
