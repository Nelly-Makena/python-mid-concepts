import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("Mille to Kilometer Converter ")

window.geometry("500x500")

entry =Entry(width=10)
entry.grid(column=1,row=0, padx=70, pady=20)

label_1 = tk.Label(window, text="Miles")
label_1.grid(column=2,row=0 )

label_2 = tk.Label(window, text="is equal to")
label_2.grid(column=0,row=1 )

label_3 = tk.Label(window, text="0")
label_3.grid(column=1,row=1 )

label_4 = tk.Label(window, text="Km")
label_4.grid(column=2,row=1 )

def calculate():
    answer=float(entry.get())
    final = answer * 1.7
    final = round(final, 0)
    label_3.config(text=str(final))
    return label_3



button= Button(window, text="Calculate ", command=calculate )
button.grid(column=1,row=2,padx=10)





















window.mainloop()

