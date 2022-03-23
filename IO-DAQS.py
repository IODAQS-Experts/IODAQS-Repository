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

        self.CreateWidgets()

    def CreateWidgets(self):
        self.CreateNotebook()
        self.AddTab1_Notebook()
        self.AddTab2_Notebook()
        self.AddTab3_Notebook()
    
    def CreateNotebook(self):
        self.notebook = ttk.Notebook(self.MainWindow)
        self.notebook.pack(pady=10, expand =True)

    def AddTab1_Notebook(self):
        self.FrameTab1 = ttk.Frame(self.notebook, width=400, height=280)
        self.FrameTab1.pack(fill='both', expand=True)
        self.notebook.add(self.FrameTab1, text= "Apartado 1")
    
    def AddTab2_Notebook(self):
        self.FrameTab1 = ttk.Frame(self.notebook, width=400, height=280)
        self.FrameTab1.pack(fill='both', expand=True)
        self.notebook.add(self.FrameTab1, text= "Apartado 2")

    def AddTab3_Notebook(self):
        self.FrameTab1 = ttk.Frame(self.notebook, width=400, height=280)
        self.FrameTab1.pack(fill='both', expand=True)
        self.notebook.add(self.FrameTab1, text= "Apartado 3")


if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()