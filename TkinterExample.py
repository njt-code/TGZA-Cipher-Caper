from tkinter import *
from tkinter import ttk
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='stop', width = 25, command = r.destroy)
button.pack()
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text ="Quit", command=root.destroy).grid(column=1,row=0)
root.mainloop()