# Fecha: 03 /marzo / 2022
#Julio de Jesús Moreno Sánchez
# Programa piloto

import serial
import time

# class MYSerial():
#     def __init__(self):
#         return

try:
    arduino = serial.Serial("com3",9600)
    num = 1
    while True:
        text = arduino.readline().decode('ascii', errors='strict')
        if num ==1:
            choice = input("insert command: ").upper()
            arduino.write(choice.encode('ascii',errors='strict'))
            if choice == "X":
                print("Exiting Program")
                arduino.close()
                break 
            num +=1
        
##        else:
        ##time.sleep(1)   


        print(text)
        
except:
    print("serial port couldn't be opened")        


#port lookup terminal command: python -m serial.tools.list_ports