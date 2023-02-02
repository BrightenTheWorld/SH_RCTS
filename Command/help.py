
from tkinter import *
from tkinter import ttk

def about(Cretomain):
    aboutwindow=Toplevel()
    aboutwindow.title("About C-ReTo")
    aboutwindow.geometry("200x200+300+100")
    aboutwindow.resizable(True, True)
    about_LB = ttk.Label(aboutwindow, text="C-ReTo py v1.0")
    about_LB.place(relx=0.5, rely=0.5, anchor=CENTER)
