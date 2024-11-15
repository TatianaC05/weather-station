'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07-10-2024
Dev: Tatiana C. 
'''

from database import insert_data
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

last_temperature = None
last_humidity = None

while True:
    #data = service.readline.decode('utf-8').strip() #A la derecha borra datos
    data = service.readline().decode('utf-8').rstrip() #a la izquierda borra datos
   
    if data:
        try:
        #print(data)
             temperature, humidity = map(float, data.split(","))    
             print(f"Temperature: {temperature}°C")
             print(f"Humidity: {humidity}%")
        
             # Insertar datos solo si hay cambios
             if temperature != last_temperature or humidity != last_humidity:
                insert_data(temperature, humidity)
                last_temperature = temperature
                last_humidity = humidity               
        except ValueError:
         print("Error en el formato de los datos recibidos.")
        
    
        
        #Here Insert Into
        # 1. Create new model data called test_data (en database.py)
        #Fields: id,tem,hum,created_at
        # 2. method to insert data into test_data(aqui en insert into data -- variables temperature y humidity -- datos guardados en la tabla)
        # 3. Update method: Insert data when detect changes in temp or hum 
        # 4. Create a menu option: List sensor data
        # 5. Create new option Graphics with matplotlib
    time.sleep(1)
    
    