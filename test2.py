import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import ttkbootstrap.dialogs as di
from tkinter import *
from tkinter import font


#
# root = Tk()
#
# f = font.families()
# print(type(f))
# print(f)
# root.mainloop()
def dialogs_box():
    tp = tk.Toplevel()
    # main = ttk.Frame(
    #     master = tp,
    #     relief = SOLID,
    #     borderwidth = 2,
    # )
    # main.pack(expand = True, fill = BOTH)
    d = di.dialogs.FontDialog()
    body = d.create_body(master = tp)
    body.pack()
    but = d.create_buttonbox(master = tp)
    but.pack()
    print(d)


# create the root window
root = tk.Tk()
root.geometry("500x500")

button = tk.Button(root, text = "button", command = dialogs_box)
button.pack()
# d = dialogs.Dialog(title = "dialogs")

root.mainloop()
