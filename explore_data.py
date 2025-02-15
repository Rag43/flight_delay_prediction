import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Connect to the SQLite db
conn = sqlite3.connect("flights.db")

#load flight data into a pandas df
df = pd.read_sql_query("SELECT * FROM flights", conn)

conn.close()

#Print columns in dataframe
print("Columns: " + df.columns)

#print first 5 rows
print(df.head())

#summary stats
print(df.describe())

# Plot distribution using pyplot
plt.hist(df["DepDelay"], bins = 30, edgecolor = "black")
plt.xlabel("Departure Delay (minutes)")
plt.ylabel("Number of flights")
plt.title("Distribution of flight delays")
plt.show()
