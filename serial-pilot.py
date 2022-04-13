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

    def commands():
        print("""*********************
* 1 >> Turn on led *
* 0 >> Turn off led  *
* X >> Exit         *
*********************
        """)

    while True:
        commands()
        choice = input("insert command: ").upper()

        if choice == "1":
            print("led status: ON\n")
            command = "," + choice
            arduino.write(command.encode("ascii"))
        elif choice == "0":
            led=0
            print("led status: OFF\n")
            command = "," + choice
            arduino.write(command.encode("ascii"))
        elif choice == "X":
            print("Exiting Program")
            arduino.close()
            break
        else:
            print("Invalid choice...try again\n")
except:
    print("serial port couldn't be opened")        


#port lookup terminal command: python -m serial.tools.list_ports