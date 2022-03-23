#Porject Name: IO-DAQS (Input Output Data Acquisition System)       juliomoreno7217@gmail.com
#Creation date: 2022 / march / 3 / 16:55 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os

class IO_DAQS:
    def __init__(self, Window):
        self.MainWindow = Window
        self.Sart_Time = 0
        self.End_Time = 0

    def CreateWidgets(self):
        #Crear un menu de ventanas (tabs)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(pady=10, expand =True)

        self.notebook.add(self.notebook,text= "Apartado 1")
        self.notebook.add(self.notebook,text= "Apartado 2")



if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()