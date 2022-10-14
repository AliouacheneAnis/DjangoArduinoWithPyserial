#Nom         : Python code for connecting Arduino to Python
#Auteur      : Anis Aliouachene 
#Date        : 12-10-2022
#Description : lire a partir du serial avec l'utilisation de la bibliotheque Pyserial 
#That's Engineering
#29/04/2020

from ast import For
import serial 
import time
import schedule
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Arduino.settings")
django.setup()
from AHT20.models import Data

def main_func():
    arduino = serial.Serial('COM34', 9600)  # faire la connexion avec le serial sur le port COM34 avec la frequence 9600 

    print('Established serial connection to Arduino')

    arduino_data = arduino.readline()  # lire les donnees a partir du serial 
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8")) # decoder les valeurs 
    temp = float(decoded_values)   # stocker la valeur decoder en float 
    data = Data()     # stocker la valeur dans la base de donnees 
    data.Temperature = temp
    data.save()
    arduino_data = 0
    arduino.close() # fermer la connexion avec le serial 

    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------

print('Program started')

# Setting up the Arduino 
schedule.every(10).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)