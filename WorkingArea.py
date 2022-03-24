#Creation date: 2022 / march / 3 / 22:48 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os

class Tab2Widgets:
    def __init__(self):
        pass

    def CreateWidgets_Tab2(self,ParentFrame):    
        self.CreateLabelFrames(ParentFrame)
        self.CreateLabels(ParentFrame)
        self.CreateButtons(ParentFrame)
    
    
    def CreateLabels(self,ParentFrame):
        #Tab Title
        self.Title=Label(
            ParentFrame,
            text = 'Welcome "WorkingArea"',
            padx=50,pady=20,
            anchor='e',
            font=('Arial Rounded MT Bold', 20),
            relief="solid"
            ).grid(row=0, column=0, columnspan=4)


    def CreateLabelFrames(self,ParentFrame):
        self.MeasurementTime = LabelFrame(ParentFrame, width=300, height= 200, text="Tiempo de Medición", 
        font=('Arial Rounded MT Bold', 12), labelanchor= "nw", relief="solid").grid(row=1, column=0, pady=20)

        # Labels in MeasurementTime Label Frame
        Label(
            ParentFrame,
            text = 'Tiempo Inicial',
            #padx=50,pady=20,
            anchor='e',
            font=('Arial Rounded MT Bold', 9),
            relief="solid"
            ).grid(row=3, column=0)
        

    def CreateButtons(self,ParentFrame):
        pass
    