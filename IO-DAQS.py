#Porject Name: IO-DAQS (Input Output Data Acquisition System)       juliomoreno7217@gmail.com
#Creation date: 2022 / march / 3 / 16:55 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from WorkingArea import Tab2Widgets
import time
import os

class IO_DAQS(Tab2Widgets):
    def __init__(self, Window):
        self.MainWindow = Window
        self.MainWindow_Width="1200"
        self.MainWindow_Height="550"
        self.MainWindow.geometry('{}x{}'.format(self.MainWindow_Width,self.MainWindow_Height))
        
        self.CreateWidgets()

    def CreateWidgets(self):
        self.CreateNotebook()
        self.AddTabs_Notebook(3)

    def CreateNotebook(self):
        self.notebook = ttk.Notebook(self.MainWindow)
        self.notebook.pack(pady=10, expand =True)
        self.notebook.grid(row=0,column=0, columnspan=2)

    def AddTabs_Notebook(self,AmountTabs):
        for tab in range(1,AmountTabs+1):             #Amount of Tabs starts at 1 and increases as indicated
            self.FrameTab = ttk.Frame(self.notebook)
            self.FrameTab.pack(fill='both')
  
            self.notebook.add(self.FrameTab, text= "Apartado {}".format(str(tab)))
            self.FillTabs(tab,self.FrameTab) 
        return self.notebook.tabs()
    
    def FillTabs(self,tab,parent):      #To do: Not to sue numbers, but Notebook's names
        if tab == 1:
            self.FillTab1(parent)
        elif tab == 2:
            self.CreateWidgets_Tab2(parent)
        elif tab == 3:
            self.FillTab3(parent)
        
    def FillTab1(self,parent):
        Label(parent, text = 'Welcome "Home" ',padx=50, pady=20,font=('Arial Rounded MT Bold', 20)).grid(row=0, column=0)

    
    def FillTab3(self,parent):
        Label(parent, text = 'Welcome "About us"',padx=50,pady=20, font=('Arial Rounded MT Bold', 20)).grid(row=0, column=0)


if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()