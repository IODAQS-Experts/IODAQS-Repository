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
        cahrarray = list(text)
        print(cahrarray,len(cahrarray))
        if text == "Measurements completed!\r\n":
            print("Text detected, loop stopped")
            break
        if num ==1:
            choice = input("insert command: ").upper()
            arduino.write(choice.encode('ascii',errors='strict'))
            if choice == "X":
                print("Exiting Program")
                arduino.close()
                break 
            num +=1 
    print("Text detected, loop stopped")
except:
    print("serial port couldn't be opened")        


#port lookup terminal command: python -m serial.tools.list_ports