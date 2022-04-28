#Porject Name: IO-DAQS (Input Output Data Acquisition System)       juliomoreno7217@gmail.com
#Creation date: 2022 / march / 3 / 16:55 h          

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from WorkingArea import Tab2Widgets    
import time
import os
import serial
import math

class IO_DAQS(Tab2Widgets):
    def __init__(self, Window):
        super().__init__()
        self.MainWindow = Window
        self.MainWindow_Width="650"
        self.MainWindow_Height="650"
        self.MainWindow.geometry('{}x{}'.format(self.MainWindow_Width,self.MainWindow_Height))
        self.Title="Interfaz Python-Arduino"

        self.CreateWidgets()

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
        
        self.Title1 = Label(self.FrameTab1, text = 'Welcome "Home" ',padx=50, pady=20,font=('Arial Rounded MT Bold', 20))
        self.Title1.grid(row=0, column=0)
    
    def FillTab3(self,ParentName):
        self.FrameTab3 = ttk.Frame(ParentName, width='1200', height='600')
        self.FrameTab3.grid(row=1,column=0)

        self.Title3 = Label(self.FrameTab3, text = 'Welcome "About us"',padx=50,pady=20, font=('Arial Rounded MT Bold', 20))
        self.Title3.grid(row=0, column=0)
    
    
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##
    def RunMeasurements(self):
        self.SendDataToArduino(self.EvaluateDataType())
        self.ReadDataFromArduino()
       

    def EvaluateDataType(self):
        try:
            ##Data##Conditioning##Section####Data##Conditioning##Section##
            ##Data##Conditioning##Section####Data##Conditioning##Section##

            #Sampling-time-prefix adecuation
            prefix={'s':1,'ks':1000,'ms':.001,'us':.000001}
            
            for key in prefix:
                if self.SamplingPrefix.get()==key:
                    self.SamplingTime=str(round(float(self.SampligCoefficient.get())*prefix.get(key),6))

            #Time quantities (in seconds) must be greater than 0!      
            if float(self.MeasurementTime.get())>0 and float(self.SamplingTime)>=.0018 and float(self.MeasurementTime.get())>float(self.SamplingTime):
                
                #Converting times to microseconds:
                MeasurementTime = float(self.MeasurementTime.get())*1000000
                SamplingTime = float(self.SamplingTime)*1000000

                #InputVoltage convertion to a 0-255 value (for ditial pins)
                MaxVoltage = 5
                InputVoltage_decimal = math.trunc((255/MaxVoltage)*self.InputVoltage.get())
                print(InputVoltage_decimal)

                return str(MeasurementTime),str(SamplingTime),self.SignalType.get(),str(InputVoltage_decimal)
        except:
            pass      

    def SendDataToArduino(self,parameters=()):
        try:    
            self.DataChain = ",".join(parameters)   #makes a single string separated by the symbol inside ""
            print(self.DataChain)
            
            self.EvaluateConexion()

            print(self.arduino.readline().decode(encoding='ascii', errors='strict'))
            self.arduino.write(self.DataChain.encode("ascii", errors='strict'))
            print("Data Sent!!")
            
        except:
            self.ShowErrorMessage("Incorrect Data Type, invalid 'Tiempo de medicion' or 'muestreo'*")
            
    
    def EvaluateConexion(self):
        try:
            self.arduino = serial.Serial()    #Open serial Port
            self.arduino.port = "com3"
            self.arduino.baudrate = 9600
            self.arduino.open()
        except:
            self.ShowErrorMessage("Arduino Connection Failed*")
        
    
    def ShowErrorMessage(self, message):
        #The must appear a window showing the error, and the inputs must be set to default
        print("\n{}\n".format(message))   


    def ReadDataFromArduino(self):
        try:
            reading = "Measurements started!"
            self.readings = []
            while reading != "Measurements completed!\r\n":
                reading = self.arduino.readline().decode(encoding='ascii', errors='strict')
                self.readings.append(reading)
            print("Task done")
            for i in self.readings:
                print(i)
        except:
            self.ShowErrorMessage("Arduino Connection Failed*")
        

    def StopMeasurements(self):
        "Serial Port Closed!!"
        self.arduino.close()
        pass


    def SaveMeasurements(self):
        pass


if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()