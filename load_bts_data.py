import sqlite3
import pandas as pd

#Load cleaned BTS dataset
df = pd.read_csv("Jan_24_cleaned.csv")

#Connect to SQLite database (create db if not exist)
conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

#Create the flights table if not exist
cursor.execute("""CREATE TABLE IF NOT EXISTS flights (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               year INTEGER,
               month INTEGER,
               day INTEGER,
               airline TEXT,
               flight_number INTEGER,
               origin TEXT,
               destination TEXT,
               departure_time INTEGER,
               departure_delay INTEGER,
               distance REAL
               );
               """)

#Rename columns to match db schema
df.rename(columns={
    "YEAR": "year",
    "MONTH": "month",
    "DAY_OF_MONTH": "day",
    "OP_UNIQUE_CARRIER": "airline",
    "OP_CARRIER_FL_NUM": "flight_number",
    "ORIGIN_AIRPORT_ID": "origin",
    "DEST_AIRPORT_ID": "destination",
    "DEP_TIME": "departure_time",
    "DEP_DELAY": "departure_delay",
    "DISTANCE": "distance"
}, inplace=True)

#Insert data into SQLite db
df.to_sql("flights", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("BTS Flight data loaded successfully into SQLite database")