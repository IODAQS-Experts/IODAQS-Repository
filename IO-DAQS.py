#Porject Name: IO-DAQS (Input Output Data Acquisition System)       juliomoreno7217@gmail.com
#Creation date: 2022 / march / 3 / 16:55 h          

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from WorkingArea import Tab2Widgets    
import time
import os
import serial
import math
from tkinter.filedialog import asksaveasfile
import numpy 
from datetime import datetime

import matplotlib
matplotlib.use("TkAgg")         #backend
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import random



class IO_DAQS(Tab2Widgets):
    def __init__(self, Window):
        super().__init__()
        self.MainWindow = Window
        self.MainWindow_Width="1050"
        self.MainWindow_Height="700"
        self.MainWindow.geometry('{}x{}'.format(self.MainWindow_Width,self.MainWindow_Height))
        self.Title="Interfaz Python-Arduino"

        self.CreateWidgets()

        #Graph settings:
        self.GraphFigure = Figure(figsize=(5,4.5),dpi=100,edgecolor='black')
        self.Graph = self.GraphFigure.add_subplot(111)
            
            #canvas._tkcanvas.destroy()
        self.canvas = FigureCanvasTkAgg(self.GraphFigure, self.MatplotlibGraph_LFrame)
        self.canvas.get_tk_widget().pack(side=TOP, fill = BOTH, expand=False)
        toolbar = NavigationToolbar2Tk(self.canvas, self.MatplotlibGraph_LFrame)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=False)
        self.SetGraphProperties()


    def CreateWidgets(self):
        self.CreateNotebook()
        self.AddTabs_Notebook()

    def CreateNotebook(self):
        self.notebook = ttk.Notebook(self.MainWindow,
            width=self.MainWindow_Width,
            height=self.MainWindow_Height)
        self.notebook.grid(row=0,column=0, padx=10, ipadx=20)

    def AddTabs_Notebook(self):
        self.FillTabs(self.notebook)
        self.notebook.add(self.FrameTab1, text= "Apartado 1")       
        self.notebook.add(self.FrameTab2, text= "Apartado 2")
        self.notebook.add(self.FrameTab3, text= "Apartado 3")
           
    def FillTabs(self,ParentName):      
            self.FillTab1(ParentName)
            self.CreateWidgets_Tab2(ParentName)
            self.FillTab3(ParentName)
            

            
    #To do: Filltab1 and FilTab3 muest be gone!     
    def FillTab1(self,ParentName):
        self.FrameTab1 = ttk.Frame(ParentName, width='1200', height='600')
        self.FrameTab1.grid(row=1,column=0)
        
        self.Title1 = Label(self.FrameTab1, text = 'Menú Principal',padx=50, pady=20,font=('Arial Rounded MT Bold', 20))
        self.Title1.grid(row=0, column=0)
    
    def FillTab3(self,ParentName):
        self.FrameTab3 = ttk.Frame(ParentName, width='1200', height='600')
        self.FrameTab3.grid(row=1,column=0, columnspan=4)

        self.Title3 = Label(self.FrameTab3, text = 'Acerca de Nosotros',padx=50,pady=20, font=('Arial Rounded MT Bold', 20))
        self.Title3.grid(row=0, column=0)

        self.AboutUs = Label(self.FrameTab3, text = """
        Porgrama desarrollado por: Julio de Jesús Moreno Sánchez

        Correo: juliomoreno7217@gmail.com

        Link del repositorio: https://github.com/IODAQS-Experts/IODAQS-Repository.git

        Fecha de elaboración: marzo 23 - mayo 20, 2022

        """,anchor='e', font=('Arial Rounded MT Bold', 10))
        self.AboutUs.grid(row=1, column=0)
    
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##
    def RunMeasurements(self):
        self.SendDataToArduino(self.EvaluateDataType())
        self.ReadDataFromArduino()
        self.Create_ReadMeasurementsArrays()
        self.PlotData()

    def EvaluateDataType(self):
        try:
            ##Data##Conditioning##Section####Data##Conditioning##Section##
            ##Data##Conditioning##Section####Data##Conditioning##Section##

            #Sampling-time-prefix adecuation
            prefix={'s':1,'ks':1000,'ms':.001,'us':.000001}
            
            for key in prefix:
                if self.SamplingPrefix.get()==key:
                    self.SamplingTime=str(round(float(self.SampligCoefficient.get())*prefix.get(key),6))
                
                if self.PeriodPrefix.get()==key:
                    self.Period=str(round(float(self.PeriodCoefficient.get())*prefix.get(key),6))

            #Time quantities (in seconds) must be greater than 0!      
            if float(self.MeasurementTime.get())>0 and float(self.SamplingTime)>=.0018 and float(self.MeasurementTime.get())>float(self.SamplingTime) and float(self.Period)>0:
                
                #Converting times to microseconds:
                MeasurementTime = float(self.MeasurementTime.get())
                SamplingTime = float(self.SamplingTime)
                Period = float(self.Period)

                #InputVoltage convertion to a 0-255 value (for ditial pins)
                self.MaxVoltage = 5
                InputFinalVoltage_decimal = math.trunc((255/self.MaxVoltage)*self.FinalVoltage.get())


                InputInitialVoltage_decimal = math.trunc((255/self.MaxVoltage)*self.InitialVoltage.get())


                if self.SignalType.get()=='step':
                    InputFinalVoltage_decimal=0
                
                seed = random.randint(-99999999,99999999)

                if self.SignalType.get()=='noise' and InputInitialVoltage_decimal>=InputFinalVoltage_decimal:
                    self.ShowErrorMessage( "Error!","!El voltaje minimo debe ser menor que el voltaje máximo. Por seguridad los valores se han invertido para coincidir!")
                    InputInitialVoltage_decimal, InputFinalVoltage_decimal=InputFinalVoltage_decimal,InputInitialVoltage_decimal
                
                return str(MeasurementTime),str(SamplingTime),self.SignalType.get(),str(InputInitialVoltage_decimal),str(InputFinalVoltage_decimal),str(Period),str(seed)
                
        except:
            pass    

    def SendDataToArduino(self,parameters=()):
        try:    
            self.DataChain = ",".join(parameters)   #makes a single string separated by the symbol inside ""
            
            self.EvaluateConexion()

            self.arduino.readline().decode(encoding='ascii', errors='strict')
            self.arduino.write(self.DataChain.encode("ascii", errors='strict'))
            
            
        except:
            self.ShowErrorMessage("Error de datos" , "Datos (tiempos o voltajes) inválidos*")
            self.measurementString.set("0")
            self.samplingString.set("0")
    
    def EvaluateConexion(self):
        try:
            self.arduino = serial.Serial()    #Open serial Port
            self.arduino.port = self.SerialPort.get()
            self.arduino.baudrate = 115200
            self.arduino.open()
        except:
           self.ShowErrorMessage("Fallo en Conexión","¡Falló la Conexión con Arduino!")
        
    def ShowErrorMessage(self, message,title):
        #The must appear a window showing the error, and the inputs must be set to default
        messagebox.showerror(message, title)  

    def ReadDataFromArduino(self):
        try:
            reading = "Measurements started!"
            self.readings = []

            while reading != "Measurements completed!\r\n":
                reading = self.arduino.readline().decode(encoding='ascii', errors='strict')
                self.readings.append(reading) 

            messagebox.showinfo(message="Lectura Exitosa!", title="¡Datos leídos exitosamente!") 
        except:
            self.ShowErrorMessage( "Fallo en Conexión","¡Falló la Conexión con Arduino!")
        
    def StopMeasurements(self):
        "Serial Port Closed!!"
        self.arduino.close()
        pass

    def SaveMeasurements(self):
        if len( self.InputVoltageArray) != 0:
            files = [('All Files', '*.*'), 
                ('Comma Separated Values Document', '*.cvs'),
                ('Excel Document','.xls'),
                ('Text Document', '*.txt')]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            if file:
                if self.SignalType.get()=="step":
                    file.write("""Date: {0}
        Measuring time (s): {1}
        Sampling time (s): {2}
        Signal Type: {3}
        Input voltage (V): {4} 
        """.format(datetime.now(),self.MeasurementTime.get(),self.SamplingTime,self.SignalType.get(),self.InitialVoltage.get()))

                elif self.SignalType.get()=="slope":
                    file.write("""Date: {0}
        Measuring time (s): {1}
        Sampling time (s): {2}
        Signal Type: {3}
        Initial voltage (V): {4}
        Final voltage (V): {5}
        """.format(datetime.now(),self.MeasurementTime.get(),self.SamplingTime,self.SignalType.get(),self.InitialVoltage.get(),self.FinalVoltage.get()))

                elif self.SignalType.get()=="sine":
                    file.write("""Date: {0}
        Measuring time (s): {1}
        Sampling time (s): {2}
        Signal Type: {3}
        Amplitude voltage (V): {4}
        Equilibrium voltage (V): {5}
        Period (s): {6}
        """.format(datetime.now(),self.MeasurementTime.get(),self.SamplingTime,self.SignalType.get(),self.InitialVoltage.get(),self.FinalVoltage.get(),self.Period))

                elif self.SignalType.get()=="noise":
                    file.write("""Date: {0}
        Measuring time (s): {1}
        Sampling time (s): {2}
        Signal Type: {3}
        Minimum voltage (V): {4}
        Maximum voltage (V): {5}
        """.format(datetime.now(),self.MeasurementTime.get(),self.SamplingTime,self.SignalType.get(),self.InitialVoltage.get(),self.FinalVoltage.get()))
                
                
                file.write("\n[ Time(s), Input(V), Output(V) ]: \n\n")
                numpy.savetxt(file,self.MeasurementsArray,delimiter=',')
                
                messagebox.showinfo(message="Guardado Exitoso!", title="¡Datos guardados exitosamente!") 
                file.close()
        
    def Create_ReadMeasurementsArrays(self):
        try:
            #Organizing info in lists:
            self.InputVoltageList = []
            self.OutputVoltageList = []
            self.TimeList =[]

            self.MeasurementsList=[]
            for index in range(2,(len(self.readings)-1),3):             
                #The last data is always time so the index is referenced to each datatime indexes' position (because of how readline() works)
                #time in seconds
                self.TimeList.append(float(self.readings[index][:-2])/1000000)   
                #Voltages conversion*
                self.OutputVoltageList.append(self.MaxVoltage*(float(self.readings[index-1][:-2])/1023))  
                self.InputVoltageList.append(self.MaxVoltage*(float(self.readings[index-2][:-2])/1023))   

                self.MeasurementsList.append([float(self.readings[index][:-2])/1000000,
                                            self.MaxVoltage*(float(self.readings[index-2][:-2])/1023),
                                            self.MaxVoltage*(float(self.readings[index-1][:-2])/1023)])
            # Arrays are transformed into arrays:
            self.InputVoltageArray = numpy.array(self.InputVoltageList)
            self.OutputVoltageArray = numpy.array(self.OutputVoltageList)
            self.TimeArray = numpy.array(self.TimeList)
            self.MeasurementsArray = numpy.array(self.MeasurementsList)

        except:
            pass

    def PlotData(self):
        try:
            if len( self.InputVoltageArray) != 0:

                self.Graph.clear()
                self.Graph.plot(self.TimeArray,self.InputVoltageArray, color='#A5F4FA',linestyle='solid', marker='o',markersize='4', label="V_in")
                self.Graph.plot(self.TimeArray,self.OutputVoltageArray, color='#E3FA98',linestyle='solid', marker='x',markersize='4', label="V_out")
                self.canvas.draw_idle()
                self.SetGraphProperties()
        except:
            pass
        
    def SetGraphProperties(self):
        font = {'family': 'Arial Rounded MT Bold',
        'color':  'white',
        'weight': 'normal',
        'size': 12,
        }
        self.Graph.set_title('Comparación Voltaje de Entrada vs Salida', fontdict = font)
        self.Graph.grid(color='#667B84')
        self.Graph.set_xlabel("Tiempo (s)",fontdict = font)
        self.Graph.set_ylabel("Voltaje (V)",fontdict = font)
        self.Graph.legend(["V_in","V_out"])  
        self.Graph.grid(color='#667B84')
        self.GraphFigure.patch.set_facecolor('#465162')
        self.Graph.xaxis.label.set_color('white')        #setting up X-axis label color 
        self.Graph.yaxis.label.set_color('white')          #setting up Y-axis label color 
        self.Graph.set_facecolor('#465162')           #Grah Background color
        self.Graph.tick_params(axis='x', colors='#92C2E2',labelsize=10)    #setting up X-axis tick color to red
        self.Graph.tick_params(axis='y', colors='#92C2E2',labelsize=10)  #setting up Y-axis tick color to black
        pass

    def SetSliderLabel(self):
        if self.SignalType.get()=='step':
            self.InitialVoltage['label']= "Voltaje Escalón: "
            self.FinalVoltage.grid_forget()

            self.PeriodCoefficient.grid_forget()
            self.PeriodLabel.grid_forget()
            self.PeriodPrefix.grid_forget()

        elif self.SignalType.get()=='slope':
            self.FinalVoltage.grid(row=0, column=1)
            self.InitialVoltage['label'] = "Voltaje Inicial: "
            self.FinalVoltage['label'] = "Voltaje Final: "

            self.PeriodCoefficient.grid_forget()
            self.PeriodLabel.grid_forget()
            self.PeriodPrefix.grid_forget()
            
        elif self.SignalType.get()=='sine':
            self.FinalVoltage.grid(row=0, column=1)
            self.InitialVoltage['label'] = "Amplitud de Voltaje: "
            self.FinalVoltage['label'] = "Voltaje de Equilibrio: "

            self.PeriodCoefficient.grid(row=3, column=1, ipadx=0,ipady=0,)
            self.PeriodLabel.grid(row=3, column=0, ipadx=1, ipady=5, pady=5)
            self.PeriodPrefix.grid(row=3, column=2)

        elif self.SignalType.get()=='noise':
            self.FinalVoltage.grid(row=0, column=1)
            self.InitialVoltage['label'] = "Voltaje Mínimo: "
            self.FinalVoltage['label'] = "Voltaje Máximo: "

            self.PeriodCoefficient.grid_forget()
            self.PeriodLabel.grid_forget()
            self.PeriodPrefix.grid_forget()   
        pass

if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()