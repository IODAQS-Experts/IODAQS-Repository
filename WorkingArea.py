#Creation date: 2022 / march / 3 / 22:48 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os

class Tab2Widgets:
    def __init__(self,):
        pass

    def CreateWidgets_Tab2(self,ParentFrame):    
        self.CreateFrames(ParentFrame)
        self.CreateLabelFrames(self.FrameTab2)
        self.CreateLabels(self.FrameTab2)
        self.CreateSpinBox(self.MeasurementTime)
        self.CreateButtons(ParentFrame)
    
        return self.FrameTab2
    def CreateButtons(self,ParentFrame):
        pass   


    def CreateFrames(self,ParentName):
        self.FrameTab2 = ttk.Frame(ParentName, width='1200', height='550')
        self.FrameTab2.grid(row=1,column=0)


    def CreateLabels(self,ParentFrame):
        #Tab Title

        self.Title=Label(ParentFrame,text = 'Welcome "WorkingArea"', padx=50, pady=20, anchor='e', font=('Arial Rounded MT Bold', 20), relief="solid")
        self.Title.grid(row=0, column=0, columnspan=1)

        #-------Labels in MeasurementTime Label Frame-------#
        self.StartTimeLabel=Label(self.MeasurementTime, text = 'Tiempo Inicial (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.StartTimeLabel.grid(row=0, column=0, ipadx=8, ipady=10, pady=10)

        self.EndTimeLabel=Label(self.MeasurementTime, text = 'Tiempo Final (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.EndTimeLabel.grid(row=1, column=0, ipadx=10, ipady=10, pady=10)

        self.TotalTimeLabel=Label(self.MeasurementTime, text = 'Tiempo Total (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.TotalTimeLabel.grid(row=2, column=0, columnspan=2, ipady=10, pady=10)


    def CreateLabelFrames(self,ParentFrame):
        self.MeasurementTime = LabelFrame(ParentFrame, width=300, height= 200, text="Tiempo de Medición", 
        font=('Arial Rounded MT Bold', 12), labelanchor= "nw", relief="solid")
        self.MeasurementTime.grid(row=1, column=0, padx = 40, pady=20, ipadx=20,ipady=5)
        
    def CreateSpinBox(self,ParentFrame):
        self.StartTime = Spinbox(ParentFrame, from_=0.0, to=1800.0)
        self.StartTime.grid(row=0, column=1, ipadx=30,ipady=10 )

        self.EndTime = Spinbox(ParentFrame, from_=0.0, to=1800.0)
        self.EndTime.grid(row=1, column=1, ipadx=30,ipady=10)

