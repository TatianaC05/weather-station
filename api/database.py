'''
Dev: Tatiana C.
Script description: weather-station DataBase 
Engine: SQLite3
Date: 09-09-2024 
'''

#Import database engine package (importar motor) 
import sqlite3 

#Create weather-station database connection
con = sqlite3.connect('weather_station.db')

#Create cursor 
cur = con.cursor() #permite ejecutar los comandos u operaciones crud (query)

#Users model
users_model = '''
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY,
          username TEXT NOT NULL,
          email TEXT NOT NULL,
          password TEXT NOT NULL,
          role NTEGER NOT NULL DEFAULT 1 ,
          status BOOLEAN DEFAULT true,
          created_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
          updated_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
          deleted_at NULL
      )
'''
#USensors model
sensors_model = '''
      CREATE TABLE IF NOT EXISTS sensors (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          model TEXT NOT NULL,
          description TEXT NOT NULL,
          url_datasheet TEXT NOT NULL,
          url_image TEXT NOT NULL,
          status BOOLEAN DEFAULT true,
          created_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
          updated_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
          deleted_at NULL
      )
'''

#Execute query
cur.execute(users_model)
cur.execute(sensors_model)


#Close connection
#con.close()


