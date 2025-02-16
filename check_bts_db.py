import sqlite3
import pandas as pd

conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(flights);")
columns = cursor.fetchall()

conn.close()

print("Columns in flights table: ")
for col in columns:
    print(col[1])