import sqlite3


def get_db():
    conn = sqlite3.connect('database.db')
    return conn

connection = sqlite3.connect('database.db')


cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
meters (id INTEGER PRIMARY KEY,label TEXT)"""

cursor.execute(command1)

#meter_data
command2 = """CREATE TABLE IF NOT EXISTS 
meter_data (id INTEGER PRIMARY KEY NOT NULL,meter_id INTEGER NOT NULL,timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,value INTEGER,FOREIGN KEY (meter_id) REFERENCES meters (id))"""

cursor.execute(command2)

# cursor.execute("INSERT INTO meters VALUES(11,'label 11')")
# cursor.execute("INSERT INTO meters VALUES(12,'label 12')")
# cursor.execute("INSERT INTO meters VALUES(13,'label 13')")

# cursor.execute("INSERT INTO meter_data VALUES(21,11,'2022-12-23 14:56:59',101)")
# cursor.execute("INSERT INTO meter_data VALUES(22,12,'2022-12-23 14:56:59',102)")
# cursor.execute("INSERT INTO meter_data VALUES(23,13,'2022-12-23 14:56:59',103)")


connection.commit()
connection.close()

