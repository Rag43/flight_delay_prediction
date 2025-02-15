import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Connect to SQLite db
conn = sqlite3.connect("flights.db")

# Load flight data into pd df
df = pd.read_sql_query("select * from flights", conn)

conn.close()

#Define features (X) and target (Y)
X = df[["Year", "Month", "Day", "DepTime", "Distance"]] # Features
Y = (df["DepDelay"] > 15).astype(int) # Target: 1 = delayed; 0 = not

#Split data into training (80) and testing (20) sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#train a random forest model with 100 trees
model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X_train, Y_train) # Train model

#Make predictions on the test set
y_pred = model.predict(X_test)

#Evaluate accuracy
accuracy = accuracy_score(Y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")




