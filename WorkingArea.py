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
        self.CreateLabels(ParentFrame)
        self.CreateLabelFrames(ParentFrame)
        self.CreateButtons(ParentFrame)
    
    
    def CreateLabels(self,ParentFrame):
        #Tabs Title
        Label(ParentFrame, text = 'Welcome "WorkingArea"',padx=50,pady=20, font=('Arial Rounded MT Bold', 20)).grid(row=0, column=0)

    def CreateLabelFrames(self,ParentFrame):
        pass

    def CreateButtons(self,ParentFrame):
        pass
    