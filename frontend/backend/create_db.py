import pandas as pd
import sqlite3

df = pd.read_excel('backend\dados.xlsx')

conn = sqlite3.connect('backend\dados.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sex TEXT,
    sport TEXT,
    country TEXT,
    age INT,
    status TEXT
)
''')

data_to_insert = df[['name', 'sex', 'sport', 'country', 'age', 'status']].values.tolist()
cursor.executemany('''
INSERT INTO characters (name, sex, sport, country, age, status) VALUES (?, ?, ?, ?, ?, ?)
''', data_to_insert)

conn.commit()
cursor.close()
conn.close()
