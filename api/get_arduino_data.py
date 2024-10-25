'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07-10-2024
Dev: Tatiana C. 
'''

#Import libraries
import serial 
import serial.tools.list_ports
import time
from detect_arduino_port import p

#Arduino port
arduino_port = p
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
        #print(data)
        temperature, humidity = data.split(",")       
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        
        # 1. Create new model data called test_data (en database.py)
        #Fields: id,tem,hum,created_at
        # 2. method to insert data into test_data(aqui en insert into data -- variables temperature y humidity -- datos guardados en la tabla)
        # 3. Update method: Insert data when detect changes in temp or hum 
    time.sleep(1)
    
    