import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split

conn = sqlite3.connect("flights.db")

df = pd.read_sql_query("select * from flights", conn)

conn.close()

X = df[["Year", "Month", "Day", "DepTime", "Distance"]]
y = (df["DepDelay"] > 15).astype(int) # Convert to a numPy array


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
print(X_train)
print(y_train)
