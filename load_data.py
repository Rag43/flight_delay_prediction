import sqlite3
import pandas as pd

# Load flights.csv into a pandas dataframe
df = pd.read_csv("flights.csv")

# Connect to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
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

# Insert data into the database
df.to_sql("flights", conn, if_exists="replace", index=False)

# Save and close
conn.commit()
conn.close()

print("Data loaded successfully")