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
          role TEXT NOT NULL,
          status BOOLEAN DEFAULT TRUE,
          created_at TIMESTAMP DEFAULT (datatime('now', 'localtime')),
          updated_at TIMESTAMP DEFAULT (datatime('now', 'localtime')),
          deleted_at NULL
      )
'''

#Execute query
cur.execute(users_model)


#Close connection
con.close()


