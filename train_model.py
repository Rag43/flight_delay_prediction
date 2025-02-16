import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#Connect to SQLite db
conn = sqlite3.connect("flights.db")
df = pd.read_sql_query("SELECT * FROM flights", conn)
conn.close()

#Define features (x) and target (y)
x = df[["year", "month", "day", "departure_time", "distance"]]
y = (df["departure_delay"] > 15).astype(int) # 1 - delayed; 0 - On Time

#Split data into training (80%) and testing (20%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, y_train.shape)

print("Checking for NaN values in training data...")
print(x_train.isnull().sum())
print(y_train.isnull().sum())

# Train the random forest model with 100 trees
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

#Get feature importance scores
importances = model.feature_importances_
feature_names = x_train.columns
feature_importance = sorted(zip(feature_names, importances),
                             key=lambda x: x[1], reverse=True)
print("\nFeature importance ranking:")
for feature, importance in feature_importance:
    print(f"{feature}: {importance:.4f}")

#Make predictions
y_pred = model.predict(x_test)

#check model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")


