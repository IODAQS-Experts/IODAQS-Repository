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
        self.CreateWidgets()

    def CreateWidgets(self):
        self.CreateNotebook()
        self.AddTabs_Notebook(3)
    
    def CreateNotebook(self):
        self.notebook = ttk.Notebook(self.MainWindow)
        self.notebook.pack(pady=10, expand =True)

    def AddTabs_Notebook(self,AmountTabs):
        for tab in range(1,AmountTabs+1):             #Amount of Tabs starts at 1 and increases as indicated
            self.FrameTab = ttk.Frame(self.notebook, width=400, height=280)
            self.FrameTab.pack(fill='both', expand=True)
            self.FillTabs(tab,self.FrameTab)   
            self.notebook.add(self.FrameTab, text= "Apartado {}".format(str(tab)))
    
    def FillTabs(self,tab,parent):
        if tab == 1:
            contruction = self.FillTab1(parent)
        elif tab == 2:
            contruction = self.FillTab2(parent)
        elif tab == 3:
            contruction = self.FillTab3(parent)
        else:
            pass

        return contruction
        
    def FillTab1(self,parent):
        Label(parent, text = 'Welcome "Home" ').grid(row=0, column=0)
    
    def FillTab2(self,parent):
        Label(parent, text = 'Welcome "WorkingArea"').grid(row=0, column=0)
    
    def FillTab3(self,parent):
        Label(parent, text = 'Welcome "About us"').grid(row=0, column=0)


if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()