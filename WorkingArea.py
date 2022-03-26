#Creation date: 2022 / march / 3 / 22:48 h

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os
from tkinter.tix import ComboBox

class Tab2Widgets:
    def __init__(self,):
        pass

    def CreateWidgets_Tab2(self,ParentFrame):    
        self.CreateFrames(ParentFrame)
        self.CreateLabelFrames(self.FrameTab2)
        self.CreateLabels(self.FrameTab2)
        self.CreateSpinBox(self.MeasurementTime_LFrame)
        self.CreateComboboxes()
        self.CreateSliders()
        self.CreateRadiobuttons()
        return self.FrameTab2



    def CreatButtons(self):
        pass



    def CreateComboboxes(self):
        #-------Comboboxes in SamplingRatio Label Frame----------#
        self.SamplingUnit = ttk.Combobox(self.SamplingRatio_LFrame, value=['Tiempo','Frecuencia'])
        self.SamplingUnit.set('Tiempo')
        self.SamplingUnit.grid(row=0, column=1)

        self.SamplingPrefix = ttk.Combobox(self.SamplingRatio_LFrame, value=['ks','ms','us','ps'])
        self.SamplingPrefix.set('s')
        self.SamplingPrefix.grid(row=1, column=1)  



    def CreateFrames(self,ParentName):
        self.FrameTab2 = ttk.Frame(ParentName, width='1200', height='600')
        self.FrameTab2.grid(row=1,column=0)



    def CreateLabels(self,ParentFrame):
        #-------Labels in FrameTab2-------------------------#
        self.Title=Label(ParentFrame,text = 'Welcome "WorkingArea"', padx=50, pady=20, anchor='e', font=('Arial Rounded MT Bold', 20), relief="solid")
        self.Title.grid(row=0, column=0, columnspan=1)

        #-------Labels in MeasurementTime Label Frame-------#
        self.StartTimeLabel=Label(self.MeasurementTime_LFrame, text = 'Tiempo Inicial (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.StartTimeLabel.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        self.EndTimeLabel=Label(self.MeasurementTime_LFrame, text = 'Tiempo Final (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.EndTimeLabel.grid(row=1, column=0, ipadx=1, ipady=5, pady=5)

        self.TotalTimeLabel=Label(self.MeasurementTime_LFrame, text = 'Tiempo Total (s)', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.TotalTimeLabel.grid(row=2, column=0, columnspan=2, ipady=5, pady=5)

        #-------Labels in SamplingRatio Label Frame----------#
        self.SamplingUnitLabel=Label(self.SamplingRatio_LFrame, text = 'Unidad de Muestreo:  ', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.SamplingUnitLabel.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        self.UnitPrefixLabel=Label(self.SamplingRatio_LFrame, text = 'Prefijo de Unidad:  ', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.UnitPrefixLabel.grid(row=1, column=0, ipadx=1, ipady=5, pady=5)

        self.MagnitudLabel=Label(self.SamplingRatio_LFrame, text = 'Prefijo de Unidad:  ', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.MagnitudLabel.grid(row=2, column=0, ipadx=1, ipady=5, pady=5)

        #-------Labels in Signal Label Frame-----------------#
        self.SignalTypeLabel=Label(self.Signal_LFrame, text = 'Tipo de Señal:  ', anchor='c', font=('Arial Rounded MT Bold', 9), relief="solid")
        self.SignalTypeLabel.grid(row=0, column=0, ipadx=1, ipady=5, pady=5, columnspan=2)



    def CreateLabelFrames(self,ParentFrame):
        self.MeasurementTime_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Tiempo de Medición", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.MeasurementTime_LFrame.grid(row=1, column=0, padx = 40, pady=5, ipadx=20,ipady=1)

        self.SamplingRatio_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Razón de Muestreo", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.SamplingRatio_LFrame.grid(row=1, column=1, padx = 40, pady=5, ipadx=20,ipady=5)

        self.Signal_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Careacterísticas de señal", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.Signal_LFrame.grid(row=1, column=2, padx = 40, pady=5, ipadx=20,ipady=5)



    def CreateRadiobuttons(self):
        #-------Radiobuttons in Signal Label Frame----------#
        self.StepInput = Radiobutton(self.Signal_LFrame, text='Escalon', value='step')
        self.StepInput.grid(row=1, column=0 )

        self.SlopeInput = Radiobutton(self.Signal_LFrame, text='Rampa', value='slope')
        self.SlopeInput.grid(row=1, column=1)

        self.NoiseInput = Radiobutton(self.Signal_LFrame, text='Ruido', value='noise')
        self.NoiseInput.grid(row=2, column=0)

        self.SineInput = Radiobutton(self.Signal_LFrame, text='Senoidal', value='senoidal')
        self.SineInput.grid(row=2, column=1)
        


    def CreateSliders(self):
        self.InputVoltage = Scale(self.Signal_LFrame, from_=-10, to=10, orient='horizontal', resolution=.001, label='Voltaje')
        self.InputVoltage.grid(row=3, column=0, columnspan=2)



    def CreateSpinBox(self,ParentFrame):
        #-------SpinBoxes in MeasurementTime Label Frame-------#
        self.StartTime = Spinbox(ParentFrame, from_=0.0, to=1800.0)
        self.StartTime.grid(row=0, column=1, ipadx=1,ipady=5, padx=8 )

        self.EndTime = Spinbox(ParentFrame, from_=0.0, to=1800.0)
        self.EndTime.grid(row=1, column=1, ipadx=0,ipady=0, padx=8)

        #-------SpinBoxes in SamplingRatio Label Frame----------#
        self.SampligCoefficient = Spinbox(self.SamplingRatio_LFrame, from_=0.0, to=1800.0)
        self.SampligCoefficient.grid(row=2, column=1, ipadx=0,ipady=0, padx=8)

