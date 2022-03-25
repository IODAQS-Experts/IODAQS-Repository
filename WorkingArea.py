#Creation date: 2022 / march / 3 / 22:48 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os

class Tab2Widgets:
    def __init__(self,ParentFrame):
        self.CreateWidgets_Tab2(ParentFrame)

    def CreateWidgets_Tab2(self,ParentFrame):    
        self.CreateLabelFrames(ParentFrame)
        self.CreateLabels(ParentFrame)
        self.CreateEntries(ParentFrame)
        self.CreateButtons(ParentFrame)


    def CreateLabels(self,ParentFrame):
        #Tab Title
        self.Title=Label(
            ParentFrame,
            text = 'Welcome "WorkingArea"',
            anchor='w',
            font=('Arial Rounded MT Bold', 20),
            relief="solid"
            ).grid(row=0, column=0, ipadx=50,ipady=20)

        # Labels in MeasurementTime Label Frame
        Label(
            self.MeasurementTime,
            text = 'Tiempo Inicial',
            #padx=50,pady=20,
            anchor='ne',
            font=('Arial Rounded MT Bold', 9),
            relief="solid"
            ).grid(row=1, column=1, padx=10 )

    def CreateLabelFrames(self,ParentFrame):
        self.MeasurementTime = LabelFrame(ParentFrame, width=300, height= 100, text="Tiempo de Medición", 
        font=('Arial Rounded MT Bold', 12), labelanchor= "nw", relief="solid").grid(row=1, column=0, padx=10 )

    def CreateButtons(self,ParentFrame):
        pass

    def CreateEntries(self,ParentFrame):
        self.StarTime=ttk.Entry(self.MeasurementTime).grid(row=0, column=0, padx=10)
    