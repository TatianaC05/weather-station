'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07-10-2024
Dev: Tatiana C. 
'''

#Import libraries
import serial 
import time

#Arduino port
arduino_port ='COM14'
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout=1
)

time.sleep(1) #Delay

while True:
    #data = service.readline.decode('utf-8').strip() #A la derecha borra datos
    data = service.readline().decode('utf-8').rstrip() #a la izquierda borra datos
   
    if data:
        print(data)
        #temperature, humidity = data.split(",")
        
        #print(f"Temperature: {temperature}°C")
        #print(f"Humidity: {humidity}%")
    time.sleep(1)
    
    