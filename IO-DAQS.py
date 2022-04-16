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
        super().__init__()
        self.MainWindow = Window
        self.MainWindow_Width="1200"
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
        self.EvaluateDataType()
        
    def ShowErrorMessage(self):
        #The must appear a window showing the error, and the inputs must be set to default
        print("\nIncorrect Data Type, invalid 'Tiempo de medicion' or 'muestreo'*\n")        
    
    def EvaluateDataType(self):
        try:
            print("working A")
            #Sampling-time-prefix adecuation
            prefix={'s':1,'ks':1000,'ms':.001,'us':.000001,'ns':.000000001}
            for key in prefix:
                if self.SamplingPrefix==key:
                    self.SamplingTime=str(float(self.SampligCoefficient.get()*prefix.get(key)))

            print("working B")

            #Time quantities must be greater than 0!      
            if float(self.MeasurementTime.get())>=0 and float(self.SamplingTime)>=0:
                print("Measurements started!")
                print("Tiempo de medición: ", self.MeasurementTime.get())
                print("Tiempo de muestreo: ", self.SamplingTime)
                print("Tipo de señal: ", self.SignalType.get())
                print("Voltaje de entrada: ", self.InputVoltage.get())
            else:
                self.ShowErrorMessage()
        except:
            self.ShowErrorMessage()       

    def StopMeasurements(self):
        pass

    def SaveMeasurements(self):
        pass


if __name__ == '__main__':
    Window = Tk()
    application = IO_DAQS(Window)
    Window.mainloop()