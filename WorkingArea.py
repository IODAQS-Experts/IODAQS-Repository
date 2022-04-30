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
        self.CreateButtons()
        return self.FrameTab2



    def CreateButtons(self):
        #-------Buttons in Controls Label Frame ---------#
        self.RunButton= Button(self.Controls_LFrame, command=self.RunMeasurements, text="Ejecutar", anchor='c', font=('Arial Rounded MT Bold', 9))
        self.RunButton.grid(row=0, column=0, padx=25)
        
        self.StopButton= Button(self.Controls_LFrame, command=self.StopMeasurements, text="Detener", anchor='c', font=('Arial Rounded MT Bold', 9))
        self.StopButton.grid(row=0, column=1,padx=8 )

        self.SaveButton= Button(self.Controls_LFrame, command=self.SaveMeasurements, text="Guardar", anchor='c', font=('Arial Rounded MT Bold', 9))
        self.SaveButton.grid(row=0, column=2,padx=8 )
        



    def CreateComboboxes(self):
        #-------Comboboxes in SamplingTime Label Frame----------#
        self.SamplingPrefix = ttk.Combobox(self.SamplingTime_LFrame,width=3, value=['ks','s','ms','us'])
        self.SamplingPrefix.set('s')
        self.SamplingPrefix.grid(row=0, column=2)  



    def CreateFrames(self,ParentName):
        self.FrameTab2 = ttk.Frame(ParentName, width='1200', height='600')
        self.FrameTab2.grid(row=1,column=0)



    def CreateLabels(self,ParentFrame):
        #-------Labels in FrameTab2-------------------------#
        self.Title=Label(ParentFrame,text = 'Welcome "WorkingArea"', padx=50, pady=20, anchor='e', font=('Arial Rounded MT Bold', 20), relief="solid")
        self.Title.grid(row=0, column=0, columnspan=1)

        #-------Labels in MeasurementTime Label Frame-------#
        self.EndTimeLabel=Label(self.MeasurementTime_LFrame, text = 'Duración: (s)', anchor='c', font=('Arial Rounded MT Bold', 9))
        self.EndTimeLabel.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        self.TotalTimeLabel=Label(self.MeasurementTime_LFrame, text = 'Tiempo Total: (s)', anchor='c', font=('Arial Rounded MT Bold', 9))
        self.TotalTimeLabel.grid(row=1, column=0, columnspan=2, ipady=5, pady=5)

        #-------Labels in SamplingTime Label Frame----------#
        
        self.SamplingTime_Label=Label(self.SamplingTime_LFrame, text = 'Tiempo de Muestreo:  ', anchor='c', font=('Arial Rounded MT Bold', 9))
        self.SamplingTime_Label.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        #-------Labels in Signal Label Frame-----------------#
        self.SignalTypeLabel=Label(self.Signal_LFrame, text = 'Tipo de Señal:  ', anchor='c', font=('Arial Rounded MT Bold', 9))
        self.SignalTypeLabel.grid(row=0, column=0, ipadx=1, ipady=5, pady=5, columnspan=2)



    def CreateLabelFrames(self,ParentFrame):
        self.MeasurementTime_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Tiempo de Medición", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.MeasurementTime_LFrame.grid(row=1, column=0, padx = 40, pady=15, ipadx=20,ipady=1)

        self.SamplingTime_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Razón de Muestreo", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.SamplingTime_LFrame.grid(row=2, column=0, padx = 40, pady=15, ipadx=20,ipady=5)

        self.Signal_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Careacterísticas de señal", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.Signal_LFrame.grid(row=3, column=0, padx = 40, pady=15, ipadx=20,ipady=5)

        self.Controls_LFrame = LabelFrame(ParentFrame, width=300, height= 200, text="Controles de Operación", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.Controls_LFrame.grid(row=4, column=0, padx = 40, pady=15, ipadx=20,ipady=5)



    def CreateRadiobuttons(self):
        #-------Radiobuttons in Signal Label Frame----------#
        self.SignalType = StringVar()
        self.SignalType.set("step")

        self.StepInput = Radiobutton(self.Signal_LFrame, text='Escalon', value='step', variable=self.SignalType)
        self.StepInput.grid(row=1, column=0 )

        self.SlopeInput = Radiobutton(self.Signal_LFrame, text='Rampa', value='slope', variable=self.SignalType)
        self.SlopeInput.grid(row=1, column=1)

        self.NoiseInput = Radiobutton(self.Signal_LFrame, text='Ruido', value='noise', variable=self.SignalType)
        self.NoiseInput.grid(row=2, column=0)

        self.SineInput = Radiobutton(self.Signal_LFrame, text='Senoidal', value='senoidal', variable=self.SignalType)
        self.SineInput.grid(row=2, column=1)
        


    def CreateSliders(self):
        self.InputVoltage = Scale(self.Signal_LFrame, from_=0, to=4.52, orient='horizontal', resolution=.01, label='Voltaje')
        self.InputVoltage.grid(row=3, column=0, columnspan=2)



    def CreateSpinBox(self,ParentFrame):
        #-------SpinBoxes in MeasurementTime Label Frame-------#
        self.MeasurementTime = Spinbox(ParentFrame,width=7, from_=0.0, to=1800.0)
        self.MeasurementTime.grid(row=0, column=1, ipadx=0,ipady=0, padx=8)

        #-------SpinBoxes in SamplingTime Label Frame----------#
        self.SampligCoefficient = Spinbox(self.SamplingTime_LFrame, wrap=True, width=5,  from_=0.0, to=1800.0)
        self.SampligCoefficient.grid(row=0, column=1, ipadx=0,ipady=0, padx=8)

